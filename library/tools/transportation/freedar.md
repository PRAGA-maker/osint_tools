---
id: freedar
name: Freedar
description: Use when you have an aircraft registration/callsign or an area of interest and want live ADS-B positions — returns aircraft location, altitude, callsign and track, including military/private not filtered elsewhere.
url: https://radar.freedar.uk/virtualradar/desktop.html
category: transportation
path:
- transportation
bestFor: Live flight tracking over the UK/Europe with no aircraft filtering — shows military and blocked/private aircraft that mainstream trackers hide.
selectorsIn:
- name
- vehicle-plate
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free community-run flight tracker (Freedar.uk); no account required to view the radar.
opsec: passive
opsecNote: Viewing the live map is passive — you observe broadcast ADS-B/MLAT signals aggregated by Freedar; no target is contacted and nothing is sent to the aircraft or operator.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Community-run UK aggregator (ScoobyMedia/Freedar.uk) exchanging feeds with Wigan Radar and ADSBHub; data is crowd-fed ADS-B/MLAT, accurate where receivers exist but with coverage gaps.
missingPersonsRelevance: low
coverage:
- gb
- eu
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- adsb-exchange
- flightradar24
aliases:
- Freedar.uk
- Freedar Virtual Radar
tags:
- aviation
- flight-tracking
- adsb
source: metaosint
lastVerified: '2026-07-28'
enrichment: full
---

# Freedar

> A community UK flight tracker that, unlike the big commercial sites, applies **no filtering** — so military, government and privacy-blocked aircraft still appear on the live map.

## When to use
You are tracking an aircraft or watching activity over the UK/Europe and the mainstream trackers hide what you need. Freedar's selling point is that it does not filter military or blocked/private tails, so it surfaces flights (state aircraft, surveillance, blocked bizjets) that FlightRadar24/Flightaware suppress. Use it to locate a specific registration/callsign in real time or to watch traffic over an area of interest.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the radar (https://radar.freedar.uk/virtualradar/desktop.html; the main portal is https://freedar.uk/, also on mobile).
2. Pan/zoom to your area of interest, or use the aircraft list/search to find a specific callsign or registration (`vehicle-plate`/tail number).
3. Click an aircraft to read its live details: position (`geolocation`), altitude, speed, heading, callsign, registration and type.
4. Follow the track over time; note when a target aircraft appears/disappears from coverage.
5. Pivot: a registration feeds aircraft-registry lookups (owner/operator); repeated patterns feed pattern-of-life analysis.

## Inputs → Outputs
- **In:** an aircraft callsign/registration (`name`/`vehicle-plate`), or an area to watch
- **Out:** live `geolocation` (position, altitude, heading, track) plus callsign/registration/type
- **Empty/negative result looks like:** the aircraft not shown — it may be outside receiver coverage, on the ground, or not transmitting ADS-B (some military use Mode S only / transmit intermittently). Absence is a coverage gap, not proof it isn't flying.

## Gotchas & OpSec
- Coverage depends on volunteer receivers — strongest over the UK, thinner elsewhere; MLAT fills gaps imperfectly.
- Positions are broadcast by the aircraft (ADS-B) or multilaterated; spoofing and gaps happen, so corroborate a critical track against another feed.
- Fully passive: you're a viewer of a public aggregation; nothing reaches the aircraft or operator.

## Overlaps ("do both")
- Pairs with `[[adsb-exchange]]` — the other major unfiltered tracker; cross-check a target across both for coverage and to confirm an unfiltered sighting.
- Compare against `[[flightradar24]]` to see exactly what the filtered mainstream view omits.

## Trust & verifiability
`trust: community` — a volunteer-fed UK aggregator; the raw ADS-B/MLAT data is genuine but coverage is uneven and spoofing is possible. Verify a specific aircraft's identity via its registration in an aircraft registry and against a second flight feed.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | freedar |
| category | transportation |
| selectorsIn → selectorsOut | name, vehicle-plate → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
