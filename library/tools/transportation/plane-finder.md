---
id: plane-finder
name: Plane Finder
description: Use when you have a flight number, aircraft registration, or `geolocation` and want live/historical ADS-B flight tracking — returns geolocation (aircraft position/route) leads.
url: https://planefinder.net
category: transportation
path:
- transportation
bestFor: Live and historical flight tracking by callsign, registration, route, or map area via ADS-B.
selectorsIn:
- name
- geolocation
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: Free to view live flights on the web map; playback/historical and advanced features may require a paid account. No login needed for basic live tracking.
opsec: passive
opsecNote: Passive — you view aggregated ADS-B data from Plane Finder's servers, not the aircraft. Note it aggregates volunteer receivers, so coverage is uneven and some military/blocked aircraft are hidden or delayed. Nothing you do reaches your subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Established commercial ADS-B tracker (Airnav Systems); positions come from crowd-sourced receivers, so accuracy and coverage vary by region and altitude.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- planefinder
- planefinder-army-live-flight-tracker
aliases:
- planefinder.net
- Plane Finder
tags:
- aviation
source: metaosint
lastVerified: '2026-07-29'
enrichment: full
---

# Plane Finder

> A live ADS-B flight tracker — put a flight number, tail number, or map area in and see the aircraft, its route, altitude and speed in near-real-time.

## When to use
You have a flight identifier (callsign/flight number), an aircraft registration (tail number), or a `geolocation`/airport, and you want to see what's flying: track a specific flight in real time, identify aircraft over an area, or reconstruct a route. Useful for verifying a claimed flight, spotting aircraft associated with a person/organization, or establishing that a subject's plane was airborne at a given time. Positions are crowd-sourced ADS-B, so treat coverage gaps as receiver gaps.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://planefinder.net (works in a plain browser; no login for live view).
2. Search a flight number or aircraft registration, or pan/zoom the live map to your area.
3. Click an aircraft for its data card: registration, type, operator, origin/destination, altitude, speed, and track.
4. For historical routes/playback, use the paid features if available; otherwise note current position and refresh.
5. Pivot: registration → aircraft ownership registries (FAA N-number, etc.); operator → `[[skyvector]]` for airport/route context; origin/destination → travel timeline.

## Inputs → Outputs
- **In:** flight number/callsign, aircraft registration (`name`), or `geolocation`/airport
- **Out:** live aircraft position, route, altitude/speed, registration, type, operator (`geolocation` + aircraft identity)
- **Empty/negative result looks like:** no aircraft shown for a flight/area — it may be outside ADS-B receiver coverage, not transmitting, on the ground, or a blocked/military airframe; absence is not proof it isn't flying.

## Gotchas & OpSec
- Coverage is uneven (best over populated/receiver-dense regions; poor over oceans/remote areas).
- Some aircraft are filtered/blocked or delayed (privacy programs, military).
- OpSec: passive — data comes from Plane Finder's aggregation, not the target.

## Overlaps ("do both")
- Cross-check with other trackers (Flightradar24, ADS-B Exchange) — receiver networks differ, so one may show a flight another misses. Pair with `[[skyvector]]` for airspace/airport context.

## Trust & verifiability
`trust: community` — established commercial tracker, but positions are crowd-sourced; verify a critical sighting against a second ADS-B network.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | plane-finder |
| category | transportation |
| selectorsIn → selectorsOut | name, geolocation → geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
