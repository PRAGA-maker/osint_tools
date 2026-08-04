---
id: wto-statistics
name: WTO Statistics
description: Use when you have an `employer-org` or country and want its merchandise/services trade profile — returns official bilateral trade, tariff and sector data (macro context, not person-level).
url: https://www.wto.org/english/res_e/statis_e/statis_e.htm
category: public-records
path:
- public-records
bestFor: Official country and sector trade statistics (merchandise, commercial services, tariffs) for economic context on a company, sector or jurisdiction.
selectorsIn:
- employer-org
selectorsOut:
- employer-org
status: live
pricing: free
costNote: Fully free; WTO Stats portal, dashboards, one-page profiles, downloadable Excel/CSV, and API are all open with no account.
opsec: passive
opsecNote: Read-only queries against a public intergovernmental statistics portal; no target interaction and nothing tied to your subject. Standard web-request logging by the WTO is the only footprint.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official statistics of the World Trade Organization, compiled from national and international sources; authoritative for trade flows but aggregate-level only.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- WTO Stats
- World Trade Organization statistics
tags:
- data-and-statistics
source: awesome-osint
lastVerified: '2026-08-04'
enrichment: full
---

# WTO Statistics

> The World Trade Organization's open statistics portal — authoritative country- and sector-level trade data, useful as macro context around a company, industry or jurisdiction rather than for identifying a person.

## When to use
This is a background/context source, not a people-finder. Reach for it when an investigation touches an `employer-org`, an industry, or a country and you need reliable trade figures: what a country imports/exports, bilateral trade flows, tariff levels, or a sector's commercial-services volume. Good for corroborating claims about a company's market, sizing an industry, or profiling a jurisdiction's economy.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.wto.org/english/res_e/statis_e/statis_e.htm.
2. Choose a tool: the WTO Stats portal (interactive query builder), the trade-profile one-pagers, tariff data, or the dashboards.
3. Filter by economy, product/sector, and time period.
4. Read/export the output as charts, Excel/CSV, or via the API for bulk analysis.
5. Pivot: sector and bilateral-trade figures contextualise a company's stated business; country profiles support due-diligence and sanctions/trade-risk framing.

## Inputs → Outputs
- **In:** an `employer-org`/company's country and sector (you supply the economy + product filters)
- **Out:** merchandise & commercial-services trade values/volumes, tariff data, bilateral flows, sector breakdowns — all aggregate, keyed to economy/sector not to an individual
- **Empty/negative result looks like:** no data for a very small economy, a suppressed cell, or a product/period the WTO doesn't cover — reflects reporting gaps, not absence of trade.

## Gotchas & OpSec
- Data is **aggregate** — it never resolves to a person; use it only for economic/company context.
- Figures lag (annual data especially) and rely on national reporting quality; small economies have thinner coverage.
- Cross-check headline claims against complementary sources (UN Comtrade, national statistics offices) when precision matters.

## Overlaps ("do both")
- Sits alongside other public-records and data-and-statistics sources — WTO gives the official trade layer; national statistics offices and UN Comtrade give finer or more current breakdowns.

## Trust & verifiability
`trust: trusted` — official intergovernmental statistics with documented methodology and sourcing; authoritative at the aggregate level it publishes.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wto-statistics |
| category | public-records |
| selectorsIn → selectorsOut | employer-org → employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
