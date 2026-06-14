---
id: land-viewer
name: Land Viewer
description: Use when you have a `geolocation`/`address` and want recent and historical satellite imagery (multispectral, time-slider) to inspect a site or terrain change.
url: https://eos.com/landviewer
category: geolocation
path:
- geolocation
- coordinates
bestFor: Browsing recent and historical multispectral satellite imagery for a location.
selectorsIn:
- geolocation
- address
- image
selectorsOut:
- geolocation
- image
status: live
pricing: freemium
costNote: Free browsing of public satellite imagery (Sentinel/Landsat); high-res commercial scenes, analytics, and downloads require an EOS account/paid plan.
opsec: passive
opsecNote: You browse satellite imagery of a place; the target is never contacted. A free EOS account unlocks more features.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: EOS Data Analytics' LandViewer is an established web viewer over public (Sentinel/Landsat) and commercial satellite archives, widely used in remote-sensing/OSINT work.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
aliases:
- EOS LandViewer
tags:
- geolocation
- coordinates
source: metaosint
lastVerified: ''
enrichment: full
---

# Land Viewer

> EOS LandViewer — a web viewer over public (Sentinel/Landsat) and commercial satellite archives with a time slider and multispectral band tools.

## When to use
You have a `geolocation` or `address` (a rural parcel, a search zone, a site of interest) and want to inspect recent satellite imagery and step back through past captures to detect change — disturbed ground, a newly present/absent vehicle or structure, seasonal terrain. Strong for area scoping and change detection in places Street View and aerial archives don't reach.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open eos.com/landviewer and navigate/search to your `geolocation`/`address`.
2. Pick a satellite source and date; use the time slider to compare captures across days/months/years.
3. Switch band combinations (e.g., NDVI/false-color) to highlight vegetation or surface change.
4. Sign in for higher-res/commercial scenes and downloads; compare older eras in [[historic-aerials]].

## Inputs → Outputs
- **In:** `geolocation` / `address` (and optionally an `image`/scene to compare)
- **Out:** satellite `image` scenes over time and derived map context (`geolocation`)
- **Empty/negative result looks like:** only cloud-covered or low-resolution free scenes for a date — try another date/source or the paid high-res archive.

## Gotchas & OpSec
- Human-in-the-loop: a free account widens access; the best resolution and downloads are paywalled.
- Free imagery (Sentinel/Landsat) is ~10m resolution — good for terrain/large change, not for spotting a person or small object.
- OpSec: passive — satellite imagery only; the target is not contacted.

## Overlaps ("do both")
- Pairs with [[historic-aerials]] (older US aerial archive) and [[grassgis]] (quantitative terrain/imagery analysis). Use [[google-maps-update-alerts]] to monitor for refreshes.

## Trust & verifiability
`trust: community` — EOS LandViewer is a well-established remote-sensing viewer; verify the source satellite and capture date shown for any scene.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | land-viewer |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address, image → geolocation, image |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
