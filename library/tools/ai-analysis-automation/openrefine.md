---
id: openrefine
name: OpenRefine
description: Use when you have a messy dataset from an investigation (scraped records, leaks, exports) and need to clean, cluster, and reconcile it — a local tool for wrangling tabular data before analysis.
url: https://github.com/OpenRefine
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Cleaning, deduplicating, clustering, and reconciling messy tabular data (CSV/JSON/etc.) locally.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: OpenRefine runs locally (a server on your own machine, viewed in the browser), so your data never leaves your host unless you deliberately use a reconciliation service or fetch-URLs feature — those DO send data out, so disable/avoid them for sensitive datasets. Ideal for handling case data offline.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: trusted
trustNote: Mature, well-known open-source data-wrangling tool (formerly Google Refine); runs offline and is widely used in data journalism and OSINT.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- OpenRefine
- Google Refine
tags:
- data-cleaning
- data-wrangling
- reconciliation
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# OpenRefine

> A local power tool for messy data — load a scraped or leaked dataset and clean, cluster, dedupe, and reconcile it into something you can actually analyze, all offline on your own machine.

## When to use
Not a collection tool — a processing one. When an investigation produces a messy table (scraped listings, a breach dump, a public-records export, harvested profiles) with inconsistent names, duplicate rows, or mixed formats, OpenRefine turns it into clean structured data. Its clustering finds near-duplicate values (e.g. "Jon Smith" / "John Smith"), and reconciliation can match entities to external identifiers — invaluable before you pivot on names, addresses, or orgs.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Install OpenRefine (Java app) from openrefine.org / the GitHub releases; it launches a local server you use in your browser at `127.0.0.1:3333`.
2. Create a project by importing your data (CSV, TSV, JSON, XML, Excel).
3. Clean it: facet/filter columns, use text-clustering to merge variant spellings, split/merge cells, apply GREL transforms, and dedupe.
4. Optionally reconcile against external services (Wikidata, etc.) to attach identifiers, then export the cleaned dataset for analysis or import into other tools.

## Inputs → Outputs
- **In:** a tabular/structured dataset (no single OSINT selector — it processes whatever records you load)
- **Out:** a cleaned, deduplicated, optionally entity-reconciled dataset
- **Empty/negative result looks like:** clustering finds no groups or reconciliation no matches — the data may already be clean or the reconciliation source lacks the entities; adjust the method/threshold.

## Gotchas & OpSec
- Human-in-the-loop: none, though effective use is interactive.
- OpSec: local by default — data stays on your machine. But reconciliation and "add column by fetching URLs" send data to external services; disable them for sensitive case data.
- It's for structuring data, not collecting it; garbage in still needs judgment out — clustering suggestions must be reviewed, not blindly merged.

## Overlaps ("do both")
- Complements collection/automation tools ([[spiderfoot]], scrapers, [[google-colaboratory]] notebooks) — those gather raw data, OpenRefine cleans and reconciles it before you analyze or visualize.

## Trust & verifiability
`trust: trusted` — a mature, widely-adopted open-source tool (ex-Google Refine) standard in data journalism. It's dependable for wrangling; the correctness of merges/reconciliations is your call, so review its suggestions before committing them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | openrefine |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | no |
