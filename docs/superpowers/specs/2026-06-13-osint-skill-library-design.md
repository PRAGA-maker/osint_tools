# OSINT Skill Library — Design Spec

**Date:** 2026-06-13
**Owner:** Praneel Patel
**Context:** Anthropic hackathon — long-running Claude agents that solve missing-persons cases. This library is the knowledge base those agents read from.

> Standing instruction: **do not `git commit` or `git push`** in this work. This spec is a working document, not a committed artifact.

## 1. Purpose

Build two interlocking, exhaustive trees of Markdown skill files that a Claude agent can read top-down to investigate a missing-persons case:

1. **Tools** — every free / freemium-with-usable-free-tier OSINT tool, one `.md` skill per tool, organized in a category tree (≤5 deep, ~5 leaves per end node).
2. **Strategies** — the reasoning of good investigators: patterns, antipatterns, techniques, playbooks, and case studies, organized as a **pivot graph layered over investigation phases**.

Both trees share one schema and feed a flat, generated **DB** (`index/`) for cross-sectional, non-tree queries ("all free, passive, high-MP-relevance tools that take a face and output a name").

The library is also a **self-extending rig**: it carries its own bookkeeping (`ledger/`) so an agent knows which sources are exhausted (**Go Deep**) and surfaces newly-discovered directions to the human (**Go Beyond**).

## 2. Non-goals

- No paid-only tools. Freemium is allowed only if a genuinely useful free tier exists; note what's gated in `costNote`.
- No verbatim archiving of private community chat. Discord/forum mining extracts *tools and techniques*, not conversations.
- Not a runtime/agent — this is the knowledge base. The agent that uses it is separate.

## 3. Layout

```
library/
  README.md                  # how the library works + schema summary + conventions
  schema/
    tool.schema.json         # JSON Schema (draft-07) for tool frontmatter
    strategy.schema.json     # JSON Schema for strategy frontmatter
    taxonomy.md              # controlled vocab: categories, selectors, phases, trust, interaction patterns
    templates/
      tool.template.md
      strategy.template.md
      group-index.template.md
  tools/        <cat>/<sub>/<sub>/<tool>.md   + _index.md per node
  strategies/   <phase|pivot>/.../<strategy>.md + _index.md per node
  index/        tools.json · strategies.json · library.csv · library.sqlite   (generated)
  ledger/
    sources.json             # Go Deep: every source + status + counts
    go-beyond.md             # Go Beyond: newly-surfaced directions to chase
    coverage.md              # generated: enriched vs stub, per-source exhaustion
  scripts/
    build_index.py           # walk MD frontmatter -> index/{json,csv,sqlite}
    validate.py              # schema-check + dead-link + dedup-by-domain
    seed_from_arf.py         # arf.json -> stub tool skills (breadth seed)
    new_skill.py             # scaffold a tool/strategy from template
```

The forked OSINT-Framework files (`public/arf.json`, `src/`, viz) stay in place purely as **seed + reference**. They are not the product and are not kept in sync.

## 4. Each `.md` is a valid Claude skill AND a datasheet

