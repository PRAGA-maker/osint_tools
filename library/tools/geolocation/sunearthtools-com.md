---
id: sunearthtools-com
name: SunEarthTools.com
description: Use when you have a photo's `geolocation` and want to verify or estimate the date/time from sun position and shadow direction — returns sun azimuth/elevation and shadow-length data for chronolocation.
url: https://www.sunearthtools.com
category: geolocation
path:
- geolocation
bestFor: Sun-position and shadow calculations for chronolocating outdoor photos (what time/date matches the shadows).
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free web calculators; no account. Optional login only saves settings.
opsec: passive
opsecNote: All computation is astronomical math on coordinates and dates you enter — nothing about the subject is transmitted anywhere and the target learns nothing. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Sun position is deterministic astronomy; SunEarthTools' outputs are reproducible against other ephemeris tools (SunCalc, NOAA), which is what makes it reliable for verification.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
aliases:
- SunEarthTools sun position
- sunearthtools shadow calculator
tags:
- chronolocation
- sun-position
- shadow-analysis
- geolocation
source: metaosint
lastVerified: '2026-07-17'
enrichment: full
---

# SunEarthTools.com

> A free sun-position and shadow calculator: given a location and date, it gives the sun's azimuth/elevation and shadow direction/length — the maths behind chronolocating an outdoor photo.

## When to use
You have (or have narrowed) the `geolocation` where an outdoor photo/video was taken and want to test *when* it was taken. Shadows in the image reveal the sun's azimuth and elevation; SunEarthTools lets you find the date(s)/time(s) at that location where the sun would cast exactly that shadow — confirming or refuting a claimed timestamp, or bounding when a subject was at a place. It also works the other way: given a known time, predict shadow direction to confirm a location.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.sunearthtools.com and open the "Sun position" tool.
2. Enter the location (map pin or coordinates) and a candidate date.
3. Read the sun path: azimuth (compass direction of the sun) and elevation (height above horizon) across the day, plus shadow direction/length. Match these to the shadows visible in the image.
4. Iterate dates/times until the modelled shadow direction and length match the photo. The matching window is your estimated capture time/date.
5. Pivot: a confirmed time/date anchors a subject's timeline; a mismatch flags a staged or misdated image.

## Inputs → Outputs
- **In:** a `geolocation` (coordinates) + candidate date/time; the observed shadow direction/length from the image.
- **Out:** sun azimuth/elevation, shadow direction and length — the time/date window consistent with the photo (a refined `geolocation`/time constraint).
- **Empty/negative result looks like:** no date matches the shadow → the claimed location or time is wrong, or the shadow reading is off (overcast, artificial light, wrong compass reference).

## Gotchas & OpSec
- Garbage in, garbage out: you must read the shadow's true compass bearing correctly (account for the photographer's facing direction and any map-north assumptions).
- Terrain, tall structures, and reflections distort apparent shadows; account for daylight-saving and time zone when converting to local clock time.
- Cross-check with a second ephemeris tool (SunCalc/NOAA) — agreement is the point.

## Overlaps ("do both")
- Pairs with map/satellite tools that fix the exact `geolocation`, and with EXIF/metadata tools — corroborate a claimed EXIF timestamp against the shadow-derived time.

## Trust & verifiability
`trust: trusted` — the underlying astronomy is deterministic and independently reproducible; results are verifiable against other sun-position calculators, so a matched window is strong, checkable evidence.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sunearthtools-com |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
