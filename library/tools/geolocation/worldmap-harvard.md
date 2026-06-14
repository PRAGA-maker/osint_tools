---
id: worldmap-harvard
name: WorldMap Harvard
description: Use when you need specialized GIS data layers (historical, demographic, environmental) overlaid on a base map to add context to a location, rather than a person lookup.
url: http://worldmap.harvard.edu
category: geolocation
path:
- geolocation
bestFor: Exploring and overlaying open GIS map layers (historical, demographic, thematic) on a location.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: degraded
pricing: free
costNote: Free academic platform; create an account to build/save maps.
opsec: passive
opsecNote: Browsing/building map layers on an academic GIS platform; no contact with the target.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Harvard Center for Geographic Analysis academic project; data quality is good but the platform has been in transition — verify it is still live and current.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools:
- tableau
- zeemaps
aliases:
- WorldMap
tags:
- gis
- geospatial-research-and-mapping-tools
source: awesome-osint
lastVerified: ''
enrichment: full
---

# WorldMap Harvard

> Harvard's open GIS platform for layering thematic map data (historical, demographic, environmental) — a context/analysis tool, not a people-finder.

## When to use
You have a `geolocation` and want richer spatial context than a plain map gives: historical boundaries, demographic/census layers, environmental or thematic GIS data, or a place to overlay your own dataset. This is niche for missing-persons work — useful mainly when terrain, jurisdiction, or environmental context matters — hence low direct relevance.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://worldmap.harvard.edu (confirm it still resolves — the platform has been in transition).
2. Browse existing public maps or search the layer catalog for relevant thematic data.
3. Create a free account to compose your own map, add base layers, and overlay GIS datasets or uploaded data.
4. Inspect features and export/screenshot for the case file.
5. Pivot: for plotting your own point data more simply use [[zeemaps]] or [[tableau]].

## Inputs → Outputs
- **In:** `geolocation` / area of interest (and optionally your own GIS data).
- **Out:** thematic map overlays and spatial context (qualitative `geolocation` insight).
- **Empty/negative result looks like:** no relevant layers for your region, or the platform being offline/migrated — verify availability first.

## Gotchas & OpSec
- Status **degraded**: an academic project that has changed hosting/form over time; check it is live before relying on it.
- Building/saving maps requires a free account (account-login).
- Specialist GIS tool — overkill for most missing-persons lookups; reach for it only when thematic spatial data genuinely helps.

## Overlaps ("do both")
- Overlaps with [[tableau]] and [[zeemaps]] for plotting your own geodata; WorldMap's edge is curated academic GIS layers.

## Trust & verifiability
`trust: community` — reputable academic source (Harvard CGA), but platform continuity is uncertain; confirm the data's currency and that the site is operational.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | worldmap-harvard |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
