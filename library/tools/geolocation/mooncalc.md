---
id: mooncalc
name: MoonCalc
description: Use when an outdoor photo shows the moon and you need its azimuth/elevation/phase at a date+place to confirm or break a claimed time and location.
url: https://www.mooncalc.org/
category: geolocation
path:
- geolocation
bestFor: Reconstructing moon position, phase, and rise/set for a location and timestamp to validate photo/video chronolocation.
selectorsIn:
- image
- geolocation
- metadata-exif
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free web app by the SunCalc author (Torsten Hoffmann). No account needed.
opsec: passive
opsecNote: All computation is client-side from a date and coordinates you enter; nothing about your target is sent to a third party of interest. No contact with the subject.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: community
trustNote: Widely used companion to SunCalc in the OSINT/chronolocation community; astronomical math is standard and reproducible, but you must interpret the overlay correctly.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Moon Calc
tags:
- geolocation
- chronolocation
- celestial
source: metaosint
lastVerified: ''
enrichment: full
---

# MoonCalc

> Shows the moon's azimuth, altitude, phase, and rise/set for any place and time — the lunar counterpart to SunCalc for chronolocation.

## When to use
You have an outdoor `image`/video where the moon is visible (or shadows imply a lit moon) plus a candidate `geolocation` or a claimed timestamp from `metadata-exif`. Use MoonCalc to compute where the moon *should* have been and cross-check it against the photo — confirming, narrowing, or disproving the claimed time/place. Strong for verifying the last-seen circumstances of a missing person against posted media.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open mooncalc.org and drag the map pin (or search) to the candidate location.
2. Set the date and time (use the timeline slider to sweep the day).
3. Read the moon's azimuth (compass bearing of the moonlight/disc) and altitude (height above horizon), plus phase and rise/set times.
4. Compare the predicted moon direction/elevation and illuminated fraction to the photo. Pivot to [[suncalc]]-style sun analysis for daytime shadows, and to terrain/peak tools for horizon matching.

## Inputs → Outputs
- **In:** `image`/video showing the moon, candidate `geolocation`, and a date/time (often from `metadata-exif`).
- **Out:** confirmed/refuted `geolocation` + time window (the moon geometry that fits).
- **Empty/negative result looks like:** the predicted moon is below the horizon or in a different bearing than the photo shows — the claimed time or place is wrong.

## Gotchas & OpSec
- Human-in-the-loop: you must read the azimuth/altitude overlay and match it to the scene; easy to misjudge bearing without a known reference object.
- Phase must also match the visible illuminated fraction — a useful independent check.
- Time zone / DST and local vs UTC errors are the most common mistakes; verify the displayed timezone.
- OpSec: fully passive; no target contact.

## Overlaps ("do both")
- Pairs with sun-position tools (SunCalc) and peak/horizon matchers like [[peakfinder]] — combine celestial geometry with terrain to lock a location.

## Trust & verifiability
`trust: community` — standard, reproducible astronomy from a reputable author; results are independently checkable, so confidence is high when the geometry is read correctly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mooncalc |
| category | geolocation |
| selectorsIn → selectorsOut | image, geolocation, metadata-exif → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |
