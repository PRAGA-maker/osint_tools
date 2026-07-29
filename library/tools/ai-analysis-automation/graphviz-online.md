---
id: graphviz-online
name: Graphviz Online
description: Use when you have relationship/entity data in DOT format and want a rendered graph in the browser — returns a visual link diagram exportable as SVG/PNG.
url: https://dreampuf.github.io/GraphvizOnline/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Rendering DOT-language graphs (entity/relationship diagrams) in-browser without installing Graphviz.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free, open-source, client-side page (GitHub Pages); no account. Rendering happens in your browser.
opsec: passive
opsecNote: It renders DOT locally in your browser (via a client-side Graphviz build) — your graph data is not uploaded to a server, so it's safe for sensitive relationship data. Still, treat the page like any web page: keep highly sensitive graphs offline/local Graphviz if you need zero third-party JS in the loop.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A popular open-source wrapper around Graphviz's own rendering engine (Viz.js); the layout is produced by Graphviz, a trusted, decades-old tool.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- gephi
- nodebox
aliases:
- Graphviz Online
- GraphvizOnline
tags:
- data-visualization
- graph
- link-analysis
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# Graphviz Online

> A zero-install, in-browser renderer for Graphviz DOT graphs — paste a DOT description of your entities and links and get a laid-out diagram you can export.

## When to use
A **visualization-support** tool, not a data source. Once you've mapped an investigation's relationships — people, accounts, phones, addresses and how they connect — you can express them in DOT and have Graphviz Online lay them out as a clean link diagram for analysis or a report. Reach for it when you want a quick, precise graph and don't need a full interactive analysis suite. It takes no subject selector and produces no new intelligence.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://dreampuf.github.io/GraphvizOnline/.
2. Write/paste your graph in DOT: e.g. `digraph { "Jane" -> "+15551234"; "Jane" -> "acme-llc"; }`.
3. Pick a layout engine (dot, neato, circo, twopi, fdp) to suit the graph shape.
4. It renders live; export as SVG/PNG for your report.
5. For large/interactive graphs, move to a dedicated tool (`[[gephi]]`).

## Inputs → Outputs
- **In:** none of the person selectors — a DOT graph description you write
- **Out:** a rendered link/entity diagram (SVG/PNG/other), no new data
- **Empty/negative result looks like:** a DOT syntax error or blank render — fix the DOT; there is no "query result" to interpret.

## Gotchas & OpSec
- **Not analysis, just drawing** — it lays out exactly the relationships you encode; it won't discover or infer links.
- Best for small/medium static graphs; big datasets need Gephi/Maltego-class tools.
- OpSec: **passive/local** — rendering is client-side, so your relationship data isn't uploaded.

## Overlaps ("do both")
- Compare with `[[gephi]]` and `[[nodebox]]` — Gephi for large interactive network analysis, NodeBox for custom generative visuals; Graphviz Online is the fastest path to a clean, precise static link diagram from hand-written DOT.

## Trust & verifiability
`trust: community` — an open-source front end to Graphviz's own authoritative layout engine; what you see is a faithful rendering of the DOT you supply.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | graphviz-online |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
