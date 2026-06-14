---
id: current-location
name: Current Location
description: Use when you have coordinates or a place and want to see geotagged public photos taken nearby — returns geolocated images and their source links.
url: https://current-location.com/
category: image-video-face
path:
- image-video-face
- images
- search
bestFor: Discovering geotagged public photos near a location of interest.
input: Map location, coordinates, or browser geolocation
output: Geotagged image results with source context from supported platforms
selectorsIn:
- geolocation
- address
selectorsOut:
- image
- geolocation
status: live
pricing: free
costNote: Free web map.
opsec: passive
opsecNote: Queries publicly indexed geotagged photos; no direct interaction with uploaders. The site may request your browser geolocation — decline and enter coordinates manually to avoid leaking your own position.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Small location-based photo-map utility; coverage depends on whichever public photo source it indexes, so absence of results is not conclusive.
missingPersonsRelevance: high
coverage: [global]
auth: none
api: false
localInstall: false
registration: false
relatedTools: [creepy, deepfind-me-2]
aliases: []
tags:
- geolocation
- image-search
source: arf-seed
lastVerified: ''
enrichment: full
---

# Current Location

> A map-based tool that pulls public geotagged photos taken near a point you specify — useful for putting eyes on what a place actually looks like and who has been there.

## When to use
You have a `geolocation` (coordinates) or an `address`/landmark and want imagery of that exact area — to recognize a background from a missing person's last-known photo, to spot a vehicle or sign, or to build situational awareness of a search zone. Returns photos pinned to that area rather than searching by face or by uploaded image.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://current-location.com/.
2. Enter coordinates / pan the map to the area of interest (decline the browser geolocation prompt).
3. Browse the geotagged photos returned near that point; click through to source.
4. Pivot: match a background in a case photo to one of these images; corroborate with `[[deepfind-me-2]]` (satellite/street-view) and cross-reference movement clusters from `[[creepy]]`.

## Inputs → Outputs
- **In:** `geolocation` / `address`
- **Out:** `image`, `geolocation` (geotagged photos pinned near the point, with source links)
- **Empty/negative result looks like:** no pins in the area — either nobody geotagged photos there or the indexed source has thin coverage for that region, not proof the place is unremarkable.

## Gotchas & OpSec
- Coverage is uneven; rural/low-traffic areas return little. A blank map is inconclusive.
- Human-in-the-loop: none, but the page may ask for *your* location — deny it and type coordinates instead.
- OpSec: passive; you read public uploads and never contact uploaders.

## Overlaps ("do both")
- Pairs with `[[deepfind-me-2]]` for satellite/street-view confirmation of the same spot, and with `[[creepy]]` when you are working from a username's movement pattern toward a physical area.

## Trust & verifiability
`trust: unverified` — a small utility whose value depends entirely on its underlying photo index. Every returned image links to a source you can open and verify, but absence of results proves nothing.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | current-location |
| category | image-video-face |
| selectorsIn → selectorsOut | geolocation, address → image, geolocation |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
