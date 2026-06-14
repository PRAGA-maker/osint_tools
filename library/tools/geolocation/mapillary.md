---
id: mapillary
name: Mapillary
description: Use when you need crowd-sourced street-level imagery to verify or geolocate a place from a photo — returns dated ground-level views for a geolocation.
url: https://www.mapillary.com/app/
category: geolocation
path:
- geolocation
bestFor: Crowd-sourced street-level imagery to ground-truth a location, identify a scene, or fill gaps where Google Street View has no coverage.
selectorsIn:
- geolocation
- image
selectorsOut:
- geolocation
- image
- metadata-exif
status: live
pricing: free
costNote: Free to browse; Meta-owned. An account/API key is only needed for the API or contributing imagery.
opsec: passive
opsecNote: Browsing public street imagery; no contact with the target. Be aware Mapillary is Meta-owned, so your browsing is to a major platform.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: trusted
trustNote: Large, established street-level imagery platform (Meta-owned); imagery is real and timestamped, though coverage and recency vary by area.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases: []
tags:
- geospatial-research-and-mapping-tools
- street-level-imagery
- geolocation
source: awesome-osint
lastVerified: ''
enrichment: full
---

# Mapillary

> Crowd-sourced street-level imagery (Meta-owned) — best for ground-truthing a location from a photo or covering streets Google Street View misses.

## When to use
This is a core geolocation tool. Use it when you have an `image` of an unknown place and need to match its ground-level features (signage, storefronts, road furniture, terrain) to a real `geolocation`, or when you have a `geolocation` and want to see it from street level — especially in rural roads, smaller towns, or countries where Google Street View coverage is thin. Imagery is contributed by users and dashcams, so it reaches places official street view does not, and each capture is timestamped.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.mapillary.com/app/ and navigate to your area, or paste coordinates.
2. Green coverage lines show where street-level imagery exists; click a line to enter the photo viewer.
3. Step through captures; check the capture date (recency varies widely by location).
4. Compare distinctive features in your reference photo against the ground imagery to confirm or reject the location.
5. Pivot: a confirmed match yields a precise `geolocation` to feed satellite imagery (`[[landsatlook-viewer]]`), a map (`[[maphub]]`), or a ground canvass. For bulk work, use the Mapillary API.

## Inputs → Outputs
- **In:** `geolocation` (where to look) and/or `image` (a scene to match)
- **Out:** `geolocation` (confirmed location), `image` (street-level views), `metadata-exif` (capture date/position)
- **Empty/negative result looks like:** no green coverage lines in the area (no contributed imagery), or only old captures — the place may simply be uncovered; fall back to satellite/aerial.

## Gotchas & OpSec
- Coverage is patchy and uneven — absence of imagery is not evidence about the place.
- Imagery can be years old; always read the capture date before drawing conclusions.
- Mapillary is Meta-owned; browsing is to a major platform (passive toward the subject, but not anonymous from the vendor).
- Human-in-the-loop: matching a scene to a location is your visual judgment.

## Overlaps ("do both")
- Pairs with Google Street View (use both — coverage differs) and with `[[landsatlook-viewer]]` for the aerial view; Mapillary gives the eye-level confirmation those lack.

## Trust & verifiability
`trust: trusted` — a large, established imagery platform with real, timestamped, geotagged captures. Caveat: coverage and recency vary, and contributions are crowd-sourced, so confirm the capture date and cross-check the location.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mapillary |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, image → geolocation, image, metadata-exif |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
