---
id: nga-geoint
name: NGA GEOINT
description: Use when you need open-source geospatial libraries/datasets (GeoServer plugins, geodata tools) from the US National Geospatial-Intelligence Agency's GitHub — a developer resource, not a lookup site.
url: https://github.com/ngageoint
category: geolocation
path:
- geolocation
bestFor: Open-source GEOINT software and datasets (e.g., GeoServer extensions, mosaic/elevation/format tools) for building geospatial analysis pipelines.
selectorsIn:
- geolocation
selectorsOut: []
status: live
pricing: free
costNote: US government open-source (mostly Apache/permissive licenses) on GitHub; free.
opsec: passive
opsecNote: Browsing/cloning public repositories reveals nothing about a target. What you build with the tools determines downstream OpSec.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: cli
trust: trusted
trustNote: Official GitHub org of the US National Geospatial-Intelligence Agency; reputable, well-maintained open-source GEOINT projects.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
relatedTools: []
aliases:
- National Geospatial-Intelligence Agency
- ngageoint
tags:
- geospatial-research-and-mapping-tools
- developer-tools
source: awesome-osint
lastVerified: ''
enrichment: full
---

# NGA GEOINT

> The US National Geospatial-Intelligence Agency's open-source GitHub organization — a toolbox of geospatial software for analysts who build their own pipelines, not a person-search service.

## When to use
Reach for this when you are *constructing* geospatial capability: serving and styling imagery (GeoServer plugins), handling elevation/format conversions, mosaicking, or processing large geodata for an investigation involving a `geolocation`. It does not answer "where is this person" directly; it gives you the engineering parts to analyze imagery and terrain. Low direct MP relevance, but valuable infrastructure for a serious geo team.

## How to use it (`bestInteractionPattern`: cli)
1. Browse github.com/ngageoint and pick the relevant repo (read its README for scope and maturity).
2. Clone and build per the repo's instructions (Java/Python/JS vary by project).
3. Run/integrate the tool into your geo workflow (e.g., add a GeoServer extension, run a format/elevation utility).
4. Pivot: the outputs feed your own map/analysis stack — combine with [[openlayers]] or [[overpass-turbo]] for display and querying.

## Inputs → Outputs
- **In:** `geolocation` data / imagery you supply to the tools.
- **Out:** none as ready intelligence — these are libraries/utilities that transform geodata.
- **Empty/negative result looks like:** a repo that is archived/stale or not relevant to your task; check last-commit date and stars before investing.

## Gotchas & OpSec
- This is an org of many repos of varying maturity — vet each one individually; some are demos or deprecated.
- Building these requires real dev/geospatial skills (Java toolchains, GDAL, etc.).
- OpSec: passive to clone; your own deployment dictates downstream exposure.

## Overlaps ("do both")
- Pairs with display/query tooling like [[openlayers]] and [[overpass-turbo]] — NGA provides processing components; those provide visualization and OSM extraction.

## Trust & verifiability
`trust: trusted` — official US government open-source org; code is auditable on GitHub. Honesty note: utility depends entirely on picking an active, fit-for-purpose repo.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nga-geoint |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → (tooling, no direct output) |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (manual-review) |
