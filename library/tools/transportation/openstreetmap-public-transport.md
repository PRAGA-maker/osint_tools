---
id: openstreetmap-public-transport
name: OpenStreetMap Public Transport
description: Use when you have a `geolocation`/area and want its public-transit network — returns downloadable tram/bus/metro/train route data from OpenStreetMap for that area.
url: https://wadouk.github.io/osm-public-transports/#3/27.29/5.45
category: transportation
path:
- transportation
bestFor: Downloading OpenStreetMap public-transport route data (tram, bus, metro, train) for a selected map area.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free, no account; data comes from OpenStreetMap (open data).
opsec: passive
opsecNote: You browse and download open map data — no target is contacted or alerted. The queries hit OSM/Overpass infrastructure, not any subject; standard third-party logging only.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community front end over OpenStreetMap data; coverage and accuracy depend on how well volunteers have mapped transit in that area.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools: []
aliases:
- OSM public transport
- osm-public-transports
tags:
- Maps, Geolocation and Transport
- Transport
- openstreetmap
source: cyb-detective
lastVerified: '2026-07-28'
enrichment: full
---

# OpenStreetMap Public Transport

> A map tool for pulling an area's transit network out of OpenStreetMap — select a region and download its tram, bus, metro, and train routes as data.

## When to use
Low-relevance, geospatial-support only. Reach for it when a case has a location component and you want the public-transport context of an area: what tram/bus/metro/train lines and routes run there. Useful for reasoning about how a subject could have moved through a place, identifying a station/stop near a location, or grounding a movement hypothesis in the actual transit network. It returns route/network geodata, not anything about a person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the tool at the URL above.
2. Pan/zoom to the area of interest; a **green** square around a location indicates transit data is available there.
3. Use the download buttons (right side) to pull the data for tram, bus, metro, and/or train routes.
4. Load the downloaded data into a GIS/mapping tool for analysis.
5. Pivot: overlay the transit network on a subject's known points to reason about routes, nearby stops, and travel times.

## Inputs → Outputs
- **In:** `geolocation` (a selected map area)
- **Out:** downloadable transit-route geodata (`geolocation`-based network) for that area
- **Empty/negative result looks like:** no green square / empty download — OSM has little or no transit data mapped there; coverage is volunteer-dependent, so gaps are common outside well-mapped cities.

## Gotchas & OpSec
- Coverage and accuracy depend entirely on **OSM volunteer mapping** — well-mapped cities are rich, rural/less-mapped areas may be empty or outdated.
- It gives the *network*, not live schedules or vehicle positions — pair with an official transit feed for timing.
- OpSec: **passive** — open data; nothing reaches any subject.

## Overlaps ("do both")
- Do both with official agency GTFS feeds and general OSM/mapping tools: this extracts the routes quickly, while GTFS adds schedules and the base map gives surrounding context.

## Trust & verifiability
`trust: community` — a community front end over open OpenStreetMap data. The data is as good as local mapping; verify critical route details against the operating agency's official information.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | openstreetmap-public-transport |
| category | transportation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
