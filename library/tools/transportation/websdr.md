---
id: websdr
name: WebSDR
description: Use when you have a frequency/region and want to listen to live radio from an internet-connected receiver near that location — returns audio intelligence (callsigns, voice, Morse) tied to a geolocation.
url: http://websdr.org
category: transportation
path:
- transportation
bestFor: Listening in-browser to remote software-defined radios worldwide to monitor shortwave/aviation/marine/amateur traffic from a chosen location.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free to use in a browser; the receivers are hosted by universities and volunteers, funded independently.
opsec: passive
opsecNote: You listen to publicly broadcast radio through a third party's receiver — the transmitting station cannot see you, so it is passive. The receiver operator does see your connection; use a sock-puppet browser/VPN if that matters.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: community
trustNote: websdr.org is the long-running directory of WebSDR receivers (originated at the University of Twente); individual receivers are volunteer-run.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- WebSDR.org
- Web Software Defined Radio
tags:
- radio
- sdr
- military-tracking
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# WebSDR

> A directory of internet-connected software-defined radios you can tune from your browser — listen to live shortwave, aviation, marine, and amateur traffic from a receiver near a place of interest.

## When to use
You want to monitor radio activity tied to a `geolocation` — HF/shortwave, aircraft/ATC bands, marine, or amateur traffic — but have no receiver there. WebSDR lets you tune a remote SDR near the area and listen live (voice, Morse, digital modes). It's niche situational monitoring; it surfaces `geolocation`/activity context, not a person's identity directly.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://websdr.org and pick a receiver by location/coverage from the list (many worldwide; the University of Twente HF receiver is the best known).
2. In the browser tuner, set the frequency and mode (AM/USB/LSB/CW/etc.) for the band you want.
3. Listen and, for `manual-review`, transcribe callsigns, station IDs, or spoken details; use the waterfall to find active signals.
4. Note the receiver's `geolocation` (it shapes what's audible) and the time of any transmission.
5. Pivot: a heard aircraft callsign → flight tracking / [[live-atc]]; a maritime callsign/MMSI → AIS tools.

## Inputs → Outputs
- **In:** a target `geolocation`/region and a frequency+mode to monitor.
- **Out:** live audio and a spectrum waterfall from that region — callsigns, voice, Morse, digital signals (all `manual-review`).
- **Empty/negative result looks like:** a dead/offline receiver, a quiet band with no traffic in your window, or propagation conditions that block the signal — common; try another receiver or time.

## Gotchas & OpSec
- Receivers go offline and coverage is uneven — always have a backup station.
- What you can hear depends on the receiver's location and radio propagation; a silent band isn't proof nothing is transmitting elsewhere.
- Decoding voice/Morse/digital is skill- and time-intensive; expect manual effort.

## Overlaps ("do both")
- Pairs with [[live-atc]] (curated ATC feeds) and AIS/flight trackers: WebSDR gives raw radio from a chosen location when a curated feed doesn't cover it.

## Trust & verifiability
`trust: community` — a well-known volunteer/academic network; the audio is primary-source, but confirm any callsign/detail against an authoritative registry.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | websdr |
