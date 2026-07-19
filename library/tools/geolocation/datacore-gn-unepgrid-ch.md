---
id: datacore-gn-unepgrid-ch
name: UNEP/GRID-Geneva Metadata Catalogue
description: Use when you have a `geolocation`/region and want authoritative environmental geospatial layers for it — returns UNEP GeoNetwork datasets (hydrology, land cover, boundaries).
url: https://datacore-gn.unepgrid.ch/
category: geolocation
path:
- geolocation
bestFor: Discovering and downloading UNEP/GRID-Geneva geospatial datasets — watersheds, surface water, land cover, international boundaries — for a region.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free, publicly accessible GeoNetwork metadata catalogue from UNEP/GRID-Geneva; no account to search or download most layers. (The root URL redirects into the /geonetwork/ catalogue.)
opsec: passive
opsecNote: You browse an environmental data catalogue, not a person — fully passive, nothing about your subject is exposed. Standard browsing hygiene is enough.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by UNEP/GRID-Geneva (a UNEP + Swiss FOEN + University of Geneva partnership) on open-source GeoNetwork; datasets are authoritative scientific/agency sources (e.g. HydroSHEDS).
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- GRID-Geneva GeoNetwork
- UNEP GRID Geneva catalogue
tags:
- geospatial
- environmental-data
- geonetwork
- unep
source: osint4all
lastVerified: '2026-07-19'
enrichment: full
---

# UNEP/GRID-Geneva Metadata Catalogue

> A GeoNetwork catalogue from UNEP/GRID-Geneva for finding and downloading authoritative environmental geospatial datasets — hydrology, land/surface water, land cover, and boundaries.

## When to use
You have a `geolocation` or region and need environmental/physical-geography layers to characterise it: watersheds and drainage (HydroSHEDS), surface-water extent, land cover, elevation, or international/administrative boundaries. In geolocation work this supplies terrain and hydrological context — useful for interpreting a remote scene, ruling areas in or out by physical features (rivers, water bodies), or understanding a landscape where street-level data doesn't exist.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://datacore-gn.unepgrid.ch/ — it takes you into the GeoNetwork catalogue (`/geonetwork/srv/eng/catalog.search`).
2. Search or browse by keyword/theme (hydrology, land cover, boundaries) or by area.
3. Open a dataset record to read its metadata: extent, resolution, source, date, and licence.
4. Access the data via the record's download/WMS links or the GeoNetwork API for use in GIS.
5. Pivot: load a layer over your area of interest in a GIS/mapping tool to combine physical features with imagery from `[[earth-engine-dataset]]`.

## Inputs → Outputs
- **In:** a theme/keyword or `geolocation`/region of interest
- **Out:** environmental geospatial dataset records + downloadable `geolocation` layers (hydrology, land cover, boundaries)
- **Empty/negative result looks like:** no matching dataset for a theme/area — the catalogue is environmental-science-scoped and global-to-regional in resolution; it won't hold local, street-level, or person-level data.

## Gotchas & OpSec
- Scientific/environmental scope only: this is terrain and environment data, not addresses, buildings, or people.
- Resolution is regional/global — good for landscape context, not fine detail.
- Working with the data effectively needs GIS software and some familiarity with geospatial formats/metadata.
- OpSec: fully passive catalogue browsing.

## Overlaps ("do both")
- Pairs with `[[earth-engine-dataset]]` — GRID-Geneva provides curated thematic vector/raster layers (e.g. hydrology, boundaries); Earth Engine provides the raw multi-temporal satellite imagery to overlay them on.

## Trust & verifiability
`trust: trusted` — a UNEP/university partnership publishing authoritative datasets with full metadata provenance. Reliable; still check each record's source, date, and resolution before using it for a specific location conclusion.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | datacore-gn-unepgrid-ch |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
