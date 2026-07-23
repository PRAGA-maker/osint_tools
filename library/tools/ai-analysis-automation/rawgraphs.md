---
id: rawgraphs
name: RAWGraphs
description: Use when you have tabular case data and want to turn it into a custom chart without coding — returns shareable visualizations that make patterns in your data legible; not a data source.
url: https://app.rawgraphs.io/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: No-code, open-source charting of your own spreadsheet data into flexible, editable visualizations.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open-source; runs in-browser (data stays client-side) or self-hosted. No account.
opsec: passive
opsecNote: The web app processes your data locally in the browser (nothing is uploaded), so it is safe for sensitive case data — but confirm you're on the official app and prefer self-hosting for the most sensitive work.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A well-known open-source project (originating at DensityDesign, Politecnico di Milano) featured in the Bellingcat toolkit; code is public and auditable.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- tableau-public
aliases:
- RAW Graphs
- raw graphs
tags:
- bellingcat-toolkit
- data-visualization
- data-analysis
source: bellingcat-toolkit
lastVerified: '2026-07-23'
enrichment: full
---

# RAWGraphs

> A free, open-source, no-code charting tool — paste a spreadsheet and shape it into a custom visualization to make patterns in your case data legible.

## When to use
You already have tabular investigation data — a timeline, a set of transactions, event counts, relationship tallies — and want to see it as a chart to spot patterns or present findings, without writing code. RAWGraphs is a sensemaking/output tool: it visualizes what you supply and discovers nothing new about a person on its own.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://app.rawgraphs.io/.
2. Paste or upload your data (CSV/TSV/Excel/JSON); it's parsed in-browser.
3. Pick a chart type (bumps, alluvial/Sankey, beeswarm, circle packing, etc.) suited to your question.
4. Map your columns onto the chart's dimensions, style it, and export as SVG/PNG for a report.
5. Pivot: the visualization highlights outliers/clusters worth chasing back in the source records.

## Inputs → Outputs
- **In:** your own tabular data (CSV/TSV/Excel/JSON).
- **Out:** a custom, exportable chart (SVG/PNG) — a representation of your data, not new intelligence.
- **Empty/negative result looks like:** nothing meaningful to show because the data is too sparse or the wrong chart type is chosen — a tooling/design issue, not a data finding.

## Gotchas & OpSec
- It only renders what you give it; garbage-in/garbage-out — clean and structure the data first.
- Processing is client-side (data stays in your browser), which is good for privacy but means large datasets can be slow.
- A striking chart is not evidence — always trace a highlighted pattern back to the underlying records.

## Overlaps ("do both")
- Complements [[tableau-public]]: RAWGraphs excels at quick, unusual chart types with data kept local; Tableau adds interactivity and a public-gallery discovery angle.

## Trust & verifiability
`trust: trusted` — an established open-source academic project in the Bellingcat toolkit; the code is public and the output is a faithful rendering of your own data.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | rawgraphs |
