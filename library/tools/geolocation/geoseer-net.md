---
id: geoseer-net
name: GeoSeer
description: Use when you have a place `geolocation` or theme and want to find published GIS/spatial datasets and live map services covering it — returns WMS/WFS/WCS/WMTS layers you can pull for imagery, boundaries and features.
url: https://www.geoseer.net/
category: geolocation
path:
- geolocation
bestFor: Searching millions of public GIS spatial datasets (WMS/WFS/WCS/WMTS) by place and theme.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: Web search is free; an API and higher-volume/commercial use are licensed/paid.
opsec: passive
opsecNote: You search a public index of spatial-data services; no target interaction. Note that opening a discovered WMS/WFS service does hit that third-party GIS server directly, so use a clean session if the service operator is sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Independent, well-known spatial-data search index (3.5M+ datasets across 400k+ live services); it points to third-party services whose accuracy and uptime it does not control.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- geoseer.net
- spatial data search engine
tags:
- gis
- spatial-data
- maps
source: osint4all
lastVerified: '2026-07-21'
enrichment: full
---

# GeoSeer

> A search engine for the world's published GIS layers — find WMS/WFS/WCS/WMTS services covering an area, then pull imagery, boundaries and feature data most map sites never expose.

## When to use
You're working an area `geolocation` and want authoritative spatial data for it — parcel/cadastral boundaries, land use, hydrology, addressing, imagery, infrastructure — published as live map services by governments, utilities and researchers. GeoSeer indexes those services so you can discover data that never surfaces in a normal web or map search, useful for grounding a location, mapping terrain around a last-known point, or finding local feature layers.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.geoseer.net/.
2. Search with a place name plus a theme (e.g. `parcels Yorkshire`, `flood zones Texas`), optionally constraining by service type (WMS/WFS/WCS/WMTS), projection (EPSG code), or Boolean operators.
3. Review the ranked list of matching datasets — each entry names the dataset, its host service, and coverage.
4. Open a result to get the service endpoint; load it into a WebGIS client (GeoSeer has a demo viewer) or QGIS to actually view/query the layer.
5. Pivot: a WFS feature layer can yield precise coordinates/boundaries for a location; imagery layers support visual geolocation and change-over-time analysis.

## Inputs → Outputs
- **In:** `geolocation` (place name / area) + optional theme
- **Out:** `geolocation` data — links to WMS/WFS/WCS/WMTS layers (imagery, boundaries, features) covering the area
- **Empty/negative result looks like:** few or no matching services — the area/theme isn't covered by any indexed public GIS service, or your terms are too narrow. Broaden the theme or search the region's national spatial-data portal directly.

## Gotchas & OpSec
- GeoSeer indexes *services it has found*; a discovered endpoint may be slow, moved, or access-restricted when you actually connect to it.
- Consuming a discovered WMS/WFS **connects you to that third-party server** — passive toward your subject, but the service host sees the request.
- The free tier is the web search; programmatic/bulk use needs the licensed API.

## Overlaps ("do both")
- Pairs with general mapping/imagery tools and national geoportals — GeoSeer *discovers* the specialist layers; a GIS client or mapping tool *renders and analyzes* them.

## Trust & verifiability
`trust: community` — a reputable independent index. It reliably points you to real services, but data quality and currency belong to each underlying publisher, so verify against the authoritative source layer.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | geoseer-net |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
