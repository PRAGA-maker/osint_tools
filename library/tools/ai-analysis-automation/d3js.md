---
id: d3js
name: D3.js
description: Use when you have investigation data (relationships, timelines, geodata) and want to build custom interactive visualizations — provides a JavaScript library for bespoke charts and link graphs, not a data source.
url: https://d3js.org
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Building custom, interactive data visualizations (network/link graphs, timelines, maps) from investigation data.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open-source (ISC License); a client-side JavaScript library, no service or account.
opsec: passive
opsecNote: D3 runs locally in your own browser/page against data you supply — nothing is sent anywhere and no subject is queried. Keep sensitive datasets on machines you control; a D3 page is only as private as where you host it.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: python-lib
trust: trusted
trustNote: The de-facto open-source data-visualization library (by Mike Bostock/Observable), extremely widely used and audited; it's tooling for building visuals, so accuracy depends on your data and code.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- D3
- d3js.org
- Data-Driven Documents
tags:
- visualization
- link-analysis
- charts
- javascript
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# D3.js

> The standard open-source library for building bespoke, interactive data visualizations in the browser — the toolkit behind custom link graphs, timelines, and maps when off-the-shelf charts won't do.

## When to use
D3 is a *presentation/analysis* tool, not a data source. Reach for it when your investigation has produced structured data — a network of `associate`s, a timeline of events, geodata of sightings — and you need a visualization that existing tools can't render the way you want: an interactive relationship graph, a custom timeline, a themed map. It's the right choice when you're building a reusable analytic view or a report figure and need full control; for quick graphs, a higher-level tool is faster.

## How to use it (`bestInteractionPattern`: python-lib)
1. Get D3 from https://d3js.org (npm `d3`, or a script include for a quick page).
2. Prepare your data as JSON/CSV (e.g. nodes+links for a network graph).
3. Write D3 code binding the data to SVG/Canvas elements (or start from an Observable/example template — force-directed graph, timeline, choropleth).
4. Add interactivity (zoom, drag, tooltips, filtering) to explore the data.
5. Pivot: use the visualization to spot clusters/outliers in your data, then investigate those nodes with the concrete lookup tools in this library.

## Inputs → Outputs
- **In:** none (your own structured investigation data — no external selector)
- **Out:** none directly — an interactive visualization you can read and share
- **Empty/negative result looks like:** a blank/broken render — usually a data-binding or scale bug, not "no data"; check the console and the data shape.

## Gotchas & OpSec
- Human-in-the-loop: you write the code and interpret the visual (`manual-review`); D3 is low-level, so expect real development effort.
- It visualizes whatever you feed it — garbage in, misleading graph out; validate your data first.
- For simple charts, higher-level libraries (or a link-analysis app like Maltego) are much faster.

## Overlaps ("do both")
- Complements dedicated link-analysis tools (Maltego, Gephi): those give ready-made graphs from imported data, while D3 gives full custom control — use the ready-made tool to explore, D3 to build a tailored final visualization.

## Trust & verifiability
`trust: trusted` — a mature, ubiquitous open-source library; it's reliable *infrastructure*, but the correctness of any visualization rests entirely on your data and code, so verify both.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | d3js |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | python-lib |
| opsec | passive |
| human-in-loop | yes (manual-review) |
