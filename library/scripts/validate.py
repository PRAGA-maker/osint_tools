"""Validate skills against the JSON schemas + dedup-by-domain + (optional) dead links.

Checks (errors -> non-zero exit):
  - required fields present
  - enum fields hold allowed values
  - id matches filename stem
  - url is http(s)
Warnings (do not fail the build):
  - same-domain tools not cross-linked in relatedTools (the "do both" set)
  - stub tools (informational count)

Usage:
    python library/scripts/validate.py [--check-links]
"""
import json
import os
import re
import sys
from collections import defaultdict

import _common as C

SCHEMA_DIR = os.path.join(C.LIB, "schema")

# dedup grouping + which groups are genuine "do both" suites lives in one place so
# this validator's overlap warning matches exactly what wire_related.py links.
from sibling_policy import dedup_key, is_cross_linked, should_link_group


def load_schema(name):
    with open(os.path.join(SCHEMA_DIR, name), encoding="utf-8") as f:
        return json.load(f)


def enum_map(schema):
    """field -> set(allowed) for top-level enum props and array-of-enum props (incl $ref selector)."""
    defs = schema.get("definitions", {})

    def resolve(spec):
        if "$ref" in spec:
            key = spec["$ref"].split("/")[-1]
            return defs.get(key, {})
        return spec

    out = {}
    for field, spec in schema.get("properties", {}).items():
        spec = resolve(spec)
        if "enum" in spec:
            out[field] = ("scalar", set(spec["enum"]))
        elif spec.get("type") == "array":
            items = resolve(spec.get("items", {}))
            if "enum" in items:
                out[field] = ("array", set(items["enum"]))
    return out


def validate_tree(base, schema, label, errors, warns, stats):
    required = schema.get("required", [])
    enums = enum_map(schema)
    domains = defaultdict(list)
    related_of = {}
    for path, fm, body in C.iter_skills(base):
        rel = os.path.relpath(path, C.ROOT)
        stem = os.path.basename(path)[:-3]
        stats["count"] += 1
        if fm.get("enrichment") == "stub":
            stats["stub"] += 1
        # flag/body drift: the enrichment field should match the authored body signal
        if label == "tool":
            authored = "## When to use" in (body or "")
            if authored != (fm.get("enrichment") == "full"):
                stats["drift"] += 1
        for req in required:
            if fm.get(req) in (None, ""):
                errors.append(f"{rel}: missing required '{req}'")
        if fm.get("id") and fm["id"] != stem:
            errors.append(f"{rel}: id '{fm.get('id')}' != filename '{stem}'")
        for field, (kind, allowed) in enums.items():
            if field not in fm or fm[field] in (None, "", []):
                continue
            vals = fm[field] if kind == "array" else [fm[field]]
            if not isinstance(vals, list):
                vals = [vals]
            for v in vals:
                if v not in allowed:
                    errors.append(f"{rel}: '{field}'='{v}' not in allowed {sorted(allowed)[:6]}...")
        url = fm.get("url", "")
        if label == "tool":
            if not re.match(r"^(https?://|javascript:)", url or ""):
                errors.append(f"{rel}: url not http(s)/bookmarklet: '{url[:60]}'")
            key = dedup_key(url)
            if key:
                tid = fm.get("id", stem)
                domains[key].append(tid)
                related_of[tid] = set(fm.get("relatedTools") or [])
    # dedup-by-domain warnings: only for genuine sibling suites still un-wired
    # (skip generic platforms / public-suffix false-groups / oversized per policy).
    for dom, ids in domains.items():
        if len(ids) < 2:
            continue
        ok, _reason = should_link_group(dom, ids)
        if ok and not is_cross_linked(ids, related_of):
            warns.append(f"overlap@{dom}: {', '.join(ids[:8])}{'...' if len(ids) > 8 else ''} "
                         f"-> relatedTools not cross-linked ('do both'); run wire_related.py")


def check_links(base):
    import urllib.request
    bad = []
    seen = set()
    for _p, fm, _b in C.iter_skills(base):
        url = fm.get("url", "")
        if not url or url in seen:
            continue
        seen.add(url)
        try:
            req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "Mozilla/5.0"})
            urllib.request.urlopen(req, timeout=8)
        except Exception as e:
            bad.append(f"{fm.get('id')}: {url} ({type(e).__name__})")
    return bad


def main():
    errors, warns = [], []
    stats = {"count": 0, "stub": 0, "drift": 0}
    validate_tree(C.TOOLS_DIR, load_schema("tool.schema.json"), "tool", errors, warns, stats)
    if os.path.isdir(C.STRATEGIES_DIR):
        validate_tree(C.STRATEGIES_DIR, load_schema("strategy.schema.json"), "strategy", errors, warns, stats)

    print(f"validated {stats['count']} skills ({stats['stub']} stub)")
    print(f"errors={len(errors)} warnings={len(warns)}")
    if stats["drift"]:
        print(f"  info  {stats['drift']} tools have enrichment flag != authored body "
              f"(run build_index.py to reconcile the DB/coverage)")
    for e in errors[:60]:
        print("  ERROR", e)
    for w in warns[:25]:
        print("  warn ", w)
    if len(warns) > 25:
        print(f"  ...(+{len(warns) - 25} more overlap warnings)")
    if "--check-links" in sys.argv:
        bad = check_links(C.TOOLS_DIR)
        print(f"dead links: {len(bad)}")
        for b in bad[:40]:
            print("  DEAD", b)
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
