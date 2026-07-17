---
id: flightaware
name: FlightAware
description: Use when you have a flight number, tail number (aircraft registration), or airport and want live and historical flight tracking — returns routes, times, and position history (geolocation).
url: https://flightaware.com/
category: transportation
path:
- transportation
bestFor: Tracking a specific aircraft's live position and past flights by tail number or flight number.
selectorsIn:
- vehicle-plate
status: live
pricing: freemium
costNote: Free live tracking and a limited window of flight history (typically recent months). Deeper historical archives and advanced features require a paid account.
opsec: passive
opsecNote: You query FlightAware's tracking data, not the aircraft or its owner; nothing is contacted. FlightAware logs your account activity — use a research account. Note privacy-blocked (LADD/BARR) aircraft won't show.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A leading flight-tracking service aggregating ADS-B, radar, and official feeds; data is authoritative for public (non-blocked) flights.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- Flight Aware
- flightaware.com
tags:
- aviation
- flight-tracking
source: osint4all
lastVerified: '2026-07-17'
enrichment: full
---

# FlightAware

> A flight-tracking platform — follow a specific aircraft by its tail number or a flight by its number, live and through recent history, to reconstruct where a plane (and by inference its occupants) has been.

## When to use
You have an aircraft **tail number** (registration, a `vehicle-plate`-equivalent for planes), a flight number, or an airport, and want to place an aircraft in time and space: is it airborne now and where, what route did it fly, what's its recent pattern of movements. Useful when a subject is linked to a specific aircraft (private/charter/company plane) or when corroborating travel claims — a tracked flight confirms an origin, destination, and timing. Relevance depends on the subject having an aircraft link.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://flightaware.com/ and search the **tail number** (e.g. N-, G-registration), flight number, or airport.
2. For a tail number, open the aircraft page: live position if airborne, plus a list of recent flights with dates, routes, and times.
3. Read the track log for departure/arrival airports and timing; note repeated routes (home base, frequent destinations).
4. Cross-reference the registration with the national aircraft registry (FAA/other) to link the tail number to an owner/operator.
5. Pivot: owner/operator from the registry → company/people records; airports + times → travel timeline; a home-base airport → geographic anchor.

## Inputs → Outputs
- **In:** aircraft tail number (`vehicle-plate`-equivalent), flight number, or airport
- **Out:** live position and historical flights — routes, airports, times, track (`geolocation`)
- **Empty/negative result looks like:** no data for a tail number — the aircraft hasn't flown recently in the tracked window, or it's **privacy-blocked** (FAA LADD / owner-requested block), which hides it from public tracking. Absence isn't proof it didn't fly.

## Gotchas & OpSec
- **Privacy blocks:** many private/sensitive aircraft opt out of public tracking (LADD/BARR); those simply won't appear here.
- Free history is a limited recent window; older flights need a paid tier or an alternative (ADS-B Exchange keeps unfiltered/blocked data).
- Owner identity comes from the **registry**, not FlightAware — link the tail number there.
- OpSec: **passive** — tracking-data query; the aircraft/owner isn't contacted.

## Overlaps ("do both")
- Pairs with FlightRadar24 and especially ADS-B Exchange (which shows some privacy-blocked aircraft FlightAware hides), plus the FAA/national aircraft registry to resolve tail number → owner.

## Trust & verifiability
`trust: trusted` — a major tracker aggregating ADS-B/radar/official feeds; public-flight data is authoritative, with the caveat that privacy-blocked aircraft are intentionally absent.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | flightaware |
| category | transportation |
| selectorsIn → selectorsOut | vehicle-plate → geolocation |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
