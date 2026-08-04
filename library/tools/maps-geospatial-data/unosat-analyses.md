---
id: unosat-analyses
name: UNOSAT Analyses & Rapid Mapping
description: Use when you have a `geolocation`/place tied to a disaster or conflict and want authoritative satellite-derived damage/situation maps — returns UN analyst maps, reports, and GIS data.
url: https://unosat.org/products
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Getting UN-grade satellite analysis of a conflict, disaster, or crisis area — damage assessment, flood/fire extent, displacement.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free to browse and download; produced by UNITAR/UNOSAT, funded by the Norwegian Ministry of Foreign Affairs and partners.
opsec: passive
opsecNote: You are downloading pre-published maps and reports from a UN site — nothing touches any subject. Only your own request to unosat.org is logged; use a VPN if you don't want the lookup tied to your IP.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Produced by the United Nations Satellite Centre (UNITAR/UNOSAT) with professional analysts and documented imagery sources — authoritative for crisis geospatial analysis.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- UNOSAT
- UNITAR Operational Satellite Applications Programme
- UNOSAT Rapid Mapping
tags:
- satellite-imagery
- humanitarian
- damage-assessment
- geospatial
source: bellingcat-toolkit
lastVerified: '2026-08-04'
enrichment: full
---

# UNOSAT Analyses & Rapid Mapping

> The UN's satellite-analysis service: professionally-produced maps and reports of disasters, conflicts, and crises, free to download and cross-reference.

## When to use
Your investigation is anchored to a `geolocation` or place affected by a natural disaster, armed conflict, or humanitarian emergency, and you need authoritative overhead analysis rather than raw imagery you'd have to interpret yourself. UNOSAT publishes analyst-verified damage assessments, flood/fire extents, refugee-camp mappings, and displacement analyses — invaluable for corroborating what happened at a location and when.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://unosat.org/products (the products/maps catalogue).
2. Browse or search by region, country, or event type (conflict, flood, earthquake, wildfire).
3. Open the relevant product: web maps, downloadable static maps (PDF), analytical reports, and GIS-ready data layers.
4. Read the analysis — damage points, affected areas, and dates are analyst-derived, so they can anchor a timeline or confirm the state of a place at a given date.
5. Pivot: load the GIS data into your own map, or cross-reference the `geolocation` against commercial imagery archives for a specific date/time.

## Inputs → Outputs
- **In:** `geolocation` / place name tied to a crisis event
- **Out:** analyst maps, reports, and GIS data confirming conditions at a `geolocation` and date
- **Empty/negative result looks like:** no product for your area/event — UNOSAT only maps activated emergencies, so absence means no analysis was commissioned there, not that nothing happened.

## Gotchas & OpSec
- Human-in-the-loop: none; browsing and downloads are open.
- OpSec: **passive** — everything is pre-published; no subject is contacted.
- Coverage is event-driven: UNOSAT maps crises it is tasked on, so it's excellent for major disasters/conflicts and silent on routine locations. Check the product date — a map reflects imagery from a specific acquisition, not "now."

## Overlaps ("do both")
- Pairs with commercial/open satellite archives (Sentinel, Planet, Google Earth timelapse) — UNOSAT gives the *interpreted* analysis while raw archives let you inspect other dates and verify the analysts' read yourself.

## Trust & verifiability
`trust: trusted` — a UN institution (UNITAR/UNOSAT) with named analysts and disclosed imagery sources; among the most reliable geospatial-analysis sources available.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | unosat-analyses |
