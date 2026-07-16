---
id: live-air-traffic-control
name: Live Air Traffic Control
description: Use when you have a `geolocation` (an airport) and want live and archived ATC radio audio — returns real-time and recorded controller/pilot communications for that field.
url: https://www.liveatc.net/
category: transportation
path:
- transportation
bestFor: Listening to live and archived air-traffic-control audio for a specific airport to corroborate aircraft movements and timing.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: Free live streams and a rolling archive on the website; a paid mobile app and premium archive access add convenience/history.
opsec: passive
opsecNote: You listen to publicly-broadcast, volunteer-fed radio feeds — entirely passive, no login, and nothing touches any subject. Note that intercepting/using ATC audio is legal in many countries but restricted in some (e.g. parts of Europe); know your jurisdiction.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running volunteer network of receiver feeds; audio is authentic but coverage and quality depend on local volunteers, and feeds can drop or lag.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- live-atc
aliases:
- LiveATC
- liveatc.net
tags:
- aviation
- atc-audio
- transportation
source: osint4all
lastVerified: '2026-07-16'
enrichment: full
---

# Live Air Traffic Control

> A volunteer-fed network of live and archived air-traffic-control audio — the ears to complement flight-tracking's eyes, letting you hear what controllers and pilots said at a given airport and time.

## When to use
You're building a timeline around aircraft movements at a specific airport (a `geolocation`/ICAO): confirming a departure/arrival, catching a callsign or tail number spoken on frequency, or corroborating an event flight-trackers only show as a blip. Combined with ADS-B trackers, ATC audio can tie a plane — and by extension a person of interest thought to be aboard — to a precise moment and field.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.liveatc.net/ and search/browse to the airport by ICAO/IATA code or name.
2. Pick a feed (Tower, Ground, Approach, etc.) and listen live, or use the **Archive** to pull recorded audio for a specific date/time block.
3. Note callsigns, tail numbers, runway/time details spoken on frequency.
4. Cross-reference a heard callsign with a flight-tracker (FlightAware/ADS-B Exchange) to resolve the aircraft and route.
5. Pivot: a tail number feeds aircraft-registration lookups (owner/operator); a confirmed flight ties to airport/timeline records.

## Inputs → Outputs
- **In:** `geolocation` — an airport (ICAO/IATA code or name)
- **Out:** live and archived ATC audio for that field (callsigns, tail numbers, timings) to place aircraft movements
- **Empty/negative result looks like:** no feed for that airport, or "feed offline" — many smaller fields have no volunteer receiver; a missing feed is a coverage gap, not proof of no traffic.

## Gotchas & OpSec
- Coverage is volunteer-driven — major airports are well-covered; regional/private strips often have no feed. Feeds also drop unpredictably.
- The rolling free archive is limited in depth; older audio may be gone or behind the paid tier — grab recordings promptly.
- Legality of listening to/using ATC audio varies by country — verify your jurisdiction before relying on it evidentially.

## Overlaps ("do both")
- Pairs with `[[live-atc]]` and with ADS-B flight-trackers (FlightAware, ADS-B Exchange) — trackers give the position/route, LiveATC gives the spoken callsign/context; use together to confirm an aircraft and timing.

## Trust & verifiability
`trust: community` — authentic volunteer-fed radio audio; the recordings are real, but coverage/quality depend on local receivers, so treat gaps as missing data and confirm callsigns against tracking data.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | live-air-traffic-control |
| category | transportation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
