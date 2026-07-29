---
id: flightconnections
name: FlightConnections
description: Use when you have an airport, airline `name`, or route and want to see which airlines fly it and all direct destinations from an airport — returns geolocation (routes, reachable cities) leads.
url: https://www.flightconnections.com
category: transportation
path:
- transportation
bestFor: Mapping which airlines operate a route and every direct destination reachable from a given airport.
selectorsIn:
- name
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: Free to view route maps and airline/airport connections in the browser; some advanced filters/features may be behind a paid tier. No account needed for basic use.
opsec: passive
opsecNote: Fully passive — a public route-map reference. Browsing reveals nothing about your target and touches only FlightConnections' site.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Widely-used flight-route reference; schedules/routes come from airline timetable data and can lag real-world changes (new/dropped routes, seasonal service).
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- flightconnections.com
tags:
- aviation
- routes
source: metaosint
lastVerified: '2026-07-29'
enrichment: full
---

# FlightConnections

> An interactive world map of airline routes — pick an airport and see every direct destination; pick a route and see which airlines fly it.

## When to use
You have an airport, an airline `name`, or a city pair and want to reason about air travel: where someone could fly non-stop from airport X, which airlines connect two cities, or whether a claimed direct flight actually exists. Useful for scoping plausible travel paths in a timeline, narrowing which airlines/routes to check in a flight tracker, or sanity-checking a travel claim. It shows scheduled routes, not live flights.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.flightconnections.com.
2. Enter an airport (see all its direct destinations mapped), an airline (see its whole network), or a from→to pair (see which carriers fly it).
3. Read the route map and the airline list for each connection.
4. Note the operating airlines and their codes.
5. Pivot: candidate airlines/routes → `[[plane-finder]]`/`[[skyvector]]` for actual flights and airport data; reachable cities → geolocation scoping of a travel window.

## Inputs → Outputs
- **In:** an airport, airline `name`, or city pair
- **Out:** direct destinations and operating airlines mapped (`geolocation` route network)
- **Empty/negative result looks like:** "no direct flights" between a pair, or few destinations from a small airport — means no scheduled non-stop service (a connection would be needed), not that travel is impossible.

## Gotchas & OpSec
- Reflects scheduled routes from timetable data — new, dropped, seasonal, or charter flights may be missing or stale.
- Non-stop focus: it won't plan multi-leg itineraries automatically.
- OpSec: fully passive public reference.

## Overlaps ("do both")
- Feeds `[[plane-finder]]` and `[[skyvector]]` — FlightConnections tells you which routes/airlines are possible; the trackers/charts give the live flights and airport detail.

## Trust & verifiability
`trust: community` — popular route reference from airline timetable data; verify a specific flight's current existence with a live source before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | flightconnections |
| category | transportation |
| selectorsIn → selectorsOut | name → geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
