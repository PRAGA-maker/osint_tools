---
id: google-earth-pro
name: Google Earth Pro
description: Use when you need a deep historical-imagery timeline, measurement, and high-quality exports for a location — the desktop power version of Google Earth.
url: https://www.google.com/intl/en/earth/versions/#earth-pro
category: geolocation
path:
- geolocation
bestFor: Desktop Google Earth with a rich historical-imagery slider, measurement, KML import/export, and high-res printing.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
- image
- metadata-exif
status: live
pricing: free
costNote: Free desktop download (formerly a paid product, now free for all).
opsec: passive
opsecNote: Desktop client streams Google imagery; no contact with the target. Google sees your imagery requests.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: trusted
trustNote: Google's official desktop earth client; the standard tool for historical-imagery analysis in OSINT and journalism.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- Google Earth Pro Desktop
tags:
- geospatial-research-and-mapping-tools
source: awesome-osint
lastVerified: ''
enrichment: full
---

# Google Earth Pro

> The free desktop version of Google Earth — its standout feature is a deep historical-imagery timeline, plus precise measurement, KML/KMZ import-export, and high-resolution exports.

## When to use
You have a `geolocation`/`address` and need to study how a place changed over time: was a structure, vehicle, or path present on a given date; when did a feature appear or vanish; what did a search area look like across years. The historical-imagery slider is far richer than the web version, making this the go-to for timeline-sensitive geolocation work.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download and install Google Earth Pro from the official versions page.
2. Search a place/coordinates; click the clock icon to open the historical-imagery slider and step through dates.
3. Use Ruler for distances/areas, add placemarks/paths, and import case KML.
4. Export high-res images or a movie of the timeline for the case file (imagery dates are shown — capture them as `metadata-exif`).
5. Pivot: confirm street-level detail in `[[google-maps]]`; pull additional dated scenes from `[[earthexplorer]]`.

## Inputs → Outputs
- **In:** `geolocation` or `address`.
- **Out:** dated historical `image` views with acquisition `metadata-exif` (imagery date), measurements, KML.
- **Empty/negative result looks like:** sparse historical layers in remote regions — the slider may show only a few dates, or none recent.

## Gotchas & OpSec
- Human-in-the-loop: none; it's a local install (`localInstall: true`).
- Always record the imagery date shown in the slider — undated screenshots are weak evidence.
- OpSec: passive; Google sees imagery requests, target is not contacted.

## Overlaps ("do both")
- Pairs with `[[google-earth]]` (web, lighter) and `[[earthexplorer]]` (USGS archive) — Pro is the best free historical-imagery slider; EarthExplorer has the broader raw catalog.

## Trust & verifiability
`trust: trusted` — Google's official desktop client; imagery is authoritative and each layer is dated, supporting verifiable timeline analysis.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-earth-pro |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → image, metadata-exif |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | no |
