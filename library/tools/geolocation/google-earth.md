---
id: google-earth
name: Google Earth
description: Use when you have a location and want 3D terrain, global high-res imagery, and measurement to study a site or last-known area.
url: https://earth.google.com/web/
category: geolocation
path:
- geolocation
bestFor: 3D global imagery and terrain exploration with measurement and place-marking for site study.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
- image
status: live
pricing: free
costNote: Free in-browser; no account needed for basic use.
opsec: passive
opsecNote: Renders Google's imagery in your browser; no contact with the target. Google sees your queries/IP.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Google's flagship 3D earth viewer; authoritative consumer imagery, though historical-imagery depth is better in the desktop Pro version.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Google Earth Web
tags:
- geospatial-research-and-mapping-tools
source: arf-seed
lastVerified: ''
enrichment: full
---

# Google Earth

> Google's in-browser 3D earth viewer — global high-resolution imagery, 3D terrain and buildings, measurement, and place-marking, no install required.

## When to use
You have a `geolocation`/`address` and want to study the surrounding area in 3D: terrain and elevation around a trail or last-known point, building layout, line-of-sight, distances, and visual landmarks to match against a photo. The 3D view answers spatial questions (slopes, what's visible from where) that flat maps cannot.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://earth.google.com/web/.
2. Search a place or coordinates; tilt/rotate to explore in 3D.
3. Use the measure tool for distances/areas, drop placemarks, and import/export KML.
4. For a historical-imagery timeline and richer printing, use `[[google-earth-pro]]` (desktop).
5. Pivot: confirm ground-level detail in `[[google-maps]]` Street View; pull dated archival scenes from `[[earthexplorer]]`.

## Inputs → Outputs
- **In:** `geolocation` or `address`.
- **Out:** 3D `image`/terrain views, measured distances, placemarks at a `geolocation`.
- **Empty/negative result looks like:** imagery is dated or low-res in remote areas, and 3D buildings may be absent outside major cities.

## Gotchas & OpSec
- Human-in-the-loop: none; no login for basic use.
- Web version has a limited historical-imagery slider compared to the desktop Pro client.
- OpSec: passive; Google sees your activity but the target is not contacted.

## Overlaps ("do both")
- Pairs with `[[google-earth-pro]]` (deeper history, desktop) and `[[google-maps]]` (Street View) — same data family, different depth.

## Trust & verifiability
`trust: trusted` — Google's authoritative imagery; the main caveat is imagery date/resolution varying by location.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-earth |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → geolocation, image |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
