---
id: one-network
name: one.network
description: Use when you have a `geolocation`/`address` and a date and want the roadworks, closures, and traffic disruptions there — returns a live/planned map of road events that can explain access, routes, or delays.
url: https://one.network/
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Checking road closures, roadworks, and traffic disruptions affecting a place and time (route feasibility, why someone was delayed or diverted).
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Public map is free to view (Causeway one.network, formerly Elgin/roadworks.org). The professional planning/permit tools behind it are paid, but the disruption map itself is open.
opsec: passive
opsecNote: You browse a public roadworks map by area/date; nothing about your subject is disclosed. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Causeway (one.network is the successor to Elgin's roadworks.org); it aggregates official road-authority permit and works data, so events are authority-sourced.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- one.network
- Elgin roadworks
- roadworks.org
tags:
- mapsandlocationsites
- Maps & Location Related Sites
- traffic
- roadworks
source: uk-osint
lastVerified: '2026-07-19'
enrichment: full
---

# one.network

> A live and planned map of roadworks, closures, and traffic disruption — context for whether a route was passable at a given place and time.

## When to use
You have a `geolocation`/`address` and a date, and you need to know the road situation there: active roadworks, full/partial closures, diversions, events, and traffic disruption. This helps assess whether a claimed route was feasible, explain why a subject or vehicle was delayed or diverted, narrow which roads were usable during a search window, or corroborate a timeline against a closure. Coverage is strongest in the UK and other regions where road authorities publish permit data.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://one.network/ and navigate/search to the area or `address`.
2. Set the date/time window — the map shows current, planned, and (where available) recent works and closures.
3. Read the event markers: type (works, closure, event), dates, responsible authority/contractor, and expected impact.
4. Note the coverage caveat — completeness depends on the local authority feeding data; sparse areas aren't necessarily clear.
5. Pivot: a closure/diversion reshapes a route hypothesis you then check against CCTV/ANPR locations or witness statements.

## Inputs → Outputs
- **In:** `geolocation` / `address` + date window
- **Out:** `geolocation`-anchored road events — roadworks, closures, diversions, traffic disruption with dates and responsible party
- **Empty/negative result looks like:** no events for an area/date can mean genuinely clear roads *or* that the local authority doesn't publish to the platform — absence isn't proof a road was open.

## Gotchas & OpSec
- Human-in-the-loop: none for the public map.
- Data completeness varies by jurisdiction and authority; treat gaps as "not reported here," and confirm a critical closure with the local authority.
- Historical depth is limited compared with live/planned data — the further back the date, the thinner the record.

## Overlaps ("do both")
- Pairs with a live traffic/map service and with `[[inciweb]]`-style incident maps — one.network specializes in road events and permits; a general map confirms the geography and a fire/incident map explains non-roadworks closures.

## Trust & verifiability
`trust: trusted` — Causeway's one.network aggregates official road-authority permit and works data, so events are authority-sourced; the caveat is coverage completeness, not accuracy of the events shown.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | one-network |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation, address → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
