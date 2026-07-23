---
id: live-atc
name: Live ATC
description: Use when you have an aircraft near a covered airport and want tail numbers/callsigns from live tower audio — returns vehicle-plate (tail number) and geolocation context that flight-trackers may hide.
url: https://www.liveatc.net/
category: transportation
path:
- transportation
bestFor: Listening to live/archived air-traffic-control audio to catch a tail number or callsign an aircraft tried to keep off flight-tracking sites.
selectorsIn:
- vehicle-plate
- geolocation
selectorsOut:
- vehicle-plate
- geolocation
status: live
pricing: free
costNote: Free to stream live and to access recent archived recordings; volunteer-run, funded by donations/store.
opsec: passive
opsecNote: You are listening to publicly broadcast, unencrypted radio; nothing about you or the aircraft owner is transmitted — fully passive. Note that recording/relaying ATC audio has local legal nuances in some jurisdictions.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running volunteer network of receiver feeds; coverage and audio quality depend on local volunteers, but the audio itself is primary-source.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- live-air-traffic-control
aliases:
- LiveATC.net
tags:
- bellingcat-toolkit
- transport
- aviation
source: bellingcat-toolkit
lastVerified: '2026-07-23'
enrichment: full
---

# Live ATC

> A volunteer network streaming live and archived air-traffic-control radio — the audio channel where an aircraft must identify itself even when it's hidden from flight-tracking sites.

## When to use
You are tracking an aircraft near a LiveATC-covered airport and it's blocked/obscured on ADS-B trackers (FlightAware/ADSB-Exchange), or you want to confirm a `vehicle-plate` (tail number) or callsign at a specific time and place. Because pilots must radio their identity to the tower, the audio can yield a tail number or intentions that the map layers won't show. It corroborates aircraft movement tied to a place and time, not a person directly.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.liveatc.net/ and find the airport (by ICAO/IATA code or map) and the relevant feed (Tower, Ground, Approach).
2. Stream the live feed, or open the **Archive** to fetch a recent 30-minute recording covering the time window you care about.
3. Listen for the aircraft's tail number/callsign and instructions (runway, departure/arrival) — this is `manual-review`, you're transcribing audio by ear.
4. Note the `geolocation` (which airport/sector) and timestamp of the transmission.
5. Pivot: a recovered tail number → an aircraft registry (FAA N-number / ICAO registration) to attribute ownership; a callsign → flight-tracking history.

## Inputs → Outputs
- **In:** an airport/time window (and optionally a known `vehicle-plate`/callsign to listen for).
- **Out:** spoken `vehicle-plate` (tail number), callsign, and movement context tied to a `geolocation` and time.
- **Empty/negative result looks like:** no feed for that airport, a dead/silent stream, an archive gap, or audio where your aircraft never transmits in the captured window — common; coverage is volunteer-dependent.

## Gotchas & OpSec
- Coverage is patchy — only airports with a local volunteer receiver are online, and feeds drop out.
- Audio is noisy and fast; expect to replay archives and cross-check the tail number against a registry.
- Recording/rebroadcasting ATC audio has legal nuance in some countries even though listening is public — check local rules before republishing clips.

## Overlaps ("do both")
- Pairs with ADS-B flight trackers: when a plane is blocked or turns off its transponder, LiveATC audio can still catch the callsign/tail number the trackers miss.

## Trust & verifiability
`trust: community` — volunteer-operated, but the audio is primary-source; a tail number heard here should still be confirmed against an official aircraft registry.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | live-atc |
