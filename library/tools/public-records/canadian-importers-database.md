---
id: canadian-importers-database
name: Canadian Importers Database
description: Use when you have a product/commodity or place and want to find Canadian companies importing it — returns importer `employer-org` names by product, city, and country of origin.
url: https://ised-isde.canada.ca/site/canadian-importers-database/en
category: public-records
path:
- public-records
bestFor: Identifying major Canadian importers of a given product (or in a given city / from a given country) from official CBSA customs data.
selectorsIn:
- employer-org
selectorsOut:
- employer-org
status: live
pricing: free
costNote: Free official government database; no account. Underlying data also published as open data on open.canada.ca.
opsec: passive
opsecNote: You query a Government of Canada database, not any company — the search is invisible to the importers listed. Nothing sensitive is submitted; standard research-browser hygiene is enough.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Innovation, Science and Economic Development Canada (ISED) from customs data collected by the Canada Border Services Agency (CBSA) — authoritative, though it shows only "major" importers (~top 80% of a product's imports), not every company.
missingPersonsRelevance: medium
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- gov-data-canada
- federal-corporation-search-canada
- canadian-business-research
- canadian-department-of-finance
- canadian-intellectual-property-office
- canadian-trademarks-database
- completed-access-to-information-requests
- government-of-canada-open-data
aliases:
- CID
- Canadian Importers Database
tags:
- canada
- trade
- importers
- government-records
source: osint4all
lastVerified: '2026-07-18'
enrichment: full
---

# Canadian Importers Database

> The Government of Canada's official list of major importers by product — search a commodity, city, or country of origin and get the Canadian companies bringing those goods in, built from CBSA customs data.

## When to use
Your investigation involves trade, a Canadian business, or a supply chain, and you want to know which companies import a particular product into Canada — or what a specific city's importers or a given country's exporters-to-Canada look like. It links a `product`/commodity to importer `employer-org`s, which can corroborate that a company deals in certain goods, surface businesses tied to a subject, or map who sources from a country of interest. Business/trade-intelligence angle rather than person lookup.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://ised-isde.canada.ca/site/canadian-importers-database/en.
2. Choose a search method: **by product** (name or HS commodity code), **by city**, or **by country of origin**.
3. Run the search — results list the major importing companies (`employer-org`s) for that product/place, representing up to ~80% of imports.
4. Note company names and, where shown, locations; the tool identifies "major" importers, so smaller ones may be absent.
5. Pivot: an importer `employer-org` → a corporate registry (officers, address) and business-research tools; cross-reference against open trade datasets on open.canada.ca.

## Inputs → Outputs
- **In:** product / HS commodity code, city, or country of origin (querying toward `employer-org`)
- **Out:** major Canadian importer `employer-org` names for that product/place
- **Empty/negative result looks like:** no companies listed — either no major importer matches (small-volume imports are excluded), or the product/code was too specific; broaden the commodity or try a related code.

## Gotchas & OpSec
- Shows only **major** importers (~top 80% by volume) — absence does NOT mean a company doesn't import that good.
- Data reflects a specific customs year (check the stated year); it's not real-time shipment tracking.
- No exact quantities/values per company — it's a directory of who imports, not how much.
- Fully passive and anonymous.

## Overlaps ("do both")
- Pairs with `[[federal-corporation-search-canada]]` and `[[canadian-business-research]]` (resolve an importer to its corporate record/officers) and `[[gov-data-canada]]` (the open-data version of the underlying trade data).

## Trust & verifiability
`trust: trusted` — an authoritative ISED database sourced from CBSA customs records, with the same data mirrored as open data, so importer listings trace back to official government sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | canadian-importers-database |
| category | public-records |
| selectorsIn → selectorsOut | employer-org → employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
