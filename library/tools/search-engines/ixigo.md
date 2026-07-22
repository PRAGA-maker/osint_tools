---
id: ixigo
name: ixigo
description: Use when you have an Indian train/flight/PNR or `geolocation` context and want travel-status and route info — returns `geolocation` schedule/status context for India travel.
url: http://www.ixigo.com/
category: search-engines
path:
- search-engines
bestFor: Checking Indian train/flight schedules, live running status and PNR/route information.
selectorsIn:
- geolocation
- document-id
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: Free to search schedules, live train status and PNR status; bookings are the paid/commercial side.
opsec: passive
opsecNote: Schedule and status lookups are passive. A PNR status check requires the traveller's PNR number (which you must already lawfully hold) — do not attempt to obtain or brute-force someone else's PNR; that would be intrusive and likely unlawful.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A large, established Indian travel aggregator pulling from official rail/air feeds; schedule/status data is generally reliable, sourced from operators.
missingPersonsRelevance: medium
coverage:
- in
auth: none
api: false
localInstall: false
registration: false
aliases:
- ixigo.com
tags:
- travel
- india
- transport-schedules
source: toddington-resources
lastVerified: '2026-07-22'
enrichment: full
---

# ixigo

> A major Indian travel aggregator — most useful in OSINT as a free lookup for train/flight schedules, live running status and route feasibility across India.

## When to use
You are reasoning about movement within India: which trains/flights connect two places, whether a service was running/late on a given day, or how long a route takes. Given a `geolocation` pair (origin/destination) you can check schedules and live status to test the plausibility of a travel account or estimate arrival windows. If you *lawfully* hold a traveller's PNR (`document-id`), ixigo's PNR status shows the booking's current state and coach/berth — but never seek out a third party's PNR you have no right to.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.ixigo.com/ and choose Trains or Flights.
2. For route/timing: enter origin and destination (`geolocation`) and a date to see services, durations and schedules.
3. For live status: use "Live Train Status" with a train number to see current running position/delay.
4. For a held PNR: use "PNR Status" with the 10-digit PNR (`document-id`) to see booking status. Pivot: schedule/timing feeds timeline reconstruction and search-area reasoning.

## Inputs → Outputs
- **In:** `geolocation` (origin/destination), train/flight number, or a lawfully-held PNR (`document-id`)
- **Out:** `geolocation` context — schedules, durations, live running status, and (with a PNR) booking status
- **Empty/negative result looks like:** no service for the route/date, or "PNR not found/expired" — schedules aren't a person-locator, only a feasibility/timeline aid.

## Gotchas & OpSec
- India-only; a travel-logistics aid, not a people-search — it does not reveal who is travelling from a route query.
- PNR checks need a number you legitimately possess; do not attempt to obtain another person's PNR.
- Passive; no subject notification.

## Overlaps ("do both")
- Pairs with flight-tracking (FlightAware/Flightradar24) and mapping tools — ixigo covers Indian rail/air schedules specifically; those add live aircraft tracking and geography.

## Trust & verifiability
`trust: community` — a large established aggregator sourcing official operator feeds; schedule/status data is reliable, though it is logistics context, not identity data.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ixigo |
| category | search-engines |
| selectorsIn → selectorsOut | geolocation, document-id → geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
