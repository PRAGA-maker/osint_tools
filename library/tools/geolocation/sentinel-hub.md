---
id: sentinel-hub
name: Sentinel Hub
description: Use when you need dated, recent satellite imagery of an area to detect change over time or confirm current ground conditions.
url: https://www.sentinel-hub.com/explore/sentinelplayground/
category: geolocation
path:
- geolocation
bestFor: Browser viewer for dated Sentinel/Landsat satellite imagery with band combinations and time-slider change detection.
selectorsIn: [geolocation, address]
selectorsOut: [geolocation, metadata]
status: live
pricing: freemium
costNote: Sentinel Playground viewer is free; programmatic Sentinel Hub API access and high-volume use are paid.
opsec: passive
opsecNote: Public imagery viewer; you only reveal your own access to the site, never the target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Run by Sinergise (Planet); serves official ESA Copernicus Sentinel and USGS Landsat data — authoritative, dated imagery.
missingPersonsRelevance: high
coverage: [global]
auth: none
api: true
localInstall: false
registration: false
aliases: [Sentinel Playground]
tags:
- geospatial-research-and-mapping-tools
source: awesome-osint
lastVerified: ''
enrichment: full
---

# Sentinel Hub

> A browser viewer (Sentinel Playground) for official, dated ESA Sentinel and USGS Landsat satellite imagery, with band combinations and a time slider for change detection.

## When to use
You have a `geolocation` or `address` and need imagery with a known capture date, or want to compare an area across time — e.g. confirming current ground conditions for a search, spotting changes (new structures, vehicles, vegetation, flooding) near a last-known location, or selecting imagery from the day of a disappearance. The dated, time-sliced imagery is the key differentiator versus undated consumer viewers.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.sentinel-hub.com/explore/sentinelplayground/ and navigate to your `geolocation`/`address`.
2. Pick a satellite (Sentinel-2, Landsat) and a date from the calendar; cloud-filter as needed.
3. Choose a band combination (true color, NDVI, false color) to surface different features.
4. Read the imagery with its capture-date `metadata`. Pivot: download/stitch multi-provider imagery in `[[sas-planet]]`, analyze in `[[qgis]]`, or commission higher-res scenes via `[[skyfi-com-satellite-open-data]]`.

## Inputs → Outputs
- **In:** `geolocation`, `address` (area of interest)
- **Out:** dated satellite imagery (`geolocation` + capture-date `metadata`) and band views
- **Empty/negative result looks like:** cloudy/empty scene for a date — pick another pass; Sentinel-2 resolution (~10 m) cannot resolve people or small objects.

## Gotchas & OpSec
- Human-in-the-loop: none for the free viewer; the API requires an account/key.
- OpSec: fully passive; you only touch the imagery service, never the target.
- Resolution limit: Sentinel ~10 m, Landsat ~15-30 m — good for landscape/change, not for identifying individuals or vehicles. For finer detail go to commercial sources.

## Overlaps ("do both")
- Pairs with `[[skyfi-com-satellite-open-data]]` (higher-res commercial scenes), `[[sas-planet]]` (multi-provider downloads) and `[[qgis]]` (analysis). Use Sentinel Hub for the authoritative dated layer.

## Trust & verifiability
`trust: trusted` — operated by Sinergise (Planet) and serving official ESA Copernicus and USGS data; imagery is authoritative and timestamped.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sentinel-hub |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → geolocation, metadata |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
