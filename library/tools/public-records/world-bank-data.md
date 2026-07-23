---
id: world-bank-data
name: World Bank Data
description: Use when you have an employer-org, country, or region and want authoritative development/economic statistics to corroborate context — returns employer-org and location-level indicator data.
url: https://data.worldbank.org
category: public-records
path:
- public-records
bestFor: Free, authoritative country- and region-level development statistics for background and corroboration.
selectorsIn:
- employer-org
- address
selectorsOut:
- employer-org
status: live
pricing: free
costNote: Completely free and open; no account required. A documented developer API is available for bulk/programmatic access.
opsec: passive
opsecNote: Fully passive — you query a public open-data portal, not the subject. No selectors about a person are sent anywhere.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party open-data portal of the World Bank; the World Development Indicators are internationally standardized official statistics.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- the-world-bank-open-data-catalog
- world-bank-investing-across-borders
- world-integrated-trade-solution
aliases:
- World Development Indicators
- WDI
tags:
- data-and-statistics
- public-records
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# World Bank Data

> The World Bank's free open-data portal — country- and region-level development, economic, and demographic statistics with a public API.

## When to use
You are building context around a place, a sector, or an `employer-org` rather than pinpointing a person. Use it to corroborate the plausibility of a claim (a company's country's export/GDP figures, a region's population/health/connectivity indicators) or to characterize the environment a subject lives or operates in. It is background/corroboration data, not a people-search source.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://data.worldbank.org.
2. Search or browse by **Country** (a place) or by **Indicator** (e.g. population, GDP, mobile subscriptions).
3. Read the time series on the indicator page; use **DataBank** to build a custom cross-country/time table.
4. For bulk use, hit the developer API (`api.worldbank.org/v2/...`) — no key required — to pull the same series as JSON/XML.
5. Pivot: figures here support or undercut a claim; combine with a company registry or trade-data tool for entity-level detail.

## Inputs → Outputs
- **In:** a country/region, an indicator, or an `employer-org`/`address` you want country context for.
- **Out:** standardized indicator values (population, economy, health, infrastructure, digital connectivity) at country/region granularity.
- **Empty/negative result looks like:** an indicator with no data for the chosen country/year (blank cells or gaps in the series) — common for small states and older years. It never returns person-level data.

## Gotchas & OpSec
- Aggregated to country/region level — do not expect anything about an individual.
- Latest years are often estimates or missing; check the data notes before quoting a figure.
- Different indicators use different source methodologies; cross-country comparisons can hide definitional differences.

## Overlaps ("do both")
- Pairs with [[the-world-bank-open-data-catalog]] and [[world-integrated-trade-solution]] — the catalog exposes the underlying datasets and WITS gives entity/commodity-level trade flows, while this portal is the fast indicator front-end.

## Trust & verifiability
`trust: trusted` — first-party official statistics from the World Bank; every series is documented with its source and methodology.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | world-bank-data |
