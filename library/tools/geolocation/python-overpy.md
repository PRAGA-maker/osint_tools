---
id: python-overpy
name: OverPy (python-overpy)
description: Use when you have a `geolocation` or a described place feature and want to query OpenStreetMap data programmatically — returns matching map features (coordinates, tags) as geolocation leads.
url: https://github.com/DinoTools/python-overpy
category: geolocation
path:
- geolocation
bestFor: Scripting Overpass (OpenStreetMap) queries from Python to find or verify map features by type, tag, or bounding box — the automation layer for chronolocation/geolocation puzzles.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
- address
status: live
pricing: free
costNote: Free and open-source (MIT), installed via pip. Uses the public Overpass API (free; rate-limited by the endpoint you choose).
opsec: passive
opsecNote: Queries hit a public Overpass API endpoint, not the target — you are reading OpenStreetMap data, so nothing is disclosed to any subject. Vary/choose your Overpass endpoint to respect rate limits; no sock puppet needed for the OSM data itself.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: python-lib
trust: community
trustNote: Mature, actively maintained Python wrapper (350+ commits, CI) for the Overpass API; reliability of results is that of OpenStreetMap's crowd-sourced data.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
relatedTools:
- overpass-turbo
aliases:
- python-overpy
- overpy
tags:
- maps-geolocation-and-transport
- openstreetmap
- python
source: cyb-detective
lastVerified: '2026-07-17'
enrichment: full
---

# OverPy (python-overpy)

> A Python wrapper for the OpenStreetMap Overpass API — script the "find every X near here" queries that geolocation work depends on, and parse the results as data.

## When to use
You are geolocating a photo/video or verifying a location and need to programmatically ask OpenStreetMap questions: "list all churches within this bounding box," "find windmills near these coordinates," "which streets have this name in this region." When a still shows a distinctive feature (a water tower, a specific shop chain, a road pattern), OverPy lets you enumerate candidate matches from OSM at scale instead of eyeballing a map, then narrow to a `geolocation`.

## How to use it (`bestInteractionPattern`: python-lib)
1. Install: `pip install overpy`.
2. In Python, build an Overpass QL query and run it:
   ```python
   import overpy
   api = overpy.Overpass()
   result = api.query('node["amenity"="place_of_worship"](50.6,7.0,50.8,7.3);out;')
   for node in result.nodes:
       print(node.lat, node.lon, node.tags.get("name"))
   ```
3. Iterate the query (feature type, tags, bounding box) to match the distinctive feature you see in your source imagery.
4. Cross-reference returned coordinates against satellite/street imagery to confirm.
5. Pivot: a confirmed `geolocation`/`address` → mapping and street-level imagery tools; a named feature → local records.

## Inputs → Outputs
- **In:** `geolocation` / a described OSM feature (tags + bounding box)
- **Out:** matching OSM features — coordinates, tags, sometimes an `address` — as structured Python objects
- **Empty/negative result looks like:** an empty result set — the feature isn't mapped in OSM for that area, or your query/tag is wrong. OSM coverage is uneven; absence isn't proof the feature doesn't exist.

## Gotchas & OpSec
- You must know Overpass QL and OSM tagging conventions; a wrong tag returns nothing even when the feature exists.
- Public Overpass endpoints rate-limit and occasionally time out on large queries — narrow the bounding box.
- Data quality is crowd-sourced; verify any match against imagery before concluding.

## Overlaps ("do both")
- Pairs with `[[overpass-turbo]]` — Overpass Turbo is the interactive web UI for building/visualising the same queries; prototype visually there, then automate/batch with OverPy.

## Trust & verifiability
`trust: community` — a well-maintained open-source library. It faithfully returns OpenStreetMap data, so accuracy tracks OSM's crowd-sourced quality; always confirm a candidate location with imagery.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | python-overpy |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation, address |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | python-lib |
| opsec | passive |
| human-in-loop | no |
