---
id: understanding-war-map-room
name: ISW Map Room
description: Use when you have a conflict `geolocation` or date and want authoritative, dated control-of-terrain maps — returns front-line positions and named settlements over time.
url: https://www.understandingwar.org/map-room
category: transportation
path:
- transportation
bestFor: Reading dated, sourced conflict maps (front lines, control of terrain, strikes) for active war zones.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
- address
status: live
pricing: free
costNote: Free to view; the Institute for the Study of War publishes the maps openly, funded as a nonpartisan nonprofit.
opsec: passive
opsecNote: Passive reading of published analytical maps. No target interaction; ISW logs standard web analytics. Use a clean browser for sensitive research.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Published by the Institute for the Study of War (ISW), a recognised Washington-based conflict-analysis institution whose assessments are sourced and widely cited.
missingPersonsRelevance: low
coverage:
- ua
- ru
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- liveuamap
- google-my-maps
aliases:
- Understanding War Map Room
- ISW Interactive Map
- understandingwar.org map room
tags:
- Maps, Geolocation and Transport
- Military tracking
- conflict-mapping
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# ISW Map Room

> The Institute for the Study of War's collection of dated, sourced conflict maps — the authoritative baseline for who controlled what terrain, and when.

## When to use
You are geolocating or dating media from an active conflict (Russia–Ukraine, the Middle East, and others) and need to know the front-line situation at a place and time: was a settlement under attack, contested, or captured on a given date? ISW's regularly-updated control-of-terrain maps let you place a named town relative to the front and check a claimed timeline against the documented situation.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.understandingwar.org/map-room.
2. Filter by theatre (Ukraine, Middle East, China–Taiwan, etc.), team, date, and map type.
3. Open the map for the date closest to your media; read the front line, controlled zones, and named settlements/axes of advance.
4. Cross-reference a specific `geolocation` in your material against the map to establish whether it was contested or controlled at that time.
5. Pivot: confirmed place names feed mapping/Street View and other conflict trackers (`[[liveuamap]]`) for corroboration and finer detail.

## Inputs → Outputs
- **In:** a conflict `geolocation` and/or date
- **Out:** dated control-of-terrain maps, front-line positions, named settlements (`address`/`geolocation`)
- **Empty/negative result looks like:** no map covers your exact area/date — ISW maps are theatre-level and periodic, so fine-grained or off-theatre spots may need a dedicated tracker.

## Gotchas & OpSec
- Maps are analytical assessments with an "as of" date and inherent lag — treat them as sourced estimates, not minute-by-minute truth.
- Coverage centres on major theatres ISW tracks; smaller conflicts may be absent.
- OpSec: fully passive; only standard analytics apply.

## Overlaps ("do both")
- Pairs with `[[liveuamap]]` — ISW gives sourced, expert control-of-terrain assessments; Liveuamap gives denser, near-real-time crowd/OSINT-sourced events. Use ISW for the authoritative baseline and Liveuamap for granular recency.

## Trust & verifiability
`trust: trusted` — produced by the Institute for the Study of War, a nonpartisan analytical institution; maps are sourced and dated, widely relied upon by journalists and analysts.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | understanding-war-map-room |
| category | transportation |
| selectorsIn → selectorsOut | geolocation → geolocation, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
