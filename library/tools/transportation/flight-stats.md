---
id: flight-stats
name: FlightStats
description: Use when you have a flight number, route or airport and want status/history — returns real-time and historical flight data to confirm a person's travel timing and route.
url: https://www.flightstats.com/
category: transportation
path:
- transportation
bestFor: Checking real-time or historical flight status by flight number, route or airport to corroborate travel.
selectorsIn:
- name
- geolocation
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: Freemium — live flight tracking, airport conditions and delays are free; flight alerts and deeper historical data need a paid tier (from ~$2.99). Operated by Cirium (RELX).
opsec: passive
opsecNote: Anonymous flight/airport lookups against a public tracker; no person is queried directly and no one is notified. This corroborates a flight, not a named passenger — it never reveals who was aboard.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A long-established commercial aviation-data service (now Cirium/RELX); flight status and historical on-time data are authoritative operational records.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- FlightStats
- Cirium FlightStats
tags:
- toddington
- curated-directory
- specialty-search
- aviation
- flight-tracking
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# FlightStats

> A veteran flight-tracking service (now Cirium) — look up any flight's status, route and history, plus airport conditions, to corroborate a travel claim.

## When to use
A subject's movements involve a flight — a claimed trip, a departure/arrival window, a mentioned flight number or route — and you want to check whether that flight actually operated, when, and between where. FlightStats gives real-time status and historical records for flights and airports worldwide. It can confirm a flight existed on a date, establish realistic arrival/departure times for a timeline, and characterize an airport's delays. It corroborates *the flight*, never the passenger manifest — use it to test the plausibility of a travel account, not to identify who flew.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.flightstats.com/ and choose Flight Tracker (by flight number) or the airport tools.
2. Enter the flight number + date, or the route/airport, to get status: scheduled vs actual times, gate, terminal, delays.
3. Use Historical Flight Status to confirm a past flight and its actual timing.
4. Cross-check with another tracker (FlightAware/Flightradar24) for coverage and live position.
5. Pivot: confirmed flight times anchor a `geolocation`/timeline; the origin/destination airports frame where a subject was.

## Inputs → Outputs
- **In:** flight number / route / airport (+ date), tied to a subject's claimed travel
- **Out:** flight status and history (times, gates, delays) → a corroborated travel `geolocation`/timeline
- **Empty/negative result looks like:** no flight found for that number/date — the flight didn't operate as claimed, the number is wrong, or it's outside coverage; historical depth may need a paid tier.

## Gotchas & OpSec
- Human-in-the-loop: none; alerts and deep history are paywalled, but live status is free.
- It confirms flights, NOT passengers — never infer who was aboard from this.
- Cross-check a second tracker; a single source can miss codeshares or reschedules.

## Overlaps ("do both")
- Pairs with FlightAware / Flightradar24 — those add live positions and broader ADS-B coverage; FlightStats adds strong historical on-time records.

## Trust & verifiability
`trust: trusted` — an established Cirium/RELX aviation-data service; flight and airport records are authoritative operational data.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | flight-stats |
| category | transportation |
| selectorsIn → selectorsOut | name, geolocation → geolocation |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
