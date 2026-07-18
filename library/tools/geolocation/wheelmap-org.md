---
id: wheelmap-org
name: Wheelmap.org
description: Use when you have a `geolocation` and want a crowdsourced map of wheelchair-accessible public places nearby — returns place types, addresses, and accessibility status.
url: https://wheelmap.org
category: geolocation
path:
- geolocation
bestFor: Enumerating public venues (cafés, libraries, transit stops, shops) around a point and their wheelchair-accessibility status.
selectorsIn:
- geolocation
selectorsOut:
- address
- geolocation
status: live
pricing: free
costNote: Free non-profit service (Sozialhelden e.V., Berlin); all data is open and free to view and share. Built on OpenStreetMap.
opsec: passive
opsecNote: Passive — you browse an open crowdsourced map; no query touches any subject. Editing/tagging a place, however, is tied to your OpenStreetMap account, so use a research account if contributing.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Crowdsourced on top of OpenStreetMap; accessibility tags and place data are contributed by volunteers and vary in freshness and completeness.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- openstreetmap
aliases:
- Wheelmap
- wheelmap.org
tags:
- Maps, Geolocation and Transport
- accessibility
- openstreetmap
source: cyb-detective
lastVerified: '2026-07-18'
enrichment: full
---

# Wheelmap.org

> A crowdsourced OpenStreetMap overlay of 3M+ public places rated for wheelchair accessibility on a simple traffic-light scale.

## When to use
You have a `geolocation` (a city, an address, a point where a subject was last seen) and want to enumerate the public venues around it. Wheelmap catalogs 180 categories of public places — cafés, libraries, pools, shops, transit stops — with their `address` and an accessibility rating. In a missing-persons context this is a supporting/enrichment tool: it helps build a picture of the accessible venues in an area (relevant when the subject uses a wheelchair or mobility aid), or simply as another point-of-interest layer over a location.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://wheelmap.org and search a city or place name, or navigate the map to the `geolocation` of interest.
2. Read the markers: green = fully accessible, yellow = partially, red = not accessible, grey = unrated.
3. Click a marker for the place name, category, `address`, and coordinates.
4. Filter by category to narrow to relevant venue types.
5. Pivot: a specific venue's address/coordinates feed street-view, business-listing, and local-directory tools; for automation, Wheelmap exposes a public API (see wheelmap.org developer docs).

## Inputs → Outputs
- **In:** `geolocation`
- **Out:** `address` and `geolocation` of nearby public places, plus category and accessibility rating
- **Empty/negative result looks like:** a sparse or all-grey map — the area simply has few contributor-tagged places; it reflects contributor coverage, not the actual absence of venues.

## Gotchas & OpSec
- Coverage is uneven: dense in German/European cities, thin elsewhere; grey markers mean "unrated," not "inaccessible."
- Place data inherits OpenStreetMap's freshness — a venue may have closed since it was tagged.
- This is a places tool, not a people tool; it cannot locate an individual, only characterize an area.
- OpSec: passive browsing; contributing edits is tied to an OSM account.

## Overlaps ("do both")
- Pairs with `[[openstreetmap]]` — Wheelmap is a themed accessibility view of the same OSM data; use OSM directly for the full POI set and Wheelmap when accessibility status matters.

## Trust & verifiability
`trust: community` — volunteer-contributed on OpenStreetMap; treat individual accessibility ratings and place details as crowd input to be confirmed, not authoritative facts.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wheelmap-org |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → address, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
