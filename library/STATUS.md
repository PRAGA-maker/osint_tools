# OSINT Skill Library — Status (2026-06-13)

A knowledge base for long-running Claude agents working **missing-persons** cases. Two skill trees + one schema + a generated cross-sectional DB + a self-extending harvest rig.

## What's in it now

| | count | notes |
|---|---|---|
| **Tools** (`tools/`) | **3,670** | one `.md` skill per tool, ≤5-deep category tree, deduped, categorized |
| — full (authored/harvested-rich) | ~170 | rich description + selectors |
| — stub (valid frontmatter, thin body) | ~3,500 | enrichment backlog, tracked |
| **Strategies** (`strategies/`) | **80** | pivot-graph over phases; patterns/antipatterns/techniques/playbooks/case-studies |
| **Group-index nav skills** (`_index.md`) | ~250 | one-line accounting per folder |
| **Sources tracked** (`ledger/sources.json`) | 31 | 12 tools + 5 strategy sources mined; 14 queued for wave 2 |
| **Validation** | **0 errors** | `scripts/validate.py` green; 346 same-domain "do both" overlap hints |

## How to use it

- **Browse the tree:** start at `tools/_index.md` / `strategies/_index.md`, descend via `_index.md` group skills.
- **Cross-sectional query (the DB):** `index/library.sqlite`, `index/tools.json`, `index/library.csv`.
  ```sql
  SELECT id,name,url FROM tools
  WHERE pricing IN('free','freemium') AND opsec='passive'
    AND missingPersonsRelevance='high'
    AND selectorsIn LIKE '%face%' AND selectorsOut LIKE '%name%';
  ```
- **Schema/vocab:** `schema/taxonomy.md` (selectors, trust rubric, interaction patterns, phases).
- **Add/maintain:** `scripts/new_skill.py`, then `scripts/build_index.py` (rebuild DB+coverage+nav) and `scripts/validate.py`.

## The rig (Go Deep / Go Beyond)

- **Go Deep** — `ledger/sources.json` tracks every source to `exhausted`; `ledger/coverage.md` shows stub-vs-full and folders that need splitting.
- **Go Beyond** — `ledger/go-beyond.md` is the frontier log; every harvest agent appends newly-found directions. Wave 1 already surfaced 14 new sources (MetaOSINT, Bellingcat Toolkit, cyb_detective, sinwindie/OSINT, osintambition, IntelTechniques, cupidcr4wl, ...).

## What was done this session

1. Schema + taxonomy + templates + spec + 5 working scripts (seed, index, validate, 2× ingest).
2. Seeded 1,138 tools from the forked OSINT-Framework `arf.json`.
3. Harvest wave 1 (background workflows + agents): +2,532 tools across 12 sources; 63 strategies across 5 sources — all deduped, categorized, schema-valid.
4. Hand-authored strategy exemplars + skeleton (phases, pivots, patterns, antipatterns, playbooks, platforms).
5. Full DB + coverage + frontier ledger.

## Next steps (queued, not yet done)

- **Wave 2 harvest** of the 14 queued frontier sources (`status: queued` in `sources.json`).
- **Kimi Agent Swarm + Trace Labs Discord** pass via Chrome MCP (interactive; resource/technique channels only, PII-free) — `kimi-swarm` and `tl-discord` sources.
- **Enrichment pass:** upgrade high-MP stub tools (`enrichment: stub`) to full skills by reading each tool's actual site (better than list one-liners).
- **Dead-link prune:** `python scripts/validate.py --check-links` (network-heavy) to retire dead URLs.
- **Cross-link overlaps:** wire `relatedTools` for the 346 same-domain "do both" groups.
