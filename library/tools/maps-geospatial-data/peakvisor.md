---
id: peakvisor
name: PeakVisor
description: Use when you have a photo showing mountains/terrain and a rough `geolocation` and want to identify peaks and confirm the vantage point — returns a refined `geolocation` via 3-D terrain matching.
url: https://peakvisor.com/
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Identifying mountain peaks and skyline/ridge lines in a photo to verify or narrow where it was taken.
selectorsIn:
- geolocation
- address
- image
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: Free web 3-D map and peak identification; a "PeakVisor PRO" subscription unlocks offline maps and advanced app features.
opsec: passive
opsecNote: You work against PeakVisor's terrain model and your own imagery, not the subject or their accounts — fully passive. No signal reaches anyone connected to the photo.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Well-regarded outdoor/terrain app used in the geolocation community (listed in Bellingcat's toolkit); peak data is crowd/DB-sourced and generally accurate for named summits.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- PeakVisor 3D map
tags:
- maps-geospatial-data
- geolocation
- terrain
- bellingcat-toolkit
source: bellingcat-toolkit
lastVerified: '2026-07-23'
enrichment: full
relatedTools:
- peakvisor-com
---

# PeakVisor

> A 3-D terrain and peak-identification tool — match the mountains in a photo against a rendered global elevation model to pin down where it was shot.

## When to use
You have an outdoor `image` with mountains, ridges, or a distinctive skyline and a rough `geolocation`/`address`, and you need to confirm or narrow the exact vantage point. PeakVisor names the visible summits and lets you rotate a 3-D panorama from any point, so you can align the real photo's skyline to the model — a core chronogeolocation move.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://peakvisor.com/ and navigate the 3-D map to your candidate area.
2. Position the virtual viewpoint and pan the horizon; PeakVisor labels each peak with name and elevation.
3. Compare the model's ridge line, peak spacing, and relative heights to the photo. Use the photo-fitting / panorama feature to line them up.
4. Iterate the viewpoint until the skyline matches, then read off the confirmed `geolocation`. Pivot into `[[google-earth]]`/mapping tools and sun-position checks to fix time of day.

## Inputs → Outputs
- **In:** `geolocation`/`address` (candidate area) + the reference `image`
- **Out:** confirmed/narrowed `geolocation` (viewpoint) plus named peaks
- **Empty/negative result looks like:** no skyline alignment anywhere in your candidate area — the photo is likely from a different region, or the horizon is too generic/obscured to match.

## Gotchas & OpSec
- Works only when identifiable terrain (peaks, ridges) is visible; flat or forested scenes give nothing.
- Peak naming/DB coverage is best for well-known ranges; remote areas may be sparse.
- Offline maps and some features are behind PRO; the web 3-D view is enough for skyline matching.

## Overlaps ("do both")
- Pairs with `[[peakvisor-com]]` and general 3-D mapping (`[[google-earth]]`) — cross-check the skyline match against satellite/terrain from a second engine before you commit to a location.

## Trust & verifiability
`trust: community` — a mature terrain app cited in Bellingcat's toolkit; peak identifications are reliable for named summits, but always corroborate a geolocation with a second source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | peakvisor |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation, address, image → geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
