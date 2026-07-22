---
id: openseamap
name: OpenSeaMap
description: Use when you have a maritime `geolocation` and want nautical context — sea marks, harbours, shipping lanes, depths — returns a nautical chart layer over the location.
url: https://map.openseamap.org/
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Getting nautical/maritime map context (buoys, harbours, lanes, sea marks) for a coastal or open-water location.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free, community-built on OpenStreetMap data; no account.
opsec: passive
opsecNote: Browsing a public map is passive and reveals nothing to any subject — standard browser hygiene is enough.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: An OpenStreetMap-based crowdsourced nautical chart; coverage and accuracy vary by region and must not be used for actual navigation.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- openseamap-the-free-nautical-chart
- what3words
- convert-geographic-units
aliases:
- OpenSeaMap
- open sea map
tags:
- bellingcat-toolkit
- maps
- maritime
source: bellingcat-toolkit
lastVerified: '2026-07-22'
enrichment: full
---

# OpenSeaMap

> A free, crowdsourced nautical chart layered on OpenStreetMap — sea marks, harbours, shipping lanes and depths for making sense of a location on or near the water.

## When to use
An investigation touches the sea: a `geolocation` from a vessel photo, a coastal incident, a harbour, or a point in open water where you need maritime context that street maps lack. OpenSeaMap overlays buoys, beacons, harbour facilities, ferry/shipping lanes and depth information, which helps you interpret what a coordinate near the coast actually is (a marina berth? a lane? a hazard?).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://map.openseamap.org/.
2. Navigate to the `geolocation`/`address`, or paste coordinates to centre the map.
3. Toggle layers — sea marks, harbours, depth contours, and overlays for weather/traffic where available.
4. Click features (buoys, harbours) to read their attributes and identifiers.
5. Pivot: combine with vessel-tracking (AIS/MarineTraffic) to tie a lane or harbour to specific ship movements; use `[[convert-geographic-units]]` to reformat coordinates for other maritime systems.

## Inputs → Outputs
- **In:** a maritime `geolocation` or coastal `address`
- **Out:** a nautical chart layer — sea marks, harbours, lanes, depths — for that `geolocation`
- **Empty/negative result looks like:** sparse or missing sea marks in a region means the crowdsourced data is thin there, not that the water is featureless — corroborate with official charts.

## Gotchas & OpSec
- Crowdsourced and explicitly **not for navigation** — coverage and accuracy are uneven; official hydrographic charts are authoritative.
- AIS/traffic overlays depend on third-party feeds that may lag or be incomplete.
- OpSec: passive; a public map with no login.

## Overlaps ("do both")
- Pairs with vessel-tracking/AIS tools and `[[what3words]]` — OpenSeaMap gives the nautical backdrop, AIS gives the moving ships, and what3words gives a shareable pin for a specific spot.

## Trust & verifiability
`trust: community` — an OSM-based volunteer chart; treat features as leads and confirm anything safety- or evidence-critical against official maritime sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | openseamap |
