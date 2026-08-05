---
id: sesric-databases
name: SESRIC Databases
description: Use when you need socio-economic statistics for OIC (Muslim-majority) countries — returns indicators by country/year for context on a place tied to an investigation.
url: http://www.sesric.org/databases-index.php
category: public-records
path:
- public-records
bestFor: Country-level socio-economic indicators for the 57 OIC member states.
selectorsIn:
- address
selectorsOut:
- address
status: live
pricing: free
costNote: Free public statistical databases (OICStat and related tools); no account required to query.
opsec: passive
opsecNote: Passive — you query aggregate national statistics, not individuals. Nothing about a person or target is transmitted; it is background/context data.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: SESRIC is the official statistical arm of the Organisation of Islamic Cooperation; OICStat draws on national and international statistical sources, so figures are authoritative aggregate data (with the usual national-statistics caveats).
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- sesric-basic-social-and-economic-indicators
aliases:
- SESRIC
- OICStat
tags:
- data-and-statistics
- country-data
source: awesome-osint
lastVerified: '2026-08-05'
enrichment: full
---

# SESRIC Databases

> The statistical portal of the OIC (Organisation of Islamic Cooperation): country-level socio-economic indicators for its 57 member states, via the OICStat database.

## When to use
Your investigation touches a place in the Muslim-majority world and you need reliable country-level context — demographics, economy, health, education, migration — to frame a lead (e.g. baseline conditions in a region a missing person travelled to). This is macro/aggregate context, not a person-level record; use it to understand the environment, not to identify anyone.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.sesric.org/databases-index.php.
2. Enter **OICStat** — the main database (1,850+ indicators across 27 categories, 57 countries, back to 1970).
3. Select country/countries, indicator(s), and year range; run the query.
4. Read the tables/charts; export where offered. Companion tools (OIC-CIF "Countries in Figures", OIC Ranker, motion charts) give quick comparisons.
5. Pivot: country baselines contextualise other findings (e.g. is a claimed statistic plausible?); combine with national statistics offices and World Bank/UN data for corroboration.

## Inputs → Outputs
- **In:** a country/region of interest (`address`-level geography) + indicator
- **Out:** socio-economic indicator values by country/year (contextual data about a place, `address`-level)
- **Empty/negative result looks like:** no data for a chosen indicator/year/country — coverage gaps are common for specific indicators or recent years; check the source year and try a broader indicator or another statistical body.

## Gotchas & OpSec
- Aggregate national statistics only — nothing about individuals; wrong tool for person-level lookups.
- Scope is OIC member states; for non-OIC countries use World Bank/UN/national sources.
- Figures depend on member states' own reporting, so timeliness and completeness vary by country.
- OpSec: fully passive, target-neutral background data.

## Overlaps ("do both")
- Cross-check indicators against World Bank Open Data, UN databases, and the country's own statistics office — the sources often diverge slightly, and agreement raises confidence in a figure.

## Trust & verifiability
`trust: trusted` — an official OIC statistical body; figures are authoritative aggregates sourced from national/international statistics, with the standard caveat that national reporting quality varies.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sesric-databases |
