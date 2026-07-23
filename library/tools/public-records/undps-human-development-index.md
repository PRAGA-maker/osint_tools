---
id: undps-human-development-index
name: UNDP Human Development Index
description: Use when you have a country/`geolocation` and want socio-economic baseline data — returns HDI and related development indicators by country and year.
url: https://hdr.undp.org/data-center
category: public-records
path:
- public-records
bestFor: Authoritative country-level development statistics (HDI, life expectancy, education, income) for context and baselines.
selectorsIn:
- geolocation
selectorsOut: []
status: live
pricing: free
costNote: Free official UN Development Programme data; downloadable tables/CSV. No account.
opsec: passive
opsecNote: You read/download public UN statistics; nothing is tied to any target. Downloading the full dataset and querying locally leaks nothing.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Published by the UNDP Human Development Report Office — a primary, authoritative source for international development indicators.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- human-development-reports
aliases:
- HDI
- UNDP HDR Data Center
- Human Development Index
tags:
- data-and-statistics
- development-indicators
- reference
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# UNDP Human Development Index

> The UN's country-level development scorecard: HDI plus life-expectancy, schooling, and income indicators for nearly every country, over time.

## When to use
You need authoritative socio-economic *context* for a country or region tied to an investigation — baseline development level, life expectancy, education, gross national income — rather than data on a specific person. Useful for framing an environment (e.g. understanding conditions in a region relevant to a migration, trafficking, or humanitarian case) or for comparative/background analysis. It is reference statistics, not a people-finder; missing-persons relevance is low and purely contextual.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the HDR Data Center at https://hdr.undp.org/data-center.
2. Select a country/`geolocation` and the indicator(s) of interest (HDI, life expectancy at birth, expected/mean years of schooling, GNI per capita), and a year or range.
3. Read the on-page tables/charts, or download the full dataset (CSV) to analyse offline; the HDR office also exposes a data API.
4. Pivot: use the figures as context in a report, or compare across countries/years to characterise a region's conditions.

## Inputs → Outputs
- **In:** a country / `geolocation` (+ indicator and year)
- **Out:** HDI value and rank, plus component indicators (life expectancy, education, income) — country-level, no personal data
- **Empty/negative result looks like:** "no data" for a country/year — some states have gaps or aren't ranked in a given edition; absence reflects data availability, not a real zero.

## Gotchas & OpSec
- This is **aggregate country data** — it never identifies or describes individuals.
- Methodology and country coverage change between annual editions; note which report year you're citing.
- OpSec: fully passive reading/download of public statistics.

## Overlaps ("do both")
- Complements `[[human-development-reports]]` (the narrative reports behind the numbers) and other country-statistics sources (World Bank, UN Data) — use HDI for a quick composite, the others for deeper indicator breakdowns.

## Trust & verifiability
`trust: trusted` — a primary UNDP publication with documented methodology; authoritative for what it measures (country-level development), with the caveat of per-country data gaps and edition-to-edition methodology shifts.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | undps-human-development-index |
| category | public-records |
| selectorsIn → selectorsOut | geolocation → — |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
