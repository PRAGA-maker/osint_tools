---
id: direkht-ban-guru
name: Direkt bahn.guru (direct train map)
description: Use when you have a European (esp. German) rail station as a `geolocation`/`address` anchor and want to know every city reachable by a single direct train — returns a map of no-change destinations with travel times.
url: https://direkt.bahn.guru/
category: transportation
path:
- transportation
bestFor: Mapping which cities are reachable from a station by a single direct train, with journey times.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free, no account; a hobby project built on public Deutsche Bahn/HAFAS timetable data.
opsec: passive
opsecNote: You only type a public station name and the query hits a public timetable API — nothing about your subject is submitted. Standard VPN hygiene is enough.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Independent open project by a known German transit-data developer; accurate for DB/European long-distance rail, not an official operator site.
missingPersonsRelevance: low
coverage:
- de
- eu
auth: none
api: false
localInstall: false
registration: false
aliases:
- direkt.bahn.guru
- Direct train connections
tags:
- transport
- railway
- germany
- geolocation
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# Direkt bahn.guru

> Type a station and see, on a map, every city you can reach from it with no train change — plus the travel time to each.

## When to use
You have a subject anchored to a European (mostly German-speaking / DB-network) rail station — a last-known station, a ticket, a mentioned town — and you want a realistic picture of where a *single, no-change* train could have taken them. It answers "which places are one direct train away, and how long?" which helps bound a travel radius or prioritise destination cities in a missing-persons or movement-reconstruction context.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://direkt.bahn.guru/.
2. Type the origin station name; pick the matching station from the autocomplete.
3. Read the map: dots mark cities reachable by a direct train; colour encodes travel time (shorter = one end of the scale, longer = the other). Hover a dot for the destination and duration.
4. Note the reachable set and times — this is your candidate destination list for further checks.
5. Pivot: feed likely destination cities into local records, CCTV/witness canvassing, or a full journey planner (bahn.de) for exact schedules.

## Inputs → Outputs
- **In:** origin station (an `address`/`geolocation` anchor)
- **Out:** set of directly-reachable cities with travel times (`geolocation` list)
- **Empty/negative result looks like:** a small, sparse map (a minor station with few direct services) or no autocomplete match (station not in the DB/HAFAS dataset, or outside coverage). Sparse ≠ unreachable — it just means few *direct* trains; connections with changes are not shown.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: **passive** — only a public station name is sent to a public timetable API; nothing about your subject leaks.
- Scope is *direct* trains only — no multi-leg journeys — and coverage is strongest for Germany/DACH and long-distance European rail; regional/non-DB networks may be incomplete.

## Overlaps ("do both")
- Complements a full trip planner and mapping tools like `[[openstreetmap]]` — bahn.guru scopes the *direct-reach* radius fast; a planner then gives exact times and multi-change routes for the destinations you shortlist.

## Trust & verifiability
`trust: community` — an independent open project on public Deutsche Bahn/HAFAS data; reliable for direct-connection reachability, but confirm exact departures on the official bahn.de before acting on timing.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | direkht-ban-guru |
| category | transportation |
| selectorsIn → selectorsOut | geolocation, address → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
