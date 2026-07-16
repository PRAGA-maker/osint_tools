#!/usr/bin/env python3
"""Snap enum-drift values back to the schema vocabulary.

The autonomous authoring pass sometimes emits plausible-but-wrong enum tokens
(e.g. 'metadata' instead of 'metadata-exif', auth 'unknown', a browser-extension
reason filed under humanInLoopReason). This normalizes every tool skill in place
so `validate.py` stays green. It is safe to run every enrichment cycle.

Fixes applied (only to files that actually drift):
  - selectorsIn / selectorsOut : 'metadata' -> 'metadata-exif', then de-dup
  - auth                       : any value not in schema enum -> 'none'  (schema default)
  - missingPersonsRelevance    : any value not in {high,medium,low} -> 'low'
  - humanInLoopReason          : drop any item not in the schema enum (e.g. 'browser-extension')

Usage:
    python library/scripts/normalize_enums.py            # apply fixes
    python library/scripts/normalize_enums.py --dry-run  # report only
"""
import json
import os
import sys

import _common as C

SCHEMA = os.path.join(C.LIB, "schema", "tool.schema.json")

# explicit remaps for known typos/aliases (value -> canonical schema token)
SELECTOR_REMAP = {"metadata": "metadata-exif"}


def load_enums():
    s = json.load(open(SCHEMA, encoding="utf-8"))
    defs = s.get("definitions", {})
    sel = set(defs.get("selector", {}).get("enum", []))
    props = s["properties"]
    auth = set(props["auth"]["enum"])
    mp = set(props["missingPersonsRelevance"]["enum"])
    hil = set(props["humanInLoopReason"]["items"]["enum"])
    return sel, auth, mp, hil


def fix_selector_list(vals, allowed):
    """Remap known aliases, drop empties, de-dup preserving order."""
    out, seen = [], set()
    for v in vals or []:
        v = SELECTOR_REMAP.get(v, v)
        if v in seen:
            continue
        seen.add(v)
        out.append(v)
    return out


def main():
    dry = "--dry-run" in sys.argv
    sel, auth, mp, hil = load_enums()
    changed = 0
    counts = {"selectorsIn": 0, "selectorsOut": 0, "auth": 0,
              "missingPersonsRelevance": 0, "humanInLoopReason": 0}
    for path, fm, body in C.iter_skills(C.TOOLS_DIR):
        fm = dict(fm)
        touched = False

        for key in ("selectorsIn", "selectorsOut"):
            cur = fm.get(key)
            if isinstance(cur, list):
                new = fix_selector_list(cur, sel)
                if new != cur:
                    fm[key] = new
                    counts[key] += 1
                    touched = True

        if fm.get("auth") not in auth and "auth" in fm:
            fm["auth"] = "none"
            counts["auth"] += 1
            touched = True

        if fm.get("missingPersonsRelevance") not in mp and fm.get("missingPersonsRelevance"):
            fm["missingPersonsRelevance"] = "low"
            counts["missingPersonsRelevance"] += 1
            touched = True

        hlr = fm.get("humanInLoopReason")
        if isinstance(hlr, list):
            new = [x for x in hlr if x in hil]
            if new != hlr:
                fm["humanInLoopReason"] = new
                counts["humanInLoopReason"] += 1
                touched = True

        if touched:
            changed += 1
            if not dry:
                C.write_skill(path, fm, body)

    print(f"{'[dry-run] would change' if dry else 'changed'} {changed} files")
    for k, v in counts.items():
        if v:
            print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
