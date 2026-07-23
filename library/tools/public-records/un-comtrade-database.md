---
id: un-comtrade-database
name: UN COMTRADE Database
description: Use when you need official country-to-country trade statistics for context — returns bilateral import/export volumes and values by product, country and year.
url: http://comtrade.un.org
category: public-records
path:
- public-records
bestFor: Authoritative bilateral trade statistics (by product/country/year) for investigative context.
selectorsIn:
- employer-org
selectorsOut: []
status: live
pricing: free
costNote: Free access to the UN's official trade statistics via the web UI and API (Comtrade / Comtrade Plus); premium/bulk tiers exist but core data is free.
opsec: passive
opsecNote: Aggregate national trade statistics — no personal data, no target interaction; fully passive contextual research.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The United Nations' official international trade statistics database, compiled from national reporting; the authoritative source for macro trade data.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- UN Comtrade
- Comtrade Plus
tags:
- public-records
- trade-data
- economics
- context
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
relatedTools:
- statistics-and-data
- un-data
- un-security-council-consolidated-list
- unstats-social-indicators
---

# UN COMTRADE Database

> The United Nations' official trade-statistics repository — how much of what product flowed between which countries, by year.

## When to use
Not a people-finder — use it for hard trade context: verifying claimed import/export relationships, spotting anomalies (e.g. a commodity flow that shouldn't exist, sanctions-relevant trade), sizing a market a company operates in, and grounding investigative claims in official numbers. Complements the Atlas of Economic Complexity with the underlying raw statistics.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://comtrade.un.org (UN Comtrade / Comtrade Plus).
2. Query by reporter country, partner country, commodity code (HS), trade flow (import/export), and year.
3. Read the results: trade value and quantity for that combination; export CSV or pull via the API.
4. Pivot: an unusual bilateral flow points to specific commodities/companies to investigate via corporate registries and shipment databases.

## Inputs → Outputs
- **In:** country + commodity + year selection (an `employer-org`'s sector for context)
- **Out:** bilateral trade values/quantities (no personal selector)
- **Empty/negative result looks like:** no data for a country-year-commodity — the country didn't report (reporting gaps are common), not necessarily that no trade occurred; check mirror data (partner's report).

## Gotchas & OpSec
- Data lags (often 1–2 years) and depends on national reporting — gaps and revisions are normal.
- "Mirror" discrepancies (reporter vs partner figures) are common; cross-check both sides.
- Aggregate/macro only — it never names a company or transaction.

## Overlaps ("do both")
- Pairs with `[[the-atlas-of-economic-complexity]]` (visual/derived from this) and shipment/bill-of-lading databases — Comtrade gives the official aggregate; those add the picture and the actual shippers.

## Trust & verifiability
`trust: trusted` — the UN's official trade database; authoritative within its reporting-lag and coverage limits, so note gaps and use mirror data to sanity-check.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | un-comtrade-database |
| category | public-records |
| selectorsIn → selectorsOut | employer-org →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
