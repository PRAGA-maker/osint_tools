---
id: power-plants-in-the-united-states
name: Power Plants in the United States
description: Use when you have a US `geolocation`/`address` and want to identify nearby electricity-generating facilities, their fuel type and operator — returns `geolocation`, `employer-org`.
url: https://www.arcgis.com/apps/dashboards/201fc98c0d74482d8b3acb0c4cc47f16
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Locating and identifying power-generation plants near a US point of interest and reading their operator/fuel type.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
- employer-org
status: live
pricing: free
costNote: Free public ArcGIS dashboard; no account needed to pan, zoom or click plant markers.
opsec: passive
opsecNote: A read-only Esri/ArcGIS map layer — no query touches any person. Only your connection to arcgis.com is exposed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Community-published ArcGIS dashboard built on public EIA/federal generation datasets; provenance of the specific layer is not first-party, so treat plant attributes as reference not gospel.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- US Power Plants dashboard
tags:
- infrastructure
- geospatial
source: osint4all
lastVerified: '2026-07-22'
enrichment: full
---

# Power Plants in the United States

> A public ArcGIS dashboard mapping US electricity-generating facilities — used in OSINT for infrastructure and geospatial context around a location.

## When to use
You have a US `geolocation` or `address` and need to know what power-generation infrastructure sits near it — for situational/geospatial context (e.g. corroborating a photo's background, mapping the industry footprint of an area, or identifying a facility's operator). Not a people-lookup; it is a location/infrastructure reference layer.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the dashboard URL in a browser.
2. Pan/zoom to the area of interest, or search the map for a place/`address`.
3. Click a plant marker to read its attributes: coordinates (`geolocation`), fuel/generation type, nameplate capacity, and operating company (`employer-org`).
4. Pivot: feed an operator name into a business-registry lookup, or coordinates into a mapping/imagery tool for ground-truthing.

## Inputs → Outputs
- **In:** `geolocation` / `address` (an area to inspect)
- **Out:** `geolocation` (plant coordinates), `employer-org` (operator/utility), plus fuel type and capacity attributes
- **Empty/negative result looks like:** no markers in the viewport — means no catalogued generating facility there, not that the area lacks all infrastructure.

## Gotchas & OpSec
- Coverage and freshness depend on the underlying federal generation dataset; small or new facilities may be missing.
- Dashboard is community-published, so a broken/retired ArcGIS item is possible — if the map fails to load, the item may have been unshared.
- OpSec: passive, read-only; nothing is logged against any person.

## Overlaps ("do both")
- Pairs with satellite/aerial imagery and mapping tools: this identifies and names a facility while imagery lets you verify it on the ground.

## Trust & verifiability
`trust: community` — a third-party ArcGIS dashboard over public generation data; useful for orientation, but confirm any operator/capacity detail against the primary EIA source before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | power-plants-in-the-united-states |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation, address → geolocation, employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
