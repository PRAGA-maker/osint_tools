---
id: rain-alarm
name: Rain Alarm
description: Use when you have a `geolocation` and want live precipitation/radar for that spot — returns current and approaching-rain `geolocation` weather context.
url: http://rain-alarm.com
category: geolocation
path:
- geolocation
bestFor: Checking real-time rain/snow radar and approaching-precipitation for a specific location or timeframe.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: Free web map and basic app; a paid premium tier removes ads and adds extra alert/forecast features. Free tier is sufficient for radar checks.
opsec: passive
opsecNote: Viewing the public radar map is passive and reveals nothing to any target. If you install the mobile app and enable location alerts, you share your own device location with the provider (Foreca-sourced) — use a chosen map coordinate rather than your live GPS when investigating someone else's area.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A commercial consumer weather app aggregating third-party radar (Foreca, national met services); reliable as live weather, but not an authoritative historical-archive source.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Rain Alarm radar
tags:
- Maps, Geolocation and Transport
- Nature
source: cyb-detective
lastVerified: '2026-07-22'
enrichment: full
---

# Rain Alarm

> A live global precipitation-radar map (web + app) that answers "is it/was it raining there right now?" — weather context for a location, not a people lookup.

## When to use
You have a `geolocation` and need the current weather picture: is precipitation falling now, and is a band of rain/snow moving toward that spot? In investigative work this corroborates or challenges accounts tied to a place and time — e.g. testing whether "it was pouring when I left" fits the radar, scoping conditions for a current ground search, or planning field observation. It shows *live* radar, so it is best for now-casting, not historical reconstruction.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the web app and pan/zoom to the target `geolocation` (or search a place name).
2. Read the radar overlay: coloured cells show rain/snow/mixed/freezing precipitation with intensity in mm/h; animate the loop to see movement and direction.
3. For ongoing monitoring of an area, the mobile app can push "approaching rain" alerts for a chosen point.
4. Pivot: combine with terrain/search-area maps for a current field operation, or with authoritative historical weather archives when you need conditions for a *past* date the live radar cannot show.

## Inputs → Outputs
- **In:** `geolocation`
- **Out:** `geolocation` weather context — current precipitation presence, type, intensity and movement
- **Empty/negative result looks like:** clear radar over the area (no precipitation), or "no coverage" where radar data is unavailable for that region — the latter is a data gap, not confirmed dry weather.

## Gotchas & OpSec
- Live only: it does not provide historical radar for a past date/time — use a dedicated weather-history archive for that.
- Coverage is uneven; some regions have no radar feed at all, which reads as blank, not "no rain."
- Passive on the web; the app's alert feature shares *your* location — set a fixed map point instead of live GPS when working someone else's area.

## Overlaps ("do both")
- Pairs with historical weather-archive tools (for past conditions) and with terrain/mapping tools (for scoping a physical search) — this one supplies only the live precipitation layer.

## Trust & verifiability
`trust: unverified` — a legitimate commercial weather app over third-party radar feeds; accurate for live conditions but not an authoritative record for evidentiary use.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | rain-alarm |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
