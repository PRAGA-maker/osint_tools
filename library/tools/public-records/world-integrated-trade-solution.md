---
id: world-integrated-trade-solution
name: World Integrated Trade Solution (WITS)
description: Use when you have a country and product/sector and want detailed trade & tariff data — the World Bank's WITS returns bilateral flows and tariffs (macro context, not person-level).
url: https://wits.worldbank.org
category: public-records
path:
- public-records
bestFor: Granular bilateral trade and tariff statistics by country and product (HS/SITC codes) for economic and sector context.
selectorsIn:
- employer-org
selectorsOut:
- employer-org
status: live
pricing: free
costNote: Free; the World Bank's WITS portal offers open querying and downloads, though bulk/advanced use may prompt a free registration.
opsec: passive
opsecNote: Read-only queries against a public World Bank data platform — no target interaction; nothing about a subject is transmitted. Only your own access is logged.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the World Bank, aggregating UN Comtrade, TRAINS and WTO sources; authoritative for trade/tariff data at country-product granularity, but aggregate — never resolves to a person.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: true
relatedTools:
- the-world-bank-open-data-catalog
- world-bank-data
- world-bank-investing-across-borders
aliases:
- WITS
- World Bank WITS
tags:
- data-and-statistics
source: awesome-osint
lastVerified: '2026-08-04'
enrichment: full
---

# World Integrated Trade Solution (WITS)

> The World Bank's deep-dive trade database — bilateral import/export flows and tariffs down to individual product codes, drawing on UN Comtrade, TRAINS and WTO. Context for companies and sectors, not a people-finder.

## When to use
An investigation touches an `employer-org`/company, an industry, or a country's trade, and you need granular, authoritative figures: what two countries trade in a specific product (HS/SITC code), applied and preferred tariff rates, or a sector's import/export composition. Use it to corroborate claims about a business's market, size a supply chain, or profile a jurisdiction's trade — more granular than headline WTO figures.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://wits.worldbank.org.
2. Choose a data source (UN Comtrade for trade, TRAINS/WTO for tariffs) and build a query: reporter/partner country, product (HS/SITC), year.
3. (Advanced/bulk queries may ask for a free account.)
4. Read/export the results as tables, charts, or via the API.
5. Pivot: product-level flows contextualise a company's stated business and supply chain; pair with company registries for the corporate layer.

## Inputs → Outputs
- **In:** country + product/sector (an `employer-org`'s market context you define via filters)
- **Out:** bilateral trade values/volumes and tariff rates by product/partner/year — aggregate, keyed to economy/product, not to an individual
- **Empty/negative result looks like:** no data for a country-product-year — reporting gaps, embargoed/suppressed cells, or a partner that doesn't report; reflects data availability, not absence of trade.

## Gotchas & OpSec
- **Aggregate only** — it never identifies a person or a specific firm's shipments; use strictly for economic/sector context.
- Trade data lags and depends on national reporting; mirror flows (reporter vs partner figures) can disagree — cross-check both sides.
- Product-code granularity is powerful but easy to misuse; make sure you're comparing like HS/SITC codes across years.

## Overlaps ("do both")
- Complements [[world-bank-data]] and [[the-world-bank-open-data-catalog]] (broader indicators) and the WTO statistics portal — WITS is the granular product/tariff layer; use the others for macro indicators.

## Trust & verifiability
`trust: trusted` — a World Bank platform over authoritative UN/WTO sources with documented methodology; aggregate figures are citable and reproducible.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | world-integrated-trade-solution |
| category | public-records |
| selectorsIn → selectorsOut | employer-org → employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
