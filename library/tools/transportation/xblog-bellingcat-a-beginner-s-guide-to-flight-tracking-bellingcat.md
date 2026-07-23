---
id: xblog-bellingcat-a-beginner-s-guide-to-flight-tracking-bellingcat
name: 'Bellingcat: A Beginner''s Guide to Flight Tracking'
description: Use as a methodology guide when you need to track an aircraft or research flight history — teaches which ADS-B/flight-tracking tools to use and how, turning a tail/flight number into geolocation.
url: https://www.bellingcat.com/resources/how-tos/2019/10/15/a-beginners-guide-to-flight-tracking
category: transportation
path:
- transportation
bestFor: Learning the flight-tracking workflow — tools, tail-number lookups, and history sources — for aviation investigations.
selectorsIn:
- name
- vehicle-plate
selectorsOut:
- geolocation
status: live
pricing: free
opsec: passive
opsecNote: This is a how-to article you read — no query about any target and no footprint. The tools it points to (ADS-B trackers) are themselves passive receivers of aircraft broadcasts; following them alerts no one. Be aware some aircraft owners block/limit their tail numbers on certain trackers.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Authored by Bellingcat, a leading open-source-investigation organization; a well-regarded, if dated (2019), primer.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- bellingcat
- bellingcat-com
- bellingcat-openstreetmap-search
- these-are-the-tools-open-source-researchers-say-they-need
aliases:
- Beginner's Guide to Flight Tracking
tags:
- aviation
- flight-tracking
- methodology-guide
source: metaosint
lastVerified: '2026-07-23'
enrichment: full
---

# Bellingcat: A Beginner's Guide to Flight Tracking

> A Bellingcat how-to that teaches the flight-tracking workflow — which ADS-B tools to use, how to look up a tail number, and how to reconstruct where an aircraft has been.

## When to use
A methodology reference, not a lookup tool itself. Reach for it when an investigation touches aviation — a specific aircraft (by tail/registration `vehicle-plate` or flight number/`name`), a person linked to a plane, or an event with air movement — and you need to know *how* to track it and which platforms to use. It walks through the concepts and the toolset so you can then go to the live trackers and geolocate the aircraft's history.

## How to use it (`bestInteractionPattern`: web-manual)
1. Read the guide: https://www.bellingcat.com/resources/how-tos/2019/10/15/a-beginners-guide-to-flight-tracking.
2. Learn the core moves — reading ADS-B on Flightradar24 / ADS-B Exchange, resolving a tail number to an aircraft, and finding historical tracks.
3. Apply it on the live tools: enter the tail/registration or flight number and read current position and route history (`selectorsOut`).
4. Pivot: an aircraft's routes place it (and associated people) at times/locations; combine with ownership registries and imagery for confirmation.

## Inputs → Outputs
- **In:** `vehicle-plate` (tail/registration) or `name` (flight number/callsign) — as concepts to apply on the trackers
- **Out:** `geolocation` (aircraft positions/routes) once you apply the method on a tracker
- **Empty/negative result looks like:** the guide can't "return" data — if a tail number shows no track on the tools it points to, the aircraft may be off, blocked from tracking, or outside ADS-B coverage.

## Gotchas & OpSec
- Human-in-the-loop: none (reading).
- OpSec: passive — an article, and the tools it teaches are passive ADS-B receivers.
- Dated (2019): some tool names/UIs have changed and ADS-B Exchange is now the preferred unfiltered source; use the guide for concepts, then current tools for data. Some owners block their tail numbers on filtered trackers.

## Overlaps ("do both")
- Points you to live trackers (Flightradar24, ADS-B Exchange, OpenSky) and pairs with the broader [[bellingcat]] toolkit — read this for method, then use the trackers and aircraft registries for the actual data.

## Trust & verifiability
`trust: trusted` — from Bellingcat, an authoritative open-source-investigation source. It's guidance rather than data, so its value is the method; verify any aircraft finding on current, unfiltered tracking tools.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | xblog-bellingcat-a-beginner-s-guide-to-flight-tracking-bellingcat |
| category | transportation |
| selectorsIn → selectorsOut | name, vehicle-plate → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
