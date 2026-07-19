---
id: earth-engine-dataset
name: Earth Engine Data Catalog
description: Use when you have a `geolocation` and want historical/current satellite and geospatial data for it — returns 40+ years of imagery, terrain, land-cover and night-lights datasets.
url: https://developers.google.com/earth-engine/datasets/
category: geolocation
path:
- geolocation
bestFor: Accessing decades of satellite imagery (Landsat, Sentinel, MODIS), elevation, land-cover, and night-lights data for a location, analysable at planetary scale.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
- metadata-exif
status: live
pricing: freemium
costNote: Free for non-commercial/research use via a Google account and Earth Engine sign-up; the raw catalog is browsable without login. Commercial use requires a paid plan.
opsec: passive
opsecNote: You query Google's imagery archive, not the target — nothing about your subject is exposed. The one attributable step is Earth Engine access via a Google account; use a research/sock-puppet Google account, not a personal one.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Google Earth Engine is a first-party, well-documented planetary-scale geospatial platform aggregating authoritative datasets (NASA/USGS Landsat, ESA Sentinel, etc.).
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
aliases:
- Google Earth Engine
- GEE Data Catalog
tags:
- satellite
- geospatial
- remote-sensing
- google
source: osint4all
lastVerified: '2026-07-19'
enrichment: full
---

# Earth Engine Data Catalog

> Google's planetary-scale archive of satellite and geospatial datasets — 40+ years of imagery plus terrain, land-cover, and night-lights — searchable and analysable for any location.

## When to use
You have a `geolocation` and need imagery or geospatial context over time: what a place looked like on a given date, how it changed across years, elevation/terrain, land cover, or night-time lights (a proxy for activity/habitation). In geolocation and missing-persons work this supports verifying that a scene matches a location on a specific date, spotting seasonal/temporal changes, and analysing remote areas where street-level imagery is absent.

## How to use it (`bestInteractionPattern`: web-manual)
1. Browse the catalog at https://developers.google.com/earth-engine/datasets/ (no login) to find a dataset — Landsat (since 1972), Sentinel, MODIS (daily since 1999), DEMs, land-cover, VIIRS night-lights.
2. Sign in to Earth Engine with a (sock-puppet) Google account for analysis via the Code Editor or Python API.
3. Load a dataset, filter by your area/coordinates and a date range, and visualise or export the imagery/values.
4. Compare across dates to detect change; read metadata (acquisition date, resolution, cloud cover) for each scene.
5. Pivot: a confirmed date/appearance corroborates a photo geolocation; feed derived coordinates into mapping/street-level tools.

## Inputs → Outputs
- **In:** `geolocation` (coordinates/area) + date range + chosen dataset
- **Out:** satellite/geospatial imagery and layers for that place/time, with scene `metadata-exif` (date, resolution, sensor)
- **Empty/negative result looks like:** no scenes for a date/area, or all cloud-obscured — a coverage/cloud gap, not evidence about the ground.

## Gotchas & OpSec
- There's a real learning curve — meaningful analysis uses the Code Editor / Python API, not just browsing.
- Resolution limits detail: free public imagery (10–30 m for Landsat/Sentinel) won't resolve a person or a car; it's landscape/context scale.
- Human-in-the-loop: Earth Engine access requires a Google account sign-up — use a research account.
- Commercial use is paid; keep usage research/non-commercial. OpSec: passive toward the target.

## Overlaps ("do both")
- Pairs with `[[bellingcat-openstreetmap-search]]` and `[[copernix]]` — Earth Engine supplies the imagery/temporal layer; those help identify and describe the specific place within it.

## Trust & verifiability
`trust: trusted` — a Google first-party platform aggregating authoritative government/agency datasets. Data provenance is strong; still confirm each scene's date and cloud-cover metadata before drawing time-specific conclusions.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | earth-engine-dataset |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation, metadata-exif |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
