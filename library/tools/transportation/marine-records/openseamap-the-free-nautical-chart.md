---
id: openseamap-the-free-nautical-chart
name: OpenSeaMap - The free nautical chart
description: Use when you have a `geolocation` on or near water and want maritime context — returns seamarks, harbours/marinas, navigational aids, and depth/nautical overlays.
url: https://www.openseamap.org
category: transportation
path:
- transportation
- marine-records
bestFor: Reading nautical chart data — seamarks, harbours, marinas, lights, buoys — over an OpenStreetMap base for coastal/marine geolocation.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free, open, crowd-sourced (OpenStreetMap project). No account for viewing.
opsec: passive
opsecNote: A static map you read — no target interaction, nothing is notified. Only your own IP touches the tiles/site; use a VPN if the collection is sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Community/crowd-sourced (OpenStreetMap seamark data). Good for orientation and infrastructure, but not an official navigational chart — coverage and accuracy vary by region and contributor activity.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- openseamap
aliases:
- OpenSeaMap
- openseamap.org
tags:
- nautical
- marine
- maps
- geolocation
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# OpenSeaMap - The free nautical chart

> The OpenStreetMap of the sea — a free nautical chart layer showing seamarks, harbours, marinas, lights, and buoys for coastal and maritime geolocation.

## When to use
Your case touches the water — a photo taken from a boat or harbour, a marina you're trying to identify, a coastal `geolocation` to contextualise. OpenSeaMap overlays nautical detail (seamarks, navigation aids, harbour/marina facilities, depth hints) that land maps omit, helping you pin a coastal location, identify a port, or understand maritime infrastructure near a point of interest.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.openseamap.org and navigate to your `geolocation` (coordinates, port name, or by panning the map).
2. Zoom in to render the seamark layer: harbours, marinas, lights, buoys, and navigational marks.
3. Click features for detail (light characteristics, harbour facilities) to match against clues in a photo (a specific lighthouse pattern, a marina layout).
4. Cross-reference with a satellite/imagery base and land maps to confirm the exact spot.
5. Pivot: an identified harbour/marina feeds vessel-tracking (AIS) tools and local records; the confirmed `geolocation` feeds broader mapping.

## Inputs → Outputs
- **In:** `geolocation` (coordinates, port name, or map area)
- **Out:** `geolocation` context — seamarks, harbours/marinas, lights/buoys, navigational and depth overlays
- **Empty/negative result looks like:** sparse or missing seamark data in a region — coverage is contributor-dependent, so a bare area means "not mapped," not "no infrastructure."

## Gotchas & OpSec
- Not an official chart — never rely on it for actual navigation; for OSINT it's orientation, not authority.
- Coverage is uneven; well-sailed European waters are dense, remote coasts thin.
- Fully passive; no target interaction.

## Overlaps ("do both")
- Pairs with AIS vessel-tracking and satellite-imagery tools — OpenSeaMap identifies the port/marine feature, trackers show the boats there, and imagery confirms the ground truth.

## Trust & verifiability
`trust: community` — crowd-sourced OSM seamark data. Reliable for infrastructure orientation; verify any precise location against imagery and an official source before drawing conclusions.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | openseamap-the-free-nautical-chart |
| category | transportation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
