---
id: international-monetary-fund
name: IMF Data
description: Use when you need macro-financial context on a country or lending program — returns economic indicators, exchange rates, and IMF program/publication records.
url: https://www.imf.org/en/Data
category: public-records
path:
- public-records
bestFor: Authoritative country-level economic data and IMF lending/program records for background and entity context.
selectorsIn:
- employer-org
selectorsOut:
- employer-org
status: live
pricing: free
costNote: Free, official IMF data portal; most datasets are open with no account (bulk API access also free).
opsec: passive
opsecNote: Passive access to a public institutional data portal; you query countries and indicators, not people, so there is nothing subject-specific to leak.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party International Monetary Fund data; authoritative for the economic indicators and program records it publishes.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- imf-world-economic-outlook-database
aliases:
- IMF Data
- imf.org/data
tags:
- toddington
- curated-directory
- company-search
- economic-data
source: toddington-resources
lastVerified: '2026-07-22'
enrichment: full
---

# IMF Data

> The IMF's official data hub — country-level economic indicators and lending-program records that provide authoritative background context, not person-level records.

## When to use
An investigation touches a country's economy, a state financial program, or an organisation whose activity depends on macro conditions (sanctions exposure, currency, debt, IMF lending), and you need authoritative figures rather than journalism. IMF Data supplies exchange rates, balance-of-payments, government finance, and program/arrangement records. This is contextual/entity-level intelligence — it helps you understand the environment around a subject or organisation, not locate an individual.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.imf.org/en/Data and pick a database (IFS, BOP, GFS, Exchange Rates) or the country pages.
2. Select the country/`employer-org`-relevant economy and the indicators/time range you need.
3. Read the figures or export them; note the IMF program/arrangement history for a country if relevant.
4. For scale/automation, use the free IMF data API.
5. Pivot: economic context frames why an organisation or scheme behaves as it does; program records point to the responsible ministries/officials to research elsewhere.

## Inputs → Outputs
- **In:** a country / economy / `employer-org` context
- **Out:** economic indicators, exchange rates, and IMF lending/program records for that entity
- **Empty/negative result looks like:** a country/indicator with no series (small or non-reporting economies, or a metric the IMF does not track). That is a data-coverage gap, not an error.

## Gotchas & OpSec
- This is macro-economic, entity-level data — it will not identify or locate a person; use it for background only.
- Series definitions and vintages differ across databases; read the metadata before comparing figures.

## Overlaps ("do both")
- Pairs with the World Bank Open Data and `[[imf-world-economic-outlook-database]]` — cross-check indicators across sources, since coverage and methodology differ.

## Trust & verifiability
`trust: trusted` — first-party IMF data, authoritative for what it publishes; the only caveat is scope (macro/economic, not personal) and normal series-definition care.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | international-monetary-fund |
| category | public-records |
| selectorsIn → selectorsOut | employer-org → employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
