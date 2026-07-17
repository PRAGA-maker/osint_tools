---
id: timeanddate-com
name: timeanddate.com
description: Use when you have a `geolocation` and a date/time and want the exact sun/shadow, timezone, or day-length — supports chronolocation of photos and verifying claimed timelines.
url: https://www.timeanddate.com/time/map/
category: geolocation
path:
- geolocation
bestFor: Chronolocation — computing sun position, shadow direction, and daylight times for a place and date to test when a photo was taken.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free reference site (ad-supported); core sun/time/timezone calculators need no account.
opsec: passive
opsecNote: Pure astronomical/time reference lookups; nothing about the target is submitted and no one is alerted. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Long-established, widely-cited reference site; sun/moon/timezone data is astronomically computed and authoritative.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- astronomy-sun-moon-eclipses
- suncalc
aliases:
- timeanddate
- Time and Date
tags:
- timezones
- Time Zones & Converters
- chronolocation
source: uk-osint
lastVerified: '2026-07-17'
enrichment: full
---

# timeanddate.com

> A reference site for time, timezones, and precise sun/moon positions — an OSINT chronolocation aid for pinning *when* an outdoor photo was taken from the shadows in it.

## When to use
You have (or suspect) a `geolocation` for an outdoor photo and want to test or derive the time it was taken. Given a place and date, timeanddate.com gives the sun's azimuth/elevation through the day, sunrise/sunset, and day length — so you can check whether the shadows in the image match a claimed time, or estimate the time from shadow direction/length. Also useful for converting a photo/message timestamp across timezones when reconstructing a subject's timeline.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.timeanddate.com/ and pick the tool: **Sun Calculator** (`/sun/`) for sunrise/sunset/position, or the world clock/time-zone converter.
2. Enter the city/location (or nearest one) and the date.
3. Read sunrise, sunset, solar noon, and the sun's azimuth/altitude table through the day.
4. Compare shadow direction and length in the photo against the sun azimuth/elevation to bracket the capture time (shadows point away from the sun; short shadows ≈ high sun ≈ midday).
5. Pivot: a derived time + place lets you cross-check against transit/weather/CCTV records and other timeline evidence; for interactive shadow modelling, use `[[suncalc]]`.

## Inputs → Outputs
- **In:** a `geolocation`/city and a date (and optionally a time)
- **Out:** sun azimuth/elevation, sunrise/sunset/day length, timezone/UTC offset → constrains the `geolocation`/time of a photo
- **Empty/negative result looks like:** the tool always returns astronomical values; a "wrong" answer means the shadows DON'T match the claimed time — treat that mismatch as a lead (staged/misdated photo), not a tool failure.

## Gotchas & OpSec
- You need a reasonably accurate location first — chronolocation *refines* time given place; it can't find the place on its own.
- Terrain, buildings, and daylight-saving transitions affect real-world shadows; account for DST and local obstructions.
- Historical dates are fine (astronomy is deterministic), but confirm the correct year's DST rules for that country.

## Overlaps ("do both")
- Pairs with `[[suncalc]]` — SunCalc overlays the sun path on an interactive map for visual shadow matching; timeanddate gives precise tabular values. Use both to bracket a time.
- Pairs with `[[astronomy-sun-moon-eclipses]]` for moon phase / celestial cross-checks on night imagery.

## Trust & verifiability
`trust: trusted` — an established, widely-referenced site; its sun/moon/timezone figures are astronomically computed and reproducible, so results are verifiable against any other ephemeris.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | timeanddate-com |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
