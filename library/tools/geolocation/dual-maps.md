---
id: dual-maps
name: Dual Maps
description: Use when geolocating a spot and you want Google map, satellite, and Street View synchronized in one view — pan one panel and the others follow, easing imagery cross-reference.
url: https://data.mashedworld.com/dualmaps/map.htm
category: geolocation
path:
- geolocation
bestFor: Viewing Google map + aerial/satellite + Street View of the same coordinates side by side, synchronized.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
- image
status: unknown
pricing: free
costNote: Free mashup (MashedWorld); relies on Google/Bing map APIs whose availability can change.
opsec: passive
opsecNote: Displays third-party map tiles and Street View; it does not contact or notify anyone at the location.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: An older third-party Google/Bing maps mashup (MashedWorld). Depends on upstream map APIs that frequently break legacy mashups — verify it still renders before relying on it.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- MashedWorld Dual Maps
- dualmaps
tags:
- geospatial-research-and-mapping-tools
- street-view
- map-comparison
source: arf-seed
lastVerified: ''
enrichment: full
---

# Dual Maps

> A maps mashup that shows a Google map, an aerial/satellite layer, and Google Street View of the **same** point side by side and keeps them synchronized — move one panel and the others recenter.

## When to use
You are pinning down a `geolocation`/`address` and want to corroborate it across views at once: confirm a building's roofline from satellite while checking the same spot at ground level in Street View. In missing-persons geolocation, this speeds confirming that a photographed scene matches a candidate location, because you see plan view and street view together without flipping between tabs.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://data.mashedworld.com/dualmaps/map.htm (first confirm it still loads — legacy mashups break when upstream APIs change).
2. Enter an `address` or navigate the map to your `geolocation` of interest.
3. Pan/zoom one panel; the satellite and Street View panels stay locked to the same point and heading.
4. Read the synchronized views to confirm or reject a location. Pivot: lock the final coordinates with [[ctlrq-address-lookup]] for the street address.

## Inputs → Outputs
- **In:** `geolocation` (coordinates) or `address`
- **Out:** `geolocation` (confirmed spot) + `image` (synchronized map/aerial/Street View)
- **Empty/negative result looks like:** blank or error panels (upstream map API broke), or no Street View coverage for the area — common in rural/non-roadside locations.

## Gotchas & OpSec
- As a legacy mashup it is fragile: if Google/Bing change their embed APIs, panels may fail to load — treat `status: unknown` and verify.
- Street View imagery can be years out of date; what you see may not reflect current conditions.
- OpSec: passive — you view public map tiles; nobody at the location is contacted or alerted.

## Overlaps ("do both")
- Pairs with [[ctlrq-address-lookup]] (convert the confirmed pin to a street address) and with native Google Maps/Earth, which you should fall back to if this mashup is broken.

## Trust & verifiability
`trust: unverified` — a third-party mashup dependent on external map APIs, with no guarantee it still renders. The underlying imagery is Google/Bing (reliable); this tool's value is only the synchronized layout, so verify it loads and cross-check on native maps.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | dual-maps |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → geolocation, image |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
