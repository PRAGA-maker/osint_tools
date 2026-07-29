---
id: europe-station-maps-floor-plan
name: NS International Station Maps & Floor Plans
description: Use when you have a European railway station `address`/`geolocation` and want its interior floor plan and platform layout — returns detailed station layout for geolocation/movement analysis.
url: https://www.nsinternational.com/en/stations/station-maps-floor-plan
category: transportation
path:
- transportation
bestFor: Interior floor plans and platform layouts of major European train stations for geolocation and route reconstruction.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
- address
status: live
pricing: free
costNote: Free reference maps from NS International (Dutch Railways' international arm); no account.
opsec: passive
opsecNote: You browse published station reference maps on a public rail site; nothing about a subject is submitted. Fully observational — a background/enrichment resource, not a query against a person.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Published by NS International (Nederlandse Spoorwegen), the official Dutch rail operator; the station layouts are authoritative operator data.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- NS International station maps
- European station floor plans
tags:
- Maps, Geolocation and Transport
- Railway
- reference-map
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# NS International Station Maps & Floor Plans

> Official interior floor plans and platform layouts for major European train stations — a reference layer for geolocating footage or reconstructing a subject's movement through a station.

## When to use
You have imagery, CCTV, or a witness account placing a subject inside or around a major European railway station, and you need the interior layout — entrances, platform numbering, concourse shops, exits — to geolocate a photo/video or reconstruct a route. This is enrichment/reference, not a person-lookup: it turns "a train station" into a specific, mappable interior.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the NS International station-maps page.
2. Select the relevant station (coverage centers on Dutch and connected Western-European international-service stations — Amsterdam, Rotterdam, Brussels, etc.).
3. Open the floor plan / platform map and compare interior features (signage, kiosks, platform numbers, staircases) against your imagery to fix the exact location.
4. Pivot: a confirmed platform/exit ties to timetables and CCTV placement; a station `address`/`geolocation` feeds mapping and transit-schedule tools.

## Inputs → Outputs
- **In:** a station identity or approximate `geolocation`/`address`
- **Out:** interior floor plan, platform layout, entrance/exit and amenity positions → refined `geolocation`/`address`
- **Empty/negative result looks like:** the station isn't in NS International's network (no map available) — fall back to OpenStreetMap indoor data or the local operator's site.

## Gotchas & OpSec
- Coverage is limited to NS International's served stations, not all of Europe — for stations outside that network use the national operator or OSM.
- Layouts change with renovations; verify the map's currency against recent street-level or satellite imagery when precision matters.
- **Passive**: purely a published reference; no subject data leaves your side.

## Overlaps ("do both")
- Pairs with general mapping/geolocation tools in `maps-geospatial-data`: use those to place the station on the ground, this to resolve the interior.

## Trust & verifiability
`trust: trusted` — first-party operator maps, authoritative for platform/layout facts, with renovation-driven staleness the only caveat.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | europe-station-maps-floor-plan |
