---
id: wildeye
name: WildEye
description: Use when you have a `name`, location or case tied to wildlife/environmental crime and want documented seizures, arrests, court cases and convictions — returns mapped incidents with names and outcomes.
url: https://global.wildeye.oxpeckers.org/
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Tracking wildlife/environmental crime incidents and prosecutions (seizures, arrests, court cases, convictions) on an interactive global map.
selectorsIn:
- name
- geolocation
selectorsOut:
- name
- geolocation
- employer-org
status: live
pricing: free
costNote: Free public interactive map/database published by the Oxpeckers investigative journalism unit; data is downloadable.
opsec: passive
opsecNote: Passive — you browse a published journalism database; no query about your subject is exposed to any adversary. Standard sock-puppet browsing hygiene is enough.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Maintained by Oxpeckers Investigative Environmental Journalism; incidents are sourced from court records and reporting, though coverage depends on what has been documented.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- '#WildEye'
- Oxpeckers WildEye
tags:
- environmental-crime
- wildlife-crime
- court-records
source: awesome-osint
lastVerified: '2026-08-05'
enrichment: full
---

# WildEye

> Oxpeckers' interactive map of wildlife and environmental crime — filter seizures, arrests, court cases and convictions by place to surface the people and organisations behind them.

## When to use
Your subject may be connected to wildlife or environmental crime (poaching, trafficking, illegal logging/fishing), or you're profiling a region's enforcement record. WildEye lets you filter documented incidents and prosecutions by type and location, exposing defendant `name`s, court outcomes, and the organisations/`geolocation`s involved.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://global.wildeye.oxpeckers.org/ (or a regional edition: Asia, Europe, Southern/Eastern Africa).
2. Use "Filter map pins" to toggle Seizures / Arrests / Court Cases / Convictions.
3. Click a pin to read the incident: species, location, people/entities named, and prosecution status.
4. Pivot: take a defendant `name` into people-search and court-record tools; use the "Get #WildEye Data" export for bulk cross-referencing.

## Inputs → Outputs
- **In:** `name` (suspect/defendant) or `geolocation` (region of interest)
- **Out:** `name`, `geolocation`, `employer-org` (named individuals, locations, and companies in documented cases and convictions)
- **Empty/negative result looks like:** no pins in an area/filter means nothing has been documented there in WildEye — an absence of records, not proof no crime occurred.

## Gotchas & OpSec
- Human-in-the-loop: none; fully browsable.
- Coverage is only as complete as what Oxpeckers has logged — strong in some regions, thin in others; treat gaps as unknowns.
- It records documented/reported cases; corroborate any name against primary court records before asserting guilt.

## Overlaps ("do both")
- Pair with national court-record and company-registry tools: WildEye points you to the case and the names, those confirm the legal outcome and any corporate links.

## Trust & verifiability
`trust: trusted` — a curated investigative-journalism database built from court records and reporting; reliable as a lead source, with the usual caveat that coverage is uneven by region.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wildeye |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | name, geolocation → name, geolocation, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
