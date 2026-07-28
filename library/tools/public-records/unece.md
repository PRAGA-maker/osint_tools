---
id: unece
name: UNECE Statistical Database
description: Use when you have a country/region and want official UNECE cross-country statistics (population, migration, transport, gender, forestry) — returns aggregate context, no person data.
url: http://w3.unece.org/PXWeb/en
category: public-records
path:
- public-records
bestFor: Pulling official cross-country statistics for Europe, North America and Central Asia from one PXWeb portal.
selectorsIn:
- address
selectorsOut: []
status: live
pricing: free
costNote: Free public statistical portal run by a UN body; no account or payment. Data is downloadable as tables/CSV.
opsec: passive
opsecNote: Passive read of aggregate public statistics; there is no target-specific query, so nothing about a subject is disclosed. No sock puppet needed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official statistics portal of the United Nations Economic Commission for Europe, compiled from member states' national statistical offices.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- UN Economic Commission for Europe statistics
- UNECE PXWeb
tags:
- statistics
- public-records
- un-data
source: awesome-osint
lastVerified: '2026-07-28'
enrichment: full
---

# UNECE Statistical Database

> The UN Economic Commission for Europe's PXWeb portal — official aggregate statistics across ~50 member countries in Europe, North America and Central Asia.

## When to use
You need authoritative background numbers for a country or region — population and migration, transport and road-safety, gender, forestry/timber, economic indicators — to give an investigation context rather than to identify a person. This is a macro/context source: it characterises a place or trend, it does not return anyone's details. Reach for it when a case turns on demographic or migration context (e.g. displacement, cross-border movement, sector conditions) in the UNECE region.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://w3.unece.org/PXWeb/en.
2. Browse the theme tree (Population, Migration, Transport, Gender, Forestry, Economy, etc.).
3. Open a table and select the country/region (`address`), years and variables you want.
4. Read or export the resulting table (HTML/CSV/Excel) for the aggregate figures.
5. Pivot: use the numbers to frame or corroborate context; combine with national statistics offices or Eurostat/UN Data for finer or complementary series.

## Inputs → Outputs
- **In:** a country/region (`address`) plus a chosen theme and time range
- **Out:** aggregate statistical tables (population, migration, transport, gender, forestry, economy). No person-level `selectorsOut`.
- **Empty/negative result looks like:** a table with blank cells or "..." for a country/year — that series simply isn't reported for that member state, not an error.

## Gotchas & OpSec
- OpSec: fully passive; there is no per-target query to leak.
- This is aggregate data only — it will never identify or locate an individual. Wrong tool if you need person selectors.
- Coverage is the UNECE membership (Europe, North America, Central Asia, Caucasus); outside that, use the relevant regional UN commission.

## Overlaps ("do both")
- Complements other official-statistics sources in `public-records` — UNECE harmonises cross-country series that individual national portals present differently; use national offices for depth, UNECE for comparability.

## Trust & verifiability
`trust: trusted` — a first-party UN statistical portal aggregating member states' official national statistics.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | unece |
| category | public-records |
| selectorsIn → selectorsOut | address → — |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
