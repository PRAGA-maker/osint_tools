---
id: meteoblue
name: MeteoBlue
description: Use when you have a `geolocation` and a date and want the historical or forecast weather conditions there — returns weather archive data (temperature, precipitation, wind, cloud cover) tied to a place and time.
url: https://www.meteoblue.com/
category: geolocation
path:
- geolocation
bestFor: Reconstructing what the weather was doing at a specific place and time (e.g. corroborating a witness account, dating a photo, or assessing search conditions).
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: Core forecasts and the point-and-click "Weather Archive / History & Climate" pages are free with ads. Ad-free (~€9/yr) and "point+" high-resolution history (~€50/yr) are paid; the free archive is enough for most investigative corroboration.
opsec: passive
opsecNote: You are querying a public weather site about a place, not a person. Nothing about the subject is disclosed to Meteoblue. Fully passive; no sock puppet needed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by meteoblue AG (spun out of the University of Basel); a long-established meteorological data provider, not a scraper.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- meteoblue.com
- meteoblue Weather Archive
tags:
- Maps, Geolocation and Transport
- Nature
- weather
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# MeteoBlue

> A global weather-archive and forecast service used to reconstruct the conditions at a specific place and time.

## When to use
You have a `geolocation` (place name or coordinates) and a date, and you need to know what the weather was actually doing there — temperature, rain/snow, wind, cloud cover, daylight. Useful for corroborating or challenging a timeline ("the witness says it was a clear evening"), estimating when an outdoor photo was taken, or judging exposure and search conditions in a wilderness disappearance.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.meteoblue.com/ and search the location (city, address, or coordinates) in the top search box.
2. From the location page, open **History & Climate → Weather Archive**.
3. Pick the date or date range. Read the archived hourly/daily conditions: temperature, precipitation, wind speed/direction, cloud cover, sunshine.
4. For forward-looking work (planning a ground search), use the 7-/14-day forecast tabs instead.
5. Pivot: cross-check the reconstructed conditions against photo shadows/EXIF or witness statements.

## Inputs → Outputs
- **In:** `geolocation` (place or coordinates) + a target date
- **Out:** `geolocation`-anchored weather record — temperature, precipitation, wind, cloud/sun for that place and time
- **Empty/negative result looks like:** archive coverage thins out for very remote points and for older dates; you may get modelled (reanalysis) values rather than a nearby station reading, so treat sparse locations as estimates, not measurements.

## Gotchas & OpSec
- Human-in-the-loop: none — it's a normal web lookup.
- Free archive resolution is coarser than the paid "point+" history; free values are model reanalysis, not certified station data, so don't present them as a single-station observation.
- Times are shown in the location's local zone by default; confirm the zone before comparing against a timestamp.

## Overlaps ("do both")
- Pairs with a sun-position/shadow tool (e.g. `[[suncalc]]`) — Meteoblue tells you cloud cover and precipitation, the sun tool tells you light direction and daylight window; together they date and place an outdoor scene.

## Trust & verifiability
`trust: trusted` — meteoblue AG is an established meteorological company with academic roots; data is modelled reanalysis/forecast, so cite it as authoritative for conditions but not as a single-station observation.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | meteoblue |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
