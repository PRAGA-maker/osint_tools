---
id: apple-maps
name: Apple Maps
description: Use when you have an `address` or `geolocation` and want an independent basemap plus street-level "Look Around" imagery to verify or geolocate a place — returns precise `geolocation` and street-level `image`s.
url: https://www.apple.com/maps/
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: A second-source basemap and Look Around street-level imagery for geolocation and place verification, distinct from Google's coverage.
selectorsIn:
- address
- geolocation
selectorsOut:
- geolocation
- image
status: live
pricing: free
costNote: Free consumer mapping service from Apple; the web version is public (no Apple ID needed to browse), the app ships on Apple devices.
opsec: passive
opsecNote: Browsing maps and imagery reveals nothing to any subject. Apple logs map requests against your device/IP (and Apple ID if signed in) — use a clean session and stay signed out for sensitive lookups.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party Apple mapping data and imagery; an authoritative, independently-collected basemap that usefully differs from Google's coverage and capture dates.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- google-maps
- google-earth
- bing-maps
aliases:
- Apple Maps Look Around
- maps.apple.com
tags:
- bellingcat-toolkit
- maps
source: bellingcat-toolkit
lastVerified: '2026-07-23'
enrichment: full
---

# Apple Maps

> Apple's first-party map with satellite/3D imagery and street-level "Look Around" — a second, independently-captured basemap for cross-checking a location against Google.

## When to use
You have an `address` or `geolocation` and want to confirm what's actually there, or you're geolocating a photo and need imagery from a *different* provider than Google. Because Apple collects its own imagery on its own schedule, Look Around and Apple's satellite layer frequently show a different capture date or angle than Street View — which can resolve a geolocation that Google's imagery leaves ambiguous, or reveal change over time when the two disagree.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open Apple Maps on the web (maps.apple.com / linked from apple.com/maps) or the app on an Apple device.
2. Search the `address` or drop a pin at the `geolocation`.
3. Switch layers — Standard, Satellite/Hybrid, and 3D where available.
4. Where the Look Around (binoculars) icon appears, open street-level imagery and pan/move through it.
5. Pivot: confirmed coordinates feed a report or a chronolocation; a distinctive feature in Look Around cross-references against `[[google-maps]]` Street View for date/detail differences.

## Inputs → Outputs
- **In:** `address` or `geolocation`
- **Out:** precise `geolocation` (coordinates), satellite/3D and street-level `image`s of the site
- **Empty/negative result looks like:** no Look Around available for the pin (coverage is far thinner than Google Street View outside major regions), or the address doesn't resolve — fall back to Google/Bing rather than assuming the place doesn't exist.

## Gotchas & OpSec
- Look Around coverage is much narrower than Google Street View — expect gaps outside large cities and certain countries. Absence of imagery is a coverage gap, not evidence.
- Full 3D/Look Around fidelity historically favored the app over the web; if the web view is thin, the mobile app may show more.
- OpSec: passive — no target-side visibility; stay signed out of your Apple ID for sensitive sessions.

## Overlaps ("do both")
- Pairs with `[[google-maps]]`, `[[google-earth]]` and `[[bing-maps]]` — always geolocate across providers: differing capture dates and angles between Apple Look Around and Google Street View are exactly what confirm (or break) a location hypothesis.

## Trust & verifiability
`trust: trusted` — first-party Apple data and imagery; its main value in OSINT is precisely that it is collected independently of Google, giving you a genuine second source rather than a mirror.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | apple-maps |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | address, geolocation → geolocation, image |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
