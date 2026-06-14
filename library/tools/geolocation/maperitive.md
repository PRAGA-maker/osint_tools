---
id: maperitive
name: Maperitive
description: Use when you need to render or export custom OpenStreetMap maps/tiles offline on the desktop — a map-rendering app, not a lookup service.
url: http://maperitive.net
category: geolocation
path:
- geolocation
bestFor: Desktop rendering and export of custom OpenStreetMap-based maps and tiles for offline analysis or printing.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: degraded
pricing: free
costNote: Free Windows desktop application; development appears stalled/unmaintained.
opsec: passive
opsecNote: Renders maps locally from OSM data you load; no contact with any target.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: desktop-app
trust: community
trustNote: Established but seemingly unmaintained OSM rendering tool; a cartography utility, not a data source.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases: []
tags:
- geospatial-research-and-mapping-tools
- cartography
- osm
source: awesome-osint
lastVerified: ''
enrichment: full
---

# Maperitive

> Free Windows desktop app for rendering and exporting custom OpenStreetMap maps and tiles — a cartography tool for producing maps, not for finding people.

## When to use
You need an offline, printable, or custom-styled map of an area — for a field search packet, an annotated route, or generating tiles to use elsewhere. It works from a `geolocation` (an area you load from OSM) and outputs styled map images/tiles. It holds no personal data and performs no lookups, so its direct value to locating a missing person is low; it is a production/output tool. Development appears inactive, so treat it as legacy.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download and run Maperitive (Windows; runs under Mono on other OSes).
2. Load an OSM data source / web map for your area of interest.
3. Apply a rendering ruleset/style and zoom to your region.
4. Export the rendered map as an image or generate tiles for offline use.
5. Pivot: print a clean area map for a ground search, or feed exported tiles into another mapping workflow.

## Inputs → Outputs
- **In:** `geolocation` (an OSM area you load)
- **Out:** `geolocation` (a rendered/exported map image or tile set)
- **Empty/negative result looks like:** rendering errors or missing OSM data for the area; the tool itself never "searches", so there is no investigative empty state.

## Gotchas & OpSec
- Appears unmaintained — expect rough edges and limited support; modern alternatives (QGIS, web tile tools) may be better.
- Desktop install required; Windows-first.
- OpSec: passive; all rendering is local from data you supply.

## Overlaps ("do both")
- For interactive/no-code mapping use `[[maphub]]` or `[[leaflet]]`; Maperitive is for offline rendering/printing.

## Trust & verifiability
`trust: community` — a known OSM cartography tool, but seemingly unmaintained. It produces maps from OSM data; it is not an investigative source and yields no claims to verify beyond your inputs.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | maperitive |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | yes |
