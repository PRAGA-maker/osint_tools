---
id: suncalc-2
name: SunCalc
description: Use when a photo shows a shadow and you need to confirm or narrow the time of day / date / facing direction at a known location.
url: https://suncalc.org/
category: geolocation
path:
- geolocation
- geolocation-tools
bestFor: Validating photo timestamps and camera/subject orientation from shadow length and direction.
input: Date/time and coordinates
output: Sun azimuth/elevation and daylight phase data
selectorsIn:
- geolocation
- metadata-exif
selectorsOut:
- geolocation
- metadata-exif
status: live
pricing: free
costNote: Fully free, no account.
opsec: passive
opsecNote: Runs client-side against open sun-position data; you never touch the target or any target-controlled server.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Based on the widely used SunCalc model (Vladimir Agafonkin's open algorithm); deterministic astronomical math, independently reproducible.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- timeanddate
- shadowfinder
aliases: []
tags:
- chronolocation
- shadow-analysis
source: arf-seed
lastVerified: ''
enrichment: full
---

# SunCalc

> Browser sun-position calculator that turns a place + time into sun azimuth/elevation — the core of shadow-based chronolocation.

## When to use
You have a photo or video of a missing person (or a vehicle/landmark) at a `geolocation` you can identify on the map, and you want to verify a claimed timestamp or estimate the unknown time of day. Shadows in the frame give direction (azimuth) and length (elevation); SunCalc tells you what date/time produces that sun geometry there. Equally useful in reverse: fix the time, read the sun direction, and infer which way the camera faced.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://suncalc.org/.
2. Drag the map pin (or type an address) to the location shown in your image. The pin sets the coordinates.
3. Set the date and drag the time slider. SunCalc draws the sun's compass direction and shows azimuth, elevation, and sunrise/sunset/golden-hour times.
4. Compare the drawn sun direction against the shadow direction in your photo (shadows point opposite the sun). Match elevation to shadow length (low sun = long shadow).
5. Pivot: feed the narrowed time window back into the case timeline; pair with [[timeanddate]] for sunrise/sunset tables and historical day-length checks.

## Inputs → Outputs
- **In:** `geolocation` (map pin/coordinates), candidate date/time, plus any `metadata-exif` timestamp you're testing.
- **Out:** sun azimuth + elevation, daylight phases (refines `geolocation`/time, validates `metadata-exif`).
- **Empty/negative result looks like:** the modeled sun direction can't be reconciled with the shadow at any plausible time — implying the timestamp, the location, or the photo is wrong.

## Gotchas & OpSec
- No login, no captcha; fully passive and client-side.
- Indoor scenes, overcast skies, and artificial light defeat it — you need a clear outdoor shadow.
- Daylight-saving and time-zone offsets are a common error source; double-check the displayed timezone matches the location.
- It models the present-day sun path; the sun's geometry for a given calendar date is stable year to year, so historical dates are fine.

## Overlaps ("do both")
- Pairs with [[timeanddate]] for precise sunrise/sunset/twilight tables and past-date lookups.
- Complements dedicated shadow-to-time solvers (e.g. ShadowFinder) when you need the reverse computation.

## Trust & verifiability
`trust: trusted` — built on the well-established SunCalc astronomical algorithm; output is deterministic and can be cross-checked against any independent ephemeris.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | suncalc-2 |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, metadata-exif → geolocation, metadata-exif |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
