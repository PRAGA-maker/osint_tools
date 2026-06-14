---
id: modest-maps
name: Modest Maps
description: Use when a developer needs a lightweight library to build a custom slippy-map viewer — not a lookup tool for finding a person.
url: http://modestmaps.com
category: geolocation
path:
- geolocation
bestFor: Embedding a minimal, tile-based interactive map in a custom OSINT web app.
selectorsIn:
- geolocation
selectorsOut: []
status: degraded
pricing: free
costNote: Open-source (BSD); no cost. Library/developer dependency, not a hosted service.
opsec: passive
opsecNote: Client-side display library. Tile requests go to whatever tile provider you configure; choose one you control or trust to avoid leaking the AOI.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: python-lib
trust: community
trustNote: Long-standing open-source mapping library (originally Stamen/MapBox-era). Largely superseded by Leaflet/OpenLayers and effectively unmaintained.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- openlayers
aliases:
- ModestMaps
tags:
- geospatial-research-and-mapping-tools
- mapping-library
source: awesome-osint
lastVerified: ''
enrichment: full
---

# Modest Maps

> A small, BSD-licensed display library for building tile-based interactive maps — a developer building block, not an investigative lookup tool.

## When to use
Reach for this only if you are *building* a custom geolocation viewer and want a minimal map widget to plot a `geolocation` (coordinates, AOI bounds, candidate points) on tiles. It does not search for people, addresses, or imagery — it renders what you give it. For actual investigation, use [[openstreetmap]] or [[overpass-turbo]] instead.

## How to use it (`bestInteractionPattern`: python-lib)
1. Pick the port for your stack (originally ActionScript/Processing/Python; the Python port is the OSINT-relevant one).
2. Install/include the library and point it at a tile source (OSM, your own tile server).
3. Pass coordinates/bounds to center and zoom; add markers for candidate locations.
4. Pivot: this is a presentation layer — feed it points produced by real geolocation tooling.

## Inputs → Outputs
- **In:** `geolocation` (coordinates / bounding box to display).
- **Out:** none as data — it produces a rendered map image/widget, not new intelligence.
- **Empty/negative result looks like:** a blank or default-centered map (you supplied no valid coordinates or no tiles loaded).

## Gotchas & OpSec
- Human-in-the-loop: none; it is code you run.
- OpSec: passive locally, but tile fetches reveal your area of interest to the tile provider. Self-host or proxy tiles for sensitive work.
- Largely abandoned; modern projects should prefer Leaflet or [[openlayers]].

## Overlaps ("do both")
- Pairs with [[openlayers]] — both are map display libraries; OpenLayers is actively maintained and far more capable.

## Trust & verifiability
`trust: community` — established open-source project, but stale and rarely the right choice today; included for completeness of the mapping-library shelf.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | modest-maps |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → (rendering only) |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | python-lib |
| opsec | passive |
| human-in-loop | no |
