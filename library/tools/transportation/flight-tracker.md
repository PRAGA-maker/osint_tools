---
id: flight-tracker
name: Flight Tracker (ADS-B Exchange)
description: Use when you have an aircraft registration/callsign or a location and want live flight positions — returns real-time aircraft geolocation and identity.
url: https://global.adsbexchange.com/virtualradar/desktop.html
category: transportation
path:
- transportation
bestFor: Live, unfiltered real-time tracking of aircraft by registration, callsign, or map area.
selectorsIn:
- name
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: The live map is free to browse with no account. ADS-B Exchange sells historical data / API access; real-time map viewing is open.
opsec: passive
opsecNote: You read a crowd-sourced feed of aircraft transponder broadcasts — nothing you do touches the aircraft or its operator, and there's no signal back to any subject. Only ADS-B Exchange sees your browsing; use a VPN if you want to keep even that private.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: ADS-B Exchange is the best-known *unfiltered* flight tracker — it does not honour the block lists that hide private/government jets on FlightRadar24/FlightAware, so its coverage of sensitive aircraft is stronger. Data is community-fed, so gaps exist where no receiver is nearby.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- ads-b-exchange
- ads-b-exchange-radar-view
- ads-b-historical-flight-viewer
aliases:
- ADS-B Exchange
- ADSB Exchange VirtualRadar
tags:
- aviation
- flight-tracking
- geolocation
source: metaosint
lastVerified: '2026-07-23'
enrichment: full
---

# Flight Tracker (ADS-B Exchange)

> ADS-B Exchange's live radar — real-time aircraft positions from a global network of volunteer receivers, and crucially *unfiltered*: it shows private and government jets that other trackers hide.

## When to use
You have an aircraft registration (tail number), an ICAO hex, a callsign, or a `geolocation` (a place you want to see overhead traffic for) and need to know where an aircraft is right now — or watch an area for movements. Its selling point for investigations is that it doesn't obey the privacy block lists FlightRadar24/FlightAware use, so it can track jets those tools suppress.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://global.adsbexchange.com/virtualradar/desktop.html (or the main globe view at adsbexchange.com).
2. Search by aircraft registration, ICAO hex, or callsign; or pan/zoom the map to a `geolocation` of interest.
3. Click an aircraft to see its current position, altitude, speed, heading, registration, and type.
4. Note gaps: coverage depends on nearby volunteer receivers — over oceans/remote areas an aircraft may drop off the map without having landed.
5. Pivot: a registration feeds aircraft-ownership/registry lookups (FAA/CAA registries); a live position corroborates or refutes a location/time claim.

## Inputs → Outputs
- **In:** aircraft registration / ICAO hex / callsign (`name`), or a `geolocation` / map area
- **Out:** real-time aircraft `geolocation` (position, altitude, heading) plus identity (registration, type)
- **Empty/negative result looks like:** no aircraft found / it vanishes from the map — either it isn't currently airborne and transmitting ADS-B, or no receiver is in range. Absence ≠ grounded.

## Gotchas & OpSec
- Coverage is receiver-dependent: sparse over oceans and remote regions; an aircraft can disappear mid-flight simply for lack of a nearby receiver.
- Shows only aircraft broadcasting ADS-B; some military/older aircraft don't, or transmit intermittently.
- OpSec: **passive** — reading transponder broadcasts; nothing reaches the aircraft or operator.

## Overlaps ("do both")
- Complements the related ADS-B Exchange views and historical viewer (`[[ads-b-historical-flight-viewer]]`) — use the live map for now, the historical tools for past flights. Cross-check FlightRadar24 too, but remember ADS-B Exchange is the one that won't hide blocked aircraft.

## Trust & verifiability
`trust: trusted` — a respected, community-fed, unfiltered tracker. Positions are as accurate as the receiving network; treat coverage gaps as missing data, not as evidence an aircraft landed or disappeared.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | flight-tracker |
| category | transportation |
| selectorsIn → selectorsOut | name, geolocation → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
