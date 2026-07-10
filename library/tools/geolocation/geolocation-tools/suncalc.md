---
id: suncalc
name: SunCalc
description: Use when you have coordinates and a photo with shadows and want to verify time/location (chronolocation) — returns sun azimuth/elevation and shadow direction for any place and moment.
url: https://suncalc.net/
category: geolocation
path:
- geolocation
- geolocation-tools
bestFor: Chronolocation — checking whether the sun position/shadows in a photo are consistent with a claimed place, date and time.
selectorsIn:
- geolocation
- image
selectorsOut:
- metadata-exif
- geolocation
status: live
pricing: free
costNote: Free web tool; no account.
opsec: passive
opsecNote: Purely a calculation over map/astronomical data — you don't touch the subject or any account. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Sun-position math is deterministic astronomy; SunCalc's azimuth/elevation output is reliable. The interpretation (matching shadows in a photo) is where analyst error enters, not the data.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- online-exif-viewer
- google-reverse-image-search
aliases:
- suncalc.net
- SunCalc.org
tags:
- geolocation
- chronolocation
- shadows
- verification
source: arf-seed
lastVerified: '2026-07-10'
enrichment: full
---

# SunCalc

> A sun-position calculator for chronolocation — given a location, date and time it returns the sun's azimuth/elevation and shadow direction, so you can test whether a photo's shadows match a claimed place and moment.

## When to use
You have a photo with visible shadows (or the sun itself) and a candidate `geolocation`, and you want to verify or narrow *when* and *where* it was taken. By comparing the shadow direction/length in the image to SunCalc's predicted sun position, you can confirm a claimed time/date, expose a fake, or estimate the time a photo was taken at a known place — a core Bellingcat-style geolocation/chronolocation technique.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://suncalc.net/ and drop the pin on the candidate location (or enter coordinates).
2. Set the date and drag the time; the tool shows sun azimuth/elevation and the shadow direction line on the map.
3. Compare to the photo: does the shadow direction/length and sun height match? Sweep the time to find when it would match.
4. If shadows can't match at that location on that date, the claim is inconsistent — investigate.
5. Pivot: combine with `[[online-exif-viewer]]` (any embedded GPS/timestamp to test against) and `[[google-reverse-image-search]]` to pin the exact spot before running SunCalc.

## Inputs → Outputs
- **In:** `geolocation` (coordinates) + date/time; and an `image` with shadows to compare
- **Out:** `metadata-exif`-style astronomical data (sun azimuth/elevation, shadow bearing) that confirms/narrows the photo's `geolocation`/time
- **Empty/negative result looks like:** no time on the given date produces the observed shadow geometry — meaning the location or the claimed date/time is wrong (a finding, not a failure).

## Gotchas & OpSec
- You need a reasonably exact location first — SunCalc verifies a hypothesis, it doesn't find the spot; pin it via reverse-image/landmark work.
- Shadow reading is error-prone (foreshortening, uneven ground, DST/timezone); double-check the timezone and be conservative.
- OpSec: fully passive calculation.

## Overlaps ("do both")
- Pairs with `[[online-exif-viewer]]` (test embedded timestamp/GPS against the sun geometry) and `[[google-reverse-image-search]]` (establish the location to plug in). Do both: locate, then chronolocate.

## Trust & verifiability
`trust: trusted` — the underlying astronomy is exact; reliability hinges on your location estimate and careful shadow interpretation, so state assumptions and cross-check the timezone.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | suncalc |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, image → metadata-exif, geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
</content>
