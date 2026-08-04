---
id: unesco-institute-for-statistics
name: UNESCO Institute for Statistics
description: Use when you need education, science, culture or communication statistics for a country — returns internationally-comparable indicators (literacy, enrolment, R&D spend).
url: https://uis.unesco.org
category: public-records
path:
- public-records
bestFor: Authoritative country-level statistics on education, science, culture and communication for contextualising a place or population.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open from UNESCO's statistics arm; data explorer and bulk downloads, no account.
opsec: passive
opsecNote: Passive, aggregate statistical data — you query countries/indicators, not an individual. No subject data is disclosed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The UNESCO Institute for Statistics (UIS) is the UN's official source for global education, science and culture data; authoritative.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- UIS
- uis.unesco.org
tags:
- data-and-statistics
source: awesome-osint
lastVerified: '2026-08-04'
enrichment: full
---

# UNESCO Institute for Statistics

> UNESCO's official statistics arm — country-level education, science and culture indicators for context, not person-level records.

## When to use
Your case touches a country's education system, research capacity, or cultural/communication sector and you want authoritative, internationally-comparable indicators (literacy, school enrolment, R&D expenditure, researchers per capita). It is aggregate data; it identifies no individuals.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://uis.unesco.org and use the UIS data explorer (or bulk downloads).
2. Filter by country, indicator, and year.
3. Read the indicators and note the reference year and definition.
4. Cite the specific indicator/year; corroborate with national statistics offices where precision matters.

## Inputs → Outputs
- **In:** a country/indicator (not a personal selector)
- **Out:** education/science/culture indicators and datasets
- **Empty/negative result looks like:** gaps for some countries/years — UIS coverage varies; fall back to national sources.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: passive; nothing about a subject is entered.
- Indicators are aggregate and periodic — context, not individual fact; mind differing national definitions.

## Overlaps ("do both")
- Complements the World Bank, `[[ilostat]]` and UNDP `[[human-development-reports]]` data: UIS is the education/science/culture-specific layer alongside those broader development indicators.

## Trust & verifiability
`trust: trusted` — the UN's official source for these statistics; authoritative within its coverage and definitions.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | unesco-institute-for-statistics |
| category | public-records |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
