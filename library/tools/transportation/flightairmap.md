---
id: flightairmap
name: FlightAirMap
description: Use when you have an aircraft/vessel `vehicle-plate` registration or callsign and want live position and history — returns `geolocation` track and route.
url: https://www.flightairmap.com/
category: transportation
path:
- transportation
bestFor: Live 2D/3D map of aircraft, ships and trackers with searchable history by registration, airline or airport.
selectorsIn:
- vehicle-plate
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free and open source (AGPLv3). The public demo site is free to browse; you can also self-host your own instance from ADS-B/AIS feeds at no cost.
opsec: passive
opsecNote: Browsing tracks is passive and reveals nothing to the aircraft/vessel operator. If you self-host from your own receiver, that receiver is local and offline-capable. Standard web hygiene for the public site.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Established open-source tracking platform (Ysurac/FlightAirMap); data quality depends on the ADS-B/AIS feeds behind a given instance.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- flight air map
- Ysurac FlightAirMap
tags:
- flight-tracking
- ship-tracking
- ads-b
- ais
source: osint4all
lastVerified: '2026-07-17'
enrichment: full
---

# FlightAirMap

> An open-source live map of aircraft, ships and trackers fed by ADS-B/AIS/APRS — search by registration, callsign, airline, airport or vessel and see current position, route and statistics.

## When to use
You have an aircraft registration or a vessel identifier (treated here as a `vehicle-plate`), or a callsign/flight number, and you want its live `geolocation`, its route, and historical movement statistics. Useful for placing a known aircraft/boat associated with a person or organisation, confirming a claimed journey, or watching activity around an airport or port. Because it is self-hostable, it is also handy when you run your own receiver and want a private tracker not tied to a commercial service.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the public demo at https://www.flightairmap.com/ (or your own self-hosted instance).
2. Use the search to look up the aircraft/vessel by registration (`vehicle-plate`), callsign, airline, airport or vessel name.
3. Read the live map: the selected craft shows current `geolocation`, heading, altitude/speed and its recent track; the detail page adds route and historical stats.
4. Note the data source — a given instance only "sees" what its feeds cover; the public demo's coverage differs from a self-hosted receiver's local range.
5. Pivot: cross-check the registration against an aircraft/vessel registry to tie the tail number/hull to an owner.

## Inputs → Outputs
- **In:** `vehicle-plate` (aircraft registration / vessel identifier) or callsign
- **Out:** `geolocation` (live position + track), route and movement statistics
- **Empty/negative result looks like:** no current track — the craft is not transmitting, is out of the instance's receiver range, or has ADS-B/AIS disabled (common for privacy-blocked or military craft). Absence is not proof it is grounded.

## Gotchas & OpSec
- OpSec: **passive** — you observe broadcast signals; the operator learns nothing.
- Coverage is feed-dependent: gaps over oceans, remote regions and where no receiver listens. The public demo is not global-complete.
- Privacy-blocked tail numbers and non-transmitting craft simply do not appear.

## Overlaps ("do both")
- Pairs with commercial flight/ship trackers and aircraft/vessel registries — trackers give live position, registries tie the identifier to an owner.

## Trust & verifiability
`trust: community` — mature open-source software; positions are only as good as the ADS-B/AIS feeds behind the instance, so corroborate with a second tracker for anything decisive.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | flightairmap |
| category | transportation |
| selectorsIn → selectorsOut | vehicle-plate → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
