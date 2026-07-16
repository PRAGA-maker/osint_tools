---
id: gaisma
name: Gaisma
description: Use when you have a candidate `geolocation` and photo shadows/sun position and want sunrise/sunset/solar-angle data to confirm or time the shot — returns solar timing data.
url: https://www.gaisma.com/en/
category: geolocation
path:
- geolocation
bestFor: Looking up sunrise, sunset, dawn, dusk and sun-path data for a named location to sanity-check where/when a photo was taken.
selectorsIn:
- geolocation
- image
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free reference site; no account or payment. (Enum lacks a "free-reference" nuance — there is no paid tier.)
opsec: passive
opsecNote: You look up a location's solar data on a static reference site — nothing about the subject is transmitted and no one is notified. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running free reference site for solar/climate data by location; astronomical values are standard almanac calculations, reliable for the coarse checks OSINT needs.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- gaisma.com
tags:
- Maps, Geolocation and Transport
- Nature
source: cyb-detective
lastVerified: '2026-07-16'
enrichment: full
---

# Gaisma

> A simple global reference for sunrise/sunset, dawn/dusk and sun-path data by location — a lightweight way to reason about shadows and lighting when chronolocating a photo.

## When to use
You have a candidate `geolocation` for an outdoor photo (from EXIF, a landmark, or a guess) and want to test it against the sun: does the shadow direction and length in the image fit sunrise/sunset times and the sun's azimuth for that place and season? Or you have a confirmed place and want to bound *when* a shot was taken from the lighting.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open gaisma.com and browse by continent or search for the nearest listed city/location to your candidate site.
2. Read the location page: monthly sunrise/sunset/dawn/dusk tables, day length, and sun-path/declination data.
3. Compare against your photo — shadow direction implies sun azimuth; shadow length implies sun elevation; both must be consistent with the date/time you suspect.
4. Cross-check with a fuller sun-position tool (SunCalc, timeanddate.com) for exact azimuth/elevation at a specific timestamp — Gaisma is the quick sanity pass.
5. Pivot: a confirmed or refuted location tightens or breaks your geolocation hypothesis; a plausible time-window narrows a timeline.

## Inputs → Outputs
- **In:** a candidate `geolocation` (place/coords) and an `image` whose lighting you're analyzing
- **Out:** solar timing/position data that supports or contradicts the candidate `geolocation`/time
- **Empty/negative result looks like:** no listed location near your coordinates (Gaisma is city-indexed, not arbitrary-coordinate) — use SunCalc/timeanddate for precise coordinates instead.

## Gotchas & OpSec
- It's city/place indexed, not a click-anywhere map — for exact coordinates a dedicated sun-position calculator is better.
- Data is coarse (monthly tables); for minute-level shadow analysis use a precise tool.
- Interface is dated but the almanac values are standard and trustworthy for coarse checks.
- OpSec: fully passive reference lookup.

## Overlaps ("do both")
- Pairs with precise sun-position calculators (SunCalc, timeanddate.com) — Gaisma gives a fast, simple read; the calculators give exact azimuth/elevation for a specific timestamp and coordinate.

## Trust & verifiability
`trust: community` — an independent free reference; its solar figures are standard astronomical calculations, so they're reliable, but confirm precise angles with a coordinate-level tool before drawing firm conclusions.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gaisma |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, image → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
