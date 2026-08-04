---
id: utm-grid-zones
name: UTM Grid Zones
description: Use when you have a `geolocation` expressed in (or needing) UTM and want to understand the zone system — returns a world UTM-zone reference map to place/convert coordinates.
url: http://dmap.co.uk/utmworld.htm
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: A one-glance world map and explainer of UTM/UPS grid zones for reading and sanity-checking UTM coordinates during geolocation.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free static reference page (Alan Morton / dmap.co.uk); a downloadable PDF of the zone map is provided at no cost.
opsec: passive
opsecNote: A static reference document — you fetch a public web page and nothing about your subject leaves your machine. No target interaction whatsoever.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-standing cartography reference page (also cited in the Bellingcat toolkit); the UTM zone facts it states are standard and independently verifiable.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- UTM world grid
- Universal Transverse Mercator zones
tags:
- bellingcat-toolkit
- maps
source: bellingcat-toolkit
lastVerified: '2026-08-04'
enrichment: full
---

# UTM Grid Zones

> A world reference map and plain-language explainer of the Universal Transverse Mercator grid — the "which zone is this?" cheatsheet when a coordinate is written in UTM instead of lat/long.

## When to use
You have a `geolocation` given in UTM form (e.g. `33T 0500000 5000000`) or need to reason about UTM zones during geolocation. UTM splits the world into 60 longitudinal zones (1–60) and 20 latitude bands (C–X, 80°S to 84°N); this page shows that grid on a world map and explains the easting/northing convention, so you can identify the correct zone and sanity-check a conversion.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://dmap.co.uk/utmworld.htm (or download its PDF zone map).
2. Locate the zone number/band for your area of interest on the world grid.
3. Use the explainer to interpret the easting (metres from the 500,000 m central-meridian origin) and northing.
4. Pivot: once you know the zone, run the actual conversion in a coordinate-converter tool, then plot the resulting lat/long on a mapping tool.

## Inputs → Outputs
- **In:** `geolocation` in UTM (or an area you need the zone for)
- **Out:** the correct UTM `geolocation` zone/band context to interpret or convert the coordinate
- **Empty/negative result looks like:** N/A — it's a static reference, not a query engine; the failure mode is simply misreading the grid, so cross-check the zone against a converter.

## Gotchas & OpSec
- This is a **reference, not a converter** — it helps you understand and locate the zone; do the numeric lat/long conversion in a dedicated tool.
- Watch the two easy UTM mistakes: confusing latitude *band letters* with the N/S hemisphere flag, and forgetting the 500,000 m false-easting origin.

## Overlaps ("do both")
- Pairs with a coordinate-conversion tool and a base map — this explains the grid, the converter turns UTM into lat/long, and the map plots it.

## Trust & verifiability
`trust: community` — an individual's cartography page, but the UTM facts are standard and match authoritative sources (e.g. NGA/USGS definitions); the map is a convenience, not a novel dataset.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | utm-grid-zones |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
