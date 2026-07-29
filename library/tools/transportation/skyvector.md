---
id: skyvector
name: SkyVector
description: Use when you have a `geolocation`, airport code, or navaid and want free aeronautical charts, airport data and flight-planning info — returns geolocation and airport/route context.
url: https://skyvector.com/
category: transportation
path:
- transportation
bestFor: Free interactive aeronautical charts (VFR/IFR), airport/navaid data, and route planning worldwide.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: Free to view charts, airport data, and plan routes in the browser; no account required. Optional paid/pro features exist for pilots.
opsec: passive
opsecNote: Fully passive — you browse public aeronautical charts and airport data. Nothing reaches your target. Charts reflect official aeronautical sources, not live aircraft positions (use a flight tracker for that).
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Long-established aviation charting site rendering official FAA/ICAO aeronautical data; authoritative for chart/airport/navaid information.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- skyvector.com
tags:
- Maps, Geolocation and Transport
- Aviation
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# SkyVector

> Free, browser-based aeronautical charts and airport data — the map layer for understanding the airspace, airports, and routes around a location of interest.

## When to use
You have a `geolocation`, an airport identifier (ICAO/IATA/FAA code), or a navaid, and you need aviation context: what airports and airstrips are near a point, runway and frequency data, airspace boundaries, and plausible flight routes between two fields. Useful for grounding an aviation lead — confirming an airfield exists at a coordinate, identifying the nearest airports to a last-known location, or sanity-checking a claimed flight path. It shows charts and static aeronautical data, not live aircraft.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://skyvector.com/.
2. Search an airport code or pan/zoom the chart to your `geolocation`; toggle VFR/IFR chart layers.
3. Click an airport for its data card (runways, frequencies, elevation, operator).
4. Use the flight-plan bar to enter departure/destination identifiers and read the great-circle route, distance, and en-route navaids.
5. Pivot: an airport code → flight-tracking tools (`[[plane-finder]]`) for actual traffic; nearby airfields → ground-search geography for a route lead.

## Inputs → Outputs
- **In:** `geolocation`, airport/navaid identifier, or a route (dep→dest)
- **Out:** aeronautical charts, airport/runway/frequency data, airspace boundaries, route distance and waypoints (`geolocation` context)
- **Empty/negative result looks like:** an unrecognized identifier returns no airport card; remote areas may show no charted airfields — meaning none is officially charted, not that no airstrip exists.

## Gotchas & OpSec
- Static aeronautical data, not live flights — pair with a tracker for real aircraft positions.
- Chart currency depends on the official source cycle; very recent changes may lag.
- OpSec: fully passive; no exposure.

## Overlaps ("do both")
- Pairs with `[[plane-finder]]` and other ADS-B trackers — SkyVector gives the airspace/airport map; the trackers put actual aircraft on it.

## Trust & verifiability
`trust: trusted` — renders official FAA/ICAO aeronautical data; authoritative for charts and airport/navaid facts.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | skyvector |
| category | transportation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
