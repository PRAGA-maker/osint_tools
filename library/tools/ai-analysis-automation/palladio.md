---
id: palladio
name: Palladio
description: Use when you have tabular relationship data (people, places, dates, links) and want to visualise it as a network graph, map, or timeline — an analysis tool for seeing connections, not a data source.
url: http://hdlab.stanford.edu/palladio
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Turning a spreadsheet of entities and relationships into interactive network graphs, maps, and filtered lists.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open source (MIT), from Stanford's Humanities + Design lab.
opsec: passive
opsecNote: Runs in your browser on data you paste/upload; nothing is queried about a subject and (for the classic client-side app) your data stays local. Still, don't upload sensitive case data to any hosted instance you don't control.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Academic tool maintained by Stanford's Humanities + Design lab; open source and widely used for historical/network analysis.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Stanford Palladio
tags:
- infographics-and-data-visualization
- network-analysis
- link-analysis
source: awesome-osint
lastVerified: '2026-07-23'
relatedTools:
- highwire-free-online-full-text-articles
- regular-expression-analyzer
- stanford-large-network-dataset-collection
- swap-stanford-edu
---

# Palladio

> A free, browser-based data-visualisation tool for relationships: feed it a table of entities and links and it draws network graphs, maps, and filterable views so patterns and connections surface.

## When to use
This is analysis tooling, not a collector. Use it when you've gathered structured data — a list of people and their associates, addresses over time, accounts and the entities behind them — and want to *see* the structure: who connects to whom, which nodes are central, how things cluster geographically or over time. It turns a spreadsheet of findings into an interactive graph/map for spotting links you'd miss in rows.

## How to use it (`bestInteractionPattern`: web-manual)
1. Prepare your data as a table (columns for the entities and the relationship between them).
2. Open the Palladio app and load the data (paste, drag-and-drop a .csv/.tsv, or link a public file).
3. Build views: **Graph** (network of two dimensions, e.g. person→associate), **Map** (if you have coordinates), **List**/**Gallery** for filtered browsing.
4. Filter and facet to isolate subsets; export Graph/Map as SVG or List as CSV for your report.
5. Pivot: a central node or unexpected link in the graph tells you where to dig next with data-source tools.

## Inputs → Outputs
- **In:** your own tabular relationship data (no subject selector — you supply what you've gathered)
- **Out:** interactive network graph, map, and filtered views; exportable SVG/CSV
- **Empty/negative result looks like:** a sparse/disconnected graph — usually means thin or poorly-structured input, not that no relationships exist.

## Gotchas & OpSec
- Garbage in, garbage out: the visualisation only reflects the data you provide; it adds no external intelligence.
- Data prep (consistent entity names, clean columns) determines whether the graph is legible.
- OpSec: **passive** and local for the classic app; keep sensitive case data off any hosted instance you don't control.

## Overlaps ("do both")
- Pairs with heavier link-analysis tools (Maltego, Gephi) and note tools like `[[logseq]]` — Palladio is quick and free for exploring relationships; dedicated graph platforms scale further.

## Trust & verifiability
`trust: trusted` — a reputable open-source academic tool; it faithfully renders your data, so verifiability rests on the sourcing of the data you feed it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | palladio |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
