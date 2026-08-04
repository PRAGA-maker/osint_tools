---
id: human-development-reports
name: Human Development Reports
description: Use when you need country-level human-development indicators for context on a place — returns HDI, poverty, gender and inequality indices for 190+ economies.
url: https://hdr.undp.org/
category: public-records
path:
- public-records
bestFor: Authoritative UNDP indices (HDI, MPI, gender indices) to contextualise the country/region a case touches.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and publicly available from the UNDP; reports and data downloads require no account.
opsec: passive
opsecNote: Passive reference data — you query countries/indicators, not an individual. No subject data is disclosed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Published by the UNDP Human Development Report Office; a primary, authoritative source for its own composite indices.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- undps-human-development-index
aliases:
- UNDP HDR
- HDRO
- hdr.undp.org
tags:
- data-and-statistics
source: awesome-osint
lastVerified: '2026-08-04'
enrichment: full
---

# Human Development Reports

> The UNDP's global human-development data — country-level context (living standards, poverty, gender, inequality), not person-level records.

## When to use
Your case touches a particular country or region and you want authoritative context on conditions there — Human Development Index, Multidimensional Poverty Index, gender and inequality indices. Useful for framing a report or assessing environment; it holds no data about specific individuals.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://hdr.undp.org/.
2. Browse by country (each has an HDI profile) or by index/topic; the global reports give cross-country comparisons.
3. Read the relevant indicators for the country/region and note the report year (indices update periodically).
4. Cite the specific index and year; pair with World Bank / national statistics data for corroboration and depth.

## Inputs → Outputs
- **In:** a country/region (not a personal selector)
- **Out:** HDI and related composite indices, country profiles, thematic reports
- **Empty/negative result looks like:** a territory not covered by the indices (small/disputed territories) — pivot to national or World Bank sources.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: passive; nothing about a subject is entered.
- Indices are periodic composites — always note the edition year and read them as context, not real-time data.

## Overlaps ("do both")
- Complements the `[[world-bank-enterprise-surveys]]`-style economic data and national statistics: UNDP gives human-development composites, those give economic/firm detail; use together for a rounded country picture.

## Trust & verifiability
`trust: trusted` — a primary UN source for its own indices; authoritative within their defined methodology and coverage.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | human-development-reports |
| category | public-records |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
