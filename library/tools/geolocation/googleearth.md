---
id: googleearth
name: Google Earth
description: Use when you have an `address` or `geolocation` and want to study the place — satellite/3D imagery, historical timeline, terrain and measurements — returns geospatial `metadata-exif` context.
url: https://www.google.com/earth
category: geolocation
path:
- geolocation
bestFor: Visually studying and verifying a location — current and historical satellite/3D imagery, Street View, terrain and distance measurement.
selectorsIn:
- address
- geolocation
selectorsOut:
- geolocation
- metadata-exif
status: live
pricing: free
costNote: Free (web and desktop Pro); no account needed for the web version.
opsec: passive
opsecNote: You view Google's imagery of a place, not the subject — the target isn't notified. Fully passive. Note imagery is dated (months/years old), not a live feed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Google's first-party geospatial product; imagery is authoritative but time-stamped and periodically updated, not real-time.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Google Earth Pro
- Google Earth Web
tags:
- toddington
- curated-directory
- geo-location-mapping-tools
- satellite
- mapping
source: toddington-resources
lastVerified: '2026-07-11'
enrichment: full
---

# Google Earth

> Google's global geospatial browser: satellite and 3D imagery, Street View, a historical-imagery timeline, terrain and measurement tools — the core workspace for studying and verifying any location.

## When to use
You have an `address` or `geolocation` (coordinates) and need to *understand* the place: confirm what's there, study surroundings and access routes, compare how it looked across years (historical imagery), measure distances/areas, or corroborate a photo/video's setting for geolocation. Central to both verifying a claimed location and chronolocating imagery via the historical timeline.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://earth.google.com/ (web) or Google Earth Pro (desktop, for the richest tools).
2. Enter the `address` or paste `lat,long`; the view flies to the location.
3. Study it: switch to 3D/Street View, toggle **historical imagery** (desktop Pro) to scrub the timeline, and use the ruler to measure distances/areas.
4. For geolocation, match landmarks, roads, rooflines and terrain from a target photo/video against the imagery.
5. Pivot: confirmed coordinates feed mapping/records; the historical timeline supports chronolocation; nearby features become new leads.

## Inputs → Outputs
- **In:** `address` or `geolocation` (coordinates)
- **Out:** confirmed `geolocation`, geospatial `metadata-exif` context (imagery date, terrain, measurements, historical views)
- **Empty/negative result looks like:** low-resolution or cloud-obscured imagery, or no 3D/Street View for remote areas — the place exists but detail is limited; try dates in the historical timeline or other providers.

## Gotchas & OpSec
- Imagery is **dated** (months to years old), not live — always check the capture date before drawing time-sensitive conclusions.
- Historical-imagery scrubbing is a **Pro/desktop** feature; the web version is more limited.
- Resolution and 3D coverage vary hugely by region — rural/remote areas may be coarse.

## Overlaps ("do both")
- Pairs with Google Maps/Street View, Bing Maps, Yandex Maps and Sentinel/satellite tools — cross-check because imagery date, angle and resolution differ per provider, which matters for verification and chronolocation.

## Trust & verifiability
`trust: trusted` — Google's first-party imagery is authoritative, but every view is time-stamped and periodically refreshed; anchor conclusions to the imagery capture date, not "now."

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | googleearth |
| category | geolocation |
| selectorsIn → selectorsOut | address, geolocation → geolocation, metadata-exif |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
