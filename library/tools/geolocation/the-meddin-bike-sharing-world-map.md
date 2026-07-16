---
id: the-meddin-bike-sharing-world-map
name: The Meddin Bike-sharing World Map
description: Use when you have a `geolocation` and want to identify the bike-share system, operator, and station layout there — returns local bikeshare details to corroborate a scene.
url: https://bikesharingworldmap.com/
category: geolocation
path:
- geolocation
bestFor: A global directory/map of bike-sharing systems — operators, bike types, station networks, and recently closed/suspended services by city.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free to browse and search; the project also publishes periodic reports. No account.
opsec: passive
opsecNote: Browsing a reference map is passive — nothing about a subject is submitted and no one is notified. Ordinary browsing hygiene is enough.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The Meddin/PBSC-associated bike-share world map is a well-known industry reference; system/operator data is curated and reliable, though station-level detail may lag reality.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Bike Sharing World Map
- Meddin bikeshare map
tags:
- Maps, Geolocation and Transport
- Urban and industrial infrastructure
source: cyb-detective
lastVerified: '2026-07-16'
enrichment: full
---

# The Meddin Bike-sharing World Map

> A global reference map of bike-share systems — a niche geolocation aid for identifying which scheme, operator, and branded bikes/docks belong to a place seen in a photo.

## When to use
You're geolocating an image that shows shared bikes or docking stations, and you want to identify the scheme (branding, bike color/style, dock design) and pin it to a city/operator. The distinctive branding of a bike-share system is a strong location clue — this map tells you which cities run which systems, narrowing candidates. A supporting tool, not a primary locator.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the map and either browse to a candidate region or search a city.
2. Identify the local system(s): operator name, bike type, dock/station style, and platform.
3. Match the branding/design in your image to the system's known appearance to confirm or narrow the city.
4. Note recently closed/suspended systems — a defunct scheme in a photo dates the image.
5. Pivot: a confirmed system localizes the scene to that operator's coverage area, which you then refine with satellite/streetview.

## Inputs → Outputs
- **In:** a `geolocation` clue (a bike-share scheme/branding seen in imagery, or a city name)
- **Out:** the local bike-share system's operator, bike/dock style, and coverage `geolocation`
- **Empty/negative result looks like:** no listed system for the area — the place has no (indexed) bike-share, or the map hasn't catalogued it; the branding clue then can't be resolved here.

## Gotchas & OpSec
- Narrow use — only helps when shared bikes/docks are visible in the material.
- Station-level detail can lag real-world changes; treat "recently closed" data as approximate.
- It identifies the *system*, not an individual — pair with imagery tools to pin the exact spot.
- OpSec: passive reference browsing.

## Overlaps ("do both")
- Pairs with satellite/streetview and OSM tools (e.g. `[[overpass-api]]`) — this identifies the bike-share system to narrow the city; the mapping tools confirm the exact location.

## Trust & verifiability
`trust: trusted` — an established industry reference; system/operator data is reliable, but confirm the specific location with independent imagery before concluding.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | the-meddin-bike-sharing-world-map |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
