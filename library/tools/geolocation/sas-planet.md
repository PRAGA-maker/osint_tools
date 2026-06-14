---
id: sas-planet
name: SAS Planet
description: Use when you need to download and cache high-res satellite/aerial imagery from many providers for offline geolocation work.
url: http://www.sasgis.org/sasplaneta/
category: geolocation
path:
- geolocation
bestFor: Windows app aggregating many satellite/map providers to view and download cached, offline-usable imagery.
selectorsIn: [geolocation, address]
selectorsOut: [geolocation, metadata]
status: live
pricing: free
opsec: passive
opsecNote: Runs locally and pulls tiles from public map providers; it queries providers, not your target, but provider requests go out over your IP.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: community
trustNote: Long-standing open Russian-origin GIS imagery tool (SASGIS); widely used in OSINT, free, but a Windows binary you should obtain from the official site.
missingPersonsRelevance: high
coverage: [global]
auth: none
api: false
localInstall: true
registration: false
aliases: [SAS.Planet, SASPlanet]
tags:
- geospatial-research-and-mapping-tools
source: awesome-osint
lastVerified: ''
enrichment: full
---

# SAS Planet

> A free Windows application that aggregates dozens of satellite, aerial and map providers into one viewer and lets you download imagery for offline use.

## When to use
You have a `geolocation` or `address` and want to compare imagery across many sources (Google, Bing, Yandex, Esri, historical layers) in one place, or you need to download/cache high-resolution tiles to analyze offline or load into `[[qgis]]`. Strong for missing-persons search planning over remote terrain and for finding the one provider whose imagery is clearest or most recent for an area.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download SAS.Planet from the official SASGIS site and run it on Windows.
2. Pick a map/imagery provider from the source list and navigate to your `geolocation`/`address`.
3. Compare layers, then select an area and download/stitch the tiles to disk (`geolocation` + `metadata` such as imagery date where available).
4. Pivot: load the saved imagery into `[[qgis]]` for measurement, or annotate findings in `[[scribblemaps]]`.

## Inputs → Outputs
- **In:** `geolocation`, `address` (area to view)
- **Out:** downloaded imagery tiles with `geolocation` and `metadata` (provider, zoom, sometimes capture date)
- **Empty/negative result looks like:** blank/grey tiles at high zoom — that provider lacks coverage there; switch providers.

## Gotchas & OpSec
- Human-in-the-loop: none; it is a GUI app.
- OpSec: passive toward the target — it queries public map providers, not the person. But those requests go out over your IP; use a VPN if provider-side logging is a concern.
- It is a third-party Windows binary that scrapes provider tiles; download only from the official site and be aware some providers' terms restrict bulk downloads.

## Overlaps ("do both")
- Pairs with `[[qgis]]` (analyze the imagery you download) and complements `[[sentinel-hub]]`/`[[satellites-pro]]` by aggregating many commercial providers in one interface.

## Trust & verifiability
`trust: community` — a long-established, widely used open imagery tool in the OSINT community; free and capable, but a downloadable binary, so obtain it from the official SASGIS source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sas-planet |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → geolocation, metadata |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | no |
