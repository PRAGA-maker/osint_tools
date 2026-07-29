---
id: observable
name: Observable
description: Use when you have a dataset and want to explore/visualize it interactively in the browser — a JavaScript notebook platform for building and sharing OSINT data analyses.
url: https://observablehq.com/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Building interactive, reproducible data visualizations and analyses (networks, timelines, maps) from investigation data in a browser notebook.
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
costNote: Free tier covers public notebooks and personal use; paid plans add private notebooks, collaboration and larger data. Open-source pieces (D3, Observable Plot, the Framework) are free to self-host.
opsec: passive
opsecNote: Observable runs your code and can host your notebooks. By default a hosted notebook may be PUBLIC — never paste raw case data, PII, or a subject's identifiers into a public notebook. For sensitive work use private notebooks (paid), run Observable Framework locally/offline, or strip data to non-identifying form before uploading.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A reputable data-viz platform from the team behind D3.js; the tooling is well-regarded. Trust concerns are operational (accidental public exposure of your data), not tool integrity.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- what-goes-on-mastodon
aliases:
- ObservableHQ
- Observable notebooks
tags:
- infographics-and-data-visualization
- data-analysis
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# Observable

> A browser-based JavaScript notebook platform (from the makers of D3.js) for interactive data exploration and visualization — the analysis/presentation layer for OSINT data you've already collected.

## When to use
You have structured data from an investigation — a scrape, an exported dataset, a list of relationships or events — and want to explore, transform, and **visualize** it: force-directed network graphs of associates, timelines, geographic maps, or charts to spot patterns. Observable lets you write live JS (with D3/Observable Plot) in reactive cells and publish an interactive result. It's an analysis/communication tool, not a collector — it produces no subject data on its own.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to observablehq.com and start a notebook (or run Observable Framework locally for offline/private work).
2. Load your data (upload a file attachment, paste JSON/CSV, or fetch from an API) — see OpSec before uploading anything sensitive.
3. Write reactive cells to clean/transform the data and build visuals with Observable Plot or D3.
4. Iterate interactively; add inputs/sliders to explore.
5. Keep it **private** (or local) for casework; publish only sanitized, shareable analyses.

## Inputs → Outputs
- **In:** your own dataset (not a subject selector)
- **Out:** interactive charts, network graphs, maps, and reproducible analysis notebooks
- **Empty/negative result looks like:** N/A — it visualizes what you give it; the failure mode is messy input producing a misleading chart, so validate the data first.

## Gotchas & OpSec
- **Default-public risk:** hosted notebooks can be public — never put PII/case data in a public notebook; use private notebooks or run locally.
- It's a viz layer, not evidence — a compelling graph can overstate weak data; keep provenance for every point.
- Requires some JavaScript comfort; for no-code needs, a simpler charting tool may fit better.

## Overlaps ("do both")
- Complements collection/scraping tools (they gather; Observable analyzes) and other charting libraries like `[[highcharts]]` — choose Observable when you want reactive, code-driven exploration rather than a drop-in chart widget.

## Trust & verifiability
`trust: community` — a well-regarded platform from the D3.js team; the tooling is solid, and the only real caution is operational: don't leak sensitive data through a public notebook.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | observable |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
