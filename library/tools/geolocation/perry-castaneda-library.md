---
id: perry-castaneda-library
name: Perry Castaneda Library
description: Use when you have a place name or region and need historical/topographic/political reference maps to interpret a geolocation.
url: https://www.lib.utexas.edu/maps
category: geolocation
path:
- geolocation
bestFor: Free, downloadable reference map collection (UT Austin) for country, city, topographic and historical maps.
selectorsIn: [geolocation, address]
selectorsOut: [geolocation, metadata]
status: live
pricing: free
opsec: passive
opsecNote: Static public library archive; browsing leaks nothing about your target, only your own access to lib.utexas.edu.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Hosted by the University of Texas at Austin Libraries (PCL Map Collection), a long-standing, authoritative public archive.
missingPersonsRelevance: high
coverage: [global]
auth: none
api: false
localInstall: false
registration: false
aliases: [PCL Map Collection, UT Library Maps]
tags:
- geospatial-research-and-mapping-tools
source: awesome-osint
lastVerified: ''
enrichment: full
---

# Perry Castaneda Library

> The University of Texas Perry-Castañeda Library (PCL) Map Collection — a large, free archive of country, city, topographic, thematic and historical maps.

## When to use
You have a `geolocation` (place name, region, or rough `address`) and need an authoritative reference map to interpret terrain, administrative boundaries, road layout, or how an area looked historically. Useful when corroborating a missing-person sighting location, understanding remote/rural terrain for search planning, or sourcing maps for regions where modern web maps are sparse.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.lib.utexas.edu/maps and browse by region (continent/country) or use the site search.
2. Open the country/city/topographic map index for your area of interest.
3. Download the map image/PDF (`geolocation`/`metadata` context: scale, date, projection).
4. Pivot: cross-reference terrain against satellite imagery in `[[sentinel-hub]]` or annotate findings in `[[scribblemaps]]`.

## Inputs → Outputs
- **In:** `geolocation`, `address` (a place/region to look up)
- **Out:** reference map files plus `metadata` (map date, scale, source)
- **Empty/negative result looks like:** no map index entry for that country/region — the collection is broad but not exhaustive, especially for fine street-level coverage outside major cities.

## Gotchas & OpSec
- Human-in-the-loop: none; static downloads, no login or captcha.
- OpSec: fully passive. You only touch a public university server; the target is never contacted.
- Many maps are scanned historical documents — verify the date before treating them as current.

## Overlaps ("do both")
- Pairs with `[[sentinel-hub]]` and `[[sas-planet]]` because PCL gives authoritative cartographic/terrain context while those give current imagery.

## Trust & verifiability
`trust: trusted` — maintained by the UT Austin Libraries, a recognized authoritative archive widely cited in geography and OSINT.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | perry-castaneda-library |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → geolocation, metadata |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
