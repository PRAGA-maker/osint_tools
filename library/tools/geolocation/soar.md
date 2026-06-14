---
id: soar
name: SOAR
description: Use when you want to browse a community digital atlas of maps and imagery layers for an area, beyond standard basemaps.
url: https://soar.earth/
category: geolocation
path:
- geolocation
bestFor: A "digital atlas" platform aggregating satellite, drone and community-contributed maps/imagery for an area.
selectorsIn: [geolocation, address]
selectorsOut: [geolocation, metadata]
status: live
pricing: freemium
costNote: Browsing the public atlas is free; some contributed/high-res layers and uploads may require an account or payment.
opsec: passive
opsecNote: Browsing a public map platform; you only reveal your own access, not the target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Commercial community map-sharing platform; layer quality and freshness vary because much content is user-contributed.
missingPersonsRelevance: medium
coverage: [global]
auth: none
api: false
localInstall: false
registration: false
aliases: [Soar.Earth]
tags:
- geospatial-research-and-mapping-tools
source: awesome-osint
lastVerified: ''
enrichment: full
---

# SOAR

> A "digital atlas" web platform aggregating satellite, aerial, drone and community-contributed maps and imagery into one browsable map of the world.

## When to use
You have a `geolocation`/`address` and want to see whether non-standard imagery or specialist maps exist for that area — drone captures, historical or thematic layers, community uploads — that mainstream basemaps lack. Useful for filling coverage gaps over remote areas in search planning.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://soar.earth/ and navigate to your `geolocation`/`address`.
2. Browse the available layers/maps contributed for that area and open ones of interest.
3. Inspect imagery and read any `metadata` (source, date) the contributor provided.
4. Pivot: corroborate with authoritative dated imagery in `[[sentinel-hub]]` and analyze in `[[qgis]]`.

## Inputs → Outputs
- **In:** `geolocation`, `address`
- **Out:** available community/satellite map layers (`geolocation` + contributor `metadata`)
- **Empty/negative result looks like:** only base satellite layers and no specialist contributions for the area — coverage is uneven and community-driven.

## Gotchas & OpSec
- Human-in-the-loop: none for browsing; uploading/contributing needs an account.
- OpSec: passive; you only touch the platform, never the target.
- Much content is user-contributed, so date/provenance/accuracy vary — verify before relying on a layer.

## Overlaps ("do both")
- Pairs with `[[sentinel-hub]]` and `[[sas-planet]]` for authoritative imagery; SOAR's value is unusual community/drone layers others lack.

## Trust & verifiability
`trust: community` — a legitimate commercial map-sharing platform, but layer quality and freshness vary because content is largely user-contributed; verify provenance per layer.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | soar |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → geolocation, metadata |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
