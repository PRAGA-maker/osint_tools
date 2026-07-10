---
id: old-maps-online
name: Old Maps Online
description: Use when you have a `geolocation` or place `address` and want historical maps of that spot across time — returns historical map imagery and period place/boundary context.
url: https://www.oldmapsonline.org
category: geolocation
path:
- geolocation
bestFor: Finding period-accurate historical maps for a location to interpret old addresses, vanished place names and changed boundaries.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
- address
status: live
pricing: free
costNote: Free, open-access web portal aggregating maps from 50+ libraries; an optional mobile app exists. No account needed to search or view.
opsec: passive
opsecNote: You are searching a public map archive by place, not querying anything about a person. No target interaction; standard browser hygiene is sufficient.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Reputable aggregator pulling from 50+ national libraries and archives. Map georeferencing is generally good but approximate; treat overlays as close, not survey-exact.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- OldMapsOnline
tags:
- toddington
- curated-directory
- geo-location-mapping-tools
- historical-maps
source: toddington-resources
lastVerified: '2026-07-10'
enrichment: full
---

# Old Maps Online

> A search portal over 500,000+ historical maps from 50+ libraries: see what a location looked like — and what it was called — at a chosen point in history.

## When to use
You have a `geolocation` (coordinates or a spot on a map) or a place `address` — especially an *old* one — and need historical context: what a street/village/parcel was called decades or centuries ago, how boundaries shifted, or which structures existed then. Invaluable when a lead references a former place name, a demolished building, or an address that no longer resolves on modern maps.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.oldmapsonline.org and open the search/map view.
2. Type a place name into the search box, or pan/zoom the map to your area of interest — results in the side panel update automatically as thumbnails.
3. Use the **timeline** to restrict to a period; the results and any boundary display update to that era.
4. Click a thumbnail to view full metadata (source library, date, scale) and open the high-resolution map; overlay it on a modern base map to compare then-vs-now.
5. Pivot: a resolved historical place name or footprint feeds genealogical/records searches and lets you re-query modern geolocation tools with the correct current name.

## Inputs → Outputs
- **In:** `geolocation` (coords / map position) or place `address`/name
- **Out:** historical map imagery for that spot and time, with period `geolocation`/`address` context (old names, boundaries)
- **Empty/negative result looks like:** few or no thumbnails for the area/era. Coverage is uneven by region and period — a gap means no contributing library holds a georeferenced map there, not that the place didn't exist.

## Gotchas & OpSec
- Coverage varies widely by country and century; well-mapped regions (Europe, North America) are richer than others.
- Georeferencing is approximate — overlays are close but not survey-grade; don't use them for precise metric measurement.
- It maps *places*, not people; value is contextual (interpreting an address/lead), not identifying.
- OpSec: passive; no target is queried.

## Overlaps ("do both")
- Do alongside modern mapping/satellite tools: Old Maps Online tells you what a location *was*, the modern map tells you what it *is* — together they resolve changed place names on a lead.

## Trust & verifiability
`trust: community` — a respected aggregator sourcing from national libraries and archives, so the underlying maps are authentic primary documents; the only caveat is approximate georeferencing, so verify exact positions against the original scan.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | old-maps-online |
</content>
