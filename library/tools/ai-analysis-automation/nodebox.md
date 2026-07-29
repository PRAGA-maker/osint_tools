---
id: nodebox
name: NodeBox
description: Use when you have a dataset (connections, entities) and want to build custom node-based visualizations without heavy coding — returns generative graphics/data visuals, not intelligence.
url: https://www.nodebox.net
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Node-based, low-code data visualization and generative graphics from a prepared dataset.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open-source (NodeBox 3); desktop app, source on GitHub, content under Creative Commons.
opsec: passive
opsecNote: Runs locally on data you feed it — nothing is sent anywhere, so it leaks nothing about your case. The only care needed is handling the underlying investigative data securely on your machine.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: community
trustNote: An established open-source creative-coding/data-viz project; reputable, but a design tool rather than an OSINT-specific one.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- gephi
- maltego
aliases:
- NodeBox
- nodebox.net
tags:
- data-visualization
- generative
- analysis
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# NodeBox

> An open-source, node-based tool for data visualization and generative graphics — build a custom visual of your data by wiring nodes together, no heavy programming required.

## When to use
This is a **presentation/analysis-support** tool, not a data source. Once you've *collected* an investigation's data — an entity/relationship list, a timeline, a set of coordinates — NodeBox lets you turn it into a bespoke visual (network diagram, timeline graphic, custom chart) by connecting processing nodes. Reach for it when off-the-shelf link-analysis output isn't the shape you need and you want fine control over the visualization. It takes no subject selector and produces no new intelligence.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download NodeBox 3 from https://www.nodebox.net (or build from GitHub) and install.
2. Import/prepare your data (CSV/structured input) locally.
3. Wire nodes to filter, map, and lay out the data into the visual you want.
4. Iterate on the node graph; export the graphic for your report/briefing.
5. Keep the source data secure — the value is *your* investigative data, not the tool.

## Inputs → Outputs
- **In:** none of the person selectors — a prepared dataset you supply
- **Out:** a custom visualization/graphic (no new personal data)
- **Empty/negative result looks like:** N/A — output is whatever your node graph renders; a blank result means your data/wiring, not a query miss.

## Gotchas & OpSec
- **Not an OSINT collection tool** — it visualizes data you already have; expectations should be about presentation, not discovery.
- Learning curve for the node paradigm; for standard link analysis a purpose-built tool may be faster.
- OpSec: **passive/local** — nothing leaves your machine; secure the underlying data.

## Overlaps ("do both")
- Compare with `[[gephi]]` and `[[maltego]]` — Gephi/Maltego are purpose-built for network/link analysis and will be faster for entity graphs; use NodeBox when you need a *custom* or generative visual they can't produce.

## Trust & verifiability
`trust: community` — a legitimate, open-source design tool; it's trustworthy software, just general-purpose rather than OSINT-specific.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nodebox |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | no |
