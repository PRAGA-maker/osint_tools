---
id: openlayers
name: OpenLayers
description: Use when you are building a custom geospatial web app and need a powerful JS map library to display layers, imagery, and analysis results — not a person-lookup tool.
url: http://openlayers.org
category: geolocation
path:
- geolocation
bestFor: Building custom interactive web maps that overlay multiple data sources, imagery, and GeoJSON for investigative dashboards.
selectorsIn:
- geolocation
selectorsOut: []
status: live
pricing: free
costNote: Open-source (BSD-2). Free; you supply your own tile/imagery sources.
opsec: passive
opsecNote: Client-side display library. Whatever tile/imagery/API endpoints you configure will see your requests; choose providers you trust for sensitive AOIs.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: python-lib
trust: trusted
trustNote: Mature, actively maintained, widely deployed open-source mapping library (OSGeo project). Authoritative as a developer dependency.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
relatedTools:
- modest-maps
- openstreetmap
aliases:
- OL
tags:
- geospatial-research-and-mapping-tools
- mapping-library
source: awesome-osint
lastVerified: ''
enrichment: full
---

# OpenLayers

> A high-performance, open-source JavaScript library for building interactive web maps — the engine behind custom geo dashboards, not an investigative lookup.

## When to use
Reach for this only when you are *building* tooling: you want to overlay multiple layers (OSM, satellite, WMS/WMTS, your own GeoJSON of candidate `geolocation` points and search areas) in a custom web app. It renders and lets users interact with geodata; it does not itself find people or addresses. Low direct MP relevance, high value if you're standing up a geolocation workbench.

## How to use it (`bestInteractionPattern`: python-lib)
1. Add OpenLayers to your web project (npm or CDN); it's a JS library, used as a code dependency.
2. Define a `Map` with view (center/zoom) and add `TileLayer`s for basemaps/imagery plus `VectorLayer`s for your features.
3. Load investigative data as GeoJSON (candidate locations, AOIs, tower positions from [[opencellid]]) and style/interact with it.
4. Pivot: this is the display surface — feed it outputs from [[overpass-turbo]], geocoders, and imagery sources.

## Inputs → Outputs
- **In:** `geolocation` data (coordinates, GeoJSON, tile/imagery URLs) you provide in code.
- **Out:** none as intelligence — an interactive rendered map for analysis/presentation.
- **Empty/negative result looks like:** a blank/grey map (misconfigured projection, bad tile URL, or no features added).

## Gotchas & OpSec
- Requires JS/web-dev skill; steeper than drop-in tools. Mind coordinate projections (EPSG:3857 vs 4326).
- OpSec: passive locally; configured tile/imagery providers see your requests — self-host or proxy for sensitive work.

## Overlaps ("do both")
- Supersedes [[modest-maps]] (older, stale). Pairs naturally with [[openstreetmap]] as a basemap source.

## Trust & verifiability
`trust: trusted` — mature OSGeo project, openly auditable and widely used in production geospatial systems.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | openlayers |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → (rendering only) |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | python-lib |
| opsec | passive |
| human-in-loop | no |
