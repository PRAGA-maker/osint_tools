---
id: mapbox
name: MapBox
description: Use when you need to build custom maps, geocode at scale, or run isochrone/routing queries via API — a mapping platform, not an investigative database.
url: https://www.mapbox.com
category: geolocation
path:
- geolocation
bestFor: Developer mapping platform — custom basemaps, batch geocoding, and routing/isochrone APIs to support geospatial analysis.
selectorsIn:
- address
- geolocation
selectorsOut:
- geolocation
- address
status: live
pricing: freemium
costNote: Free tier with monthly request quota; paid beyond that. API key required for programmatic use.
opsec: passive
opsecNote: API/platform calls hit Mapbox servers, not the target. You disclose your queries to Mapbox; nothing reaches the subject.
humanInLoop: true
humanInLoopReason:
- api-key
- account-login
bestInteractionPattern: api
trust: trusted
trustNote: Established commercial mapping platform; reliable infrastructure but a tool for building maps, not a source of personal data.
missingPersonsRelevance: medium
coverage:
- global
auth: api-key
api: true
localInstall: false
registration: true
aliases: []
tags:
- geospatial-research-and-mapping-tools
- geocoding
- routing
- platform
source: awesome-osint
lastVerified: ''
enrichment: full
---

# MapBox

> Commercial mapping/geospatial platform — custom basemaps plus geocoding, routing, and isochrone APIs to power your own analysis, not a database of people or places to query for a subject.

## When to use
You need to do geospatial analysis at scale or in a custom map: batch-geocode many addresses, compute travel-time areas (isochrones — "everywhere reachable within 30 min of this point"), or build a styled case map. Reach for this when no-code tools and single-lookup geocoders are not enough and you can work via API. It produces coordinates, routes, and reachability areas from inputs you supply; it does not return personal records.

## How to use it (`bestInteractionPattern`: api)
1. Register at https://www.mapbox.com and obtain an access token (API key).
2. Call the relevant API: Geocoding (address ↔ coordinates), Directions (routing), or Isochrone (reachability polygons).
3. Parse the JSON response (coordinates, route geometry, isochrone polygon).
4. Visualize on a Mapbox GL or `[[leaflet]]` map if you need a picture.
5. Pivot: an isochrone around a last-known point bounds a realistic search/canvass area; batch geocoding feeds a clustering analysis.

## Inputs → Outputs
- **In:** `address` or `geolocation` (single or batch)
- **Out:** `geolocation`, `address`, route geometry, and travel-time areas
- **Empty/negative result looks like:** a geocode with low relevance score or an empty feature list — refine the query string or check your token/quota.

## Gotchas & OpSec
- Requires an account and API key; usage is metered and your queries are visible to Mapbox.
- Free tier has monthly request caps; large batches can exceed them.
- This is infrastructure, not an OSINT data source — do not represent it as one.
- OpSec: passive toward the subject; you are disclosing queries to a vendor, so use an appropriate account if attribution matters.

## Overlaps ("do both")
- Pairs with `[[leaflet]]` for rendering and `[[map-maker]]`/`[[latlong]]` for one-off geocodes; use Mapbox when you need batch/isochrone scale.

## Trust & verifiability
`trust: trusted` — a well-established commercial platform with reliable geocoding/routing. Trust applies to the infrastructure; any investigative conclusion still depends on the inputs and your interpretation.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mapbox |
| category | geolocation |
| selectorsIn → selectorsOut | address, geolocation → geolocation, address |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | api |
| opsec | passive |
| human-in-loop | yes |
