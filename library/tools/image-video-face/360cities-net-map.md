---
id: 360cities-net-map
name: 360Cities Map
description: Use when you have a `geolocation` and want ground-level imagery — returns a world map of geolocated 360° panoramic photos to verify or compare a location.
url: https://360cities.net/map
category: image-video-face
path:
- image-video-face
bestFor: Browsing geolocated 360° panoramas as a Street View alternative for location verification.
selectorsIn:
- geolocation
selectorsOut:
- image
- geolocation
status: live
pricing: freemium
costNote: Free to browse and view panoramas on the map; licensing/downloading high-res imagery is paid, but viewing for OSINT is free.
opsec: passive
opsecNote: Passive map/imagery browsing hosted by 360Cities; you view locations, not people, so nothing subject-specific is disclosed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Contributor-uploaded panoramas with stated geolocations; coverage is uneven and a photo's placement/date depends on the uploader.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- 360cities.net
- 360Cities panoramas
tags:
- Maps, Geolocation and Transport
- Street View
- panorama
source: cyb-detective
lastVerified: '2026-07-22'
enrichment: full
---

# 360Cities Map

> A world map of user-contributed 360° panoramas — a Street View alternative that often has ground-level imagery where Google's coverage is thin, useful for verifying or matching a location.

## When to use
You have a `geolocation` (from a photo background, a check-in, or a witness) and need ground-level imagery to confirm or compare it — especially in places Google Street View doesn't cover (interiors, pedestrian areas, some countries). 360Cities hosts immersive panoramas pinned to coordinates, so you can compare landmarks, signage, and scenery against a subject's photo to corroborate where it was taken (chronogeolocation/geolocation verification).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://360cities.net/map and navigate to the area of interest.
2. Open nearby panorama pins and look around (360°) for landmarks, signage, terrain, and building details.
3. Compare those features against the image you are trying to place; note matches/mismatches and the panorama's stated location/date.
4. Use it to confirm or exclude a candidate location, or to gather visual context for an area.
5. Pivot: a confirmed `geolocation` narrows searches on local records/news; matched landmarks feed further mapping and imagery tools.

## Inputs → Outputs
- **In:** `geolocation` / a location to verify
- **Out:** geolocated 360° `image` panoramas and their `geolocation`
- **Empty/negative result looks like:** no panoramas near your area — coverage is contributor-driven and patchy, so many places have none. Absence means no one uploaded here, not that the location is wrong; fall back to Street View / Mapillary.

## Gotchas & OpSec
- Coverage is uneven and often dated; a panorama's placement and timestamp depend on the uploader, so verify before relying on it.
- It shows places, not people — use it purely for location verification and context.

## Overlaps ("do both")
- Pairs with Google Street View, Mapillary, and KartaView — run several, since each has imagery the others lack; 360Cities frequently fills gaps in immersive, pedestrian, or non-US coverage.

## Trust & verifiability
`trust: community` — contributor-uploaded imagery with self-stated geolocations; genuine but uneven, so treat a panorama as corroboration to cross-check, not proof on its own.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | 360cities-net-map |
| category | image-video-face |
| selectorsIn → selectorsOut | geolocation → image, geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
