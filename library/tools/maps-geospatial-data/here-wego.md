---
id: here-wego
name: HERE WeGo
description: Use when you have an `address`/`geolocation` and want an independent map, satellite/street view, and routing alternative to Google/Apple — returns geolocation, routes, and place details.
url: https://wego.here.com/
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: A free, independent web map for cross-referencing addresses, places, and routes against Google/Apple Maps.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
- address
status: live
pricing: free
costNote: Free to use in the browser and app (HERE also sells a developer API/SDK, but the WeGo consumer map is free).
opsec: passive
opsecNote: Searching a location on HERE WeGo is a passive map query — the target is not involved and not alerted. HERE's basemap is built from different sources than Google, so it can confirm or contradict a location; it does not provide user-generated location history about people.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by HERE Technologies, a major mapping/geodata company; a mainstream, independent basemap source.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- here-2
- here-com-geolocation-and-mapping-tool
- here-maps
aliases:
- HERE WeGo
- wego.here.com
tags:
- maps
- geocoding
- routing
- bellingcat-toolkit
source: bellingcat-toolkit
lastVerified: '2026-07-23'
enrichment: full
---

# HERE WeGo

> HERE Technologies' free consumer map — an independent basemap for geocoding addresses, checking places, and planning routes when you want a second source alongside Google/Apple Maps.

## When to use
You have an `address` or `geolocation` and want to verify or enrich it on a map that isn't Google. Because HERE builds its cartography from different data (it's a major automotive/logistics mapping provider), it can corroborate a location, show labels/roads/POIs Google renders differently, and give alternative routing — valuable for triangulating a place or resolving a discrepancy between sources.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://wego.here.com/.
2. Search the `address` or drop/enter `geolocation` coordinates.
3. Read the result: map placement, place details/POIs, and satellite imagery where available; use the directions panel for route/distance/time between points (`selectorsOut`).
4. Pivot: cross-check the placement against Google/Bing/Yandex maps; use HERE's routing to estimate travel time between two locations in a timeline.

## Inputs → Outputs
- **In:** `address` or `geolocation` (coordinates / place name)
- **Out:** `geolocation` (map placement, POIs), `address` (reverse-geocoded), routes/distances
- **Empty/negative result looks like:** a place not found or mislabeled — HERE's POI/label coverage differs by region; fall back to another map provider rather than assuming the location is invalid.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: passive — a map query with no target involvement.
- It's a basemap, not a people/location-history source; regional imagery freshness and POI coverage vary, so always cross-map a critical location.

## Overlaps ("do both")
- Pairs with other HERE entries [[here-maps]] / [[here-com-geolocation-and-mapping-tool]] and with Google/Bing/Yandex maps — multi-map cross-referencing is the whole point, since each provider's imagery and labels differ.

## Trust & verifiability
`trust: trusted` — HERE Technologies is a mainstream, well-resourced mapping company, so its basemap and geocoding are authoritative; differences from Google usually reflect genuine source variation rather than error, which is exactly why it's useful as a second opinion.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | here-wego |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation, address → geolocation, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
