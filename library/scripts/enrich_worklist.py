#!/usr/bin/env python3
"""Prioritized worklist of tool skills that still need authoring.

A skill needs authoring if its body lacks the `## When to use` prose section
(the reliable signal — the `enrichment:` frontmatter field is unreliable).
Ordered by missingPersonsRelevance: high, then medium, then low.

Usage:
    python library/scripts/enrich_worklist.py [N]   # print first N (default 60) + REMAINING count
"""
import os
import random
import re
import sys

ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tools")
N = int(sys.argv[1]) if len(sys.argv) > 1 else 60


def main():
    hi, med, lo = [], [], []
    for dp, _, fs in os.walk(ROOT):
        for f in fs:
            if not f.endswith(".md") or f == "_index.md":
                continue
            p = os.path.join(dp, f)
            s = open(p, encoding="utf-8").read()
            if "## When to use" in s:
                continue  # already authored
            m = re.search(r"^missingPersonsRelevance:\s*(\w+)", s, re.M)
            mp = m.group(1) if m else "low"
            bucket = hi if mp == "high" else med if mp == "medium" else lo
            bucket.append(p.replace("\\", "/"))
    # Shuffle within each priority tier so concurrent/overlapping runs pick
    # different files (avoids two agents authoring the same file -> rebase conflicts).
    for bucket in (hi, med, lo):
        random.shuffle(bucket)
    queue = hi + med + lo
    for p in queue[:N]:
        print(p)
    print(f"REMAINING: {len(queue)}  (high={len(hi)} medium={len(med)} low={len(lo)})")


if __name__ == "__main__":
    main()
