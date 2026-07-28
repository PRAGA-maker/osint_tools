---
id: rammb-slider
name: RAMMB SLIDER
description: Use when you have a `geolocation`/`address` and want recent, time-stepped satellite imagery of that spot for weather/scene verification — returns time-stamped satellite `geolocation` views.
url: https://rammb-slider.cira.colostate.edu/
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Browsing zoomable, time-animated geostationary satellite imagery (GOES, Himawari, Meteosat) over any point on Earth.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free public tool from CIRA (Colorado State University) using NOAA/partner satellite data; no account.
opsec: passive
opsecNote: Passive imagery browsing — queries hit CIRA/NOAA servers, nothing touches any subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by CIRA at Colorado State University with official NOAA/EUMETSAT/JMA satellite feeds; an authoritative imagery source.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- SLIDER
- CIRA SLIDER
tags:
- bellingcat-toolkit
- satellite-imagery
- weather
- chronolocation
source: bellingcat-toolkit
lastVerified: '2026-07-28'
enrichment: full
---

# RAMMB SLIDER

> A fast, zoomable, time-animated window on geostationary weather satellites — scrub back through hours or days of imagery over any location.

## When to use
You have a `geolocation`/`address` and want to know what the sky and broad ground conditions looked like there at a given time — to chronolocate a photo/video by matching its weather and cloud patterns to the satellite record, to confirm a claimed date/place, or to observe large-scale events (smoke plumes, storms, flooding). SLIDER lets you pick a satellite/sector, pan to the spot, and step through time.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://rammb-slider.cira.colostate.edu/.
2. Choose the satellite covering your region (GOES-East/West for the Americas, Himawari for Asia-Pacific, Meteosat for Europe/Africa) and a sector.
3. Pan/zoom to your `geolocation`; pick a band/product (visible, infrared, etc.).
4. Use the time controls to animate or step to the date/time of interest.
5. Pivot: compare the observed cloud/weather pattern against a photo or claim to support or refute a time/place hypothesis; combine with ground-level imagery.

## Inputs → Outputs
- **In:** `geolocation` / `address` (navigate the viewer) + a target date/time
- **Out:** time-stamped geostationary satellite imagery over that `geolocation`
- **Empty/negative result looks like:** imagery unavailable for a very old date or a gap in a satellite's archive, or resolution too coarse to see a small feature — SLIDER shows weather/scene scale, not street-level detail.

## Gotchas & OpSec
- Geostationary imagery is **weather/regional scale**, not high-resolution ground detail — great for cloud/chronolocation, not for reading a license plate.
- Coverage and archive depth differ per satellite; the poles are poorly seen by geostationary sensors.
- OpSec: passive; browsing hits CIRA/NOAA only.

## Overlaps ("do both")
- Pair with high-resolution satellite/aerial tools and multi-provider map tools like [[mapswitcher]] — SLIDER supplies the weather/time context, those supply the ground-level detail.

## Trust & verifiability
`trust: trusted` — a university/NOAA-backed tool serving official satellite data; imagery is authoritative, and timestamps are reliable for chronolocation.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | rammb-slider |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation, address → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
