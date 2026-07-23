---
id: planefinder
name: PlaneFinder
description: Use when you have a flight number, callsign, or aircraft registration and want its live/historical position — returns real-time `geolocation`, route, and altitude.
url: https://planefinder.net/
category: transportation
path:
- transportation
bestFor: Tracking a specific aircraft's live position and recent flight history on a world map.
selectorsIn:
- vehicle-plate
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: Free live map and basic tracking in-browser; deeper playback/history and ad-free use sit behind a paid subscription/app tier.
opsec: passive
opsecNote: "You query PlaneFinder's aggregated ADS-B feed, never the aircraft — tracking is passive and invisible to the target. PlaneFinder logs your session/queries; use a sock-puppet browser if the airframe you're tracking is sensitive. Note some military/private aircraft are filtered or blocked from public feeds."
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Established commercial ADS-B/MLAT flight-tracking network (part of the Airnav/PlaneFinder ecosystem) featured in the Bellingcat toolkit; coverage depends on volunteer receiver density.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- plane-finder
- planefinder-army-live-flight-tracker
aliases:
- PlaneFinder.net
- Plane Finder
tags:
- bellingcat-toolkit
- transport
- flight-tracking
source: bellingcat-toolkit
lastVerified: '2026-07-23'
enrichment: full
---

# PlaneFinder

> A live ADS-B flight-tracking map: enter a flight number, callsign, or registration and see where the aircraft is now, plus its recent track.

## When to use
You have a flight number, callsign, or aircraft registration (tail number) tied to a subject or event and want to place that aircraft in space and time — confirming a person was on/near a flight, reconstructing a route, or corroborating a departure/arrival. One of several interchangeable trackers; useful cross-check when another (FlightRadar24, ADS-B Exchange) filters an airframe PlaneFinder still shows. Aircraft-focused, so direct missing-persons relevance is low.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://planefinder.net/ and use the search box for a flight number, callsign, or registration.
2. Click the aircraft to see live `geolocation`, altitude, speed, heading, and origin/destination.
3. Open the flight's details/playback for its recent track; compare across days for a pattern-of-life on a private aircraft.
4. Cross-check the same identifier on another tracker — coverage and filtering differ, so an airframe missing here may appear there.
5. Pivot a registration to an aircraft-registry lookup for owner/operator (`employer-org`) detail.

## Inputs → Outputs
- **In:** flight number / callsign / registration (mapped loosely to `vehicle-plate`)
- **Out:** live and recent `geolocation`, altitude/speed, route, aircraft type
- **Empty/negative result looks like:** no track / "no data" — the aircraft may be on the ground, out of receiver coverage, or filtered from public feeds; absence is not proof it isn't flying.

## Gotchas & OpSec
- Coverage depends on volunteer ADS-B receivers; oceanic and remote areas have gaps.
- Some military and privacy-blocked (LADD/PIA) aircraft are filtered — a blank result can be deliberate suppression, not inactivity.
- Free tier limits historical playback; deep history needs the paid tier or a cross-tracker with better archives.

## Overlaps ("do both")
- Run alongside the sibling entries [[plane-finder]] and [[planefinder-army-live-flight-tracker]], and other ADS-B trackers — no single network sees every airframe, so corroborate a track across two before trusting it.

## Trust & verifiability
`trust: trusted` — an established commercial tracking network cited by Bellingcat; the live data is authoritative where receivers exist, with coverage gaps and deliberate filtering as the main caveats.
