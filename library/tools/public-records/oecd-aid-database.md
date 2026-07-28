---
id: oecd-aid-database
name: OECD Aid Database
description: Use when you have an `employer-org` (donor/agency/NGO) and want its official development-aid flows — returns funding records by donor, recipient, sector and year.
url: http://www.oecd.org/dac/stats/data.htm
category: public-records
path:
- public-records
bestFor: Tracing official development assistance (ODA) flows between donors, recipient countries and implementing organisations.
selectorsIn:
- employer-org
selectorsOut:
- employer-org
- geolocation
status: live
pricing: free
costNote: Free public statistics; no account needed to browse or download via the OECD Data Explorer.
opsec: passive
opsecNote: Passive query against a public statistical portal — nothing reaches any subject. Data is aggregate/activity-level (donors, agencies, projects), not individuals, so there is minimal personal-privacy exposure.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official OECD Development Assistance Committee (DAC) statistics — the authoritative international source for ODA figures.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- oecd-data
aliases:
- OECD DAC statistics
- Creditor Reporting System
- OECD Data Explorer
tags:
- data-and-statistics
- development-finance
source: awesome-osint
lastVerified: '2026-07-28'
enrichment: full
---

# OECD Aid Database

> The OECD Development Assistance Committee's official statistics on aid flows — who funds what, where, in which sector, and when.

## When to use
You are investigating an `employer-org` in the development/aid space — a donor government, a bilateral agency, a multilateral fund, or an implementing NGO — and want the paper trail of official development assistance (ODA) it gave or received. The DAC databases (CRS activity-level data, DAC2A disbursements) let you follow money between donors and recipient countries by sector and year.

## How to use it (`bestInteractionPattern`: web-manual)
1. Start at the OECD development-finance data page (the legacy `oecd.org/dac/stats/data.htm` now points into the **OECD Data Explorer**, since OECD.Stat was retired in March 2024).
2. Choose a dataset — **CRS** (Creditor Reporting System, activity/project-level, 60+ attributes) for granular project records, or **DAC2A** for aggregate disbursements to countries/regions.
3. Filter by donor, recipient, sector, flow type and year; view online or export CSV/SDMX.
4. For automation, use the OECD Data Explorer / SDMX API.
5. Pivot: an implementing organisation named in a CRS record feeds corporate-registry and NGO-transparency lookups.

## Inputs → Outputs
- **In:** `employer-org` (donor/agency/recipient) — plus sector/year filters
- **Out:** funding records tying donor `employer-org`s to recipient `geolocation`s, amounts, sectors, project descriptions
- **Empty/negative result looks like:** no rows for the filter combination — the entity may not report to the DAC, or the aid predates coverage; absence isn't proof no funding occurred.

## Gotchas & OpSec
- The old `data.htm` URL is a redirect; the current home is the OECD Data Explorer — don't assume the legacy page is dead.
- Data is aggregate and activity-level, not person-level — good for organisational money-trails, not for finding an individual.
- Reporting lags 1–2 years and depends on each donor self-reporting; recent flows may be incomplete.
- CRS project descriptions are free-text and inconsistently detailed.

## Overlaps ("do both")
- Pairs with [[oecd-data]] and NGO/charity-registry tools — the DAC database gives the official flow figures, while registries give the legal/organisational identity of the parties.

## Trust & verifiability
`trust: trusted` — the authoritative, methodologically-documented international source for ODA statistics, maintained by the OECD DAC.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | oecd-aid-database |
| category | public-records |
| selectorsIn → selectorsOut | employer-org → employer-org, geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
