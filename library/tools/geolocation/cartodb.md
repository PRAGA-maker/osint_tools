---
id: cartodb
name: CartoDB
description: Use when you have a sizeable spatial dataset (addresses, coordinates, geometries) and need cloud-based mapping, SQL/spatial analysis, and shareable web maps beyond simple plotting.
url: https://cartodb.com
category: geolocation
path:
- geolocation
bestFor: Cloud-native spatial analysis and web-map building on your own datasets (SQL, spatial functions, enrichment, dashboards).
selectorsIn: [address, geolocation]
selectorsOut: [geolocation, address]
status: live
pricing: freemium
costNote: "cartodb.com redirects to carto.com; there is a 'Try for free' trial/free account, but CARTO is an enterprise location-intelligence platform — sustained/large use is paid (pricing not published on the landing page)."
opsec: passive
opsecNote: You upload and analyse your own data on CARTO's cloud (and it can run on your own cloud data warehouse); it does not contact the target. Hosted/shared maps live with a third party — keep sensitive maps private.
humanInLoop: true
humanInLoopReason: [account-login]
bestInteractionPattern: web-manual
trust: community
trustNote: CARTO (formerly CartoDB) is a well-established commercial geospatial/location-intelligence platform; mature and credible, but vendor-controlled and oriented to paying enterprise users.
missingPersonsRelevance: low
coverage: [global]
auth: account
api: true
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools: [atlas, batchgeo, arcgis]
aliases: [carto, carto-com]
tags: [gis, spatial-analysis, web-maps, location-intelligence, sql]
source: awesome-osint
lastVerified: '2026-06-13'
enrichment: full
---

# CartoDB

> CARTO (formerly CartoDB) — a cloud-native location-intelligence platform: load spatial data, run SQL/spatial analysis and ML, enrich it, and publish interactive web maps and dashboards. `cartodb.com` now redirects to `carto.com`.

## When to use
You have a real spatial dataset — many `address`es or `geolocation` points, plus geometries — and need more than a pin map: SQL queries over spatial data, spatial joins/buffers, data enrichment, and a shareable interactive web map or dashboard. It's the heavyweight option when `[[batchgeo]]`'s plot-a-spreadsheet is too thin and you want analysis. Note the focus is enterprise location intelligence, so it's overkill for a quick lookup.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://carto.com (the old https://cartodb.com 301-redirects here) and start a free trial / account.
2. Connect data: upload files or connect a cloud data warehouse (BigQuery, Snowflake, Redshift, Databricks, etc.); CARTO can run analysis in-place on that warehouse.
3. Build a map in the builder; run spatial analysis components (joins, buffers, ML) and optionally enrich via the Data Observatory.
4. Publish/share an interactive map or dashboard; keep it private for sensitive data.
5. Pivot: use authoritative basemaps/layers from `[[arcgis]]`; for a lighter alternative, `[[atlas]]` or `[[batchgeo]]`.

## Inputs -> Outputs
- **In:** `address`, `geolocation` (your dataset / geometries)
- **Out:** `geolocation`, `address` (mapped, geocoded, analysed, enriched)
- **Empty/negative result looks like:** rows that fail to geocode, or analysis returning empty where geometries don't intersect — check your input geometry/CRS.

## Gotchas & OpSec
- Human-in-the-loop: account/trial required; sustained or large-scale use is a paid enterprise product, not a free utility.
- It's an analysis platform, not a people-search — it maps and analyses *your* data, it doesn't find a person.
- Hosted maps/data sit with a third party (or your linked warehouse); keep case data private and mind data-handling policies.
- Heavier setup than simple plotters — don't reach for it for a one-off address list.

## Overlaps ("do both")
- Pairs with `[[atlas]]` as an alternative cloud GIS (pick one workspace).
- Pairs with `[[batchgeo]]` for quick plotting and `[[arcgis]]` for authoritative reference layers.

## Trust & verifiability
`trust: community` — CARTO is a mature, credible commercial geospatial platform. Outputs are your own analysis, so reliability tracks your input data quality and CRS handling; verify geocoding and projections before drawing conclusions.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cartodb |
| category | geolocation |
| selectorsIn → selectorsOut | address, geolocation → geolocation, address |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
