---
id: firms
name: FIRMS
description: Use when you have a `geolocation`/date and want to know if a fire or thermal anomaly was detected there — returns satellite-detected active-fire points with timestamps.
url: https://firms.modaps.eosdis.nasa.gov/map/
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Checking NASA satellite active-fire/thermal-anomaly detections for a location and date range (near-real-time and historical).
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free NASA/EOSDIS service. Interactive map is open; the download API needs a free MAP_KEY.
opsec: passive
opsecNote: Querying satellite fire data is passive — it concerns places, not people, and touches nothing about a subject. Fully passive; only your IP hits NASA's servers.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by NASA's Earth Science Data Systems (FIRMS/EOSDIS); authoritative satellite detection data (MODIS/VIIRS), scientifically calibrated.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- nasa-firms
- nasa-worldview
- nasa-earthdata-search
- nasa-kids-club
aliases:
- Fire Information for Resource Management System
- NASA FIRMS
tags:
- satellite
- fire-detection
- geospatial
source: osint4all
lastVerified: '2026-07-16'
enrichment: full
---

# FIRMS

> NASA's Fire Information for Resource Management System — a map of satellite-detected active fires and thermal anomalies worldwide, near-real-time and historical, pinpointed by coordinate and timestamp.

## When to use
You have a `geolocation` and a date, and you need to know whether a fire or intense heat source was detected there — to corroborate a reported wildfire, an explosion/burn event, industrial activity, or the timing of a fire seen in imagery. It's a specialist geospatial-verification tool: it confirms *thermal events at a place and time*, not people, so relevance to missing-persons is indirect (event/timeline corroboration).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the FIRMS map and navigate to the area of interest.
2. Set the date range and choose the sensor (MODIS, VIIRS) and confidence filter.
3. Read the detected fire points: each has coordinates, acquisition date/time, sensor, and confidence.
4. For bulk/automated pulls, request a free MAP_KEY and use the download API.
5. Pivot: a confirmed detection anchors an event to a precise time/place, supporting or refuting a claim or a photo's alleged timing.

## Inputs → Outputs
- **In:** a `geolocation` + date range
- **Out:** satellite-detected active-fire/thermal points at that `geolocation` with timestamps and confidence
- **Empty/negative result looks like:** no detections — no thermal anomaly was seen (or it was below the sensor's threshold / obscured by cloud); absence isn't proof no fire occurred, just none detected.

## Gotchas & OpSec
- Resolution is coarse (375 m–1 km pixels) — it flags a general area, not an exact building.
- Detection depends on satellite overpass timing and cloud cover; brief or small fires can be missed.
- Confidence values matter — low-confidence points include false positives (e.g. hot industrial sites, sun glint).
- OpSec: fully passive.

## Overlaps ("do both")
- Pairs with `[[nasa-worldview]]` and Sentinel imagery — FIRMS flags *where/when* a thermal event was detected; imagery tools let you *see* the smoke/burn scar to confirm it.

## Trust & verifiability
`trust: trusted` — authoritative NASA satellite data; detections are scientifically calibrated, though interpretation (what caused a hotspot) still needs corroboration.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | firms |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
