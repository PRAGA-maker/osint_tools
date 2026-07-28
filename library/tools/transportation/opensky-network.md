---
id: opensky-network
name: OpenSky Network
description: Use when you have an aircraft `vehicle-plate` (tail/ICAO24) or callsign and want live and historical ADS-B positions — returns geolocation tracks, including data other trackers hide.
url: https://opensky-network.org/
category: transportation
path:
- transportation
bestFor: Live and historical aircraft position tracking from raw ADS-B, including flights filtered out of commercial trackers.
selectorsIn:
- vehicle-plate
- name
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: Free for research/non-commercial use. Live REST/state API is free (anonymous or with a free account for higher limits); the deeper historical archive requires a free academic/research account. No paid tier needed for typical OSINT.
opsec: passive
opsecNote: You query OpenSky's servers, never the aircraft, so tracking is passive and invisible to the target. Requests are tied to your account/IP and rate-limited; use a research account you're comfortable being associated with the query.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A non-profit, academia-backed community ADS-B network (used widely in aviation research and journalism). Data is crowd-sourced receiver feeds — coverage gaps exist, but what's reported is raw sensor data, not editorialised.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
invitationOnly: false
relatedTools:
- ads-b-exchange-radar-view
- flight-radar-24
- airnav-radarbox
tags:
- bellingcat-toolkit
- transport
- aviation
- adsb
source: bellingcat-toolkit
lastVerified: '2026-07-28'
enrichment: full
---

# OpenSky Network

> A non-profit, community-fed ADS-B network with an open API and a deep historical archive — the researcher's flight tracker, and one that doesn't honour the block-lists commercial sites apply.

## When to use
You have an aircraft identifier — tail number/registration (`vehicle-plate`), ICAO24 hex, or callsign — and need where it is now or where it has been. Especially valuable when a subject aircraft is hidden on FlightRadar24/RadarBox (OpenSky doesn't apply owner block-lists), or when you need raw historical tracks for analysis rather than a pretty live map.

## How to use it (`bestInteractionPattern`: web-manual / api)
1. Register a free account (needed for the API and historical data).
2. Live check: use the map/Network Explorer, or the REST state API (`/states/all` filtered by ICAO24) to get current position, altitude, and callsign.
3. Historical: query the flights/tracks endpoints (or the research data archive) by ICAO24 and time window to reconstruct past movements.
4. Read outputs: latitude/longitude, altitude, velocity, and timestamps — a `geolocation` trail.
5. Pivot: an ICAO24/registration → owner lookup in a national aircraft registry; a track ending at an airport → ground research; cross-check with `[[ads-b-exchange-radar-view]]` for coverage gaps.

## Inputs → Outputs
- **In:** `vehicle-plate` (registration), ICAO24 hex, or callsign (`name`) + optional time window
- **Out:** `geolocation` — live and historical position/altitude/velocity tracks
- **Empty/negative result looks like:** no state vectors returned — the aircraft may be on the ground, out of receiver coverage (oceans, low altitude, sparse regions), or not ADS-B-equipped. Absence is a coverage gap, not proof it isn't flying.

## Gotchas & OpSec
- Coverage depends on volunteer receivers — expect gaps over oceans, remote areas, and at low altitude.
- Free API is rate-limited; the full historical archive is gated behind a research/academic account and its terms.
- Passive and target-invisible, but tie queries to a research identity you're fine attaching to the case.

## Overlaps ("do both")
- Pairs with `[[ads-b-exchange-radar-view]]` — both are "unfiltered" trackers that show blocked aircraft; run both to cover receiver gaps.
- Cross-reference `[[flight-radar-24]]`/`[[airnav-radarbox]]` for richer flight metadata (routes, schedules) that OpenSky's raw feed lacks.

## Trust & verifiability
`trust: trusted` — an established non-profit research network. The data is raw ADS-B (reliable when present), and its no-block-list policy makes it authoritative for aircraft other trackers suppress. Confirm identity via the aircraft registry before attributing a track to an owner.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | opensky-network |
| category | transportation |
| selectorsIn → selectorsOut | vehicle-plate, name → geolocation |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
