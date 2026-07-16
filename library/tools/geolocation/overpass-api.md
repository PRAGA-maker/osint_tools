---
id: overpass-api
name: Overpass API
description: Use when you have a `geolocation` and want to query OpenStreetMap features or see map edits over a date range — returns matching OSM objects and change history.
url: https://overpass-api.de/achavi/
category: geolocation
path:
- geolocation
bestFor: Querying OpenStreetMap's database for specific features near a point, and (via achavi) visualizing OSM changesets over a date range.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
- address
status: live
pricing: free
costNote: Free public endpoint. No account, but the shared server enforces rate/timeout limits — heavy queries are throttled.
opsec: passive
opsecNote: Queries hit a public OSM mirror, not the subject; nothing is disclosed to anyone you're investigating. Passive. Your IP is visible to the Overpass server — use a VPN if you care about that, but there is no target-side exposure.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: api
trust: trusted
trustNote: Community-run infrastructure over authoritative OpenStreetMap data; the data is crowdsourced but transparent and widely relied upon for geolocation work.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- shadow-finder
aliases:
- Overpass Turbo
- achavi
- Augmented OSM Change Viewer
tags:
- Maps, Geolocation and Transport
- Tools
source: cyb-detective
lastVerified: '2026-07-16'
enrichment: full
---

# Overpass API

> A query engine over the full OpenStreetMap database — find every feature of a given type near a point, or (via the achavi change viewer at this URL) watch how the map for an area was edited over a date range.

## When to use
You're geolocating an image or bounding a search area and need to query OSM structurally: "list all fuel stations / churches / distinctive towers within N metres of this point," or "what features match these tags near here." The achavi endpoint additionally shows recent OSM *changes* over a date window — useful for spotting newly-mapped structures or activity in a region.

## How to use it (`bestInteractionPattern`: api)
1. For feature queries, use Overpass Turbo (overpass-turbo.eu) to write/visualise Overpass QL; the raw API lives at overpass-api.de. For change history, open the achavi URL and set the bbox/date range.
2. Write a query — e.g. `node[amenity=place_of_worship](around:500,LAT,LON);out;` to find worship sites near a coordinate.
3. Run it; results render on the map and as structured data (name tags, coordinates, addresses where tagged).
4. Use matches to corroborate a geolocation hypothesis: does the scene's distinctive feature exist at the candidate location?
5. Pivot: matched OSM objects give exact `geolocation` and sometimes a tagged `address`/name, feeding satellite/streetview confirmation.

## Inputs → Outputs
- **In:** a `geolocation` (bbox/point) + feature tags
- **Out:** matching OSM objects with coordinates, name/`address` tags; achavi returns changeset history for the area
- **Empty/negative result looks like:** zero elements returned — no OSM features match the tags there (the feature may be unmapped, not absent) or the query/bbox is wrong; broaden tags or radius.

## Gotchas & OpSec
- Data completeness varies by region — rural/less-mapped areas have sparse coverage; absence in OSM ≠ absence on the ground.
- Query timeouts/rate limits on the public server; keep bboxes tight or run your own instance for heavy work.
- Overpass QL has a learning curve — Overpass Turbo's wizard helps build queries.
- OpSec: fully passive.

## Overlaps ("do both")
- Pairs with `[[shadow-finder]]` and satellite/streetview tools — Overpass narrows *where* a feature is; shadow/imagery tools confirm *that* candidate against the actual photo.

## Trust & verifiability
`trust: trusted` — authoritative OpenStreetMap data via community infrastructure; crowdsourced tags can be wrong or stale, so confirm a candidate location with imagery.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | overpass-api |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | api |
| opsec | passive |
| human-in-loop | no |
