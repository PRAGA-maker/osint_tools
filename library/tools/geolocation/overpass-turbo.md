---
id: overpass-turbo
name: Overpass Turbo
description: Use when you need to find every place matching specific features (e.g., all schools/churches/diners with a feature) within an area — query OSM data, not just browse it.
url: https://overpass-turbo.eu/
category: geolocation
path:
- geolocation
bestFor: Querying OpenStreetMap for all features matching tags within a bounding box — turning "a place that looks like X near Y" into a candidate list.
selectorsIn:
- geolocation
- name
- address
selectorsOut:
- geolocation
- address
status: live
pricing: free
costNote: Free web frontend to the Overpass API. No account needed; heavy queries are subject to server timeouts/fair-use.
opsec: passive
opsecNote: Queries hit the public Overpass API, not the subject. No target interaction; nothing about the person is sent.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: community
trustNote: Standard, widely used frontend to OSM's Overpass query engine; results are exactly as complete/accurate as the underlying OSM data.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- openstreetmap
aliases:
- Overpass-Turbo
tags:
- geospatial-research-and-mapping-tools
- osm-query
source: arf-seed
lastVerified: ''
enrichment: full
---

# Overpass Turbo

> A web frontend to OpenStreetMap's Overpass query engine — find every feature matching a set of tags within an area, the power tool for narrowing "where could this be."

## When to use
You can describe a location by its features but don't know the exact spot: "find all churches with a square tower within 20 km of town X," "all diners named 'Star' in this county," "every quarry near this river." Given a candidate `geolocation` (search area) plus distinguishing attributes (a `name` on a sign, a place type), Overpass Turbo returns a finite candidate list to check — invaluable for chronolocation and for narrowing last-known-location searches.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open overpass-turbo.eu; set the map to your area of interest (the `{{bbox}}` is taken from the view).
2. Write or use the Wizard to generate an Overpass QL query (e.g., `amenity=place_of_worship` within bbox, optionally `name~"..."`).
3. Run it; matching features draw on the map. Inspect each result's tags and coordinates.
4. Export as GeoJSON/KML to plot in [[openlayers]] or another tool, then verify top candidates against satellite/street-view imagery.

## Inputs → Outputs
- **In:** a search-area `geolocation`/bbox plus feature criteria (tags, optionally a `name` or `address` fragment).
- **Out:** a list of candidate `geolocation`s (and `address` tags where present) matching your criteria.
- **Empty/negative result looks like:** zero features returned — either none exist in OSM there (under-mapped) or your tag filter is wrong; loosen the query and reconsider tagging.

## Gotchas & OpSec
- Requires learning Overpass QL (the Wizard helps); easy to mis-tag and get empty/over-broad results.
- Large/unbounded queries time out — always constrain to a bbox/area.
- Completeness is bounded by OSM tagging; an unmapped feature won't appear. The manual-review step is verifying each candidate against imagery.
- OpSec: passive; no subject contact.

## Overlaps ("do both")
- Built directly on [[openstreetmap]] data — browse OSM to understand tags, then use Overpass Turbo to enumerate every matching feature.

## Trust & verifiability
`trust: community` — a transparent query layer over openly auditable OSM data; results are reproducible, with completeness limited only by OSM coverage.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | overpass-turbo |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, name, address → geolocation, address |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |
