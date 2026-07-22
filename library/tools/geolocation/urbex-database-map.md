---
id: urbex-database-map
name: URBEX database map
description: Use when you have an approximate `geolocation` in Europe and want to identify abandoned/derelict "lost places" nearby — returns mapped `geolocation` points and site photos.
url: https://www.urbex.nl/map/
category: geolocation
path:
- geolocation
bestFor: Locating abandoned/derelict buildings and "lost places" across Europe on an interactive map.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
- image
status: live
pricing: freemium
costNote: The public map is free to browse; the community adds and curates locations. Some detailed submissions may require a free account.
opsec: passive
opsecNote: Browsing the public map is passive and touches no subject infrastructure. Use it purely as a terrain/venue reference, never to query about a named person. If you register to see hidden coordinates, use a sock-puppet account.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Community-maintained urbex catalogue (urbex.nl); coordinates are user-submitted and can be approximate, stale, or deliberately fuzzed to deter looting.
missingPersonsRelevance: medium
coverage:
- eu
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Urbex database
- urbex.nl map
tags:
- Maps, Geolocation and Transport
- Anomalies and "Lost Places"
source: cyb-detective
lastVerified: '2026-07-22'
enrichment: full
---

# URBEX database map

> A community map of abandoned and derelict "lost places" across Europe — useful for reasoning about where someone might shelter, squat, or explore.

## When to use
You have an approximate `geolocation` (a region, town, or last-known area) in Europe and want to enumerate nearby abandoned buildings, factories, hospitals, bunkers, or other derelict sites. In a missing-persons context this generates a search-terrain list: derelict structures are common shelter points, urbex destinations, and hazard sites, so the map surfaces candidate locations to check against last-known movements or a subject's known urban-exploration hobby.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.urbex.nl/map/ in a browser.
2. Pan/zoom to the target region. Clusters expand into individual pins as you zoom in.
3. Click a pin to read the location type (factory, hospital, chateau, bunker, etc.), photos, and any coordinates/notes contributors added.
4. Record each candidate `geolocation` and cross-reference against the subject's last-known location, travel direction, or interests.
5. Pivot: feed promising coordinates to a satellite/street-level viewer to assess access, then to ground search.

## Inputs → Outputs
- **In:** `geolocation` (region/area to browse)
- **Out:** `geolocation` (coordinates of abandoned sites), `image` (site photos), site type/description
- **Empty/negative result looks like:** a region with no pins means no contributor has logged sites there — absence of coverage, not absence of derelict sites. Do not treat an empty area as cleared.

## Gotchas & OpSec
- Coordinates are user-submitted; some are intentionally coarse or offset to protect fragile sites. Verify on satellite imagery before dispatching anyone.
- Coverage is densest in the Netherlands/Belgium/Germany and thins elsewhere.
- OpSec: passive browsing only — this is a venue reference, not a person lookup. Never solicit the community about a named individual.

## Overlaps ("do both")
- Pairs with general satellite/street-view mapping tools for access assessment, and with other abandoned-site catalogues, since each community maps different regions and no single database is complete.

## Trust & verifiability
`trust: community` — curated by urbex hobbyists, not an authority. Treat entries as leads to verify with imagery, not confirmed accessible locations.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | urbex-database-map |
| category | geolocation |
