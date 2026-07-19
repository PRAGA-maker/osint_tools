---
id: sentinel-hub-eo-browser
name: Sentinel Hub EO Browser
description: Use when you have a `geolocation`/coordinates and want dated satellite imagery of that spot — returns time-stamped multispectral imagery for verification and change-detection.
url: https://apps.sentinel-hub.com/eo-browser/
category: image-video-face
path:
- image-video-face
bestFor: Pulling dated, multispectral satellite imagery (Sentinel/Landsat/MODIS) for a coordinate to verify a location or detect change over time.
selectorsIn:
- geolocation
- image
selectorsOut:
- geolocation
- metadata-exif
status: live
pricing: freemium
costNote: Free browsing/visualization of the full public archive; a free account unlocks time-lapse, custom scripts and downloads. Paid Sentinel Hub plans are for API/commercial use, not needed for manual imagery review.
opsec: passive
opsecNote: You query an imagery archive, never the subject or the location's owner — fully passive. A free account ties usage to an email; use a sock-puppet email if you want zero attribution.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Sinergise/Planet over official ESA Copernicus and USGS Landsat archives; the imagery is authoritative satellite data with reliable acquisition dates.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- sentinel-hub
- sentinel-hub-playground
aliases:
- EO Browser
- Sentinel Hub EO Browser
tags:
- Maps, Geolocation and Transport
- Satellite/aerial imagery
- geolocation
- change-detection
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# Sentinel Hub EO Browser

> A free web viewer over the Copernicus (Sentinel) and Landsat satellite archives — pick a coordinate and a date range to pull time-stamped, multispectral imagery for location verification and change-detection.

## When to use
You have a `geolocation` (coordinates, or a place you can pin on the map) and want to *see* it from space on a specific date — to corroborate a claimed location, spot when a structure appeared/disappeared, check environmental context (flooding, fire scars, construction), or build a before/after timeline. Unlike a single static basemap, EO Browser lets you scrub through years of dated acquisitions, which is what makes it useful for verification.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://apps.sentinel-hub.com/eo-browser/ (sign in with a free Copernicus/Sentinel Hub account to enable time-lapse and downloads).
2. Navigate/search to the location, or paste coordinates.
3. Pick a data source (Sentinel-2 for 10 m optical, Sentinel-1 for radar/cloud-penetrating, Landsat for deep history) and a date; browse the available acquisitions on that spot.
4. Switch visualizations (True Color, NDVI, false-color) to bring out water, vegetation, burn scars, or bare ground; use the time-lapse to see change.
5. Download/screenshot the dated frame for your report.
6. Pivot: confirmed imagery + acquisition date feeds a timeline; anomalies feed higher-resolution commercial imagery or ground photos.

## Inputs → Outputs
- **In:** `geolocation`/coordinates (and a target date range); optionally an `image` you're trying to geolocate/verify
- **Out:** dated multispectral satellite frames with acquisition `metadata-exif` (sensor, date, cloud cover) confirming what a `geolocation` looked like when
- **Empty/negative result looks like:** no cloud-free scene in your window, or resolution too coarse to resolve the feature (Sentinel-2 is ~10 m — cars/people aren't visible) — absence of detail is a resolution limit, not proof nothing is there.

## Gotchas & OpSec
- Resolution: ~10 m (Sentinel-2) means you see buildings, fields, roads — not individuals or plates; use for context, not fine detail.
- Cloud cover and revisit gaps limit which dates are usable; radar (Sentinel-1) sees through clouds.
- Human-in-the-loop: a free login is needed for time-lapse/downloads.
- OpSec: passive; nothing reaches the location's owner.

## Overlaps ("do both")
- Pairs with `[[sentinel-hub-playground]]` (quick single-scene view) and higher-resolution basemaps (Google/Bing/Yandex satellite) — use EO Browser for *dated* multispectral history, commercial basemaps for sharper single snapshots.

## Trust & verifiability
`trust: trusted` — authoritative ESA/USGS satellite archives with reliable timestamps; every frame is a citable, re-retrievable acquisition, making it strong verification evidence.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sentinel-hub-eo-browser |
| category | image-video-face |
| selectorsIn → selectorsOut | geolocation, image → geolocation, metadata-exif |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
