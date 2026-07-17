---
id: ads-b-exchange
name: ADS-B Exchange
description: Use when you have an aircraft identifier or a `geolocation`/time and want unfiltered live or historical flight tracks — returns positions, altitude, and traceable flight-path history.
url: https://www.adsbexchange.com/
category: transportation
path:
- transportation
- air-traffic-records
bestFor: Unfiltered aircraft tracking and historical flight-pattern analysis, including flights other trackers hide.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: The live globe map at globe.adsbexchange.com is free. A Community/RapidAPI developer API and full historical archives require registration and/or paid tiers.
opsec: passive
opsecNote: You are reading broadcast telemetry aggregated from a volunteer receiver network, not contacting any aircraft or person — fully passive. Nothing you look up is exposed to the subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Independent, community-fed network of 25,000+ receivers; well-regarded in journalism/OSINT precisely because, unlike FlightAware/Flightradar24, it does not honour block-list requests.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- ads-b-exchange-radar-view
- ads-b-historical-flight-viewer
- flight-tracker
aliases:
- ADSBexchange
- adsbx
tags:
- aviation
- flight-tracking
- geolocation
source: arf-seed
lastVerified: '2026-07-17'
enrichment: full
---

# ADS-B Exchange

> The largest *unfiltered* flight-tracking network — it shows aircraft (private jets, government, LADD-blocked tails) that commercial trackers deliberately hide.

## When to use
You want to know where an aircraft has been or is now: a known tail/hex tied to a person or organization, or "what was overhead at this place and time." Useful for corroborating a subject's travel, confirming an aircraft was near a location during an incident, or reconstructing a flight after the fact. Its edge over other trackers is that it does not suppress blocked or sensitive aircraft.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the live map at https://globe.adsbexchange.com/.
2. Locate the aircraft:
   - Click a target on the map, or
   - Search by ICAO hex code, registration/tail number, callsign, or squawk, or
   - Pan/zoom to a `geolocation` to see everything currently overhead.
3. Read the readout: live position, altitude, speed, heading, and a traceable recent track. Click through for the flight path.
4. For past flights, use the historical/heatmap views (or the API/archives — registration/paid) to pull tracks for a specific date; correlate the path against your timeline.
5. Pivot: a registration → an owner via a civil aircraft registry (e.g. FAA registry); a repeated route → home base / pattern of life.

## Inputs → Outputs
- **In:** aircraft hex/registration/callsign, or a `geolocation` + time window
- **Out:** live position, altitude, speed, heading, and historical `geolocation` track data (flight path over time)
- **Empty/negative result looks like:** no aircraft matching the identifier, or a gap in the track — ADS-B coverage depends on nearby receivers, so remote/ocean/low-altitude segments can be missing. A gap is a coverage hole, not proof the aircraft was grounded.

## Gotchas & OpSec
- Fully passive — you read broadcast data; nobody is alerted.
- Coverage is receiver-dependent: dense over populated areas, sparse over oceans and remote terrain. Missing track ≠ aircraft didn't fly.
- Deep historical data and programmatic access sit behind registration/paid tiers; the live map and recent history are free.
- Owner identity is NOT here — ADS-B gives you the tail; you resolve the owner via a separate aircraft registry.

## Overlaps ("do both")
- Pairs with `[[ads-b-exchange-radar-view]]` and `[[ads-b-historical-flight-viewer]]` (same data, different views) and `[[flight-tracker]]`. Do both: cross-check a tail against a commercial tracker — if ADS-B Exchange shows it but the others don't, that itself is a signal the aircraft is block-listed.

## Trust & verifiability
`trust: community` — data comes from a large volunteer receiver network, not an official source, so individual position points can carry receiver error; the aggregate track is highly reliable and the platform is a mainstay of open-source aviation investigation.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ads-b-exchange |
| category | transportation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
