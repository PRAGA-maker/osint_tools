---
id: sun-rise-noon-and-set-time-and-direction
name: Sollumis (sun position & direction)
description: Use when you have a candidate `geolocation` and a date and want the sun's azimuth/altitude to chrono-locate a photo by its shadows — returns sun timings and directions to test against an image.
url: https://sollumis.com
category: geolocation
path:
- geolocation
bestFor: Chronolocation — matching shadow direction/length in a photo to sun position at a place and time.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free web tool; no account or payment.
opsec: passive
opsecNote: A client-side astronomy calculator. You enter a location/date, not anything about a person; nothing about the subject is transmitted. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A single-purpose solar-position visualizer; the underlying astronomy is deterministic and checkable against other sun calculators (SunCalc, NOAA).
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- sollumis.com
- sun position tool
tags:
- chronolocation
- geolocation
source: metaosint
lastVerified: '2026-07-22'
enrichment: full
---

# Sollumis (sun position & direction)

> Plot the sun's path over any location and date — the workhorse for chrono-locating a photo from its shadows.

## When to use
You have a photo of interest (from a missing subject, a suspect, or a location) and want to estimate or confirm WHEN it was taken, or verify a claimed location/time. Given a candidate `geolocation` and date, Sollumis shows sunrise/noon/sunset times plus the sun's azimuth (compass direction) and altitude (height). Compare that against the direction and length of shadows in the image: a mismatch disproves a claimed place/time; a match corroborates it.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://sollumis.com.
2. Click the map or search to set the candidate `geolocation`.
3. Set the month/day/year (and timezone) you're testing.
4. Read the outputs: sunrise/noon/sunset times, sunrise & sunset **azimuth**, and noon **altitude**.
5. Compare to the photo: shadows point opposite the sun's azimuth; shadow length tracks altitude. Iterate the time until the modelled sun matches the observed shadows.
6. Pivot: a confirmed time/location narrows a timeline; feed the coordinates to satellite/street-view tools for scene matching.

## Inputs → Outputs
- **In:** `geolocation` (place) + date/time being tested
- **Out:** `geolocation`-linked solar data — sunrise/noon/sunset times, sun azimuth and altitude (i.e. shadow direction/length model)
- **Empty/negative result looks like:** the tool always returns numbers; a "negative" is when the modelled sun direction/altitude cannot match the photo's shadows at any time that day — evidence the claimed place or date is wrong.

## Gotchas & OpSec
- It models the sun only; terrain, tall buildings, and overcast skies alter real shadows. Use as corroboration, not sole proof.
- Get the timezone/DST right — an hour's error swings the azimuth noticeably.
- OpSec: passive; nothing about the subject leaves your browser.

## Overlaps ("do both")
- Pairs with SunCalc/NOAA solar calculators to cross-check the astronomy, and with satellite/street-view tools to match the physical scene once the time is pinned.

## Trust & verifiability
`trust: unverified` — a third-party visualizer, but its output is deterministic astronomy you can independently verify against multiple sun-position calculators, so the numbers are trustworthy even if the site isn't audited.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sun-rise-noon-and-set-time-and-direction |
| category | geolocation |
