---
id: qgis
name: QGIS
description: Use when you need to overlay, measure and analyze geospatial layers (imagery, terrain, coordinates) for serious location analysis.
url: http://qgis.org
category: geolocation
path:
- geolocation
bestFor: Full-featured free/open-source desktop GIS for layering, measuring and analyzing geospatial data.
selectorsIn: [geolocation, address, metadata]
selectorsOut: [geolocation, metadata]
status: live
pricing: free
opsec: passive
opsecNote: Runs locally on your machine; basemaps/plugins may call external tile servers, but no target data is sent anywhere by the app itself.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: trusted
trustNote: Flagship OSGeo project, widely used in government, academia and professional OSINT; open source and actively maintained.
missingPersonsRelevance: high
coverage: [global]
auth: none
api: false
localInstall: true
registration: false
aliases: [Quantum GIS]
tags:
- geospatial-research-and-mapping-tools
source: awesome-osint
lastVerified: ''
enrichment: full
---

# QGIS

> The leading free and open-source desktop Geographic Information System — for layering, measuring, georeferencing and analyzing spatial data.

## When to use
You have `geolocation` data (coordinates, GPS tracks, imagery, an `address` to geocode, or `metadata` like a satellite scene) and need to do real analysis: overlay multiple layers, measure distances/areas, georeference a scanned map, buffer a search radius around a last-known point, or correlate terrain with a witness description. This is the heavyweight tool when a quick web map is not enough.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download and install QGIS (Windows/macOS/Linux) from https://qgis.org.
2. Add base layers (e.g. OpenStreetMap, satellite XYZ tiles) and import your data layers (CSV of coordinates, GeoJSON, KML, imagery, GPX tracks).
3. Use measure, buffer, and georeferencer tools to analyze the area; style and annotate.
4. Export maps/figures (`geolocation` + `metadata`). Pivot: bring in imagery downloaded via `[[sas-planet]]` or scenes from `[[sentinel-hub]]`/`[[skyfi-com-satellite-open-data]]`.

## Inputs → Outputs
- **In:** `geolocation` (coordinates, tracks, imagery), `address` (geocodable), `metadata` (scene info)
- **Out:** analyzed/annotated `geolocation` layers and exportable maps with `metadata`
- **Empty/negative result looks like:** layers fail to align — usually a coordinate reference system (CRS) mismatch, not missing data.

## Gotchas & OpSec
- Human-in-the-loop: none for the app; it requires GIS skill, which is the real barrier.
- OpSec: passive and local. The app runs on your machine; only basemap tile/plugin requests go out, and none reveal your target.
- CRS/projection mistakes are the #1 source of wrong measurements — always confirm layer CRS.

## Overlaps ("do both")
- Pairs with `[[sas-planet]]` (offline imagery downloads) and `[[sentinel-hub]]`/`[[skyfi-com-satellite-open-data]]` (scene sourcing) — QGIS is where you bring those layers together for analysis.

## Trust & verifiability
`trust: trusted` — a mature OSGeo flagship project, open source, audited by a large professional community and used by governments worldwide.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | qgis |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address, metadata → geolocation, metadata |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | no |
