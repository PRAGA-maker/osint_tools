---
id: fao-map-catalog
name: FAO Map Catalog
description: Use when you have a `geolocation` or region and want authoritative land-cover, agricultural, water and terrain layers for it — returns geospatial map data.
url: https://data.apps.fao.org/map/catalog/srv/eng/catalog.search#/home
category: geolocation
path:
- geolocation
bestFor: Pulling free UN/FAO geospatial layers (land cover, agro-ecology, water, soils) to characterise a rural or remote area.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free and open under FAO's open-data policy; most layers downloadable with attribution, no account required to search or preview.
opsec: passive
opsecNote: Read-only browsing of a public UN GeoNetwork catalogue. Queries hit FAO servers only; nothing about your target is submitted. No sock puppet needed, though route through a clean session if you prefer not to associate your IP with a specific area of interest.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the UN Food and Agriculture Organization on its official GeoNetwork instance; metadata is ISO-standard and datasets are institutionally sourced.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- FAO GeoNetwork
- FAO Agro-Informatic Data Catalog
tags:
- maps
- geospatial
- environmental
source: osint4all
lastVerified: '2026-07-18'
enrichment: full
---

# FAO Map Catalog

> The UN FAO's GeoNetwork catalogue — one of the largest free repositories of thematic geospatial layers (land cover, agro-ecology, water, forests, soils) for characterising a place.

## When to use
You have a `geolocation` or an `address`/region — typically rural, agricultural, or remote — and want to understand the physical and environmental context: what the land cover is, whether it is cropland or forest, water and terrain features, agro-ecological zoning. Useful when a subject was last known near a specific rural area and you need base-layer geography that consumer map apps don't expose, or to corroborate imagery/terrain claims.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the catalogue at https://data.apps.fao.org/map/catalog/srv/eng/catalog.search#/home.
2. Search by keyword (e.g. "land cover", "GAEZ", "AQUASTAT") and/or draw/enter a spatial extent to filter datasets to your area of interest.
3. Open a dataset record to read its ISO metadata, preview the layer on the map, or download it (Shapefile, GeoTIFF, CSV) / consume it via WMS/WFS.
4. Pivot: overlay the layer in QGIS or another GIS against imagery and coordinates from `[[google-maps-scraper]]` or terrain tools to build a physical picture of the location.

## Inputs → Outputs
- **In:** `geolocation` / `address` (region or bounding area)
- **Out:** `geolocation` (map layers, land-cover/agro/water/soil data for the area)
- **Empty/negative result looks like:** a keyword or extent with no matching datasets returns an empty result list — it means FAO has no thematic layer for that query, not that the area is undocumented elsewhere.

## Gotchas & OpSec
- The catalogue is a hash-route single-page app; deep links can be slow to load and some automated fetchers get a 502 — open it in a real browser.
- Coverage is thematic (agriculture, food security, environment), not street-level; do not expect building footprints or addresses.
- OpSec: fully passive — you query FAO about a place, never about a person.

## Overlaps ("do both")
- Pairs with `[[google-maps-scraper]]` and other imagery tools — FAO supplies authoritative land-cover/terrain context while satellite/street imagery supplies the visual detail.

## Trust & verifiability
`trust: trusted` — first-party UN FAO catalogue with ISO-standard metadata; datasets are institutionally sourced and citable.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | fao-map-catalog |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
