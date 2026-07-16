---
id: pictimo
name: Pictimo
description: Use when you have a `geolocation`/place and want live public webcams there to observe or corroborate a scene — returns real-time imagery for a location.
url: https://www.pictimo.com
category: geolocation
path:
- geolocation
bestFor: Finding live public webcams by country/city/map to observe conditions at or near a location in real time.
selectorsIn:
- geolocation
- address
selectorsOut:
- image
- geolocation
status: live
pricing: free
costNote: Free worldwide live-webcam directory; no account or payment.
opsec: passive
opsecNote: You watch publicly published webcam streams — no interaction with any subject and nothing is logged against them. Cameras are third-party public feeds; corroborate a feed's stated location before trusting it, as labels can be wrong.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community/public webcam directory aggregating third-party streams; feed availability and location labels are user/operator supplied and not independently verified.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- pictimo.com
tags:
- cctv
- webcam
- geolocation
source: metaosint
lastVerified: '2026-07-16'
enrichment: full
---

# Pictimo

> A worldwide directory of live public webcams: browse by map, country, or city to pull up real-time imagery from a place.

## When to use
You have a `geolocation` or `address`/area of interest and want live eyes on it or its surroundings — to corroborate weather/conditions in a photo you're geolocating, watch a public place, or confirm that a scene matches a claimed location. Pictimo indexes public streaming cameras by location, so you can quickly find any that overlook or sit near your target area.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.pictimo.com.
2. Browse via the interactive map, or filter by country and city; you can also browse by category (beaches, monuments, streets, etc.).
3. Open a nearby webcam to view its live feed.
4. Cross-check the feed's stated location (landmarks, signage) against what you expect before relying on it.
5. Pivot: use the live imagery to corroborate a `geolocation` hypothesis, compare weather/lighting against a timestamped photo, or monitor a public location.

## Inputs → Outputs
- **In:** `geolocation` / `address` / area (browsed via map or place filters)
- **Out:** live webcam `image`/video feeds tied to a `geolocation`.
- **Empty/negative result looks like:** no cameras near the area, or a listed feed that's offline/moved — coverage is patchy and depends on who has published a public cam there.

## Gotchas & OpSec
- Coverage is uneven; many places (especially private or rural) have no public webcam at all.
- Feed location labels are operator/user supplied and can be wrong — verify with visible landmarks before trusting a "location."
- Streams go up and down; a listed camera may be dead or repositioned.
- It shows public scenes, not individuals — treat any person glimpsed as incidental, not a target you can track.

## Overlaps ("do both")
- Pairs with other webcam/CCTV directories (e.g. webcams.travel, Insecam-style indexes) and mapping tools — each indexes different cameras, and satellite/street-view fills gaps where no live cam exists.

## Trust & verifiability
`trust: community` — an aggregator of third-party public feeds; the live imagery is real but its labeling is unverified, so confirm a camera's location independently before basing conclusions on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pictimo |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → image, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
