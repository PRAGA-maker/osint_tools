---
id: emily-bz
name: emily.bz
description: Use when you have a Google Street View panorama URL and want its exact capture time — returns the precise timestamp (to ~2s) of that pano, a strong chronolocation signal (`metadata-exif`).
url: https://pano-date.emily.bz/
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Recovering the exact capture date/time of a Google Street View panorama for chronolocation.
selectorsIn:
- geolocation
selectorsOut:
- metadata-exif
status: live
pricing: free
costNote: Free and open-source; no account. Runs against Google's Street View data.
opsec: passive
opsecNote: You submit a Street View pano URL to the tool, which queries Google's imagery metadata — the subject is not involved and nothing is revealed to them. Passive chronolocation research; use a clean browser.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Open-source project (GitHub + write-up) by the author; results derive from Google's own pano metadata, so the timestamp is as authoritative as Google's data.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- pano-date
- pano date resolver
- Street View pano date
tags:
- geolocation
- chronolocation
- street-view
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# emily.bz

> A "pano date resolver" — paste a Google Street View panorama URL and it returns the exact moment that image was captured, down to a couple of seconds.

## When to use
You're doing chronolocation: you've matched a scene to a specific Google Street View panorama (a building, a corner, signage a subject stood near) and need to know *when* that Street View imagery was taken with precision far beyond Google's month/year label. The exact capture timestamp helps date-bound events, verify or refute a claim about when a place looked a certain way, and align imagery with other timeline evidence.

## How to use it (`bestInteractionPattern`: web-manual)
1. In Google Street View, navigate to the exact panorama and copy its full URL (not a shortened goo.gl link — those aren't supported).
2. Open https://pano-date.emily.bz/ and paste the pano URL.
3. Read the returned timestamp — accurate to ~2 seconds for supported panos.
4. If it fails, the pano may be older/unsupported — try a nearby/newer pano at the same location.
5. Pivot: the precise capture time anchors the imagery on your timeline and cross-checks against `metadata-exif` from photos, weather/air-quality records, or event dates.

## Inputs → Outputs
- **In:** a full Google Street View panorama URL (a `geolocation` anchor)
- **Out:** the exact capture timestamp of that pano (`metadata-exif`-grade time)
- **Empty/negative result looks like:** an error or no timestamp — usually an unsupported/older pano or a shortened URL; retry with a full URL or a different (often newer) pano.

## Gotchas & OpSec
- Only works on full pano URLs; shortened links fail. Older historical imagery may be unsupported.
- It dates the *Google imagery*, not your subject — a precise capture time tells you when Street View drove by, which you then reason about relative to the event.
- OpSec: passive; only Google's metadata is queried, nothing about the subject.

## Overlaps ("do both")
- Pairs with Google Street View / Earth and general chronolocation workflows — Street View gives the scene match, emily.bz pins the exact capture time; combine with weather-history or EXIF timestamps to triangulate a date.

## Trust & verifiability
`trust: community` — an open-source tool with a public write-up; because it reads Google's own pano metadata, the timestamp is authoritative to Google's data, and you can inspect the code to confirm the method.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | emily-bz |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation → metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
