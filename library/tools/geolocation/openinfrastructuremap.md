---
id: openinfrastructuremap
name: OpenInfrastructureMap
description: Use when an image or area shows power lines, pylons, substations, or telecom masts and you want to identify/confirm a location by its infrastructure.
url: https://openinframap.org/
category: geolocation
path:
- geolocation
bestFor: Visualizing power grids, substations, pipelines, and telecom infrastructure from OSM tags as a geolocation fingerprint.
selectorsIn:
- geolocation
- image
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free; renders OpenStreetMap infrastructure tags. No account needed.
opsec: passive
opsecNote: Browsing the map does not contact the subject; it reads public OSM data. No target interaction.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Well-regarded OSM-derived thematic map; only as complete as OSM's infrastructure tagging, which is strong in some regions and thin in others.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- openstreetmap
- openrailwaymap-2
aliases:
- OpenInfraMap
- Open Infrastructure Map
tags:
- geospatial-research-and-mapping-tools
- infrastructure
source: arf-seed
lastVerified: ''
enrichment: full
---

# OpenInfrastructureMap

> A thematic OSM map of power, telecom, and energy infrastructure — turns transmission lines, substations, and masts into a geolocation fingerprint.

## When to use
You have a photo (`image`) or area where distinctive infrastructure is visible — high-voltage pylons of a particular type, a substation, a wind/solar farm, a telecom mast — and you want to match it to a real location, or confirm a candidate `geolocation` by checking that the expected lines/substations are present. A useful supporting layer in chronolocation when natural/urban landmarks are scarce. Medium MP relevance: it corroborates a place rather than finding a person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open openinframap.org and pan/zoom to your candidate area (or paste coordinates in the URL).
2. Read the overlays: power lines (with voltage), substations, plants, and telecom/petroleum layers.
3. Compare the routing/voltage of nearby lines and the position of substations/masts against your image.
4. Pivot to [[openstreetmap]] to read the underlying tags and to satellite imagery to confirm pylon types and corridors.

## Inputs → Outputs
- **In:** candidate `geolocation` and/or an `image` showing infrastructure.
- **Out:** confirmed/narrowed `geolocation` via matching infrastructure.
- **Empty/negative result looks like:** no infrastructure rendered in the area — either genuinely none or (more likely in thin regions) simply untagged in OSM. Absence is weak evidence.

## Gotchas & OpSec
- Entirely dependent on OSM tagging quality; great in Europe/parts of the US, sparse elsewhere.
- Voltage/line classifications are contributor-entered and can be wrong — corroborate with imagery.
- OpSec: passive; no subject contact.

## Overlaps ("do both")
- Pairs with [[openstreetmap]] (raw tags) and [[openrailwaymap-2]] (rail infrastructure) — different thematic slices of the same OSM data; use whichever matches the visible feature.

## Trust & verifiability
`trust: community` — derived from openly auditable OSM data, but completeness and tag accuracy vary by region; treat as a corroborating layer, not sole proof.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | openinfrastructuremap |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, image → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
