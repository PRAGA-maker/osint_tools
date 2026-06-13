# OSINT Skill Library

A knowledge base for long-running Claude agents working **missing-persons** cases. Two interlocking trees of Markdown skills, one shared schema, a generated cross-sectional DB, and a self-extending harvest rig.

## The two trees

- **`tools/`** — one `.md` skill per tool (free / freemium-with-real-free-tier only). Organized into a category tree, ≤5 deep, ~5 leaves per end node. Every folder has a `_index.md` group skill (one-line accounting of its children).
- **`strategies/`** — investigator reasoning as a **pivot graph over phases**: patterns, antipatterns, techniques, playbooks, case studies. A strategy says "you have selector X, here's how to reach selector Y."

The two trees share a **selector vocabulary** (`schema/taxonomy.md`), so tools' `selectorsIn/Out` and strategies' `pivotFrom/To` line up into one graph.

## How a skill file is shaped

1. **YAML frontmatter** — authoritative, machine-read record (valid Claude skill: has `name` + `description`, plus all schema fields).
2. **Prose body** — when to use, step-by-step *how* (via `bestInteractionPattern`), inputs→outputs, gotchas, opsec, cross-links.
3. **Bottom metadata table** — generated datasheet, never hand-edited.

Copy `schema/templates/tool.template.md` or `strategy.template.md` to start one.

## The DB (cross-sectional search)

`scripts/build_index.py` walks all frontmatter → `index/tools.json`, `index/strategies.json`, `index/library.csv`, `index/library.sqlite`. Use the DB for non-tree queries:

```sql
-- free, passive, high-MP tools that take a face and yield a name
SELECT id, name, url FROM tools
WHERE pricing IN ('free','freemium') AND opsec='passive'
  AND missingPersonsRelevance='high'
  AND selectorsIn LIKE '%face%' AND selectorsOut LIKE '%name%';
```

## The rig (Go Deep / Go Beyond)

- **`ledger/sources.json`** — every source we mine, with `status` queued→crawling→exhausted. **Go Deep:** nothing is "done" until its source reads `exhausted`.
- **`ledger/go-beyond.md`** — the frontier. Every harvest agent MUST append newly-discovered directions (new GitHub tags, boards, DBs, categories). The human reads this to find new ground.
- **`ledger/coverage.md`** — generated report: stub vs full counts, per-source exhaustion, per-category depth.

## Conventions

- ids are kebab-case, unique per tree; filename is `<id>.md`.
- Cross-link with `[[id]]` in prose and `relatedTools` / `relatedStrategies` / `toolsUsed` in frontmatter.
- Overlapping tools: keep both, link them, note when to run together ("do both").
- Set `trust` fast via the rubric in `taxonomy.md`; default fresh finds to `unverified`.
- **No paid-only tools.** Freemium only if a useful free tier exists; record what's gated in `costNote`.

## Scripts

| script | does |
|---|---|
| `scripts/build_index.py` | frontmatter → `index/` (json, csv, sqlite) + regenerates bottom metadata tables |
| `scripts/validate.py` | required-field + enum + dead-link + dedup-by-domain checks |
| `scripts/seed_from_arf.py` | `public/arf.json` → stub tool skills (breadth seed) |
| `scripts/new_skill.py` | scaffold a tool/strategy from a template |
