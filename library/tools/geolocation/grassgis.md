---
id: grassgis
name: GrassGIS
description: Use when you need heavy-duty desktop GIS analysis of raster/vector `geolocation` data — terrain, viewshed, imagery — beyond what a web map offers.
url: http://grass.osgeo.org
category: geolocation
path:
- geolocation
bestFor: Advanced desktop geospatial analysis (terrain, raster, imagery) of location data.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free and open source (GPL); no account.
opsec: passive
opsecNote: Runs entirely on your local machine against data you supply, so nothing reaches the target or a third party.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: trusted
trustNote: GRASS GIS is a mature OSGeo project with decades of development and a large scientific user base.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- land-viewer
- historic-aerials
aliases:
- GRASS GIS
tags:
- geospatial-research-and-mapping-tools
source: awesome-osint
lastVerified: ''
enrichment: full
---

# GrassGIS

> GRASS GIS — a free, open-source desktop geographic information system for serious raster, vector, and imagery analysis of geospatial data.

## When to use
You have `geolocation` data (terrain models, satellite/aerial rasters, vector boundaries) and need real GIS analysis — viewshed/line-of-sight, slope and terrain modeling, distance/cost surfaces, image classification — that a consumer web map can't do. In a missing-persons context this supports search-area modeling (where could someone travel/be seen from a point) rather than directly finding a person, hence medium relevance.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download and install GRASS GIS from osgeo.org for your OS.
2. Create a Location/Mapset in the correct projection and import your raster/vector `geolocation` data.
3. Run analysis modules (e.g., `r.viewshed`, `r.slope.aspect`, `r.cost`) via the GUI or command console.
4. Export results (GeoTIFF/shapefile) and overlay them in a viewer like [[land-viewer]] or annotate in a case map.

## Inputs → Outputs
- **In:** `geolocation` raster/vector datasets (DEMs, imagery, boundaries)
- **Out:** derived `geolocation` analysis layers (viewsheds, terrain surfaces, classified imagery)
- **Empty/negative result looks like:** import/projection errors or empty output rasters — almost always a coordinate-system mismatch, not "no data."

## Gotchas & OpSec
- Steep learning curve; expects you to bring your own geospatial datasets.
- OpSec: passive and fully local — no network calls to the target or third parties.

## Overlaps ("do both")
- Pairs with [[land-viewer]] and [[historic-aerials]] — use those to source imagery, then bring it into GRASS for quantitative terrain/visibility analysis.

## Trust & verifiability
`trust: trusted` — GRASS GIS is a flagship OSGeo open-source project with decades of peer-reviewed scientific use.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | grassgis |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | no |
