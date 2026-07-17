---
id: flightradar24-com
name: Flightradar24.com
description: Use when you have an aircraft registration (tail number), flight number or airport and want live/recent position and routing — returns `geolocation`, operator `employer-org`.
url: https://www.flightradar24.com/
category: transportation
path:
- transportation
- air-traffic-records
bestFor: Tracking a specific aircraft's live position and recent movements by tail number or flight number.
selectorsIn:
- vehicle-plate
selectorsOut:
- geolocation
- employer-org
status: live
pricing: freemium
costNote: Free tier gives live tracking and 24h of history; Silver/Gold subscriptions unlock 90/365 days of playback and more filters. API access is paid.
opsec: passive
opsecNote: You read aggregated ADS-B/MLAT broadcast telemetry; nothing you do reaches the aircraft, crew or owner. Tracking a private/blocked tail may hit an ADS-B Exchange-style privacy filter (FR24 honours the FAA LADD/PIA block list).
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Long-established, widely-cited flight-tracking aggregator; used by newsrooms and Bellingcat. Coverage is best where ADS-B receiver density is high.
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
- flight-radar-24
aliases:
- FR24
- Flightradar24
tags:
- aviation
- flight-tracking
- ads-b
source: arf-seed
lastVerified: '2026-07-17'
enrichment: full
---

# Flightradar24.com

> The most widely-used live flight tracker — turns a tail number or flight number into a real-time map position, altitude, route and operator.

## When to use
You have an aircraft registration (tail number, e.g. `N123AB`), a flight number (e.g. `UA456`), or an airport code, and you want to know where that aircraft is now, where it is going, or where it has been in the last day. Useful for corroborating a subject's travel when you know a jet they use or a flight they were on.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.flightradar24.com/ and type the registration, flight number, or airport IATA/ICAO code into the search box.
2. Click the aircraft to see live `geolocation` (lat/long, altitude, speed, heading), the route (origin → destination), aircraft type, and the operator `employer-org`.
3. Use "Track this aircraft" to follow one tail across its day; the aircraft's data page also lists its recent flights (last 24h free).
4. For older history, use the in-app Playback (choose a date/time) — deeper history (90/365 days) needs a Silver/Gold subscription.
5. Pivot: an operator/registrant leads to FAA/registry records; a destination airport plus arrival time narrows a physical location window.

## Inputs → Outputs
- **In:** aircraft registration (`vehicle-plate`), flight number, or airport code
- **Out:** live `geolocation` + altitude/speed/heading, route, aircraft type, operator `employer-org`, recent flight list
- **Empty/negative result looks like:** no active flight for that registration (aircraft on the ground/transponder off), or a "blocked"/limited entry if the owner is on an FAA privacy (LADD/PIA) list — absence is not proof the aircraft did not fly.

## Gotchas & OpSec
- Human-in-the-loop: none; free browsing needs no account.
- OpSec: **passive** — you consume broadcast telemetry aggregated by FR24's receiver network; nothing reaches the target.
- Coverage gaps over oceans and low-receiver regions are filled by MLAT/satellite but can be sparse; a missing track can just mean no receiver was in range.
- Blocked/privacy tails are deliberately hidden; cross-check ADS-B Exchange (which ignores block lists) if a tail is suppressed here.

## Overlaps ("do both")
- Pairs with `[[flight-radar-24]]` — same service, alternate entry; use whichever record page is populated.
- Cross-check against an unfiltered ADS-B source when a tail number appears blocked, since FR24 honours privacy requests that others do not.

## Trust & verifiability
`trust: trusted` — a mature, heavily-used aggregator whose data underpins professional investigations; the main caveat is receiver coverage, not data integrity.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | flightradar24-com |
| category | transportation |
| selectorsIn → selectorsOut | vehicle-plate → geolocation, employer-org |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
