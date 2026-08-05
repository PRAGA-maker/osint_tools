---
id: wildlife-trade-portal
name: Wildlife Trade Portal
description: Use when you have a species, country, or date range and want documented wildlife-seizure/trafficking incidents — returns incident records with locations, actors, and exportable data.
url: https://www.wildlifetradeportal.org/
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Searching global wildlife seizure and trade-incident records by species, country, and date.
selectorsIn:
- name
- address
selectorsOut:
- address
- associate
status: live
pricing: free
costNote: Free, open-access public interface (the public, non-nominal slice of TRAFFIC's WITIS dataset); no account required.
opsec: passive
opsecNote: Passive — you query a published incident database; nothing is sent to any subject. Note the public data is deliberately non-nominal (it omits personal identifiers held in the restricted law-enforcement dataset), so it's already privacy-scoped.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Built and maintained by TRAFFIC (the wildlife-trade monitoring NGO) from its WITIS database of 720,000+ records; an authoritative, methodology-documented source listed in Bellingcat's toolkit.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- wildlifetradeportal.org
- TRAFFIC Wildlife Trade Portal
tags:
- bellingcat-toolkit
- environment-wildlife
- seizure-data
source: bellingcat-toolkit
lastVerified: '2026-08-05'
enrichment: full
---

# Wildlife Trade Portal

> TRAFFIC's open-access window into global wildlife-seizure data: search documented trafficking incidents by species, country, and date, and export the results.

## When to use
Your investigation touches wildlife trafficking — a suspect, company, route, or seizure — and you want documented incidents to corroborate or map it: what was seized, where, when, and (where recorded) whether organised crime, corruption, or named locations were involved. A specialist investigative database rather than a person-finder; the public data is non-nominal, so it gives context and links, not personal identifiers.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.wildlifetradeportal.org/.
2. Search/filter by species, countries involved, and date range; use advanced search for organised-crime/corruption flags, specific locations, or taxonomic detail.
3. View results as a list or via the interactive dashboard of charts and maps to spot geographic and temporal patterns.
4. Open an incident for detail — species, products, quantities, locations (`address`), and connections (`associate`-level links between places/actors where recorded).
5. Export to CSV for offline analysis. Pivot: a location/route feeds mapping; a company or named entity feeds corporate/registry lookups.

## Inputs → Outputs
- **In:** a species, country, location (`address`), or entity `name`
- **Out:** wildlife-seizure incident records — locations (`address`), routes, and recorded connections (`associate`), exportable as CSV
- **Empty/negative result looks like:** no incidents for your filters — the event may be unrecorded in WITIS, too recent to be entered, or outside its scope. Absence is not proof no seizure occurred; corroborate with CITES trade data and national enforcement sources.

## Gotchas & OpSec
- Public data is non-nominal by design — no personal identifiers; the full nominal dataset is restricted to law enforcement.
- Coverage depends on what TRAFFIC has ingested; recording is uneven across countries and years.
- It documents *incidents*, not people — use it for context/patterns, then pivot to identity sources.
- OpSec: fully passive; querying reveals nothing to any subject.

## Overlaps ("do both")
- Cross-reference with the CITES Illegal Trade Database and national seizure records — the datasets overlap partially, and combining them fills gaps and confirms an incident from more than one source.

## Trust & verifiability
`trust: trusted` — an authoritative NGO-maintained database with documented methodology; incident records are reliable within their stated scope, and the main caveat is coverage/recency, not accuracy.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wildlife-trade-portal |
