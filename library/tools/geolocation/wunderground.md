---
id: wunderground
name: Weather Underground (History)
description: Use when you have a `geolocation` and a date and want the weather that day — returns historical temperature, precipitation, wind, and conditions for that place/time.
url: https://www.wunderground.com/history
category: geolocation
path:
- geolocation
bestFor: Retrieving historical weather for a specific location and date to corroborate or challenge a timeline/photo.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: Free to browse historical daily observations by station; bulk/API access to historical data is paid.
opsec: passive
opsecNote: You query a weather archive by place and date — no subject is involved and nothing is signalled. Purely environmental data.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Observations come from official and personal weather stations aggregated by Weather Underground (IBM); station data is reliable, though the nearest station may be some distance from your exact point.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- Wunderground
- Weather Underground history
tags:
- weather
- geolocation
- timeline
source: cyb-detective
lastVerified: '2026-07-18'
enrichment: full
---

# Weather Underground (History)

> A historical weather archive by station — look up what the weather actually was at a place on a date, to test alibis, timelines, and clues in photos/video.

## When to use
You have a `geolocation` and a specific date/time and need the ground-truth weather: was it raining, how hot, wind direction, snow on the ground? Powerful for verification — does the sunny sky, wet road, or heavy coat in a photo match the claimed date/place? Does a witness's "it was pouring that night" hold up? Weather is an objective cross-check for statements, image analysis, and event timelines.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.wunderground.com/history.
2. Enter the location (city/airport/station) nearest your `geolocation` and the date.
3. Read the daily observations: high/low temperature, precipitation, humidity, wind speed/direction, and hourly conditions.
4. Compare against the claim or the visual evidence (sky, shadows, precipitation, clothing).
5. Pivot: a mismatch between claimed and actual weather is a strong lead; a match corroborates a date/place for a photo or statement.

## Inputs → Outputs
- **In:** `geolocation` (nearest station) + a date
- **Out:** historical weather for that day — temperature, precipitation, wind, conditions
- **Empty/negative result looks like:** no data for the station/date — the nearest station may lack records for that day; try an alternate nearby station before concluding.

## Gotchas & OpSec
- Readings are from the **nearest station**, which can be miles from your exact point — local microclimate/terrain may differ; use the closest reliable station and note the distance.
- Personal-weather-station data varies in quality; prefer official/airport stations for decisive checks.
- OpSec: fully passive — environmental archive.

## Overlaps ("do both")
- Pairs with sun-position/shadow tools (SunCalc) and satellite imagery: weather confirms conditions, sun tools confirm time-of-day from shadows, and both together tightly constrain when/where a photo was taken.

## Trust & verifiability
`trust: trusted` — station observations aggregated by Weather Underground (IBM). Data is reliable; the main caveat is spatial (station vs exact location), not accuracy.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wunderground |
