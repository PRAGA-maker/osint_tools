"""Ingest harvested STRATEGY candidates (staging JSON) into the strategies tree.

Reads library/ledger/harvest-strategies/<sourceId>.json (arrays of strategy
candidate objects) and writes strategy skills, routed by type. Never overwrites
an existing file (curated content wins); id collisions get a source suffix.

Routing:
  case-study -> case-studies/        antipattern -> antipatterns/
  pattern    -> patterns/            playbook    -> playbooks/
  technique/pivot with pivotFrom+pivotTo -> pivots/<from>/<to>/   else pivots/_misc/

Usage:
    python library/scripts/ingest_strategies.py [--dry-run]
"""
import glob
import json
import os
import re
import sys

import _common as C

HARVEST_DIR = os.path.join(C.LEDGER_DIR, "harvest-strategies")
TYPES = {"pattern", "antipattern", "technique", "case-study", "playbook", "pivot"}
PHASES = {"intake", "triage", "pivot", "enrichment", "verification", "reporting", "opsec"}
SELECTORS = {"name", "username", "email", "phone", "image", "face", "geolocation",
             "address", "ip-address", "mac-address", "domain", "social-profile",
             "vehicle-plate", "vin", "employer-org", "associate", "dob",
             "physical-description", "document-id", "crypto-wallet", "device-id",
             "metadata-exif", "any"}
MP = {"high", "medium", "low"}


def clean_list(v, allowed=None):
    if not isinstance(v, list):
        return []
    out = [str(x).strip().lower() for x in v if str(x).strip()]
    if allowed is not None:
        out = [x for x in out if x in allowed]
    return out


def existing_ids():
    ids = set()
    if not os.path.isdir(C.STRATEGIES_DIR):
        return ids
    for _p, fm, _b in C.iter_skills(C.STRATEGIES_DIR):
        ids.add(fm.get("id", ""))
    return ids


def target_path(typ, pf, pt):
    if typ == "case-study":
        return ["case-studies"]
    if typ in ("antipattern", "pattern", "playbook"):
        return [typ + "s" if typ != "antipattern" else "antipatterns"]
    if (typ in ("technique", "pivot")) and pf and pt:
        return ["pivots", pf[0], pt[0]]
    return ["pivots", "_misc"]


def main():
    dry = "--dry-run" in sys.argv
    files = sorted(glob.glob(os.path.join(HARVEST_DIR, "*.json")))
    if not files:
        print(f"no staging files in {HARVEST_DIR}")
        return
    ids = existing_ids()
    seen_names = set()
    stats = {"new": 0, "skip_dup": 0, "skip_exists": 0, "bad": 0, "by_type": {}}

    for fp in files:
        source_id = os.path.basename(fp)[:-5]
        try:
            cands = json.load(open(fp, encoding="utf-8"))
        except Exception as e:
            print(f"  skip {fp}: {e}")
            continue
        if isinstance(cands, dict):
            cands = cands.get("strategies", cands.get("candidates", []))
        for c in cands:
            name = C.oneline(c.get("name", ""), 120)
            summary = C.oneline(c.get("summary", ""), 600)
            if not name or not summary:
                stats["bad"] += 1
                continue
            nkey = C.slugify(name)
            if nkey in seen_names:
                stats["skip_dup"] += 1
                continue
            seen_names.add(nkey)

            typ = (c.get("type") or "technique").strip().lower()
            if typ not in TYPES:
                typ = "technique"
            phase = (c.get("phase") or "").strip().lower()
            phase = phase if phase in PHASES else ""
            pf = clean_list(c.get("pivotFrom"), SELECTORS)
            pt = clean_list(c.get("pivotTo"), SELECTORS)
            mp = (c.get("missingPersonsRelevance") or "medium").strip().lower()
            mp = mp if mp in MP else "medium"

            base = nkey
            fid = base
            i = 2
            while fid in ids:
                fid = f"{base}-{i}"
                i += 1
            ids.add(fid)
            rel = target_path(typ, pf, pt)
            fpath = os.path.join(C.STRATEGIES_DIR, *rel, fid + ".md")
            if os.path.exists(fpath):
                stats["skip_exists"] += 1
                continue

            desc = C.oneline(c.get("description") or
                             (("Use when " + c["whenToUse"]) if c.get("whenToUse") else summary), 240)
            fm = {
                "id": fid,
                "name": name,
                "description": desc,
                "type": typ,
                "summary": summary,
                "missingPersonsRelevance": mp,
            }
            if phase:
                fm["phase"] = phase
            if pf:
                fm["pivotFrom"] = pf
            if pt:
                fm["pivotTo"] = pt
            for k in ("platforms", "steps", "signals", "pitfalls", "toolsUsed", "tags"):
                v = c.get(k)
                if isinstance(v, list) and v:
                    fm[k] = [C.oneline(x, 240) for x in v]
            if isinstance(c.get("evidence"), list) and c["evidence"]:
                fm["evidence"] = c["evidence"]
            fm["trust"] = "community"
            fm["source"] = source_id

            def bullets(key, title):
                v = fm.get(key)
                return (f"## {title}\n" + "\n".join(f"- {x}" for x in v) + "\n\n") if v else ""

            body = (
                f"# {name}\n\n> {summary}\n\n"
                + (f"**When to use:** {C.oneline(c.get('whenToUse',''),400)}\n\n" if c.get("whenToUse") else "")
                + bullets("steps", "Steps")
                + bullets("signals", "Signals it's working")
                + bullets("pitfalls", "Pitfalls")
                + (f"**Tools:** {', '.join(fm['toolsUsed'])}\n\n" if fm.get("toolsUsed") else "")
                + f"_Harvested from `{source_id}` — methodology only, no case PII. Promote/curate as needed._\n"
            )
            stats["new"] += 1
            stats["by_type"][typ] = stats["by_type"].get(typ, 0) + 1
            if not dry:
                C.write_skill(fpath, fm, body)

    print(f"NEW={stats['new']} skip_dup={stats['skip_dup']} skip_exists={stats['skip_exists']} bad={stats['bad']}")
    print("by type:", json.dumps(stats["by_type"]))


if __name__ == "__main__":
    main()
