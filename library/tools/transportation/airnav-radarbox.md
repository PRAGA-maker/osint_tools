---
id: airnav-radarbox
name: AirNav RadarBox
description: Use when you have a `vehicle-plate` (aircraft registration/callsign) or a `geolocation` and want live/historical flight tracking — returns aircraft position, route and identity.
url: https://www.airnavradar.com/
category: transportation
path:
- transportation
bestFor: Tracking a specific aircraft's live position and flight history, or seeing what is flying over a location.
selectorsIn:
- vehicle-plate
- geolocation
selectorsOut:
- geolocation
- vehicle-plate
status: live
pricing: freemium
costNote: Free live map and basic aircraft info; playback/history, more filters and alerts need a paid (Business/premium) subscription. A free account unlocks a bit more.
opsec: passive
opsecNote: You query RadarBox's aggregated ADS-B network, not the aircraft — passive. A logged-in account ties searches to an identity; use a sock-puppet account if you need history features while staying unattributable.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A major commercial flight-tracking network (formerly RadarBox24) fed by crowdsourced ADS-B receivers; positions are reliable where receiver coverage exists, sparse over oceans/remote areas.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- RadarBox
- RadarBox24
- radarbox24.com
- airnavradar.com
tags:
- Maps, Geolocation and Transport
- aviation
- flight-tracking
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# AirNav RadarBox

> A global crowdsourced flight tracker (formerly RadarBox24) — follow a specific aircraft live, replay its history, or see what's overhead a location.

## When to use
You have an aircraft identifier — a registration/tail number or callsign (`vehicle-plate`) — or a `geolocation`, and you want flight information. Track a known plane's live position and route, identify an aircraft seen in a photo/video by its markings, or watch traffic over a place of interest. Useful for confirming travel, geolocating an aircraft in imagery, or building a movement timeline (playback/history is the paid feature).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.airnavradar.com/.
2. Search by registration/tail number or callsign (`vehicle-plate`), or pan/zoom the live map to your `geolocation`.
3. Click an aircraft to see details: type, registration, operator, origin/destination, altitude, speed, and current position.
4. For past movements, use flight history/playback (subscription) to reconstruct where the aircraft has been.
5. Pivot: cross-check the registration against an aircraft registry to confirm owner/operator; corroborate a track against another tracker (`[[itamilradar]]` for military, or ADS-B Exchange for filter-resistant coverage).

## Inputs → Outputs
- **In:** `vehicle-plate` (registration/callsign) or `geolocation`
- **Out:** `geolocation` (live/historical position and route) and aircraft identity (`vehicle-plate`, type, operator)
- **Empty/negative result looks like:** no current track (aircraft on the ground, transponder off, or outside receiver coverage), or history gated behind a subscription. A missing live track over oceans/remote regions is a coverage gap, not proof the flight didn't happen.

## Gotchas & OpSec
- Human-in-the-loop: none; a free account is optional for extra detail.
- OpSec: **passive** — you query the tracking network, not the aircraft. A logged-in account is attributable; sock-puppet it if needed.
- Coverage depends on volunteer ADS-B receivers; some aircraft opt out of display, and certain sensitive flights are filtered — absence is not confirmation.

## Overlaps ("do both")
- Pairs with ADS-B Exchange (less filtering), aircraft registries, and `[[itamilradar]]` (military context) — RadarBox gives an easy live/historical view; the others fill coverage gaps and confirm the airframe's owner.

## Trust & verifiability
`trust: community` — a large commercial crowdsourced network. Positions are accurate within receiver coverage and cross-checkable against other trackers, but it is aggregated third-party data, not an official ATC feed.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | airnav-radarbox |
| category | transportation |
| selectorsIn → selectorsOut | vehicle-plate, geolocation → geolocation, vehicle-plate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
