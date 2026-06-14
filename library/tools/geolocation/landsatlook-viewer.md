---
id: landsatlook-viewer
name: LandsatLook Viewer
description: Use when you need to confirm or date a rural/wilderness location from satellite imagery — returns Landsat scenes and acquisition metadata for a geolocation.
url: https://landsatlook.usgs.gov/
category: geolocation
path:
- geolocation
bestFor: Multi-year Landsat imagery review and land-cover change detection for a coordinate or area.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
- metadata-exif
status: live
pricing: free
costNote: Free, US government (USGS/NASA) public data; no account required.
opsec: passive
opsecNote: Reads public USGS imagery archives; no contact with the target and nothing about your search reaches them.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official USGS/NASA viewer over the public Landsat archive; authoritative government data source.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases: []
tags:
- satellite
- imagery
- change-detection
source: arf-seed
lastVerified: ''
enrichment: full
---

# LandsatLook Viewer

> USGS web viewer for the full Landsat satellite archive — best for reviewing how a coordinate or area changed across decades of moderate-resolution imagery.

## When to use
You have a `geolocation` (a coordinate, AOI, or place the subject was last associated with) in a rural, wilderness, or industrial setting and want to see the land at a specific date or watch how it changed over time. Useful for confirming that a feature (a structure, vehicle pull-off, cleared ground, water body) existed on or before a given date, or for spotting seasonal/landscape change that narrows where someone could have been. Not a tool for street-level detail — Landsat is 15–30 m resolution, so individual people, cars, or houses are not resolvable.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://landsatlook.usgs.gov/ and pan/zoom to your area, or paste coordinates.
2. Use the date slider/filter to pick a time window; filter by cloud cover so scenes are usable.
3. Switch band combinations (natural color, false color, NDVI) to highlight vegetation, water, or bare ground.
4. Read scene metadata (acquisition date, sensor, path/row) to anchor what you see to a specific day.
5. Pivot to higher-resolution imagery (`[[mapillary]]`, Google Earth historical, commercial satellite) once Landsat tells you which dates/areas matter.

## Inputs → Outputs
- **In:** `geolocation` (coordinate or area of interest)
- **Out:** dated `geolocation` imagery context plus scene `metadata-exif` (acquisition date, sensor, cloud cover)
- **Empty/negative result looks like:** persistent cloud cover, no scenes in the chosen window, or a feature too small to resolve at Landsat scale — switch dates or move to commercial/aerial imagery.

## Gotchas & OpSec
- Human-in-the-loop: you must visually interpret imagery and judge dates; nothing is automated.
- Resolution is the hard limit — do not claim to "see" a person, vehicle, or small structure in Landsat.
- OpSec: fully passive; reads a public government archive, leaks nothing to the subject.

## Overlaps ("do both")
- Pairs with high-resolution viewers and ground-level imagery (e.g. `[[mapillary]]`) — Landsat dates and contextualizes broad change; street/aerial imagery confirms detail.

## Trust & verifiability
`trust: trusted` — official USGS/NASA viewer over the canonical Landsat archive; data provenance is government-grade and each scene carries verifiable acquisition metadata.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | landsatlook-viewer |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation, metadata-exif |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
