---
id: oecd-data
name: OECD Data
description: Use when you need authoritative country-level economic/social statistics for context or base rates — returns official OECD indicators and datasets (not person-level data).
url: https://data.oecd.org
category: public-records
path:
- public-records
bestFor: Official comparable statistics across OECD/partner countries for background and context.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free official statistics from the OECD; downloadable, with an open data API. No account for browsing.
opsec: passive
opsecNote: Passive — you read published aggregate statistics; no subject is involved and it holds no personal data. Nothing you look up ties to an individual.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Published by the OECD, an intergovernmental organisation; authoritative, methodologically documented aggregate statistics.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- oecd-aid-database
aliases:
- data.oecd.org
- OECD Data Explorer
tags:
- data-and-statistics
- official-statistics
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# OECD Data

> The OECD's portal of official, cross-country economic and social statistics — authoritative context data, not person-level records.

## When to use
You need reliable country-level figures for context or base rates in an investigation — economics, demographics, health, migration, employment, etc. — across OECD and partner countries. This is aggregate reference data: it corroborates or frames a situation but never identifies a person; it produces no OSINT selectors.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://data.oecd.org (now often the OECD Data Explorer).
2. Search or browse by topic/indicator and select countries and time range.
3. Read the chart/table; download the data (CSV/Excel) or query it via the OECD open data API for automation.
4. Check the indicator's methodology notes before comparing across countries/years.
5. Pivot: figures provide context/base rates that inform interpretation of case-specific findings.

## Inputs → Outputs
- **In:** a topic/indicator + countries (no OSINT selector)
- **Out:** official aggregate statistics (charts, tables, downloadable series)
- **Empty/negative result looks like:** an indicator not covered for a country/year — coverage varies by dataset and reporting country.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: passive; aggregate data only, no personal information.
- It is macro/aggregate — useful for context, useless for identifying or locating an individual. Mind methodology differences when comparing countries.

## Overlaps ("do both")
- Complements other official statistics sources (national statistics offices, World Bank) — cross-reference when an indicator is missing or you need finer geography; pairs with `[[oecd-aid-database]]` for aid-flow specifics.

## Trust & verifiability
`trust: trusted` — authoritative OECD statistics with documented methodology; still cite the specific indicator/vintage, as definitions and coverage differ across datasets.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | oecd-data |
| category | public-records |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
