---
id: marine-traffic-geolocation-search
name: MarineTraffic
description: Use when you have a vessel name, IMO or MMSI (`vehicle-plate`) and want its live position and history — returns `geolocation` track, port calls and vessel details.
url: http://marinetraffic.com/ais
category: transportation
path:
- transportation
bestFor: Live and historical AIS tracking of ships worldwide by name, IMO or MMSI on a map.
selectorsIn:
- vehicle-plate
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: The live map and basic vessel lookup are free (registration unlocks more). Historical tracks, voyage history and the API are paid.
opsec: passive
opsecNote: You observe AIS broadcasts aggregated by MarineTraffic; the vessel/crew are not contacted. A free account ties queries to you — use a research login. Deep history is paywalled, not blocked-with-a-notification.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: Long-established, widely-cited AIS aggregator; live positions come from a large receiver network and are broadly reliable.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- flightairmap
aliases:
- Marine Traffic
- marinetraffic.com
tags:
- toddington
- curated-directory
- ship-tracking
- ais
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# MarineTraffic

> The best-known live ship-tracking site: give it a vessel's name, IMO or MMSI and it plots the ship's current `geolocation`, recent track, destination and port calls from crowd-sourced AIS.

## When to use
A case ties a person to a specific vessel (owner, crew, passenger, cargo) or you need to confirm a ship's whereabouts or route. MarineTraffic turns a vessel identifier (`vehicle-plate`: name / IMO number / MMSI) into live position, speed, heading, declared destination, and — with a paid tier — historical voyages and port calls. Use it to place a boat at a time/place, corroborate a claimed journey, or watch activity around a port.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to marinetraffic.com and search the vessel by name, IMO or MMSI.
2. Open the vessel page: current `geolocation`, course/speed, flag, type, and its live map marker.
3. Read the details panel for owner/operator hints, last/next port and ETA; a free account raises limits.
4. For historical track, voyage history or bulk lookups, expect a paywall (or the paid API).
5. Pivot: cross-check the IMO against vessel registries and sanctions/ownership databases to tie the hull to a company or person.

## Inputs → Outputs
- **In:** `vehicle-plate` (vessel name, IMO, or MMSI)
- **Out:** `geolocation` (live position + recent track), destination/ETA, vessel particulars
- **Empty/negative result looks like:** no live position — the ship has AIS off (going dark), is out of receiver range (mid-ocean), or the identifier is wrong. Absence is not proof the vessel is in port.

## Gotchas & OpSec
- Human-in-the-loop: much history/detail sits behind a partial paywall; the live map is the free part.
- OpSec: **passive** — AIS is broadcast; the vessel isn't alerted. Keep queries on a research account.
- AIS can be spoofed or switched off (common for illicit shipping); treat a single position as a claim, corroborate over time.

## Overlaps ("do both")
- Pairs with `[[flightairmap]]` (aircraft/vessel open-source tracker) and other AIS sites (VesselFinder) — coverage differs by receiver network, so check more than one.

## Trust & verifiability
`trust: trusted` — a mature, widely-used aggregator; live positions are generally reliable but spoofable, so verify decisive claims against a second AIS source and the vessel registry.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | marine-traffic-geolocation-search |
| category | transportation |
| selectorsIn → selectorsOut | vehicle-plate → geolocation |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
