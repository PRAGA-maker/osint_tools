---
id: vis-js
name: Vis.js
description: Use when you have entities and relationships (`associate` links, comms, infrastructure) and want an interactive link/timeline chart — a browser visualization library you build charts with (no selectors).
url: http://visjs.org
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Building interactive network/link-analysis graphs and timelines from your own relationship data.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open source (community-maintained, CC BY-SA / MIT components) via npm and CDN.
opsec: passive
opsecNote: Vis.js runs in your own browser/page and renders data you already hold — it makes no external calls about a subject and leaks nothing. If you publish a graph, remember the rendered data (names, links) is embedded in the page; keep case charts local or access-controlled.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: python-lib
trust: community
trustNote: Long-standing open-source visualization library maintained by the vis.js community on GitHub; it is a code library, not a hosted service, so it does exactly what your code tells it.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
aliases:
- visjs
- vis-network
- vis-timeline
tags:
- infographics-and-data-visualization
- link-analysis
source: awesome-osint
lastVerified: '2026-08-05'
enrichment: full
---

# Vis.js

> A browser-based visualization library (Network, Timeline, Graph2d/3d) — the build-it-yourself option for turning an investigation's entities and links into an interactive chart.

## When to use
You have assembled relationship data — people and their `associate`s, phones calling phones, domains sharing infrastructure, events on a timeline — and you want to *see* the structure interactively rather than in a table. Vis.js is a developer library you feed nodes and edges to; it renders an explorable network or timeline in a web page. It is for the analysis/presentation stage and requires a little coding; it does not gather data.

## How to use it (`bestInteractionPattern`: python-lib)
1. Add vis-network / vis-timeline via npm or a CDN `<script>` (it is a JavaScript library, usable from a small HTML page or a notebook).
2. Shape your data as `nodes` (entities) and `edges` (relationships), or a timeline dataset.
3. Instantiate the component in a container element; configure physics/layout for readability.
4. Interact — drag, zoom, cluster — to spot hubs, bridges, and isolated clusters in the graph.
5. Pivot: a high-degree node or an unexpected bridge between clusters flags who/what to investigate next.

## Inputs → Outputs
- **In:** your own nodes/edges (entities + relationships) or timeline events
- **Out:** an interactive network/timeline visualization — presentation, no personal selectors
- **Empty/negative result looks like:** a blank or hairball graph — usually a data-shaping issue (bad ids, no edges) or too many nodes without clustering, not an analytical finding.

## Gotchas & OpSec
- Human-in-the-loop: it is a library — you (or a script) must wire the data in; no GUI upload.
- OpSec: passive and local; it renders data you supply and calls nothing external. A published graph embeds its data, so keep sensitive charts private.
- Very large graphs need clustering/performance tuning; naive rendering of thousands of nodes bogs down.

## Overlaps ("do both")
- Pairs with heavier graph tooling (Maltego-style link tools, `[[graphx]]` for large-scale computation) — Vis.js is the lightweight, self-hosted rendering layer when you want a custom, embeddable chart rather than a full platform.

## Trust & verifiability
`trust: community` — a mature, widely-used open-source library; there is nothing to "trust" in output terms beyond the correctness of the data and code you feed it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | vis-js |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | python-lib |
| opsec | passive |
| human-in-loop | no |
