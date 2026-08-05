---
id: flight-radar-24
name: Flight Radar 24
description: Use when you have a flight number, aircraft registration, or callsign and want its live/last-known position and route — returns geolocation plus aircraft identity.
url: https://flightradar24.com
category: transportation
path:
- transportation
bestFor: Tracking a specific aircraft in near-real-time and reconstructing its recent flights.
selectorsIn:
- name
- vin
selectorsOut:
- geolocation
- name
status: live
pricing: freemium
costNote: Live map, flight search, and current position are free without an account; extended playback, longer flight history, and some aircraft details require a paid subscription. A free login raises limits.
opsec: passive
opsecNote: Passive — you read a public ADS-B/MLAT aggregation portal, not the aircraft or its operator. Browsing never touches the target. Only a paid account or saved alerts create an identity trail; use a sock-puppet login if you subscribe.
humanInLoop: true
humanInLoopReason:
- rate-limit
bestInteractionPattern: web-manual
trust: trusted
trustNote: The most widely used consumer flight-tracking service, aggregating a global ADS-B/MLAT receiver network plus FAA/Eurocontrol feeds; position and identity come from the aircraft's own transponder, so they are authoritative when broadcasting.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- flightradar24-com
aliases:
- FlightRadar24
- FR24
- flightradar24.com
tags:
- aviation
- ads-b
- flight-tracking
source: metaosint
lastVerified: '2026-08-05'
enrichment: full
---

# Flight Radar 24

> The default live map of world air traffic: type a flight number, tail number, or callsign and see the aircraft's current position and route.

## When to use
You have a lead tying a person to a specific flight or aircraft — a flight number (e.g. `BA286`), an aircraft registration/tail (`vin`-style, e.g. `N123AB`), or a callsign — and you want to place it on a map, confirm it flew, or reconstruct its recent movements. Useful for corroborating a claimed itinerary, tracking a private/charter aircraft linked to a subject, or confirming an arrival/departure.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://flightradar24.com and use the search box.
2. Enter the flight number, aircraft registration, or callsign. You can also click any plane icon on the live map directly.
3. Read the flight panel:
   - **Current position**, altitude, speed, heading, and departure/arrival airports with times.
   - **Aircraft**: type, registration (`vin`), operator, and often a photo.
4. For history, the flight-history tab lists recent flights of that aircraft/route — recent entries are free, deeper playback is paywalled.
5. Pivot: the registration feeds aircraft-owner registries (e.g. FAA N-number lookup); airports and times corroborate a person's location timeline.

## Inputs → Outputs
- **In:** flight number, aircraft registration (`vin`), or callsign
- **Out:** `geolocation` (live position/route + timestamps), aircraft/operator identity (`name`)
- **Empty/negative result looks like:** no search hit (wrong/expired flight number), or an aircraft shown with no live track — it is on the ground, out of receiver coverage, or its transponder is off/limited (military and some private jets are blocked or filtered). Absence of a live track is not proof no flight occurred.

## Gotchas & OpSec
- Coverage depends on ground-receiver density; over oceans and remote areas, tracks rely on satellite/MLAT and can be sparse or delayed.
- Certain aircraft (military, sensitive private jets on block lists) are hidden or show limited data.
- Flight numbers are reused daily — make sure you have the right date.
- OpSec: browsing is passive and safe; a paid account/alerts create a trail — use a dedicated identity.

## Overlaps ("do both")
- Pairs with `[[flightradar24-com]]` and cross-checks against another tracker (ADS-B Exchange, which filters fewer aircraft) — coverage and block-list policy differ, so one may show a flight the other hides.

## Trust & verifiability
`trust: trusted` — a mature aggregator of the aircraft's own ADS-B/MLAT broadcasts plus official feeds; position and identity are authoritative while transponding, with coverage and block-lists as the main caveats, not data honesty.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | flight-radar-24 |
