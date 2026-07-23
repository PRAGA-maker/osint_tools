---
id: acled-armed-conflict-location-and-event-data-project
name: ACLED (Armed Conflict Location & Event Data Project)
description: Use when you have a place and date range in a conflict/protest zone and want geolocated event data — returns geolocation and address-level event records to build local context around a subject's whereabouts.
url: https://acleddata.com/
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Geolocated, dated records of political violence and protest to establish on-the-ground context for a place and time.
selectorsIn:
- address
- geolocation
selectorsOut:
- geolocation
- address
status: live
pricing: freemium
costNote: Free Data Export Tool, downloadable files, and public dashboards; a free myACLED account unlocks the Explorer and API for advanced/bulk access.
opsec: passive
opsecNote: You query ACLED's curated event database, not the subject — passive. Note ACLED's access terms and attribution requirements when you reuse the data.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: ACLED is a widely-cited, methodologically documented conflict-data project used by researchers, journalists, and governments.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
relatedTools:
- acled-data-crisis-map
- us-crisis-monitor
aliases:
- ACLED
- Armed Conflict Location and Event Data
tags:
- bellingcat-toolkit
- conflict
- geospatial
source: bellingcat-toolkit
lastVerified: '2026-07-23'
enrichment: full
---

# ACLED (Armed Conflict Location & Event Data Project)

> A curated, geolocated database of political violence and protest events worldwide — the reference source for "what was happening at this place on this date."

## When to use
Your subject was last known in — or is being traced through — a region affected by conflict, unrest, or protest, and you need reliable local context: what violent events, clashes, or demonstrations occurred at a given `address`/`geolocation` and time. ACLED's dated, coordinate-tagged records help build a timeline of an area's security situation, corroborate or challenge a movement story, and flag danger zones. It maps events, not individuals.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://acleddata.com and use the **Data Export Tool** (free) — filter by country/region, event type, actor, and date range.
2. Or browse the regional **dashboards/monitors** (Ukraine, Gaza, US Crisis Monitor, etc.) for a mapped view.
3. For advanced querying or bulk pulls, create a free **myACLED** account and use the **Explorer**/API.
4. Read each event's date, precise `geolocation`, actors, and a sourced description; export to CSV/GeoJSON for mapping.
5. Pivot: map events onto a subject's known route; cross-reference dates with news/social posts to tighten a timeline.

## Inputs → Outputs
- **In:** a country/region + date range (and optionally an `address`/`geolocation` to filter near).
- **Out:** geolocated, dated event records (type, actors, fatalities, sourced notes) at `address`/`geolocation` granularity.
- **Empty/negative result looks like:** no coded events for that place/period — either genuinely quiet, or below ACLED's reporting threshold; absence of an event is not proof nothing happened.

## Gotchas & OpSec
- Advanced tools (Explorer/API) require a free account login; basic export/dashboards do not.
- Coverage and coding depth vary by region and rely on media/partner reporting — sparse local media means undercounting.
- Reuse is governed by ACLED's access and attribution terms; cite the dataset and version.

## Overlaps ("do both")
- Pairs with its own [[acled-data-crisis-map]] and [[us-crisis-monitor]] dashboards for a mapped view, and with general mapping tools to overlay events onto a subject's known locations.

## Trust & verifiability
`trust: trusted` — a well-established, methodologically transparent project; each event is sourced, so individual records can be traced back to their reporting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | acled-armed-conflict-location-and-event-data-project |
