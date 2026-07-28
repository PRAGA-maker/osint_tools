---
id: military-ship-tracker
name: Military Ship Tracker
description: Use when you have a naval/military vessel name or want to see military ships broadcasting AIS in an area — returns live positions and vessel identity where AIS is transmitted.
url: https://www.marinevesseltraffic.com/2013/02/military-ship-track.html
category: transportation
path:
- transportation
bestFor: Live map of military/naval vessels currently broadcasting AIS, filtered to the military ship type.
selectorsIn: []
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: Free live AIS map on MarineVesselTraffic; some detailed/historical features are paid or ad-supported.
opsec: passive
opsecNote: You read publicly-broadcast AIS positions on a third-party map — no vessel or person is contacted. AIS reflects only what ships choose to transmit; many warships run dark or spoof, so treat the map as partial and never assume absence means a vessel isn't there.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: MarineVesselTraffic aggregates crowd-sourced/terrestrial AIS; coverage and freshness vary by region and receiver density.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- submarine-tracker
aliases:
- MarineVesselTraffic military
- naval ship tracker
tags:
- maritime
- ais
- vessel-tracking
source: osint4all
lastVerified: '2026-07-28'
enrichment: full
---

# Military Ship Tracker

> A live AIS map filtered to military/naval vessels — useful for spotting where warships are *broadcasting* their position, with the standing caveat that many deliberately don't.

## When to use
You want to locate a named naval vessel, or survey which military ships are transmitting AIS in a given sea area right now, as part of conflict-monitoring, maritime, or movement-tracking work. It plots vessels self-reporting the "military" AIS type on a map with position, name/MMSI, and course. It's a maritime-geolocation aid, not a people-finder.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the military-ship map at https://www.marinevesseltraffic.com/2013/02/military-ship-track.html.
2. Pan/zoom to the region of interest; click a vessel icon for its name, MMSI, type, position, speed, and heading.
3. Search by vessel name where the interface allows, to jump to a specific ship.
4. Pivot: a confirmed position + timestamp anchors a vessel's movement; the name/MMSI feeds registry and imagery cross-checks.

## Inputs → Outputs
- **In:** area of interest or a vessel name (not a personal selector)
- **Out:** live `geolocation` (position/course) and vessel identity for ships broadcasting AIS
- **Empty/negative result looks like:** few or no military vessels shown in an area — usually means ships are running AIS-dark or the region has thin receiver coverage, **not** that no vessels are present.

## Gotchas & OpSec
- **AIS is opt-in and gameable:** warships routinely disable AIS, spoof positions, or broadcast decoy identities — absence and even presence can be deliberate. Corroborate with imagery/other sources before drawing conclusions.
- Coverage depends on terrestrial/crowd-sourced receivers; open-ocean and remote areas are sparse.
- OpSec: **passive** — reading a public map; nothing reaches any vessel or person.

## Overlaps ("do both")
- Pairs with `[[submarine-tracker]]` and broader AIS platforms (e.g. general vessel-traffic maps): this view isolates the military type, while a full-fleet tracker and OSINT imagery fill the gaps AIS leaves.

## Trust & verifiability
`trust: community` — MarineVesselTraffic aggregates crowd-sourced/terrestrial AIS. Reliable for what ships choose to transmit; inherently blind to dark or spoofed vessels, so never treat it as a complete order of battle.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | military-ship-tracker |
| category | transportation |
| selectorsIn → selectorsOut |  → geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
