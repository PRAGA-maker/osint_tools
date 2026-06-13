---
id: arcgis
name: ArcGIS
description: Use when you need authoritative basemaps, imagery, demographic, boundary, or live-feed map layers to add geographic context to a location, address, or coordinate.
url: https://livingatlas.arcgis.com/en/browse/
category: geolocation
path:
- geolocation
bestFor: Browsing Esri's curated Living Atlas of geospatial layers (imagery, basemaps, boundaries, demographics, live feeds) for location context.
selectorsIn: [geolocation, address]
selectorsOut: [geolocation, address]
status: live
pricing: freemium
costNote: Browsing the Living Atlas and viewing many layers is free; some premium/subscriber content and building/saving your own maps in ArcGIS Online require an Esri account (free public account or paid org).
opsec: passive
opsecNote: You browse Esri-hosted reference map layers; no contact with the target. Saving maps to an ArcGIS Online account ties activity to that account.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Living Atlas is curated and published by Esri, the dominant commercial GIS vendor, drawing on authoritative sources (USGS, census agencies, NOAA, etc.); content quality is high though some layers are third-party contributed.
missingPersonsRelevance: medium
coverage: [global]
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: [bing-maps, atlas, cartodb]
aliases: [arcgis-living-atlas, living-atlas]
tags: [gis, basemap, imagery, esri]
source: awesome-osint
lastVerified: '2026-06-13'
enrichment: full
---

# ArcGIS

> Esri's ArcGIS Living Atlas — a free-to-browse catalogue of authoritative geospatial layers (imagery, basemaps, boundaries, demographics, terrain, and live feeds) you can overlay to contextualise any location.

## When to use
You have a `geolocation` or `address` and need reference geography around it: high-resolution imagery, administrative/`address` boundaries, terrain and land cover, demographics, or live feeds (weather, wildfire, traffic). In missing-persons work this helps you read a search area — terrain that constrains travel, jurisdiction boundaries, population density, or current conditions overlaid on the place a person was last seen.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://livingatlas.arcgis.com/en/browse/.
2. Browse or search by category (Imagery, Basemaps, Boundaries/Places, Demographics, Landscape, Transportation, Live Feeds) and filter by region.
3. Open a layer to preview it on the map; pan/zoom to your `geolocation` of interest.
4. For analysis, open the layer in Map Viewer (ArcGIS Online) — a free Esri public account lets you combine layers and save a map; some premium layers prompt for a subscriber org.
5. Pivot: use the boundary/demographic context to scope where to search, then take coordinates to `[[bing-maps]]` for imagery or to a mapping tool like `[[cartodb]]`/`[[atlas]]` to plot your own case data.

## Inputs -> Outputs
- **In:** `geolocation`, `address` (the place you want context for)
- **Out:** `geolocation`, `address` (boundaries, place labels, contextual layers)
- **Empty/negative result looks like:** a sparse/blank layer over your area (data simply not collected there, common for very rural or non-US regions in some thematic layers).

## Gotchas & OpSec
- This is reference geography, not a people-search tool — it returns places and context, never personal records.
- "Living Atlas" mixes Esri-authoritative layers with community-contributed ones; check the layer's source/metadata before trusting it for precision work.
- Some premium/subscriber layers and any saving/analysis require an Esri account (free public or paid org); plain browsing does not.

## Overlaps ("do both")
- Pairs with `[[bing-maps]]` for current aerial imagery to complement Living Atlas thematic layers.
- Pairs with `[[cartodb]]` / `[[atlas]]` when you want to load your own case points onto authoritative basemaps.

## Trust & verifiability
`trust: trusted` — published by Esri, the leading GIS vendor, and sourced from authoritative providers. Still confirm each individual layer's provenance and date in its metadata, since community-contributed layers also appear.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | arcgis |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → geolocation, address |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
