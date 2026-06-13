"""Build the cross-sectional DB + coverage report + group-index navigation skills.

Outputs (all generated, safe to delete & rebuild):
    index/tools.json, index/strategies.json
    index/library.csv (tools), index/library-strategies.csv
    index/library.sqlite (tables: tools, strategies)
    ledger/coverage.md
    tools/**/_index.md, strategies/**/_index.md  (only created if missing)

Usage:
    python library/scripts/build_index.py
"""
import csv
import json
import os
import sqlite3

import _common as C

LIST_FIELDS_TOOL = ["path", "selectorsIn", "selectorsOut", "humanInLoopReason",
                    "coverage", "relatedTools", "aliases", "tags"]
TOOL_COLS = ["id", "name", "url", "category", "path", "description", "bestFor",
             "selectorsIn", "selectorsOut", "status", "pricing", "costNote", "opsec",
             "humanInLoop", "humanInLoopReason", "bestInteractionPattern", "trust",
             "missingPersonsRelevance", "coverage", "auth", "api", "localInstall",
             "registration", "relatedTools", "aliases", "tags", "source", "enrichment"]
STRAT_LIST_FIELDS = ["pivotFrom", "pivotTo", "platforms", "steps", "signals",
                     "pitfalls", "toolsUsed", "relatedStrategies", "tags"]
STRAT_COLS = ["id", "name", "type", "phase", "pivotFrom", "pivotTo", "platforms",
              "summary", "whenToUse", "toolsUsed", "trust", "missingPersonsRelevance",
              "tags", "source"]


def flat(fm, list_fields):
    row = {}
    for k, v in fm.items():
        if isinstance(v, list):
            row[k] = " ".join(str(x) for x in v)
        elif isinstance(v, bool):
            row[k] = "true" if v else "false"
        else:
            row[k] = "" if v is None else str(v)
    for lf in list_fields:
        row.setdefault(lf, "")
    return row


def collect(base, list_fields):
    items = []
    for path, fm, _body in C.iter_skills(base):
        fm = dict(fm)
        fm["_file"] = os.path.relpath(path, C.ROOT).replace("\\", "/")
        items.append(fm)
    items.sort(key=lambda x: (x.get("category", ""), x.get("id", "")))
    return items


def write_json(path, items):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(items, f, indent=2, ensure_ascii=False)


def write_csv(path, items, cols, list_fields):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        for it in items:
            w.writerow(flat(it, list_fields))


def write_sqlite(path, tools, strategies):
    if os.path.exists(path):
        os.remove(path)
    con = sqlite3.connect(path)
    cur = con.cursor()
    cur.execute(f"CREATE TABLE tools ({', '.join(c + ' TEXT' for c in TOOL_COLS)})")
    cur.execute(f"CREATE TABLE strategies ({', '.join(c + ' TEXT' for c in STRAT_COLS)})")
    for it in tools:
        r = flat(it, LIST_FIELDS_TOOL)
        cur.execute(f"INSERT INTO tools ({','.join(TOOL_COLS)}) VALUES ({','.join('?' * len(TOOL_COLS))})",
                    [r.get(c, "") for c in TOOL_COLS])
    for it in strategies:
        r = flat(it, STRAT_LIST_FIELDS)
        cur.execute(f"INSERT INTO strategies ({','.join(STRAT_COLS)}) VALUES ({','.join('?' * len(STRAT_COLS))})",
                    [r.get(c, "") for c in STRAT_COLS])
    con.commit()
    con.close()


def gen_group_indexes(base, tree):
    """Create _index.md where missing: one-line accounting of children."""
    made = 0
    for dirpath, dirs, files in os.walk(base):
        if os.path.basename(dirpath).startswith("."):
            continue
        idx = os.path.join(dirpath, "_index.md")
        if os.path.exists(idx):
            continue
        rel = os.path.relpath(dirpath, base).replace("\\", "/")
        group = "root" if rel == "." else rel
        lines = []
        for d in sorted(dirs):
            if d.startswith("."):
                continue
            n = sum(1 for _dp, _ds, fs in os.walk(os.path.join(dirpath, d))
                    for fn in fs if fn.endswith(".md") and fn != "_index.md")
            lines.append(f"- **`{d}/`** — {n} skill(s) below.")
        leaves = []
        for fn in sorted(files):
            if not fn.endswith(".md") or fn == "_index.md":
                continue
            fm, _b = C.parse_skill(os.path.join(dirpath, fn))
            if not fm:
                continue
            mp = fm.get("missingPersonsRelevance", "?")
            desc = C.oneline(fm.get("description", ""), 140)
            leaves.append(f"- **`{fm.get('id', fn[:-3])}`** ({mp}) — {desc}")
        fmh = {
            "name": f"{C.slugify(group)}-index",
            "description": f"Group index for {tree}/{group}: one-line accounting of children.",
            "kind": "group-index",
        }
        body = f"# {group}\n\n"
        if lines:
            body += "## Sub-groups\n" + "\n".join(lines) + "\n\n"
        if leaves:
            body += "## Skills here\n" + "\n".join(leaves) + "\n"
        body += "\n_Auto-generated by build_index.py; replace with curated prose anytime (it won't be overwritten)._\n"
        C.write_skill(idx, fmh, body)
        made += 1
    return made


