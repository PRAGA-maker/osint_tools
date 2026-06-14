---
id: flash-earth
name: Flash Earth
description: Use when you need recent/near-real-time satellite and weather imagery for an area to check conditions around a date or location.
url: https://zoom.earth/
category: geolocation
path:
- geolocation
bestFor: Fast browser review of recent satellite, cloud, and weather imagery for an area of interest.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
- image
status: live
pricing: free
costNote: Free web app (current home of the former Flash Earth at zoom.earth).
opsec: passive
opsecNote: Renders public satellite/weather tiles in your browser; no contact with the target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: zoom.earth is the live successor to the old Flash Earth; aggregates GOES/EUMETSAT and other public imagery. Reliable for weather/recent imagery, not high-res forensic detail.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Zoom Earth
tags:
- geospatial-research-and-mapping-tools
source: arf-seed
lastVerified: ''
enrichment: full
---

# Flash Earth

> Now hosted at zoom.earth, a fast web viewer for near-real-time satellite, cloud, and weather imagery layered on a global map.

## When to use
You have a `geolocation`/`address` and want to check recent or near-live conditions: cloud cover, storms, wildfires, flooding, or general satellite context around the time of a disappearance or a planned search. It answers "what did the sky/ground broadly look like there recently" rather than fine building-level detail.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://zoom.earth/.
2. Search a place or pan/zoom to coordinates.
3. Toggle layers (satellite, clouds, precipitation, fires, storms) and use the time slider to step through recent frames.
4. Note conditions for your date window; screenshot for the case file.
5. Pivot: for dated archival or high-res imagery use `[[earthexplorer]]`; for ground-level detail use `[[google-maps]]`/`[[dualmaps]]`.

## Inputs → Outputs
- **In:** `geolocation` or `address`.
- **Out:** recent satellite/weather `image` for that `geolocation`.
- **Empty/negative result looks like:** imagery is coarse or cloud-obscured for your spot — it is weather-scale, so don't expect street-level features.

## Gotchas & OpSec
- Human-in-the-loop: none; no login.
- Resolution is weather/regional scale, not forensic — wrong tool for reading signage or vehicles.
- OpSec: passive; only the imagery providers see your tile requests.

## Overlaps ("do both")
- Complements `[[earthexplorer]]` (dated, high-res archive) and `[[google-earth]]` (3D/historical) — this one is the live/recent-conditions view.

## Trust & verifiability
`trust: community` — established public-imagery aggregator (the live successor to Flash Earth); data quality inherits from GOES/EUMETSAT and similar sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | flash-earth |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → geolocation, image |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
