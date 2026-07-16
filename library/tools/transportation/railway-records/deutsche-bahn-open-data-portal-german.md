---
id: deutsche-bahn-open-data-portal-german
name: Deutsche Bahn Open-Data-Portal
description: Use when you have a German rail `geolocation`/station and want infrastructure, timetable, or station data — returns station metadata, network data, and schedules.
url: https://data.deutschebahn.com/opendata
category: transportation
path:
- transportation
- railway-records
bestFor: Open datasets on German rail stations, network infrastructure, and timetables from Deutsche Bahn.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
- address
status: live
pricing: free
costNote: Free open-data portal; datasets are openly licensed. Some live APIs (via DB's API marketplace) need a free developer key.
opsec: passive
opsecNote: Consuming open government/transport data is passive — it concerns infrastructure and schedules, not individuals, and notifies no one. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: api
trust: trusted
trustNote: Official Deutsche Bahn open-data portal; authoritative for German rail infrastructure and timetables.
missingPersonsRelevance: low
coverage:
- de
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- DB Open Data
- Deutsche Bahn Open Data
tags:
- railway
- open-data
- germany
source: arf-seed
lastVerified: '2026-07-16'
enrichment: full
---

# Deutsche Bahn Open-Data-Portal

> Deutsche Bahn's open-data portal — authoritative datasets on German rail stations, network infrastructure, and timetables, useful for placing and timing rail travel or geolocating a station scene.

## When to use
You're working a case that touches German rail: geolocating a photo taken at/near a station (station layouts, names, coordinates), reconstructing whether a rail journey was feasible at a given time (timetables), or characterizing rail infrastructure in an area. It's an infrastructure/schedule dataset — it tells you about stations and trains, not passengers — so missing-persons relevance is contextual (timeline/geolocation support).

## How to use it (`bestInteractionPattern`: api)
1. Open data.deutschebahn.com/opendata and browse the dataset catalog (stations, station facilities, timetables, network).
2. Download the relevant dataset (CSV/GTFS/etc.) or use the linked API (free developer key for live endpoints).
3. Query for a station's coordinates/`address`, facilities, or the timetable for a route/time.
4. Correlate: does a station's layout/signage match your image? Was a claimed train connection actually running then?
5. Pivot: a confirmed station geolocation feeds imagery cross-checks; timetable feasibility supports or refutes a movement claim.

## Inputs → Outputs
- **In:** a station name / `geolocation` / route + time
- **Out:** station metadata (coordinates/`address`, facilities), network/infrastructure data, and timetables
- **Empty/negative result looks like:** no dataset/record for the query — the station may be minor/unlisted, or the timetable data doesn't cover that period; DB open data is broad but not exhaustive historically.

## Gotchas & OpSec
- German rail only — irrelevant outside Germany's DB network.
- Data is infrastructure/schedule, not passenger data — it won't tell you who traveled.
- Some datasets are static snapshots; live status needs the API endpoints.
- OpSec: fully passive open data.

## Overlaps ("do both")
- Pairs with OpenRailwayMap and general geolocation tools — DB open data gives authoritative station/timetable detail; OSM/imagery confirms the physical scene.

## Trust & verifiability
`trust: trusted` — official DB open data; authoritative for German rail infrastructure and schedules.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | deutsche-bahn-open-data-portal-german |
| category | transportation |
| selectorsIn → selectorsOut | geolocation → geolocation, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | api |
| opsec | passive |
| human-in-loop | no |
