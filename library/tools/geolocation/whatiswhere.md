---
id: whatiswhere
name: WhatIsWhere
description: Use when you have a `geolocation` or `address` and want to enumerate every nearby point-of-interest by type/keyword — returns `geolocation` + `address` for matching POIs.
url: https://www.whatiswhere.com
category: geolocation
path:
- geolocation
bestFor: Multi-criteria POI enumeration around a known location using OpenStreetMap data.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
- address
status: live
pricing: free
costNote: Free to search and view POIs. No account needed for basic searches; bulk POI download may prompt registration but the map search itself is open.
opsec: passive
opsecNote: Queries hit WhatIsWhere's servers (backed by OpenStreetMap data), not the target or any account the target controls. Nothing is disclosed to the subject. Standard web hygiene (no login, generic IP) is sufficient.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Independent third-party front-end over public OpenStreetMap data. Data quality inherits OSM's crowd-sourced accuracy — good in dense areas, patchy in rural ones.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- openstreetmap
aliases:
- What Is Where
- whatiswhere.com
tags:
- toddington
- curated-directory
- geo-location-mapping-tools
- poi-search
source: toddington-resources
lastVerified: '2026-07-11'
enrichment: full
---

# WhatIsWhere

> An OpenStreetMap-backed point-of-interest search engine: pick an area and pull every hospital, hotel, ATM, place of worship, or arbitrary keyword-matched POI around it.

## When to use
You have a `geolocation` (coordinates, a pin, a town) or an `address` and need to know what is *around* it — a subject was last seen near a location and you want the nearby shelters, hostels, hospitals, bus stops, or businesses they could plausibly have reached. Also useful in reverse: you have a photo showing a specific POI type (e.g. a particular chain, a distinctive amenity) and want to enumerate candidate locations in a search radius.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.whatiswhere.com in a normal browser.
2. Navigate the map to your area of interest (search a place name/`address`, or drop the view over known coordinates).
3. Choose POI categories/types (amenity classes like hospital, hotel, fuel, place_of_worship) or enter free-text keywords; you can combine multiple criteria in one project.
4. Run the search — matching POIs plot on the map with names and, where OSM has them, addresses/coordinates. You can save/reuse the search project and download the POI set.
5. Pivot: feed a specific POI's `address`/`geolocation` into street-level imagery, or cross-reference the enumerated businesses against `[[openstreetmap]]` and local records.

## Inputs → Outputs
- **In:** `geolocation` or `address` (the search area) + a POI type/keyword filter
- **Out:** `geolocation` and `address` for each matching point of interest
- **Empty/negative result looks like:** no pins returned for the chosen type in that bounding box — usually means OSM has no such POI tagged there (common in sparse/rural regions), NOT proof none exists on the ground.

## Gotchas & OpSec
- Human-in-the-loop: none for basic search; the tool works directly in the browser.
- OpSec: **passive** — you are querying a mapping service, not the subject. Nothing reaches the target.
- Data is only as complete as OpenStreetMap in that region. Verify any critical POI against ground-truth imagery before relying on it.

## Overlaps ("do both")
- Pairs with `[[openstreetmap]]` — WhatIsWhere is a friendlier multi-criteria query layer, but raw OSM (and its Overpass queries) can surface tags and detail WhatIsWhere's UI hides.

## Trust & verifiability
`trust: community` — a useful independent interface over authoritative-ish open data. Treat the underlying OSM data as crowd-sourced: cross-check anything that drives a real-world decision.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | whatiswhere |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → geolocation, address |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