def coverage_report(tools, strategies):
    from collections import Counter, defaultdict
    total = len(tools)
    full = sum(1 for t in tools if t.get("enrichment") == "full")
    by_cat = defaultdict(lambda: [0, 0])  # [total, full]
    for t in tools:
        c = by_cat[t.get("category", "?")]
        c[0] += 1
        if t.get("enrichment") == "full":
            c[1] += 1
    mp = Counter(t.get("missingPersonsRelevance", "?") for t in tools)
    trust = Counter(t.get("trust", "?") for t in tools)

    # deep-folders needing split: leaf-count per folder > 12
    fat = []
    for dirpath, _dirs, files in os.walk(C.TOOLS_DIR):
        leaves = [f for f in files if f.endswith(".md") and f != "_index.md"]
        if len(leaves) > 12:
            fat.append((os.path.relpath(dirpath, C.ROOT).replace("\\", "/"), len(leaves)))
    fat.sort(key=lambda x: -x[1])

    src = {}
    sp = os.path.join(C.LEDGER_DIR, "sources.json")
    if os.path.exists(sp):
        src = json.load(open(sp, encoding="utf-8"))

    out = ["# Coverage — generated by build_index.py\n"]
    out.append(f"**Tools:** {total} total · {full} full · {total - full} stub "
               f"({100 * full // total if total else 0}% enriched)\n")
    out.append(f"**Strategies:** {len(strategies)} total\n")
    out.append("## Tools by MP relevance\n" + " · ".join(f"{k}: {v}" for k, v in mp.most_common()) + "\n")
    out.append("## Tools by trust\n" + " · ".join(f"{k}: {v}" for k, v in trust.most_common()) + "\n")
    out.append("## Tools by category (full/total)\n")
    for cat in sorted(by_cat):
        tot, fu = by_cat[cat]
        out.append(f"- `{cat}` — {fu}/{tot}")
    out.append("\n## Folders needing a split (>12 leaves — go deeper)\n")
    out += [f"- `{p}` — {n} leaves" for p, n in fat[:40]] or ["- none"]
    out.append("\n## Source exhaustion (Go Deep)\n")
    for s in src.get("sources", []):
        out.append(f"- `{s['id']}` [{s['status']}] — {s.get('itemsFound', 0)} items — {s['tree']} — {s['url']}")
    with open(os.path.join(C.LEDGER_DIR, "coverage.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")


def main():
    os.makedirs(C.INDEX_DIR, exist_ok=True)
    tools = collect(C.TOOLS_DIR, LIST_FIELDS_TOOL)
    strategies = collect(C.STRATEGIES_DIR, STRAT_LIST_FIELDS) if os.path.isdir(C.STRATEGIES_DIR) else []
    write_json(os.path.join(C.INDEX_DIR, "tools.json"), tools)
    write_json(os.path.join(C.INDEX_DIR, "strategies.json"), strategies)
    write_csv(os.path.join(C.INDEX_DIR, "library.csv"), tools, TOOL_COLS, LIST_FIELDS_TOOL)
    write_csv(os.path.join(C.INDEX_DIR, "library-strategies.csv"), strategies, STRAT_COLS, STRAT_LIST_FIELDS)
    write_sqlite(os.path.join(C.INDEX_DIR, "library.sqlite"), tools, strategies)
    g1 = gen_group_indexes(C.TOOLS_DIR, "tools")
    g2 = gen_group_indexes(C.STRATEGIES_DIR, "strategies") if os.path.isdir(C.STRATEGIES_DIR) else 0
    coverage_report(tools, strategies)
    print(f"indexed tools={len(tools)} strategies={len(strategies)} | group-indexes created={g1 + g2}")


if __name__ == "__main__":
    main()
