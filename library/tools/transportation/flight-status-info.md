---
id: flight-status-info
name: Flight Status Info
description: Use when you have a flight number, airline, or route and want live status and schedules — returns real-time flight status, aircraft/gate details, and airport/airline timetables.
url: https://flight-status.info/
category: transportation
path:
- transportation
bestFor: Checking a flight's live status and browsing airport/airline schedules without an airline app.
selectorsIn:
- name
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free to use; no account required.
opsec: passive
opsecNote: Passive — you read a public flight-status aggregator; nothing reaches the passenger or airline. Browsing is safe; use a clean session only if the fact that you're tracking a particular flight is itself sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A free aggregator pulling from airline and air-traffic feeds across 650+ carriers; status is only as good as those upstream feeds, so treat it as strong but not official, and confirm critical facts with the airline.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- flight-status.info
- flight-status.com
tags:
- Maps, Geolocation and Transport
- Aviation
- flight-tracking
source: cyb-detective
lastVerified: '2026-08-05'
enrichment: full
---

# Flight Status Info

> A no-frills flight-status aggregator: look up a flight by number, browse an airport's or airline's schedule, and see live status without juggling multiple carrier apps.

## When to use
You want to confirm whether a specific flight ran, is delayed, or is airborne — useful for corroborating a subject's travel claim or itinerary when you have a flight number, or the airline + route + date. It also lists airports by city and shows airport/airline timetables, so you can work backward from "they flew from X around then" to candidate flights.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://flight-status.info/ (redirects to flight-status.com).
2. Search the fastest way you can — by flight number, or by airline + route, or by departure/arrival airport + date.
3. Read the result: current status, scheduled vs actual departure/arrival times, gate/terminal, aircraft type, and a live GPS position for in-flight aircraft (`geolocation`).
4. Use the "by airport" / "by airline" and "airports by city" views to enumerate candidate flights when you only know the city and rough time.
5. Pivot: a confirmed flight's times and airports anchor a location timeline; the aircraft/route can be cross-checked on a dedicated tracker.

## Inputs → Outputs
- **In:** flight number, airline + route, or airport + date (a `name`/identifier)
- **Out:** live flight status, times, gate/aircraft details, and in-flight `geolocation`
- **Empty/negative result looks like:** no match for a flight number (wrong number or wrong date — numbers recur daily), or a listed flight with no live position (on the ground, or the feed lacks tracking). Absence isn't proof the trip didn't happen; confirm with the airline for anything critical.

## Gotchas & OpSec
- Data comes from upstream airline/ATC feeds and can lag or be incomplete; for decisions that matter, verify with the operating airline.
- Flight numbers are reused daily and codeshares muddy things — pin the exact date and operating carrier.
- Coverage is broad but not universal (charters, some regionals may be missing).
- OpSec: passive and safe.

## Overlaps ("do both")
- Cross-check live positions against `[[flight-radar-24]]` (richer ADS-B map/history) — this tool is quicker for status/schedule lookups, while FlightRadar24 gives the fuller tracking picture; using both confirms a flight and its path.

## Trust & verifiability
`trust: community` — a handy free aggregator; status reflects upstream feeds rather than the airline's own system of record, so treat it as reliable-but-unofficial and confirm anything decisive directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | flight-status-info |
