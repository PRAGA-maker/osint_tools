---
id: international-trade-center
name: ITC Country Profile (International Trade Centre)
description: Use when you have a country and want its official import/export trade statistics, top products and trading partners — returns aggregate trade context, no person data.
url: https://marketanalysis.intracen.org/en/country-profile
category: public-records
path:
- public-records
bestFor: Pulling a country's trade profile — top exports/imports, partner countries, product-level flows.
selectorsIn:
- address
selectorsOut: []
status: live
pricing: freemium
costNote: Free to view country profiles and headline trade data; deeper drill-downs in Trade Map may require a free registration. No payment for the public tiers.
opsec: passive
opsecNote: Passive read of aggregate trade statistics; there is no target-specific query, so nothing about a subject is disclosed. Registration (if you go deeper) uses an email — use a sock-puppet address if you prefer.
humanInLoop: false
humanInLoopReason:
- rate-limit
bestInteractionPattern: web-manual
trust: trusted
trustNote: Published by the International Trade Centre (joint agency of the WTO and UN); data is sourced from official national trade statistics.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- ITC
- Intracen
- Trade Map country profile
tags:
- trade-statistics
- public-records
- un-data
source: awesome-osint
lastVerified: '2026-07-28'
enrichment: full
---

# ITC Country Profile (International Trade Centre)

> The International Trade Centre's country profiles — official import/export statistics, top products and trading partners for 220+ countries. (The old `intracen.org/ByCountry.aspx` page was retired; this is its live successor.)

## When to use
You need macro trade context for a country: what it exports and imports, its main trading partners, product-level flows. In an investigation this frames the economic backdrop — e.g. understanding a commodity's trade routes, which countries a sanctioned/target good moves between, or corroborating a company's claimed import/export activity at the national level. It characterises countries and trade flows, not individuals.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://marketanalysis.intracen.org/en/country-profile (part of ITC's Market Analysis Tools; the main dataset is Trade Map).
2. Select a country (`address`) to view its trade profile — top exported/imported products and partner countries.
3. Drill into a product or partner for finer flows; deeper tariff-line detail in Trade Map may prompt a free sign-in.
4. Read/export the tables, graphs and maps for the aggregate figures.
5. Pivot: use the partner-country and product data to guide company-level or shipping OSINT (customs records, bills of lading, `[[tokyo-mou]]`-style vessel data).

## Inputs → Outputs
- **In:** a country (`address`) + optional product/partner filters
- **Out:** aggregate trade statistics — top exports/imports, partner countries, product flows. No person-level `selectorsOut`.
- **Empty/negative result looks like:** sparse or lagged figures for a country/year — some states report late or partially; treat gaps as reporting gaps, not zero trade.

## Gotchas & OpSec
- OpSec: passive; no per-target query. Deeper Trade Map access may want a free email registration — use a sock puppet if desired.
- Aggregate only: it will never name a person or a specific shipment; it's national/product-level context.
- Data is mirror-statistics (reported by each side) and can lag by months; cross-check importer vs exporter figures.

## Overlaps ("do both")
- Complements `[[unece]]` and other official-statistics portals — ITC specialises in bilateral trade flows and product detail, UNECE in broader socio-economic series; use each for its strength.

## Trust & verifiability
`trust: trusted` — a WTO/UN joint agency drawing on official national trade statistics; authoritative as aggregate data, subject to the usual reporting lags.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | international-trade-center |
| category | public-records |
| selectorsIn → selectorsOut | address → — |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (rate-limit) |
