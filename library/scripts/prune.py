#!/usr/bin/env python3
"""Prune only the UNFILLABLE stubs — tools that can never become a real skill —
so the enrichment routine can fill the rest of the backlog instead of leaving
dead ends as stubs. Fillable stubs (real tools just not authored yet) are KEPT.

Unfillable = will never be a useful authored skill:
  - numeric-duplicate  (id ends -N and the base id exists) — redundant
  - paid-only          (domain in the paid denylist, or pricing: paid) — excluded by policy
  - dead               (status: down / deprecated, or deprecated: true) — the site is gone
  - untrustworthy      (trust: untrustworthy)
Everything else — including low-MP content-free placeholders — is KEPT as
fill-backlog for the routine to author.

Authored skills (with a '## When to use' body) and keep-allowlisted ids are
never touched.

DRY-RUN BY DEFAULT — writes the candidate list to ledger/prune-candidates.json.
Nothing is deleted unless you pass --apply.

Usage:
    python library/scripts/prune.py            # dry-run: report + candidate list
    python library/scripts/prune.py --apply    # delete unfillable + log to pruned.json,
                                                #   clean orphaned nav, then run build_index.py
"""
import json
import os
import sys
from collections import Counter

import _common as C

NUMSUFFIX_RE = __import__("re").compile(r"^(.*)-(\d+)$")


def paid_denylist():
    """Seed the paid-domain denylist from what the routine already recorded as paid-excluded."""
    doms = set()
    p = os.path.join(C.LEDGER_DIR, "skipped-paid.json")
    if os.path.exists(p):
        for e in json.load(open(p, encoding="utf-8")):
            d = C.registered_domain(e.get("url", ""))
            if d:
                doms.add(d)
    return doms


# Real-but-low-MP tools that must survive a purge (audit-confirmed genuine).
KEEP_ALLOWLIST = {
    "importyeti", "courtlistener", "pepchecker", "hudson-rock-cavalier",
    "vessel-finder", "webcams-travel", "aiodnsbrute", "youngersibling",
    "national-business-register-united-kingdom",
}


def classify(fm, body, all_ids, paid_doms):
    """Return (action, reason). Only genuinely UNFILLABLE stubs are deleted."""
    if "## When to use" in (body or ""):
        return "KEEP", "authored"
    _id = fm.get("id", "")
    if _id in KEEP_ALLOWLIST:
        return "KEEP", "allowlist"

    m = NUMSUFFIX_RE.match(_id)
    if m and m.group(1) in all_ids:
        return "DELETE", f"numeric-duplicate-of:{m.group(1)}"

    dom = C.registered_domain(fm.get("url", ""))
    if fm.get("pricing") == "paid" or (dom and dom in paid_doms):
        return "DELETE", f"paid-only:{dom}"

    if fm.get("status") in ("down", "deprecated") or fm.get("deprecated") is True:
        return "DELETE", f"dead:{fm.get('status')}"

    if fm.get("trust") == "untrustworthy":
        return "DELETE", "untrustworthy"

    # Everything else — incl. low-MP content-free seeds — is a real tool awaiting
    # authoring. Keep it in the backlog for the enrichment routine to fill.
    return "KEEP", "fill-backlog"


def main():
    apply = "--apply" in sys.argv
    paid_doms = paid_denylist()
    skills = list(C.iter_skills(C.TOOLS_DIR))
    all_ids = {fm.get("id", "") for _p, fm, _b in skills}

    delete, keep = [], 0
    del_reason = Counter()
    cat_del = Counter()
    for path, fm, body in skills:
        action, reason = classify(fm, body, all_ids, paid_doms)
        if action == "DELETE":
            delete.append({
                "reason": reason, "id": fm.get("id", ""), "name": fm.get("name", ""),
                "file": os.path.relpath(path, C.ROOT).replace("\\", "/"),
                "status": fm.get("status", ""), "url": fm.get("url", ""),
            })
            del_reason[reason.split(":")[0]] += 1
            cat_del[fm.get("category", "?")] += 1
        else:
            keep += 1

    total = len(skills)
    print(f"{'APPLY' if apply else 'DRY-RUN'}: {total} tool skills")
    print(f"  DELETE (unfillable) {len(delete):5d}  ({100*len(delete)//total}%)")
    print(f"  KEEP (fillable)     {keep:5d}  ({100*keep//total}%)")
    print("\n  DELETE reasons:")
    for r, n in del_reason.most_common():
        print(f"    {r:24s} {n}")
    print("\n  DELETE by category (top 12):")
    for c, n in cat_del.most_common(12):
        print(f"    {c:30s} {n}")
    print("\n  sample DELETE files:")
    for rec in delete[:12]:
        print(f"    - {rec['file']}  [{rec['reason']}]")

    outp = os.path.join(C.LEDGER_DIR, "prune-candidates.json")
    with open(outp, "w", encoding="utf-8") as f:
        json.dump({"delete": delete}, f, indent=2, ensure_ascii=False)
    print(f"\n  wrote candidate list -> {os.path.relpath(outp, C.ROOT)}")

    if not apply:
        print("\n  (dry-run — nothing deleted. Review prune-candidates.json, then rerun with --apply.)")
        return

    # --apply: delete unfillable files, log removals.
    pruned = []
    for rec in delete:
        p = os.path.join(C.ROOT, rec["file"])
        if os.path.exists(p):
            os.remove(p)
            pruned.append(rec)
    logp = os.path.join(C.LEDGER_DIR, "pruned.json")
    prev = json.load(open(logp, encoding="utf-8")) if os.path.exists(logp) else []
    with open(logp, "w", encoding="utf-8") as f:
        json.dump(prev + pruned, f, indent=2, ensure_ascii=False)

    # Clean up nav orphaned by the deletions: drop any _index.md whose subtree no
    # longer contains a real skill, then remove now-empty directories (bottom-up).
    def has_skill(d):
        for _dp, _ds, fs in os.walk(d):
            if any(f.endswith(".md") and f != "_index.md" for f in fs):
                return True
        return False
    orphan_nav = empty_dirs = 0
    for dirpath, _dirs, _files in os.walk(C.TOOLS_DIR, topdown=False):
        idx = os.path.join(dirpath, "_index.md")
        if os.path.exists(idx) and not has_skill(dirpath):
            os.remove(idx)
            orphan_nav += 1
        if os.path.isdir(dirpath) and not os.listdir(dirpath):
            os.rmdir(dirpath)
            empty_dirs += 1

    print(f"\n  deleted {len(pruned)} unfillable files -> appended to ledger/pruned.json")
    print(f"  removed {orphan_nav} orphaned _index.md and {empty_dirs} empty directories")
    print("  NEXT: run `python library/scripts/build_index.py` to rebuild the DB/coverage.")


if __name__ == "__main__":
    main()
