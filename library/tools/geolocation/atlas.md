---
id: atlas
name: Atlas
description: Use when you have your own case location data (spreadsheet/coordinates) and want to load, map, and run spatial analysis on it collaboratively with an AI-assisted GIS.
url: https://atlas.co
category: geolocation
path:
- geolocation
bestFor: AI-assisted, collaborative GIS for mapping and analysing your own spatial data without specialist GIS skills.
selectorsIn: [address, geolocation]
selectorsOut: [geolocation, address]
status: live
pricing: freemium
costNote: A free account is available ("sign up for a free account"); higher usage, team features, and larger workloads sit behind paid tiers (pricing not published on the landing page).
opsec: passive
opsecNote: You upload and analyse your own case data on Atlas's hosted platform; it does not contact the target. Note that anything you upload lives on a third-party cloud and shared map links are viewable by anyone who has them.
humanInLoop: true
humanInLoopReason: [account-login]
bestInteractionPattern: web-manual
trust: community
trustNote: Commercial AI-native GIS SaaS (atlas.co); legitimate and functional but vendor-maintained and relatively new, so it is an analysis surface rather than an authoritative data source.
missingPersonsRelevance: low
coverage: [global]
auth: account
api: false
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools: [cartodb, batchgeo, arcgis]
aliases: [atlas-co]
tags: [gis, mapping, spatial-analysis, saas]
source: awesome-osint
lastVerified: '2026-06-13'
enrichment: full
---

# Atlas

> An AI-native, collaborative GIS (atlas.co): connect a spreadsheet or geodata, describe what you want in natural language, and it builds the map, dashboard, or spatial analysis.

## When to use
You already have case data with locations — `address`es or `geolocation` coordinates in a spreadsheet, GeoJSON, KML, shapefile, or PostgreSQL — and want to plot it, run real spatial analysis (buffers, joins, projections), and share a live map with a team without being a GIS expert. It is a workspace for *your* data, not a lookup of someone else's; reach for it to organise sightings, search grids, or movement points rather than to discover a person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://atlas.co and sign up for a free account.
2. Connect your data: upload a spreadsheet/CSV, GeoJSON/GeoTIFF/KML/GPKG/shapefile, or link a database (e.g. PostgreSQL).
3. Use the Navi AI prompt to build a map/dashboard ("plot these addresses and buffer 1km") or build layers manually.
4. Run spatial analysis on the real geometry; set up shared, live-synced maps for collaborators and (optionally) scheduled reports/alerts.
5. Pivot: export results or share a public map link; bring authoritative basemaps from `[[arcgis]]` underneath your points.

## Inputs -> Outputs
- **In:** `address`, `geolocation` (your own dataset)
- **Out:** `geolocation`, `address` (mapped, geocoded, analysed)
- **Empty/negative result looks like:** rows that fail to geocode (bad/ambiguous addresses) appear unplaced or mismatched — verify before trusting placement.

## Gotchas & OpSec
- Human-in-the-loop: requires account creation; full feature set/large workloads need a paid plan.
- This is an *analysis* tool — it does not find people or pull external records; don't expect lookups.
- Uploaded case data resides on a third-party cloud, and shared map links are accessible to anyone with the URL; keep sensitive maps private.
- AI-generated maps/analyses can be subtly wrong (bad geocodes, wrong projection); sanity-check geometry.

## Overlaps ("do both")
- Pairs with `[[cartodb]]` as an alternative cloud GIS — pick one to host your spatial workspace.
- Pairs with `[[batchgeo]]` for a lighter, no-account way to plot an address list, and `[[arcgis]]` for authoritative reference layers.

## Trust & verifiability
`trust: community` — a real, functioning commercial GIS SaaS, but vendor-controlled and newer; treat outputs as your own analysis (only as good as your inputs), not as authoritative external data.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | atlas |
| category | geolocation |
| selectorsIn → selectorsOut | address, geolocation → geolocation, address |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
