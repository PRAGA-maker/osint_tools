---
id: localfocus
name: LocalFocus
description: Use when you have a dataset (or an `address`/region) and want to turn it into maps and charts for analysis — returns geographic visualizations, not new selectors.
url: https://www.localfocus.nl
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Fast, no-code data visualization and geographic mapping of open datasets for journalists and analysts.
selectorsIn:
- geolocation
- address
selectorsOut: []
status: live
pricing: freemium
costNote: Free web-based GIS/GeoKit tools plus a 30-day trial; the full charting/mapping suite is a paid ANP subscription.
opsec: passive
opsecNote: You upload and visualize your own data on LocalFocus servers — do not paste sensitive case data into a third-party cloud tool. Anything you make public/embeddable is world-readable. Stick to open datasets, or run analysis locally when the data is sensitive.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: Commercial product from ANP (the Dutch national news agency); reputable, but a data-viz/newsroom tool rather than an investigative data source.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- ANP LocalFocus
- LocalFocus GeoKit
tags:
- infographics-and-data-visualization
source: awesome-osint
lastVerified: '2026-08-05'
enrichment: full
relatedTools:
- localfocus-nl-geokit
---

# LocalFocus

> A newsroom data-visualization platform (from Dutch news agency ANP) that turns spreadsheets into maps and charts in minutes — an analysis/presentation aid, not a lookup service.

## When to use
You already have tabular data — crime statistics, election results, demographic figures tied to a `geolocation` or `address`/region — and you want to see the pattern rather than read rows. LocalFocus is for the analysis-and-presentation stage: plotting where incidents cluster, mapping a subject's known locations against a base map, or building a shareable graphic of your findings. It does not find people; it makes data legible.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.localfocus.nl and open the free GeoKit tools, or start the trial for the full editor.
2. Upload or paste your dataset (CSV) or connect an open-data source.
3. Choose a chart or map type; geocode an address/place column to drop points on a map.
4. Style and export/embed. Keep sensitive case data out — use it for open or already-public figures.
5. Pivot: a visualized cluster tells you *where* to look next (which town's local press, which precinct), feeding geographic lookups and local-records searches.

## Inputs → Outputs
- **In:** `geolocation` / `address` columns in a dataset you supply
- **Out:** maps, charts, embeddable graphics — analytical output, no new personal selectors
- **Empty/negative result looks like:** a geocode failure (address column not resolved) or a blank map — a data/format problem, not an intelligence result.

## Gotchas & OpSec
- Human-in-the-loop: the powerful charting/mapping features sit behind a paid subscription after the trial; the free GeoKit is limited.
- OpSec: this is a cloud tool — uploaded data leaves your machine. Never upload sensitive victim/subject data; use open datasets or a local tool (QGIS) instead.
- It is Dutch-origin and news-oriented; interface and some data helpers are strongest for NL/EU contexts.

## Overlaps ("do both")
- Pairs with `[[localfocus-nl-geokit]]` — GeoKit is LocalFocus's free geographic toolset; use it for the mapping step when you do not need the paid editor.

## Trust & verifiability
`trust: community` — a legitimate commercial product from a national news agency, but it is a visualization layer; the trustworthiness of any output is only as good as the dataset you feed it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | localfocus |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | geolocation, address → — |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
