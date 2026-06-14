---
id: here-maps
name: HERE Maps
description: Use when you have an `address`/`geolocation` and want an interactive map, satellite view, and routing from HERE as a cross-check against Google Maps.
url: https://maps.here.com/
category: geolocation
path:
- geolocation
bestFor: Interactive maps, satellite imagery, and route analysis on a non-Google basemap.
selectorsIn:
- address
- geolocation
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: HERE WeGo consumer map is free; HERE developer/location APIs are freemium with paid tiers.
opsec: passive
opsecNote: Queries map and routing data only; the target is never contacted. No login needed for the consumer map.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: maps.here.com (HERE WeGo) is the consumer mapping product of HERE Technologies, a major commercial mapping vendor.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- here-2
- instant-google-street-view
- gpsvisualizer
aliases:
- HERE WeGo
tags:
- geospatial-research-and-mapping-tools
source: arf-seed
lastVerified: ''
enrichment: full
---

# HERE Maps

> HERE WeGo — the consumer interactive map and routing product from HERE Technologies, a strong non-Google basemap for cross-checking locations.

## When to use
You have an `address` or `geolocation` and want to view it, examine surroundings, and analyze routes — but on a different map provider than Google/OSM. HERE's road network, place data, and imagery age differ, so it's valuable for confirming a location or spotting detail Google missed (and vice versa).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open maps.here.com (no login required).
2. Search an `address`/place or paste `geolocation` coordinates to center the map.
3. Switch between map and satellite, and use "Directions" to estimate travel time/paths between two points.
4. Cross-reference the same point in Google-based tools; pivot to [[instant-google-street-view]] for ground-level imagery.

## Inputs → Outputs
- **In:** `address` or `geolocation`
- **Out:** interactive map/satellite view and routing (`geolocation`)
- **Empty/negative result looks like:** an address resolving to the wrong place or a country centroid — verify against [[here-2]] or re-geocode in [[gpsvisualizer]].

## Gotchas & OpSec
- No account needed for the web map; bulk/automated geocoding requires the HERE developer API and a key.
- OpSec: passive — you only query basemap/routing data; the target is not contacted.

## Overlaps ("do both")
- Same provider as [[here-2]] (corporate domain). Pair with Google/OSM maps to catch coverage and imagery-date gaps that any single provider has.

## Trust & verifiability
`trust: trusted` — HERE Technologies is an established commercial mapping vendor with reliable data.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | here-maps |
| category | geolocation |
| selectorsIn → selectorsOut | address, geolocation → geolocation |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
