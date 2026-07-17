---
id: astronomy-sun-moon-eclipses
name: Astronomy - Sun - Moon - Eclipses (timeanddate)
description: Use when you have a `geolocation` and a date/time and want the sun/moon position and light times — returns azimuth, elevation, sunrise/sunset and moon phase to verify or narrow when a photo was taken.
url: https://www.timeanddate.com/astronomy
category: geolocation
path:
- geolocation
bestFor: Chronolocation — checking sun/moon position, shadow direction and daylight times for a place and date against clues in a photo or video.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free reference site; core sun/moon tools need no account. Ad-supported, with an optional paid ad-free membership.
opsec: passive
opsecNote: A public reference lookup — you enter a location and date, nothing about the subject. Nobody is contacted or alerted.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: timeanddate.com is a long-established, widely-cited astronomical/time reference; its sun and moon calculations are reliable for chronolocation work.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- timeanddate astronomy
- sun and moon calculator
tags:
- chronolocation
source: metaosint
lastVerified: '2026-07-17'
enrichment: full
relatedTools:
- timeanddate
- timeanddate-com
---

# Astronomy - Sun - Moon - Eclipses (timeanddate)

> timeanddate.com's sun/moon toolset — the reference for chronolocation: given a place and date, it tells you exactly where the sun and moon were, so you can test a photo's claimed time.

## When to use
You have a `geolocation` (from geolocating an image) and need to confirm or narrow *when* a photo/video was taken. Shadows, sun glare, twilight colour, or a visible moon give you clues; this tool gives you the ground truth — sun azimuth/elevation, sunrise/sunset/twilight times, and moon phase for that exact spot and day — so you can check whether the scene's lighting is consistent with a claimed date/time, or estimate the time from shadow direction and length.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.timeanddate.com/astronomy and pick the relevant tool (Sun Calculator, Moon Calculator, Sun & Moon position/path, or eclipse pages).
2. Enter the `geolocation` (city, or a custom lat/long) and the candidate date.
3. Read the outputs:
   - **Sun:** azimuth (compass bearing) and elevation through the day, sunrise/sunset, civil/nautical/astronomical twilight.
   - **Moon:** phase, illumination %, moonrise/moonset, and position.
4. Compare against the image: does the shadow direction match the sun's azimuth at the claimed time? Is the twilight/darkness consistent? Is the moon phase in the photo the phase for that night?
5. Conclude: confirm, refute, or narrow the time window; feed the refined time back into the geolocation timeline.

## Inputs → Outputs
- **In:** `geolocation` + a date (and optionally a time)
- **Out:** sun azimuth/elevation, sunrise/sunset & twilight times, moon phase/illumination and rise/set — all tied to that `geolocation`
- **Empty/negative result looks like:** the tool always returns values for a valid place+date; the "negative" outcome is a *mismatch* — e.g. the photo shows a shadow pointing a direction the sun could not have cast at the claimed time, which refutes the claimed timestamp.

## Gotchas & OpSec
- Fully passive — a reference lookup, nothing about the subject leaves your machine.
- Precision depends on your location accuracy: a coarse `geolocation` gives coarse azimuth/elevation. Use the custom lat/long entry for tight work.
- Account for terrain and local horizon: computed sunrise assumes a flat horizon; mountains/buildings shift observed first/last light.
- Times are shown in the location's local time/DST — mind timezone when comparing to a camera clock (which may be wrong or in another zone).

## Overlaps ("do both")
- Pairs with `[[timeanddate]]` / `[[timeanddate-com]]` (same site, other time tools) and with a dedicated sun-position/shadow tool (e.g. SunCalc): do both to cross-check azimuth/elevation and to visualise the shadow geometry over a map.

## Trust & verifiability
`trust: trusted` — timeanddate.com is an authoritative, widely-cited astronomical reference; its sun/moon figures are dependable, so the reliability of your conclusion rides on your input location/date, not the calculator.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | astronomy-sun-moon-eclipses |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
