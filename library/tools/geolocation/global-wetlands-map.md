---
id: global-wetlands-map
name: Global Wetlands Map
description: Use when you have a `geolocation` or an outdoor `image` of watery terrain and want to test whether a spot is wetland/peatland — returns wetland classification by location.
url: https://www2.cifor.org/global-wetlands/
category: geolocation
path:
- geolocation
bestFor: Checking whether a candidate location is mapped as wetland/peatland to corroborate or challenge terrain in imagery.
selectorsIn:
- geolocation
- image
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: Free to view and download the wetland datasets; registration only needed to contribute/verify data.
opsec: passive
opsecNote: Consulting a public research map discloses nothing about your subject — you are reading environmental data. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Produced by CIFOR-ICRAF's SWAMP program (with the US Forest Service, USAID) from MODIS satellite imagery; authoritative scientific data, coarse resolution.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- CIFOR Global Wetlands Map
- Global Wetlands V3
tags:
- Maps, Geolocation and Transport
- Nature
- wetlands
source: cyb-detective
lastVerified: '2026-07-21'
enrichment: full
---

# Global Wetlands Map

> CIFOR-ICRAF's satellite-derived map of the world's wetlands, peatlands and their carbon stocks — a terrain-classification layer for corroborating watery-landscape imagery.

## When to use
You have a candidate `geolocation`, or an outdoor `image` showing swamp, marsh, mangrove, floodplain or open water, and you want to test whether that spot is actually mapped as wetland/peatland. It helps confirm or challenge a terrain claim ("this photo is in a mangrove swamp") and narrow where an outdoor scene could plausibly be. It classifies land, not people.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www2.cifor.org/global-wetlands/.
2. Navigate/zoom to your candidate location.
3. Read the wetland classification at that point (open water, mangrove, swamp, fen, floodplain, etc.) and its extent.
4. Compare against your `image`'s vegetation/water features for consistency.
5. Pivot: a confirmed wetland type narrows plausible locations; feed the refined `geolocation` to satellite/street-level tools for tighter fixing.

## Inputs → Outputs
- **In:** a candidate `geolocation` and/or an outdoor `image` of watery terrain
- **Out:** wetland/peatland classification at that `geolocation`
- **Empty/negative result looks like:** the location isn't classified as wetland (or falls in an uncovered region — coverage is tropical/subtropical-focused and not every country is included); absence isn't proof, given coarse resolution.

## Gotchas & OpSec
- Coverage gaps: the maintainers note "not all countries" are included and the focus is tropical/subtropical wetlands.
- Coarse resolution (MODIS-derived) — good for landscape-scale classification, not parcel-level precision. Don't over-read small features.
- Terrain-only: no people, structures, or activity data.
- OpSec: fully passive.

## Overlaps ("do both")
- Pairs with satellite imagery and other nature/terrain layers — this classifies wetland type, while imagery gives the actual scene to match against.

## Trust & verifiability
`trust: trusted` — a peer-reviewed scientific product from CIFOR-ICRAF's SWAMP program; reliable at landscape scale, with accuracy bounded by satellite resolution and regional coverage.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | global-wetlands-map |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, image → geolocation |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
