---
id: datawrapper
name: Datawrapper
description: Use when you have investigation data and want to turn it into clear charts, maps or tables — a free web app for publishable data visualizations.
url: https://datawrapper.de
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Quickly building professional charts, choropleth maps and sortable tables from investigation data for a report or briefing.
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
costNote: Generous free tier (create/publish charts, no account needed to try); paid plans add custom branding, larger teams and offline export options.
opsec: passive
opsecNote: A visualization tool, not a lookup — it queries no target. But whatever data you paste/upload is processed on Datawrapper's servers and published charts are public by URL; never upload sensitive PII you don't intend to expose.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Established tool used by major newsrooms (NYT, Reuters, AP, WaPo); reliable and well-documented, though the output quality depends entirely on your input data.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- datawrapper.de
tags:
- data-visualization
- charts
- reporting
source: awesome-osint
lastVerified: '2026-07-22'
enrichment: full
---

# Datawrapper

> A free, newsroom-grade web app for turning a spreadsheet of findings into clean charts, maps and tables you can drop into a report.

## When to use
You have finished the collection/analysis and now need to communicate it — a timeline of events, a map of sightings/locations, a comparison table of entities. Datawrapper is the presentation layer: paste your data, pick a chart or map type, and publish or export. Not a data source itself.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://datawrapper.de (you can start with no account).
2. Choose Chart, Map or Table and paste/upload your data (CSV or copy-paste).
3. Pick the visualization type (bar, line, choropleth/symbol map, sortable table), then refine labels, colours and annotations.
4. Publish to get an embeddable/shareable version, or export as PNG/SVG/PDF for your report.
5. Keep an offline copy of the underlying data — the chart is a view, not the evidence.

## Inputs → Outputs
- **In:** your own structured data (not a person-selector)
- **Out:** a chart, map or table (image/embed) for reporting
- **Empty/negative result looks like:** a chart that misrepresents the data — a signal your input is malformed (wrong column types, missing values), not a tool fault. Check the data table.

## Gotchas & OpSec
- Published charts are public at their URL — do not publish anything containing sensitive PII.
- Free tier is generous but adds a small attribution; paid removes it and adds branding.
- It only visualizes; it does no analysis or sourcing for you.

## Overlaps ("do both")
- Pairs with mapping tools when you need interactive/geospatial layers beyond a simple choropleth, and with spreadsheet tooling for the data prep before visualization.

## Trust & verifiability
`trust: trusted` — a mature, widely-used tool; the visualization faithfully reflects the data you supply, so verifiability rests on your source data.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | datawrapper |
