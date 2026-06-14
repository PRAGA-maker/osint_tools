---
id: openrailwaymap-2
name: OpenRailwayMap
description: Use when a photo or area shows railway tracks, stations, signals, or catenary and you want to identify/confirm a location by its rail infrastructure.
url: https://www.openrailwaymap.org/
category: geolocation
path:
- geolocation
bestFor: Identifying locations from railway features — lines, stations, signals, electrification, track speed — using OSM rail tags.
selectorsIn:
- geolocation
- image
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free; renders OpenStreetMap railway tags. No account needed.
opsec: passive
opsecNote: Browsing the map reads public OSM data and does not contact the subject. No target interaction.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Respected OSM-derived thematic map for railways; completeness tracks OSM rail tagging, which is excellent in Europe and variable elsewhere.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- openstreetmap
- openinfrastructuremap
aliases:
- Open Railway Map
- ORM
tags:
- geospatial-research-and-mapping-tools
- railway
source: arf-seed
lastVerified: ''
enrichment: full
---

# OpenRailwayMap

> A thematic OSM map specialized in railway infrastructure — lines, stations, signals, electrification — useful for geolocating scenes near tracks.

## When to use
You have an `image` or area showing rail features — track layout, a station, signal types, overhead catenary, gauge — and you want to match it to a real location or confirm a candidate `geolocation`. Rail networks are sparse and distinctive, so a visible junction, station name, or electrification style can strongly narrow location. Medium MP relevance: it corroborates a place (e.g., where media was taken) rather than locating a person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open openrailwaymap.org and pan/zoom to your candidate area.
2. Switch view modes (infrastructure / max-speed / signals / electrification) to read the specific detail visible in your photo.
3. Match line geometry, station placement, signal/catenary style, and any readable station names against the image.
4. Pivot to [[openstreetmap]] for raw tags and to satellite/street view to confirm the exact spot.

## Inputs → Outputs
- **In:** candidate `geolocation` and/or an `image` showing rail infrastructure.
- **Out:** confirmed/narrowed `geolocation`.
- **Empty/negative result looks like:** no rail features in view, or under-tagged track in a thinly mapped region — absence is weak evidence.

## Gotchas & OpSec
- Depends on OSM rail tagging; outstanding in Europe, patchier elsewhere.
- Signal/speed/electrification overlays are contributor-entered; corroborate decisive matches with imagery.
- OpSec: passive; no subject contact.

## Overlaps ("do both")
- Pairs with [[openinfrastructuremap]] (power/telecom layers) and [[openstreetmap]] — different thematic slices of the same OSM data; pick the one matching the visible feature.

## Trust & verifiability
`trust: community` — built on openly auditable OSM data, but coverage/accuracy vary by region; use as a corroborating layer alongside imagery.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | openrailwaymap-2 |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, image → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
