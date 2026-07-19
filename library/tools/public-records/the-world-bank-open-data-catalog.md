---
id: the-world-bank-open-data-catalog
name: The World Bank Open Data Catalog
description: Use when you have a country/region (`geolocation`/`address`) and want authoritative development, economic and social statistics for context — returns downloadable datasets and an open API.
url: https://datacatalog.worldbank.org/
category: public-records
path:
- public-records
bestFor: Authoritative macro development/economic/social statistics by country, downloadable and via API.
selectorsIn:
- geolocation
- address
selectorsOut: []
status: live
pricing: free
costNote: Open data — free to search, download and query via API; no account or payment required.
opsec: passive
opsecNote: Aggregate, country-level statistics — nothing here concerns an individual and nothing reaches a subject. Fully passive; no special hygiene needed beyond a normal browser.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official World Bank data platform; datasets are sourced, documented and authoritative for macro indicators (caveat: national statistics quality varies by country).
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- world-bank-data
- world-bank-investing-across-borders
- world-integrated-trade-solution
aliases:
- World Bank Data Catalog
- datacatalog.worldbank.org
tags:
- public-records
- open-data
- statistics
source: arf-seed
lastVerified: '2026-07-19'
enrichment: full
---

# The World Bank Open Data Catalog

> The World Bank's central catalog of ~7,900 development datasets — macro context (economy, health, demographics, infrastructure) by country, downloadable and API-accessible.

## When to use
You need authoritative *country-level* context, not a personal record: baseline economics, demographics, health, migration or infrastructure figures for a region tied to an investigation. Good for grounding a case — e.g. understanding the setting a subject travelled to — but it holds no data on individuals.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://datacatalog.worldbank.org/.
2. Search or filter by country (`geolocation`/`address`), indicator, or dataset name across the catalog's thousands of datasets.
3. Open a dataset for its metadata, coverage and documentation; download (CSV/Excel) or note its API endpoint.
4. For programmatic pulls, use the linked World Bank Data API (also powering [[world-bank-data]]) to query indicators by country and year.
5. Pivot: figures here are context only — combine with country-specific public records for anything person-level.

## Inputs → Outputs
- **In:** country / region (`geolocation` / `address`), indicator name
- **Out:** downloadable datasets and API series (aggregate statistics) — no personal selectors
- **Empty/negative result looks like:** no dataset for a niche indicator/country-year — expected; try a broader indicator or the sibling World Bank data portals.

## Gotchas & OpSec
- Aggregate only: this will never return names, addresses, or any individual record — set expectations accordingly.
- Data quality varies by reporting country and lags by months to years; check each dataset's vintage and source.
- OpSec: fully passive; no subject interaction.

## Overlaps ("do both")
- Pairs with [[world-bank-data]] (the indicator front end / API) and [[world-integrated-trade-solution]] (trade data) — the catalog is the discovery layer; those are the query layers. Use the catalog to find a dataset, then the sibling tool to pull it.

## Trust & verifiability
`trust: trusted` — official World Bank platform with documented, sourced datasets; authoritative for macro figures, with the standard caveat that underlying national statistics differ in quality.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | the-world-bank-open-data-catalog |
| category | public-records |
| selectorsIn → selectorsOut | geolocation, address → — |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
