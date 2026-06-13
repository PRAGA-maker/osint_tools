---
id: bing-maps
name: Bing Maps
description: Use when you need a second mapping/imagery source — Microsoft aerial and 3D views, directions, and business search — to confirm a location or compare imagery against Google.
url: https://www.bing.com/maps
category: geolocation
path:
- geolocation
bestFor: Cross-checking a location with Microsoft's aerial/3D imagery, directions, and POI/business search as an independent map source.
selectorsIn: [address, geolocation, name]
selectorsOut: [address, geolocation, employer-org]
status: live
pricing: free
costNote: Free to use in the browser; the Bing Maps / Azure Maps developer APIs require an account and key for programmatic access.
opsec: passive
opsecNote: Browsing the map does not contact the target. Searches run against Microsoft; use a clean session and don't sign into a personal Microsoft account if you want to keep research unattributed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party Microsoft mapping service; map data now sourced from TomTom, OpenStreetMap and others. Authoritative, though note Streetside and Bird's Eye oblique imagery were removed in 2025.
missingPersonsRelevance: medium
coverage: [global]
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: [baidu-maps, arcgis, batchgeo]
aliases: [microsoft-maps, bing-maps-platform]
tags: [mapping, aerial-imagery, 3d, directions, poi]
source: arf-seed
lastVerified: '2026-06-13'
enrichment: full
---

# Bing Maps

> Microsoft's free web map — road, aerial/satellite, and 3D city views plus directions and business search — most valuable as an independent second source to compare against Google/Baidu imagery.

## When to use
You have an `address`, `geolocation`, or place/business `name` and want a different map provider's view to confirm a location, see imagery captured on a different date, check 3D building context (60+ cities), or run directions/POI search. In missing-persons work its biggest value is corroboration: where Google's imagery is stale or blurred, Bing's aerial or 3D view may differ and reveal more.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.bing.com/maps.
2. Search by `address`, `name`, or coordinates; or right-click the map to read coordinates.
3. Toggle Road vs Aerial; open 3D where available (major cities) to inspect building context and angles.
4. Use Directions for driving/walking/transit routes, or search to find businesses/landmarks (`employer-org`) with contact info near a point.
5. Pivot: compare the same point in `[[baidu-maps]]` (China) or against Google imagery; layer authoritative context from `[[arcgis]]`.

## Inputs -> Outputs
- **In:** `address`, `geolocation`, `name`
- **Out:** `address`, `geolocation`, `employer-org` (nearby businesses/POIs)
- **Empty/negative result looks like:** no/low-detail imagery for remote areas, or no POI matches; note Streetside (street-level) and Bird's Eye oblique were retired in 2025, so don't expect those views anymore.

## Gotchas & OpSec
- **Feature loss (2025):** Streetside street-level imagery and Bird's Eye oblique view were removed; for street-level you'll need another provider (e.g. Google Street View / Mapillary). Don't assume Bing still has them.
- Imagery dates differ from Google — that's the point (use both), but note capture date when reasoning about "what was there."
- Avoid signing into a personal Microsoft account if you want research kept unattributed.

## Overlaps ("do both")
- Pairs with `[[baidu-maps]]` for China coverage Bing lacks, and with Google Maps generally — always compare two providers' imagery and dates.
- Pairs with `[[arcgis]]` for authoritative thematic/boundary layers over the same area.

## Trust & verifiability
`trust: trusted` — first-party Microsoft service built on TomTom/OpenStreetMap data; authoritative for base mapping and imagery. Cross-check imagery dates and use a second provider for street-level views, which Bing no longer offers.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bing-maps |
| category | geolocation |
| selectorsIn → selectorsOut | address, geolocation, name → address, geolocation, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
