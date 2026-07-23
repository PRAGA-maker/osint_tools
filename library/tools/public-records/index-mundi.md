---
id: index-mundi
name: IndexMundi
description: Use when you have a country or region and want quick comparative statistics and commodity data — returns country-level indicator data for background and corroboration, not person data.
url: https://www.indexmundi.com
category: public-records
path:
- public-records
bestFor: Fast country statistics, comparisons, and commodity prices aggregated from public sources into one browsable site.
selectorsIn:
- address
- employer-org
selectorsOut:
- employer-org
status: live
pricing: free
costNote: Free to browse; aggregates World Bank, CIA World Factbook, and commodity sources. No account.
opsec: passive
opsecNote: You browse aggregated public statistics, never querying anything about a subject — fully passive with no leakage.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running third-party aggregator; the underlying data is from authoritative sources (World Bank, CIA Factbook), but always trace a figure to its origin.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- world-bank-data
aliases:
- Index Mundi
tags:
- data-and-statistics
- public-records
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# IndexMundi

> A one-stop aggregator of country statistics, comparisons, and commodity prices — quick background context on a place, pulled from authoritative public sources.

## When to use
You need fast contextual data about a country or region relevant to a case — demographics, economy, infrastructure, commodity prices — without hunting through multiple official portals. IndexMundi collates World Bank indicators, CIA World Factbook profiles, and market data into browsable pages and country comparisons. It's background/corroboration; it returns nothing about an individual.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.indexmundi.com and pick a **Country** profile, an **Indicator**, or the **Commodity Prices** section.
2. Read the country page (population, economy, communications, transport) or build a cross-country comparison of a single indicator.
3. Use the commodity pages for price history where a case touches trade/agriculture/energy.
4. Note the cited source for any figure you'll rely on.
5. Pivot: confirm important numbers at their origin ([[world-bank-data]], CIA Factbook) before quoting.

## Inputs → Outputs
- **In:** a country/region, an indicator, or a commodity (optionally an `employer-org`/`address` you want country context for).
- **Out:** aggregated country-level statistics, comparisons, and commodity price series.
- **Empty/negative result looks like:** missing/blank values for small countries or recent years, or an outdated figure — the aggregator lags its sources; absence is a data gap, not person-level info.

## Gotchas & OpSec
- It's a mirror/aggregator: data can lag the primary source and some pages are dated — check the original for anything critical.
- Country-level only; nothing about individuals.
- The site carries ads; that's the cost of the free aggregation.

## Overlaps ("do both")
- Pairs with [[world-bank-data]]: IndexMundi is the fast browsable front-end, the World Bank portal is the authoritative source to verify and pull the raw series.

## Trust & verifiability
`trust: community` — a third-party aggregator over authoritative feeds; convenient, but cite the underlying source (World Bank/Factbook) for anything you depend on.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | index-mundi |
