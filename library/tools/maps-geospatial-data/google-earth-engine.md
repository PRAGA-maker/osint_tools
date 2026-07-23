---
id: google-earth-engine
name: Google Earth Engine
description: Use when you have a `geolocation`/area and want to analyze satellite imagery over time — returns processed multi-source imagery, indices, and change detection.
url: https://code.earthengine.google.com/
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Planetary-scale analysis of decades of satellite imagery (Landsat, Sentinel) for change detection, dating events, and land-cover analysis.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: Free for research, education, and non-commercial use (requires signing up and being approved for a free Earth Engine account); commercial use is paid. The Code Editor and Python/JS APIs are the free access points.
opsec: passive
opsecNote: You analyze archived satellite imagery on Google's servers — nothing touches the ground location or any subject. Your scripts/account are visible to Google; use a research account if attribution matters.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Google's established geospatial-analysis platform, drawing on authoritative public imagery archives (USGS/ESA); widely used by researchers and Bellingcat-listed.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
relatedTools: []
aliases:
- GEE
- Earth Engine
- code.earthengine.google.com
tags:
- satellite-imagery
- change-detection
- remote-sensing
- bellingcat-toolkit
source: bellingcat-toolkit
lastVerified: '2026-07-23'
enrichment: full
---

# Google Earth Engine

> A cloud platform that puts decades of the world's satellite imagery behind a scripting console — for measuring change over an area of interest, not just looking at one photo.

## When to use
You have a `geolocation` or `address` (a coordinate, a site, a region) and need *temporal* satellite analysis: when did a building appear, when was a field cleared, how did a shoreline or fire scar change, what was the ground state on a given date? Earth Engine hosts the Landsat and Sentinel archives (and hundreds of datasets) and lets you compute over them at scale — far beyond eyeballing a single Google Earth image. Missing-persons relevance is low but real for geolocation/verification work (dating imagery, confirming ground features, change detection around a site).

## How to use it (`bestInteractionPattern`: web-manual)
1. Sign up for a free Earth Engine account (non-commercial/research) and open the Code Editor at https://code.earthengine.google.com/ (login required).
2. In the JavaScript Code Editor, define your area of interest (draw a geometry or import coordinates), pick an image collection (e.g. `COPERNICUS/S2` for Sentinel-2), and filter by date and cloud cover.
3. Compute: map imagery, calculate indices (NDVI for vegetation, NDWI for water), or difference two dates for change detection; display layers on the map.
4. Export results (GeoTIFF/CSV) to Drive/Cloud, or use the Python API for automated/repeatable analysis.
5. Pivot: a dated change confirms or refutes a timeline; extracted coordinates feed other geo tools and imagery comparisons.

## Inputs → Outputs
- **In:** `geolocation` / `address` (area of interest) + date range + dataset
- **Out:** processed imagery, spectral indices, change-detection maps, time-series values for the `geolocation`
- **Empty/negative result looks like:** empty/blank composites — usually persistent cloud cover, a date range with no passes, or a dataset that doesn't cover the area; widen the dates or switch collections before concluding "no change."

## Gotchas & OpSec
- **Steep learning curve** — it's a coding platform (JS/Python), not a point-and-click viewer; budget time or start from Earth Engine example scripts.
- Account approval is required (free for non-commercial); commercial use needs a paid plan.
- Imagery resolution is moderate (Sentinel-2 ~10 m, Landsat ~30 m) — good for landscape change, not license plates; pair with high-res sources for detail.
- OpSec: passive; only your Google account/scripts are exposed to Google.

## Overlaps ("do both")
- Complements ready-made imagery viewers (Google Earth Pro, Sentinel Hub, Planet) and `[[govmap]]`-style national portals — use Earth Engine for *analysis over time and scale*, the viewers for quick high-res looks at a single date.

## Trust & verifiability
`trust: trusted` — a mature Google platform built on authoritative USGS/ESA archives; results are reproducible from your own scripts, which is exactly what makes it defensible for verification work.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-earth-engine |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation, address → geolocation |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
