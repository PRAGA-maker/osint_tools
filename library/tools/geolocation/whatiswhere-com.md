---
id: whatiswhere-com
name: Whatiswhere.com
description: Use when you have an approximate geolocation and want every nearby point-of-interest of a given type — returns candidate addresses and geolocations to match against a photo or clue.
url: http://whatiswhere.com
category: geolocation
path:
- geolocation
bestFor: Multi-criteria POI search over global OpenStreetMap data — list all objects of a type within an area and export the results.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
- address
status: live
pricing: free
costNote: Free web tool; no account required for basic POI search and map browsing.
opsec: passive
opsecNote: Searches run against OpenStreetMap-derived data on Whatiswhere's servers; no target is contacted and nothing is queried about a person. Standard web-log exposure only — use a clean browser if the area of interest is sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Independent front-end over OpenStreetMap data; POI accuracy and freshness are only as good as OSM's crowd-sourced entries.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- whatiswhere
aliases:
- whatiswhere
- whatiswhere.com
tags:
- geolocation
- openstreetmap
- poi-search
- Maps, Geolocation and Transport
source: cyb-detective
lastVerified: '2026-07-18'
enrichment: full
---

# Whatiswhere.com

> An OpenStreetMap-powered point-of-interest search: draw an area, pick a POI type (over 100 supported), and get every matching place — useful for narrowing where a photo or clue was taken.

## When to use
You are geolocating from an image or witness detail and have a rough `geolocation` (a city, a neighbourhood, "near a church and a petrol station"). Whatiswhere lets you list every instance of a distinctive POI type — a specific chain, a place of worship, a school, a fuel station — inside your search area, so you can cross-reference the set of candidate places against features visible in the photo and shortlist a likely `address`/`geolocation`.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://whatiswhere.com and pan/zoom the map to your area of interest (or search a place name).
2. Choose the POI type(s) you want to enumerate — the tool supports many object categories from OSM (shops, amenities, transport, worship, etc.).
3. Run the search to list all matching POIs in view; each result carries a name, coordinates, and often an address. Export the result set if you need to work through it offline.
4. Pivot: compare each candidate's surroundings (on the map / Street View elsewhere) with the photo's background to eliminate non-matches, then confirm the winning `address`.

## Inputs → Outputs
- **In:** `geolocation` (an area/place to search within)
- **Out:** `geolocation` (POI coordinates), `address` (where OSM records one)
- **Empty/negative result looks like:** no POIs of that type returned in the area — either OSM genuinely lacks them there, or the region is poorly mapped (coverage is thin in some rural/non-Western areas).

## Gotchas & OpSec
- Human-in-the-loop: none; it is a self-serve map/search tool.
- OpSec: passive — you are querying map data, not a person; no target is notified.
- Data quality: results are only as complete and current as OpenStreetMap. A missing POI is often an OSM gap, not proof the place doesn't exist — corroborate with a second map source.

## Overlaps ("do both")
- Pairs with `[[whatiswhere]]` (the same service's companion entry) and with satellite/Street-View imagery — Whatiswhere gives you the candidate list of places, and imagery confirms which one matches the scene.

## Trust & verifiability
`trust: community` — it is a reliable independent interface over OpenStreetMap; verify any single POI against OSM directly or ground-truth imagery before acting on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | whatiswhere-com |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation, address |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
