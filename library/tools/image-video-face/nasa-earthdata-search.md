---
id: nasa-earthdata-search
name: NASA Earthdata Search
description: Use when you have a `geolocation` (bounding box) and a date range and want satellite/earth-observation imagery and data covering it — returns matching granules (imagery, thermal, land-cover) you can preview and download.
url: https://search.earthdata.nasa.gov/
category: image-video-face
path:
- image-video-face
bestFor: Finding dated satellite/aerial imagery and earth-observation data over a specific area and time window (scene reconstruction, environmental context, change over time).
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: All NASA Earthdata is free. Browsing and searching need no login; downloading most collections requires a free Earthdata Login (NASA URS) account.
opsec: passive
opsecNote: You search public satellite archives by area and date; nothing about your subject is revealed. Passive. Note downloads are tied to your Earthdata Login account, so use a research account, not a personal one you want kept separate.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by NASA's Earth Science Data and Information System (ESDIS); the authoritative first-party portal to NASA/USGS earth-observation archives.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
aliases:
- Earthdata Search
- search.earthdata.nasa.gov
tags:
- Maps, Geolocation and Transport
- Satellite/aerial imagery
- earth-observation
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
relatedTools:
- firms
- nasa-firms
- nasa-kids-club
- nasa-worldview
---

# NASA Earthdata Search

> NASA's first-party portal to thousands of satellite/earth-observation collections — search dated imagery and data over any bounding box.

## When to use
You have a `geolocation` (an area you can draw a box around or name) and a date/time window, and you want overhead imagery or earth-observation data for it: to reconstruct what a scene looked like on or near a date, spot change over time (flooding, burn scars, land use), or add environmental context to a wilderness or disaster case. This is the archive-search front end; for a quick "just show me the picture" browse, `[[nasa-worldview]]` is faster.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://search.earthdata.nasa.gov/.
2. Set the **spatial** filter — draw a bounding box/point over the area (or type a place) — and the **temporal** filter (start/end dates).
3. Browse matching collections (MODIS, VIIRS, Landsat, Sentinel-mirrored sets, etc.); refine by keyword or platform in the facet panel.
4. Open a collection to see individual granules, preview imagery, and check resolution and revisit time for your date.
5. To download, sign in with a free **Earthdata Login**; add granules to the download basket or pull via the listed access URLs/API.
6. Pivot: for near-real-time fire hotspots use `[[nasa-firms]]`; for a fast visual daily mosaic use `[[nasa-worldview]]`.

## Inputs → Outputs
- **In:** `geolocation` (bounding box/point) + date range
- **Out:** matching earth-observation granules — dated satellite imagery, thermal, land/atmosphere data over that `geolocation`
- **Empty/negative result looks like:** no granules for your box+date usually means the sensor didn't pass over then, cloud/quality filters excluded it, or the resolution is too coarse for a small area — widen the date window or the box before concluding there's no coverage.

## Gotchas & OpSec
- Human-in-the-loop: downloading requires an `account-login` (free Earthdata Login); searching/previewing does not.
- Revisit gaps and cloud cover mean the pass nearest your exact date may be days off and partly obscured — check the granule's cloud metadata.
- Resolution varies hugely by instrument (250 m–1 km MODIS/VIIRS vs ~30 m Landsat); most public NASA optical data will not resolve a person or vehicle — use it for terrain/environment, not identification.

## Overlaps ("do both")
- Pairs with `[[nasa-worldview]]` (fast daily visual browse) and `[[nasa-firms]]`/`[[firms]]` (thermal fire detections) — Earthdata Search is the deep archive with downloadable granules behind those quicker viewers.

## Trust & verifiability
`trust: trusted` — it is NASA ESDIS's own portal; the data provenance is authoritative. Verifiability caveat is technical: match the granule's acquisition time, resolution, and cloud flags to your question before drawing conclusions.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nasa-earthdata-search |
| category | image-video-face |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
