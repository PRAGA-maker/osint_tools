---
id: ilostat
name: ILOSTAT
description: Use when you need labour-market statistics for a country/sector — returns employment, wages, informality and working-conditions indicators from the ILO's global database.
url: https://ilostat.ilo.org/
category: public-records
path:
- public-records
bestFor: Authoritative country- and sector-level labour statistics (employment, wages, informality, occupations) for context on a place or workforce.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open from the International Labour Organization; data explorer, bulk downloads and an API, no account. (The old ilo.org Oracle portal URL now redirects to ilostat.ilo.org.)
opsec: passive
opsecNote: Passive, aggregate statistical data — you query countries/sectors, not an individual. No subject data is disclosed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Published by the ILO (a UN agency); a primary, authoritative source for international labour statistics.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- ilo-world-employment-and-social-outlook-trends
- international-standard-classification-of-occupations
aliases:
- ILO Statistics
- ilostat.ilo.org
tags:
- data-and-statistics
source: awesome-osint
lastVerified: '2026-08-04'
enrichment: full
---

# ILOSTAT

> The ILO's global labour-statistics database — aggregate workforce context (employment, wages, informality), not person-level records.

## When to use
Your case touches a country's labour market, an occupation, or an industry and you want authoritative context — employment/unemployment rates, wages, informality, working conditions, occupational classifications. It is aggregate statistical data; it identifies no individuals.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://ilostat.ilo.org/ (the old ilo.org Oracle portal URL redirects here).
2. Use the data explorer to filter by country, indicator, sex, and year; or pull bulk downloads / the API for larger analysis.
3. Read the indicators for your country/sector and note the reference year and source survey.
4. Cite the specific indicator/year; corroborate with national statistics offices where precision matters.

## Inputs → Outputs
- **In:** a country/sector/occupation (not a personal selector)
- **Out:** labour-market indicators and downloadable datasets
- **Empty/negative result looks like:** no data for a country/year/indicator — coverage gaps exist for some economies; fall back to national sources.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: passive; nothing about a subject is entered.
- Indicators are aggregate and periodic — context, not individual fact; mind differing national definitions.

## Overlaps ("do both")
- Complements the World Bank and UNDP `[[human-development-reports]]` data: ILOSTAT is the labour-specific layer alongside those broader development indicators.

## Trust & verifiability
`trust: trusted` — a primary UN-agency source; authoritative for international labour statistics within its coverage and definitions.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ilostat |
| category | public-records |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
