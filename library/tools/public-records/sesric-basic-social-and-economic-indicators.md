---
id: sesric-basic-social-and-economic-indicators
name: SESRIC Basic Social and Economic Indicators
description: Use when you need country-level socio-economic context for one of the 57 OIC member states — returns statistical indicators (demographics, health, economy), not person-level data.
url: http://www.sesric.org/baseind.php
category: public-records
path:
- public-records
bestFor: Establishing regional/national background context (health, demography, economy) for a case set in an OIC member country.
selectorsIn:
- geolocation
selectorsOut: []
status: live
pricing: free
costNote: Free public statistics service run by an intergovernmental body; no account or payment required.
opsec: passive
opsecNote: Passive — you are querying a public statistics portal about a country, not a person. Nothing about your subject is transmitted; still route through a sock-puppet browser as routine hygiene.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by SESRIC (a subsidiary organ of the Organisation of Islamic Cooperation); figures are aggregated from World Bank, UN, WHO, FAO, ILO and similar primary sources.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- sesric-databases
aliases:
- SESRIC BASEIND
- Basic Social and Economic Indicators
tags:
- data-and-statistics
source: awesome-osint
lastVerified: '2026-08-05'
enrichment: full
---

# SESRIC Basic Social and Economic Indicators

> The BASEIND database: free national socio-economic statistics for all 57 OIC member countries, dating back to 1970 — a background/context source, not a people finder.

## When to use
You have a case anchored to a country in the OIC bloc (much of the Middle East, North/Sub-Saharan Africa, Central and South-East Asia) and need macro context — population, urbanisation, health coverage, GDP, migration figures — to frame an investigation or sanity-check a claim about a region. It does **not** take a `name`, `email` or any personal selector and will not surface a person; treat it purely as reference data.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.sesric.org/baseind.php.
2. Work through the five-step selection: pick country/countries, one of the 24 indicator categories, the specific variable, and a year range.
3. Generate the table; export as HTML, Excel or CSV if you need it offline.
4. Pivot: use figures as corroborating context (e.g. plausibility of a migration or demographic claim); person-level leads must come from other tools.

## Inputs → Outputs
- **In:** `geolocation` (country / OIC region selection)
- **Out:** socio-economic statistical indicators (no enum selectors — this is context data)
- **Empty/negative result looks like:** a variable with no data for the chosen country/year renders as blank/`..` cells; that means the indicator was not reported, not that the country is missing.

## Gotchas & OpSec
- Human-in-the-loop: none — fully self-service, no login.
- Coverage is limited to the 57 OIC member states; nothing here for other countries.
- This is aggregate national data only. Do not over-read it into individual conclusions.

## Overlaps ("do both")
- Pairs with `[[sesric-databases]]` — the same organisation's broader database hub; use BASEIND for the quick indicator lookup and the database hub for fuller thematic datasets.

## Trust & verifiability
`trust: trusted` — SESRIC is an official OIC statistical body and BASEIND republishes figures from established primary sources (World Bank, UN agencies), so the numbers are authoritative for context, if not always the most current.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sesric-basic-social-and-economic-indicators |
| category | public-records |
| selectorsIn → selectorsOut | geolocation → — |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
