---
id: ads-b-historical-flight-viewer
name: ADS-B Historical Flight Viewer (ADSBExchange)
description: Use when you have an aircraft (tail/registration, hex, or callsign) and want to replay its past flights — returns geolocation tracks and timing from ADSBExchange's historical ADS-B data.
url: https://flight-data.adsbexchange.com
category: transportation
path:
- transportation
bestFor: Replaying historical aircraft movements on ADSBExchange to reconstruct where a plane (and by inference its occupants) went and when.
selectorsIn:
- vehicle-plate
- name
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: The globe replay (history back to ~2020) is free to view with no account; bulk historical data files and ad-free access are paid/feeder-gated.
opsec: passive
opsecNote: You view recorded, publicly-broadcast ADS-B positions — nothing is sent to the aircraft or its owner, so it is passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: ADSBExchange is a well-known unfiltered crowd-sourced ADS-B network (it does not honor blocking lists), making it a primary reference for flight tracking.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- ads-b-exchange
- ads-b-exchange-radar-view
- flight-tracker
aliases:
- ADSBExchange replay
- ADS-B Exchange historical
tags:
- aviation
- flight-tracking
source: metaosint
lastVerified: '2026-07-23'
enrichment: full
---

# ADS-B Historical Flight Viewer (ADSBExchange)

> ADSBExchange's historical replay — reconstruct an aircraft's past routes and timings from crowd-sourced ADS-B, including flights other trackers hide.

## When to use
You have identified an aircraft — by `vehicle-plate` (tail/registration), ICAO hex, or callsign — often linked to a subject (a private jet, a person of interest's known plane) and want to reconstruct **where it went and when** in the past. Because ADSBExchange is unfiltered (it doesn't honor blocking programs), it frequently shows flights FlightAware/FR24 suppress. Movements can place a plane (and plausibly its occupants) at a `geolocation` and time.

## How to use it (`bestInteractionPattern`: web-manual)
1. Start at the ADSBExchange globe replay: `https://globe.adsbexchange.com/?replay` (the free viewer); the `flight-data.adsbexchange.com` host serves the underlying historical data files.
2. Search the aircraft by registration/tail, ICAO hex, or callsign; set the replay date/time window (history reaches back to ~2020).
3. Play the track to read the route, altitudes, and airports; note departure/arrival `geolocation`s and timestamps.
4. For rigorous/bulk analysis, pull the monthly historical data (first-of-month sets are free; full history is paid).
5. Pivot: a tail number → an aircraft registry (FAA N-number/ICAO) for ownership; airport stops → local records; live status → the standard radar view.

## Inputs → Outputs
- **In:** an aircraft identifier — `vehicle-plate` (tail/registration), ICAO hex, or callsign (tied to a subject `name` via ownership).
- **Out:** historical flight tracks — `geolocation` waypoints, airports, altitudes, and timestamps.
- **Empty/negative result looks like:** no track for the chosen aircraft/window — the plane didn't fly, flew outside ADS-B coverage (ocean/low altitude), or had its transponder off; a gap isn't proof it stayed put.

## Gotchas & OpSec
- Coverage depends on volunteer receivers — remote/oceanic legs can be missing even for a real flight.
- ADS-B identifies the airframe, not who was aboard — occupancy is an inference to corroborate, not a fact.
- Free replay is view-only for recent history; deep/bulk historical analysis pushes you to the paid data products.

## Overlaps ("do both")
- Pairs with [[live-atc]] and aircraft registries: ADSBExchange gives the recorded track, ATC audio can supply a callsign/tail when the transponder is off, and a registry attributes the airframe to an owner.

## Trust & verifiability
`trust: community` — crowd-sourced but widely trusted precisely because it's unfiltered; individual tracks are reproducible in the replay and cross-checkable against other ADS-B networks.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ads-b-historical-flight-viewer |
