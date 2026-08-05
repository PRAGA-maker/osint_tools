---
id: bank-for-international-settlements-statistics
name: Bank for International Settlements Statistics
description: Use when you need authoritative cross-border banking, debt, FX, or credit statistics for a country or sector — returns official BIS macro-financial datasets.
url: https://www.bis.org/statistics/index.htm
category: public-records
path:
- public-records
bestFor: Official, standardized international banking and financial statistics for country/sector-level economic context.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free public access to all BIS statistical releases and data (browser tables, charts, and bulk downloads); no account required.
opsec: passive
opsecNote: Browsing a public central-bank data portal; no target is queried and nothing about a subject is submitted. Only your own IP is visible to bis.org — standard web hygiene applies.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The Bank for International Settlements is the central bank of central banks; its statistics are authoritative, methodologically documented, and internationally standardized.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- BIS Statistics
- Bank for International Settlements data
tags:
- data-and-statistics
- financial-data
source: awesome-osint
lastVerified: '2026-08-05'
enrichment: full
---

# Bank for International Settlements Statistics

> The BIS statistics portal — authoritative, standardized international banking, debt, and FX data. Macro context, not people-search.

## When to use
You need reliable country- or sector-level financial context: cross-border bank claims, credit-to-GDP, debt securities, effective exchange rates, or property-price indices. In an investigation this is background for financial-crime, sanctions, or economic-context work — it establishes the macro picture behind a jurisdiction, not the identity of any individual.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.bis.org/statistics/index.htm.
2. Pick a dataset (e.g. Locational/Consolidated banking statistics, Global liquidity, Debt securities, Effective exchange rates, Credit to non-financial sector).
3. Filter by country, sector, and period; view as tables/charts or download the underlying data (CSV/BIS Data Portal).
4. Read the methodology notes attached to each series before interpreting figures.
5. Pivot: a country-level anomaly → national-regulator filings and news; a sector trend → corporate/records research in that jurisdiction.

## Inputs → Outputs
- **In:** none — you select a dataset and filters, not a personal selector
- **Out:** standardized macro-financial time series by country/sector (tables, charts, downloads)
- **Empty/negative result looks like:** a series with no data for a chosen country/period — BIS coverage is aggregate and reporting-country-dependent, so gaps mean "not reported," not "value is zero."

## Gotchas & OpSec
- Human-in-the-loop: none; browse and download freely.
- Scope: aggregate macro data only — it will never identify a person or account; use it for context, then go to primary records for specifics.
- Interpretation: always read the per-series methodology; BIS aggregates are precise but easy to misread without the definitions.

## Overlaps ("do both")
- Pairs with national statistical offices, IMF/World Bank data, and corporate registries — BIS gives the standardized cross-border banking view; the others fill in domestic and entity-level detail.

## Trust & verifiability
`trust: trusted` — a first-party, methodologically documented dataset from the BIS; among the most authoritative international financial statistics available.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bank-for-international-settlements-statistics |