- **Frontmatter (YAML, top):** authoritative machine-readable record. Includes `name` + `description` (so it's a valid skill) plus all schema fields. The indexer reads frontmatter.
- **Body:** skill prose — when to use, step-by-step *how* (via `bestInteractionPattern`), inputs→outputs, gotchas, opsec, cross-links.
- **Bottom:** a human-readable **metadata table**, generated from frontmatter (so it can't drift) — the "schema at the bottom."

Every tree **node** (folder) also gets a `_index.md` **group skill**: a one-line accounting of each child, so an agent can navigate the tree by reading indexes top-down without opening every leaf.

## 5. Schema (summary; full enums in `schema/taxonomy.md`)

**Tool (required: id, name, url, category, description, trust, pricing, missingPersonsRelevance, bestInteractionPattern):**
`id, name, url, category, path[], description, bestFor, input, output, selectorsIn[], selectorsOut[], status, pricing(free|freemium), costNote, opsec(passive|active), opsecNote, humanInLoop, humanInLoopReason[], bestInteractionPattern, trust, trustNote, missingPersonsRelevance, coverage[], auth, api, localInstall, registration, invitationOnly, deprecated, relatedTools[], aliases[], tags[], source, lastVerified`.

**Strategy (required: id, name, type, summary, missingPersonsRelevance):**
`id, name, type(pattern|antipattern|technique|case-study|playbook|pivot), phase, pivotFrom[], pivotTo[], platforms[], summary, whenToUse, steps[], signals[], pitfalls[], toolsUsed[], evidence[], trust, missingPersonsRelevance, relatedStrategies[], tags[], source`.

`selectorsIn/Out` (tools) and `pivotFrom/To` (strategies) share one selector vocabulary, which is what makes the two trees a single navigable graph.

## 6. The four named problems

- **Overlapping tools → "do both, tokenmaxx":** `validate.py` flags same-domain overlaps; we keep both and cross-link via `relatedTools`, with the body noting when to run them together.
- **Verifiability:** `trust` set by the rubric in `taxonomy.md` (official/known-maintainer → community repo → one-person hobby → unknown).
- **Safety:** skills flag tools that run untrusted local code or need creds; light sandbox/opsec notes. Not over-indexed.
- **Go Beyond:** every harvest agent MUST emit "new directions found" into `go-beyond.md`; reports surface them.
- **Go Deep:** `sources.json` tracks each source to `exhausted`; `coverage.md` shows half-mined sources and stub-vs-enriched counts.

## 7. Harvesting rig

Repeatable Workflow: seed ledger from arf.json + entrypoint URLs → fan-out harvest wave (one source per subagent, returns schema-valid candidates + frontier directions) → dedup/merge by domain → write `.md` skills (with trust + MP-relevance) → rebuild DB → coverage/frontier report → loop until sources exhaust and frontier stops growing.

- **Autonomous (in Workflow now):** web (WebFetch/WebSearch) + GitHub topic/repo crawl.
- **Browser-driven (main loop, Chrome MCP):** Kimi Agent Swarms (per `using-kimi-for-research`), Trace Labs Discord pins + resource/technique channels (PII-free channels only, technique extraction not transcription).

## 8. Seed strategy

`seed_from_arf.py` converts all ~1,168 arf.json leaves into **stub** tool skills (frontmatter mapped from existing JSON fields; body templated; `trust/MP-relevance/selectors` left for enrichment). This yields full breadth immediately. Enrichment waves upgrade stubs → full skills; `coverage.md` tracks the backlog. MP-critical branches (People Search, Social, Image/Face/Geo, Phone, Missing-Persons DBs) are authored to full 5-deep depth as exemplars this session.

## 9. Entrypoint sources (seed `sources.json`)

Tools: castrickclues.com · start.me/p/L1rEYQ/osint4all · start.me/p/DPYPMz/the-ultimate-osint-collection · github tracelabs/awesome-osint · github topics (osint-resources, osint-framework, footprinting, reconnaissance, intelligence-gathering) · github h1lw/xsint · osint-news.com/category/tools · TL Discord resource channels · Kimi swarm deep-dives.
Strategies: tracelabs/tofm · tracelabs/searchparty-ctf-writeups · OSINTI4L/TraceLabs-CTF-MVO-Write-up-11.25 · OSINTI4L user repos · uncovered.com/cases?classification=missing · social-platform technique writeups.

## 10. Success criteria

- Both trees scaffolded; schema + DB generator working; `validate.py` green.
- Full breadth seeded; MP-critical branches authored to depth as exemplars.
- ≥1 harvest wave completed with dedup + frontier surfacing.
- `coverage.md` and `go-beyond.md` populated so the work is resumable and the human sees new directions.
