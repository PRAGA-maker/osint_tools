---
id: the-atlas-of-economic-complexity
name: The Atlas of Economic Complexity
description: Use when you need to understand a country's trade profile and economic structure as investigative context — returns interactive export/import data by country and product.
url: http://atlas.cid.harvard.edu
category: public-records
path:
- public-records
bestFor: Exploring 50+ years of global trade flows by country and product for macro/economic context.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free interactive tool from Harvard Growth Lab (now at atlas.hks.harvard.edu); all visualizations and data downloads are free, no account.
opsec: passive
opsecNote: Aggregate national trade statistics — no personal data and no target interaction; fully passive contextual research.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Produced by Harvard's Growth Lab (Center for International Development) from UN COMTRADE-derived data with a documented cleaning methodology.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Atlas of Economic Complexity
- Harvard Growth Lab Atlas
tags:
- public-records
- trade-data
- economics
- context
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
relatedTools:
- worldmap-harvard
---

# The Atlas of Economic Complexity

> Harvard Growth Lab's interactive trade atlas — 50+ years of what every country exports and imports, by product, for macro-economic context.

## When to use
Not a people-finder — reach for it when an investigation needs *context* about a country's or region's economy: what it trades, with whom, and how its economic structure is changing. Useful for grounding stories about sanctions evasion, commodity flows, illicit trade patterns, or a company's plausible market, and for understanding the economic backdrop of a location.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://atlas.cid.harvard.edu (redirects to https://atlas.hks.harvard.edu/).
2. Pick a country or a product and choose a visualization (export/import treemaps, trade-flow maps, complexity rankings, growth projections).
3. Adjust year and trade direction to see how flows evolve over time.
4. Pivot: a dominant export product or trading partner points you at specific industries/companies to investigate via corporate registries and trade databases.

## Inputs → Outputs
- **In:** a country or product selection (no personal selector)
- **Out:** trade-flow visualizations, partner countries, product mix, complexity/growth rankings
- **Empty/negative result looks like:** sparse data for very small economies or the most recent year (trade data lags) — expected, not an error.

## Gotchas & OpSec
- Macro data only — it will never identify a person, company, or transaction; it's background, not evidence.
- Trade figures lag by 1–2 years and are cleaned/modelled, so treat exact numbers as estimates.
- Country attribution follows reporting conventions (e.g. re-exports via hubs) that can distort apparent flows.

## Overlaps ("do both")
- Complements corporate/trade registries — the Atlas tells you *which sectors and partners matter* for a country; registries and shipment databases then name the actual firms.

## Trust & verifiability
`trust: trusted` — an academic product from Harvard's Growth Lab built on UN COMTRADE data with a published methodology; authoritative for macro context.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | the-atlas-of-economic-complexity |
| category | public-records |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
