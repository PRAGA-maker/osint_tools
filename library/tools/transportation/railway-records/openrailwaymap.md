---
id: openrailwaymap
name: OpenRailwayMap
description: Use when you have a `geolocation` (an image of a railway scene or a region) and want to identify the rail line, its infrastructure and characteristics — returns `geolocation`.
url: https://www.openrailwaymap.org/
category: transportation
path:
- transportation
- railway-records
bestFor: Identifying and analysing rail infrastructure — line routes, electrification, gauge, speed and signalling — as an OSM overlay for geolocation.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free and open (OpenStreetMap-based); no account required, and the underlying data is under the ODbL licence.
opsec: passive
opsecNote: Read-only public map; querying it reveals nothing to any subject. Standard browser hygiene is enough.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Built on crowd-sourced OpenStreetMap data — coverage and accuracy vary by region and depend on volunteer mapping, so treat detail as indicative and verify against imagery.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- openrailwaymap-2
- openstreetmap
- bellingcat-openstreetmap-search
aliases:
- ORM
- OpenStreetMap railway layer
tags:
- transportation
- railway
- geolocation
- openstreetmap
source: arf-seed
lastVerified: '2026-07-21'
enrichment: full
---

# OpenRailwayMap

> The OpenStreetMap railway layer — a free, detailed overlay of the world's tracks, electrification, gauges and speeds, useful for pinning down where a rail photo was taken.

## When to use
You are geolocating a photo or video that shows railway infrastructure — tracks, a station, catenary/overhead lines, signals, a level crossing — or you need to understand the rail context of an area. OpenRailwayMap overlays rich rail metadata on the map: line routes and names, single vs multiple track, electrification type/voltage, track gauge, maximum speeds, and signalling. Matching visible features (electrified or not, number of tracks, station layout) against the map narrows a location fast.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.openrailwaymap.org/ and navigate/zoom to the candidate region.
2. Switch layers (top-right): Infrastructure, Speed, Electrification, Gauge, Signals — each recolours the map by that attribute.
3. Compare features in your image to the map: e.g. "electrified double track with a passing loop" filters the possibilities dramatically.
4. Click a line/feature to read its tags (operator, line ref, speed, voltage) and confirm the identification.
5. Pivot: cross-check the exact spot in `[[openstreetmap]]` and satellite imagery; use `[[bellingcat-openstreetmap-search]]` to query nearby tagged features.

## Inputs → Outputs
- **In:** `geolocation` — a region, coordinates, or the rail features visible in an image
- **Out:** `geolocation` — the identified line/segment plus its infrastructure attributes (route, electrification, gauge, speed, signalling)
- **Empty/negative result looks like:** an area with sparse or missing rail data (common outside Europe) — absence on the map means "not mapped here," not "no railway."

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: passive — a public map.
- Coverage is uneven: Central Europe is richly mapped, many other regions thinly. A public API and tile layers exist for programmatic use, but always corroborate a match against current satellite/street imagery before treating it as confirmed.

## Overlaps ("do both")
- Pairs with `[[openstreetmap]]` and `[[bellingcat-openstreetmap-search]]` — ORM gives the specialised rail attributes, the general OSM tools give surrounding context (roads, buildings, place names) to lock the exact point.

## Trust & verifiability
`trust: community` — crowd-sourced OSM data; excellent where mappers are active, incomplete elsewhere. Verify any geolocation claim against independent imagery.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | openrailwaymap |
| category | transportation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
