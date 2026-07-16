#!/usr/bin/env python3
"""Cross-link genuine same-provider tool suites via relatedTools ("do both").

The library design says overlapping same-domain tools should be kept and linked
so an investigator on one sees its siblings. This wires relatedTools among tools
that share a dedup domain — but only for GENUINE sibling groups: it skips generic
platforms (google.com, youtube.com, ...) where a shared domain does not mean the
tools are related, and skips oversized groups. Idempotent; safe to re-run.

Uses the same dedup_key + policy as validate.py, so after wiring the validator's
"ensure relatedTools cross-links" warning fires only for groups still un-wired.

Usage:
    python library/scripts/wire_related.py            # dry-run: report only
    python library/scripts/wire_related.py --apply     # write relatedTools, then run build_index.py
"""
import sys
from collections import defaultdict

import _common as C
from sibling_policy import GROUP_CAP, dedup_key, should_link_group


def main():
    apply = "--apply" in sys.argv
    groups = defaultdict(list)
    for path, fm, body in C.iter_skills(C.TOOLS_DIR):
        k = dedup_key(fm.get("url", ""))
        if k:
            groups[k].append([path, fm, body])

    changed = 0
    wired_groups = 0
    skipped_generic = skipped_big = 0
    samples = []
    for key, members in sorted(groups.items()):
        ids = [m[1].get("id", "") for m in members]
        if len(members) < 2:
            continue
        ok, reason = should_link_group(key, ids)
        if not ok:
            if reason == "generic":
                skipped_generic += 1
            elif reason == "oversized":
                skipped_big += 1
            continue
        wired_groups += 1
        idset = {i for i in ids if i}
        group_changed = False
        for path, fm, body in members:
            me = fm.get("id", "")
            existing = fm.get("relatedTools") or []
            want = sorted(idset - {me})
            merged = existing + [i for i in want if i not in existing]
            if merged != existing:
                fm = dict(fm)
                fm["relatedTools"] = merged
                changed += 1
                group_changed = True
                if apply:
                    C.write_skill(path, fm, body)
        if group_changed and len(samples) < 15:
            samples.append(f"{key}: {', '.join(sorted(idset))}")

    print(f"{'APPLY' if apply else 'DRY-RUN'}")
    print(f"  sibling groups to wire : {wired_groups}")
    print(f"  files getting new links: {changed}")
    print(f"  skipped generic domains: {skipped_generic}")
    print(f"  skipped oversized (>{GROUP_CAP}): {skipped_big}")
    print("\n  sample wired groups:")
    for s in samples:
        print("   -", s)
    if apply:
        print("\n  wrote relatedTools. NEXT: run build_index.py, then validate.py.")
    else:
        print("\n  (dry-run — no files changed. Rerun with --apply.)")


if __name__ == "__main__":
    main()
