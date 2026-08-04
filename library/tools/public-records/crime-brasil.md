---
id: crime-brasil
name: Crime Brasil
description: Use when you have a Brazilian city, neighborhood or region and want its crime picture — returns crime statistics and rates by locality drawn from official Brazilian police, health and court data.
url: https://crimebrasil.com.br
category: public-records
path:
- public-records
bestFor: Looking up crime statistics and rates for a Brazilian city or neighborhood.
selectorsIn:
- address
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free data-journalism platform; open datasets also published via Zenodo.
opsec: passive
opsecNote: You browse aggregate public statistics — no individual is queried and nothing reaches any subject. Fully passive contextual research.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: An independent data-journalism project aggregating official sources (SSP/ISP/SEJUSP police data, DataSUS, CNJ courts, IBGE census); reliable but a secondary aggregator, not the primary agency.
missingPersonsRelevance: low
coverage:
- br
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- crimebrasil.com.br
- Crime Brasil map
tags:
- data-and-statistics
- brazil
- crime-statistics
source: awesome-osint
lastVerified: '2026-08-04'
enrichment: full
---

# Crime Brasil

> An independent platform mapping crime across Brazil by city and neighborhood, aggregating official police, health and court data into comparable rates.

## When to use
Your investigation touches a Brazilian location and you want context on its crime environment — homicide, theft and violence rates for a city or (in covered states) a specific neighborhood. It's for area-level situational awareness and corroboration, not individual records: understanding the risk profile of a place, comparing localities, or grounding a claim about an area.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://crimebrasil.com.br.
2. Search or navigate to the city/neighborhood of interest (17 states covered; ~10 have neighborhood-level detail).
3. Read the standardized metrics (occurrences per 100,000 inhabitants) and compare localities with the built-in tools.
4. Note the data vintage — updates track each state's Secretaria de Segurança Pública release schedule.
5. Pivot: for primary records, go to the cited official sources (SSP/ISP/SEJUSP, DataSUS, CNJ); download open datasets from the project's Zenodo for deeper analysis.

## Inputs → Outputs
- **In:** Brazilian `address` / `geolocation` (city or neighborhood)
- **Out:** crime statistics and rates tied to that `geolocation`
- **Empty/negative result looks like:** a locality with no data — meaning that state/area isn't yet covered (coverage is 17 states, neighborhood detail in ~10), not that it's crime-free.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: **passive** — aggregate public statistics only; no individual lookup, no exposure.
- It's an aggregator; figures lag official releases and coverage is uneven across states. Cite the primary agency for anything consequential.

## Overlaps ("do both")
- Complements official Brazilian public-security portals and DataSUS — Crime Brasil makes the numbers comparable and mapped; the primary sources give authoritative, current figures.

## Trust & verifiability
`trust: community` — a well-sourced independent project citing official data; excellent for orientation, but verify specific figures against the named primary sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | crime-brasil |
| category | public-records |
| selectorsIn → selectorsOut | address, geolocation → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
