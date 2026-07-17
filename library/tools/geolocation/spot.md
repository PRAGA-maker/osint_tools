---
id: spot
name: Spot
description: Use when you have a `geolocation` region plus a described scene and want candidate coordinates matching that description in OpenStreetMap — returns geolocation candidates.
url: https://www.findthatspot.io/
category: geolocation
path:
- geolocation
bestFor: Narrowing where a photo/video was taken by querying OpenStreetMap for locations that match described features (a church next to a lake, a bridge near a stadium, etc.).
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free web tool built on OpenStreetMap/Overpass data; no account required.
opsec: passive
opsecNote: You query public OpenStreetMap data, not the subject; nothing is disclosed to any target. Safe from any browser.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Featured in the Bellingcat toolkit; built on open OpenStreetMap data, so results are only as complete as OSM tagging in the area.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Find That Spot
- findthatspot.io
tags:
- bellingcat-toolkit
- geolocation
- osm
source: bellingcat-toolkit
lastVerified: '2026-07-17'
enrichment: full
---

# Spot

> A geolocation helper that turns "what's near what" into an OpenStreetMap query — search a region for places matching the features you can see.

## When to use
You're geolocating an image/video and have a rough region plus identifiable features — "a church within ~200m of a lake and a school," "a football stadium next to a river." Spot lets you express that spatial relationship against OpenStreetMap and returns candidate `geolocation` points to check in satellite/Street View. It narrows a search area; it does not identify a location on its own.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.findthatspot.io/.
2. Set the map to your candidate region (pan/zoom or enter a place/`address`).
3. Build a query describing the features and their proximity (the tool exposes an Actions/Query builder over OSM/Overpass).
4. Run it and review the returned candidate points on the map.
5. Pivot: open each candidate in satellite imagery / Google Street View to confirm, then lock the `geolocation`.

## Inputs → Outputs
- **In:** a `geolocation`/`address` region + a described scene (features + proximity)
- **Out:** candidate `geolocation` points matching the query
- **Empty/negative result looks like:** no candidates — usually means the features aren't tagged in OSM for that area or the query is too strict; loosen the query or widen the region rather than concluding the place doesn't exist.

## Gotchas & OpSec
- Results depend entirely on **OpenStreetMap tagging**, which is uneven — sparse-mapping regions yield few/no hits even when the feature is really there.
- It proposes candidates, not answers; always verify each on imagery/Street View.
- Very broad queries over large areas can be slow or capped by Overpass.

## Overlaps ("do both")
- Pairs with satellite/Street View verification and with OSM feature search — Spot generates candidate coordinates, imagery confirms them.

## Trust & verifiability
`trust: community` — a Bellingcat-listed open tool over public OSM data; reliable as a candidate generator, but every result must be confirmed against ground imagery.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | spot |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
