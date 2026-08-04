---
id: chronotrains
name: Chronotrains
description: Use when you have a European city/`geolocation` and want to see everywhere reachable by train within a chosen time — returns an isochrone map of rail-reachable destinations.
url: https://www.chronotrains.com/en
category: transportation
path:
- transportation
bestFor: Visualising how far someone could travel by train from a European starting point within X hours (isochrone reachability).
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free interactive web map; no account or payment.
opsec: passive
opsecNote: You interact only with Chronotrains' own map/data — no query touches any subject and nothing is revealed to a third party. Purely analytical.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Independent project built on open rail-timetable data and featured in Bellingcat's toolkit; travel times are approximations from schedule data, not guarantees.
missingPersonsRelevance: low
coverage:
- eu
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Chrono Trains
- chronotrains isochrone map
tags:
- rail
- isochrone
- travel-time
- europe
source: bellingcat-toolkit
lastVerified: '2026-08-04'
enrichment: full
---

# Chronotrains

> An isochrone map of Europe's rail network: pick a station and a travel-time budget, and see the coloured envelope of everywhere you could reach by train within it.

## When to use
You have a European `geolocation` (a city/station) and want to reason about *movement*: given a person left from here with N hours of train travel, where could they plausibly be? Chronotrains draws the reachable area in bands (e.g. 1h, 2h, ... up to 5h+), which helps scope a search radius, sanity-check a claimed journey, or plan realistic travel windows. It's a reasoning aid over rail reachability, not a people-locator.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.chronotrains.com/en.
2. Click (or search) your starting station/city as the origin.
3. The map shades all destinations reachable within the time bands, colour-coded by duration; hover a place to read its exact rail time from the origin.
4. Adjust the origin to compare scenarios.
5. Pivot: the reachable set narrows or corroborates a location hypothesis; cross-check specific journeys against a live timetable for exact trains.

## Inputs → Outputs
- **In:** `geolocation` (European origin station/city)
- **Out:** `geolocation` set (rail-reachable destinations within the chosen time)
- **Empty/negative result looks like:** a sparse/blank envelope — the origin has poor rail links, or it's outside the covered network (coverage is Europe-centric); don't infer "unreachable" for non-rail travel.

## Gotchas & OpSec
- Coverage is European rail only; it ignores cars, flights, and buses, so it's a rail-specific reachability picture, not total mobility.
- Times are modelled from timetable data and assume good connections; real journeys with missed transfers take longer.
- OpSec: fully passive, no login.

## Overlaps ("do both")
- Complements flight-tracking and general mapping tools: Chronotrains covers the rail dimension of "how far could they get," while flight/road tools cover the others — combine them to bound a movement hypothesis across modes.

## Trust & verifiability
`trust: community` — an independent, Bellingcat-listed project built on public rail-timetable data; treat its times as good estimates and verify any specific critical journey against the operator's live schedule.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | chronotrains |
| category | transportation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
