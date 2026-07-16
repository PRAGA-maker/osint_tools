---
id: apollomapping-image-hunter
name: ApolloMapping Image Hunter
description: Use when you have a `geolocation`/area and want to find archived satellite and aerial imagery of it over time — returns a catalog of available images with dates and previews.
url: https://imagehunter.apollomapping.com/
category: image-video-face
path:
- image-video-face
bestFor: Searching commercial satellite/aerial imagery archives for a chosen map area, browsing available captures by date (early 2000s to recent).
selectorsIn:
- geolocation
selectorsOut:
- image
- geolocation
status: live
pricing: freemium
costNote: Searching the archive and previewing available imagery (thumbnails, capture dates, metadata) is free; ordering full-resolution licensed imagery is paid via ApolloMapping.
opsec: passive
opsecNote: You draw an area on a map and browse an imagery catalog — nothing about a person is submitted and no one is notified. Passive. Ordering imagery requires an account/quote that identifies you; the free search does not.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by ApolloMapping, a commercial satellite-imagery reseller; the archive index (providers, dates) is authoritative for what imagery exists, even if buying it costs money.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Image Hunter
- ApolloMapping
tags:
- Maps, Geolocation and Transport
- Satellite/aerial imagery
source: cyb-detective
lastVerified: '2026-07-16'
enrichment: full
---

# ApolloMapping Image Hunter

> A search front-end over commercial satellite/aerial imagery archives — draw a polygon and see every capture available for that spot, with dates spanning the early 2000s to a few days ago.

## When to use
You have a `geolocation` (a coordinate, a bounded area of interest) and need historical or recent overhead imagery — to see what a location looked like on a specific date, detect a change over time (new structure, vehicle presence), or find higher-resolution imagery than free maps offer. Image Hunter tells you *what imagery exists* for the area and when.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open Image Hunter and navigate the map to your area of interest.
2. Use the square/polygon tool to select the exact area.
3. Set filters (date range, cloud cover, resolution, sensor) and search.
4. Browse the returned catalog: each entry shows the capture date, provider, resolution, and a preview footprint/thumbnail (`selectorsOut`: image, geolocation).
5. Decide whether to order a full-res scene (paid) or use the metadata to guide free-source cross-checking (Google Earth history, Sentinel/Landsat).
6. Pivot: a capture date pins a change to a time window; the footprint confirms coverage before you commit to a purchase.

## Inputs → Outputs
- **In:** a `geolocation` / drawn area + date/quality filters
- **Out:** catalog of available `image`s (satellite/aerial) with dates, providers, and footprints over the `geolocation`
- **Empty/negative result looks like:** no scenes for the area/date/cloud filters — loosen the date range or cloud-cover limit; some remote areas simply have sparse commercial coverage.

## Gotchas & OpSec
- It's a *discovery/ordering* tool — full-resolution imagery is a paid purchase; the free tier tells you what's available and previews it.
- Previews are footprints/low-res; don't treat a thumbnail as analysis-grade.
- For free imagery, use the dates found here to hunt the same captures in Google Earth Pro history, Sentinel Hub, or USGS EarthExplorer.
- OpSec: passive browsing; ordering identifies you.

## Overlaps ("do both")
- Pairs with free imagery sources (Google Earth Pro historical, Sentinel Hub, USGS EarthExplorer) — Image Hunter finds *when* good imagery exists; the free archives may let you view a comparable capture without paying.

## Trust & verifiability
`trust: trusted` — authoritative commercial imagery index from ApolloMapping; the catalog reliably reflects available captures, though the imagery itself is licensed/paid.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | apollomapping-image-hunter |
| category | image-video-face |
| selectorsIn → selectorsOut | geolocation → image, geolocation |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
