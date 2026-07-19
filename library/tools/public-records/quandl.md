---
id: quandl
name: Quandl (Nasdaq Data Link)
description: Use when you need financial/economic/company market datasets for context — now Nasdaq Data Link; returns datasets on markets, companies and economics (aggregate data, not personal records).
url: https://data.nasdaq.com/
category: public-records
path:
- public-records
bestFor: Sourcing financial, economic, and market datasets (some free) for background on a company or market context.
selectorsIn:
- employer-org
selectorsOut:
- employer-org
status: live
pricing: freemium
costNote: Quandl rebranded to Nasdaq Data Link; many datasets are free (some need a free API key), premium datasets are paid.
opsec: passive
opsecNote: Passive — you query aggregated financial datasets, not a person; nothing reaches any subject. A free account/API key ties queries to you; use a research account for sensitive work.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Nasdaq (formerly Quandl); authoritative for the financial/market datasets it hosts, but it provides aggregate/market data, not individual PII.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- Quandl
- Nasdaq Data Link
tags:
- toddington
- financial-data
- company-search
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Quandl (Nasdaq Data Link)

> The financial-data platform formerly known as Quandl, now Nasdaq Data Link — market, economic, and company datasets for context, not people-search.

## When to use
You need financial or economic datasets to build context around a company or market tied to a case — pricing, fundamentals, economic indicators, trade data. It hosts aggregate datasets, not individual records, so it informs the backdrop rather than identifying a person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://data.nasdaq.com/ (quandl.com now redirects here).
2. Search the data catalogue for the market/company/economic series you need.
3. For programmatic access, register for a free API key (some datasets are free, others premium).
4. Read the output: dataset tables/time series. Pivot: use the data for context; for company ownership/officers use a company registry instead.

## Inputs → Outputs
- **In:** a dataset/company (`employer-org`) or market query
- **Out:** financial/economic datasets and time series
- **Empty/negative result looks like:** no free dataset for a query often means it's behind a premium tier or simply not hosted — check the catalogue's free-tier filter.

## Gotchas & OpSec
- **Aggregate data only** — no personal records; don't expect PII.
- The Quandl brand/URLs are legacy; use data.nasdaq.com. Some datasets moved or were retired in the transition.
- Human-in-the-loop: none (API key optional). OpSec: passive.

## Overlaps ("do both")
- Complements company registries — this gives market/financial context; a registry gives officers/ownership.

## Trust & verifiability
`trust: trusted` — Nasdaq-operated; datasets are authoritative for what they cover, but irrelevant to identifying an individual.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | quandl |
| category | public-records |
| selectorsIn → selectorsOut | employer-org → employer-org |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
