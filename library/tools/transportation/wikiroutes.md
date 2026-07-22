---
id: wikiroutes
name: WikiRoutes
description: Use when you have a `geolocation`/city and want its public-transport network — returns bus/tram/metro routes, stops and coverage for that area.
url: http://wikiroutes.info/
category: transportation
path:
- transportation
bestFor: Looking up the bus/tram/metro routes and stops serving a specific place, to reason about how a subject could have travelled to/from it.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free, no signup required.
opsec: passive
opsecNote: A public crowdsourced transit map — you query places, not people. Fully passive with nothing disclosed about any subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Crowdsourced (community-submitted and community-verified via voting); coverage and accuracy vary by city, so treat routes as indicative and cross-check locally.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- wikiroutes.info
- Routees
tags:
- transportation
- public-transit
- routes
source: bellingcat-toolkit
lastVerified: '2026-07-22'
enrichment: full
---

# WikiRoutes

> A free, crowdsourced world transit map — bus, tram and metro routes and stops for cities across every continent.

## When to use
You have a `geolocation` or `address` and want to understand the public-transport options around it: which routes pass through, where the nearest stops are, and where those lines go. Useful in movement/timeline analysis — e.g. reasoning about how a subject could plausibly have reached a location, or which line a described journey matches.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://wikiroutes.info/ and select or search the city of interest.
2. Browse the map to see every mapped route and stop, or look up a specific route to trace its full path and stops.
3. Use the trip planner to see connections between two points.
4. Note coverage quality — well-mapped cities are detailed; smaller ones may be sparse or dated.
5. Pivot: a stop near an `address` and the routes serving it inform where the subject could travel to next.

## Inputs → Outputs
- **In:** `geolocation` / `address` / city
- **Out:** transit routes, stops and network coverage (`geolocation` context) for the area
- **Empty/negative result looks like:** a city with little or no mapped data — the community hasn't covered it; fall back to the local operator's official maps.

## Gotchas & OpSec
- Crowdsourced: coverage and freshness vary a lot by city; verify against the official transit authority for anything decisive.
- Shows the network, not live/real-time service.
- OpSec: fully passive.

## Overlaps ("do both")
- Pairs with official operator maps and general mapping tools (Google/OpenStreetMap) — WikiRoutes centralises transit specifically, but confirm exact timetables/routes with the operator.

## Trust & verifiability
`trust: community` — a useful crowdsourced database, but community-maintained accuracy means routes should be corroborated against the local authority before you rely on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wikiroutes |
