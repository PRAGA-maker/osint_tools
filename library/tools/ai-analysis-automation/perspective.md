---
id: perspective
name: Perspective (FINOS)
description: Use when you have a large or streaming dataset (call records, transactions, scraped rows) and want to pivot, chart, and explore it interactively — a local analysis engine, not a selector lookup.
url: https://github.com/finos/perspective
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Interactively slicing and visualising large tabular/streaming datasets during analysis.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open-source (Apache-2.0), maintained under the OpenJS/FINOS foundation; runs locally with no service fees.
opsec: passive
opsecNote: Runs entirely on your own machine (WebAssembly in-browser, or the Python/Node/Rust library) — data never leaves your host unless you deliberately wire it to a remote source. Ideal for analysing sensitive case data offline.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: python-lib
trust: trusted
trustNote: A well-known open-source project governed by FINOS (Fintech Open Source Foundation) / OpenJS, originally built at J.P. Morgan; source is public and auditable.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
relatedTools:
- jupyter
- gephi
aliases:
- FINOS Perspective
- perspective-python
tags:
- infographics-and-data-visualization
- data-analysis
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# Perspective (FINOS)

> An open-source, in-browser/notebook analytics engine for large and streaming datasets — the pivot-and-chart layer for data you've already collected, run entirely on your own machine.

## When to use
You have accumulated a large structured dataset in an investigation — exported call/message logs, transaction rows, scraped social records, a breach dump normalised to a table — and need to explore it: pivot, filter, aggregate, and chart to find the outlier, the cluster, or the timeline. Perspective ingests big or continuously-updating tables and gives you an interactive grid and 10+ chart types without shipping the data to any cloud service.

## How to use it (`bestInteractionPattern`: python-lib)
1. Install: `pip install perspective-python` (or use the `@finos/perspective` JS package / prebuilt WebAssembly build).
2. Load your data — a Pandas/Polars DataFrame, Apache Arrow table, CSV, or a live stream.
3. In a Jupyter notebook, create a `PerspectiveWidget(df)`; in a browser app, mount the `<perspective-viewer>` custom element and feed it the table.
4. Interactively configure pivots, filters, sorts, and computed-column expressions; switch between datagrid, line, bar, heatmap, treemap, and other views to spot patterns.
5. Pivot: an entity or cluster you surface here feeds targeted lookups; export findings for a report or into `[[gephi]]` for network graphing.

## Inputs → Outputs
- **In:** a dataset (DataFrame / Arrow / CSV / stream) — not an OSINT selector
- **Out:** interactive pivots, filtered slices, and charts; a workbench, not a new selector value
- **Empty/negative result looks like:** n/a — it visualises whatever you load; a blank view means an empty/misparsed input table.

## Gotchas & OpSec
- This is analysis infrastructure, not a data source — it finds nothing on its own; you must already have the data.
- Building the C++/WASM core from source is heavy; use the published `pip`/`npm` binaries.
- OpSec: fully local by default — a strong choice for sensitive datasets, since nothing is uploaded unless you explicitly configure a remote data source.

## Overlaps ("do both")
- Pairs with `[[jupyter]]` (its natural host) and `[[gephi]]` — Perspective is best for tabular pivot/aggregation, Gephi for relationship/network graphs; use each for the shape of question it fits.

## Trust & verifiability
`trust: trusted` — an audited open-source project under FINOS/OpenJS governance (originating at J.P. Morgan); the code is public, so its behaviour is verifiable.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | perspective |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | python-lib |
| opsec | passive |
| human-in-loop | no |
