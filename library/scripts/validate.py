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

# Hosts where one domain serves many independent tools; key on host+first-path-seg
# (or full host) so distinct repos/users aren't reported as overlaps.
MULTITENANT = {"github.com", "gitlab.com", "sourceforge.net", "bitbucket.org",
               "medium.com", "wordpress.com", "blogspot.com", "gitbook.io",
               "herokuapp.com", "netlify.app", "pages.dev", "web.app",
               "firebaseapp.com", "glitch.me", "replit.app", "readthedocs.io"}


def dedup_key(url):
    dom = C.registered_domain(url)
    if not dom:
        return ""
    m = re.search(r"https?://([^/]+)(/[^/?#]*)?", url or "")
    host = (m.group(1).lower() if m else dom)
    if host.endswith(".github.io") or host.endswith(".gitlab.io"):
        return host  # user.github.io is already per-tool
    if dom in MULTITENANT:
        seg = (m.group(2) or "").strip("/") if m else ""
        return f"{dom}/{seg}" if seg else dom
    return dom


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
    for path, fm, _body in C.iter_skills(base):
        rel = os.path.relpath(path, C.ROOT)
        stem = os.path.basename(path)[:-3]
        stats["count"] += 1
        if fm.get("enrichment") == "stub":
            stats["stub"] += 1
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
                domains[key].append(fm.get("id", stem))
    # dedup-by-domain warnings
    for dom, ids in domains.items():
        if len(ids) > 1:
            warns.append(f"overlap@{dom}: {', '.join(ids[:8])}{'...' if len(ids) > 8 else ''} "
                         f"-> ensure relatedTools cross-links ('do both')")


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
    stats = {"count": 0, "stub": 0}
    validate_tree(C.TOOLS_DIR, load_schema("tool.schema.json"), "tool", errors, warns, stats)
    if os.path.isdir(C.STRATEGIES_DIR):
        validate_tree(C.STRATEGIES_DIR, load_schema("strategy.schema.json"), "strategy", errors, warns, stats)

    print(f"validated {stats['count']} skills ({stats['stub']} stub)")
    print(f"errors={len(errors)} warnings={len(warns)}")
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
