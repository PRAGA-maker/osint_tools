---
id: geoint-py
name: geoint-py
description: Use when you have a `geolocation`/region and want geospatial-intelligence workflows in Python — returns spatial grids and mapped conflict/protest event data for an area.
url: https://github.com/gisfromscratch/geoint-py
category: geolocation
path:
- geolocation
bestFor: Scripting geospatial-intelligence workflows — spatial binning grids and mapping protest/armed-conflict events over a region.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free/open-source (uses ArcGIS API for Python plus external geoprotests/geoconflicts APIs; some ArcGIS features may need an account).
opsec: passive
opsecNote: Works over aggregate event datasets and coordinates, not a named individual; nothing about a person is queried and no one is alerted. Passive.
humanInLoop: false
humanInLoopReason:
- api-key
bestInteractionPattern: python-lib
trust: community
trustNote: Individual open-source project (gisfromscratch); modest activity, last release 2023, aimed at analysts building GIS workflows.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
relatedTools:
- qgis
- kepler-gl
aliases:
- geoint-py
tags:
- geospatial
- python
- gis
source: osint4all
lastVerified: '2026-07-17'
enrichment: full
---

# geoint-py

> A Python toolkit for geospatial-intelligence workflows — spatial grids plus protest/armed-conflict event mapping over an area of interest.

## When to use
You need to analyse a *region* rather than a person: bin points into spatial grids, or visualize demonstration/armed-conflict events across an area (via its geoprotests/geoconflicts API integrations). In missing-persons work this is a niche, context-level tool — e.g. understanding unrest or event density in a region where someone was last seen — not a way to locate an individual. Reach for it when you're doing area analysis in a Python/GIS pipeline.

## How to use it (`bestInteractionPattern`: python-lib)
1. Install from https://github.com/gisfromscratch/geoint-py (Python; depends on the ArcGIS API for Python).
2. Import the toolkit and follow the bundled Jupyter notebook samples.
3. Build a rectangular grid for a bounding box to bin/aggregate spatial data, or call the geoprotests/geoconflicts helpers to pull and map recent events for an area.
4. Supply any required API keys for the external event feeds / ArcGIS.
5. Pivot: the mapped output is context — combine with `[[qgis]]` for deeper spatial analysis and with local news/records for the human-level leads.

## Inputs → Outputs
- **In:** a `geolocation` / bounding box (and event-feed parameters)
- **Out:** spatial grids and mapped protest/conflict event layers (`geolocation`)
- **Empty/negative result looks like:** an empty layer/grid — no events in the feed for that area/timeframe, or a missing API key; it doesn't mean nothing happened, only that the feed has nothing.

## Gotchas & OpSec
- Not a people-finder — it maps aggregate events and grids, so its direct value to an individual case is limited (low MP relevance).
- Depends on the ArcGIS API for Python and external event APIs; expect setup friction and possible key requirements.
- Low maintenance (last release 2023) — verify the external APIs it calls are still live before relying on it.

## Overlaps ("do both")
- Pairs with `[[qgis]]` — export/analyse the same spatial data in a full GIS; geoint-py is the scripted-workflow layer.
- Pairs with `[[kepler-gl]]` for quick visual exploration of the point/event layers.

## Trust & verifiability
`trust: community` — a single-maintainer open-source project. Outputs are only as good as the third-party event feeds it wraps; validate a sample of events against their original sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | geoint-py |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | python-lib |
| opsec | passive |
| human-in-loop | no |
