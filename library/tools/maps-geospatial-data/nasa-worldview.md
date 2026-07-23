---
id: nasa-worldview
name: NASA Worldview
description: Use when you have a `geolocation`/date and want near-real-time or historical full-Earth satellite imagery for that spot — returns daily global satellite layers you can browse and download by date.
url: https://worldview.earthdata.nasa.gov/
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Browsing daily, date-selectable satellite imagery of a location for events, fires, floods, and change over time.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free US-government (NASA EOSDIS) service; no account needed to view or download imagery.
opsec: passive
opsecNote: Fully passive — you browse NASA's public imagery layers; nothing is queried about any person and no target is contacted. Safe to use freely.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by NASA's Earth Science Data and Information System (EOSDIS); authoritative government satellite data, though moderate resolution (hundreds of metres, not street-level).
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- firms
- nasa-earthdata-search
- nasa-firms
aliases:
- Worldview
- worldview.earthdata.nasa.gov
- NASA EOSDIS Worldview
tags:
- bellingcat-toolkit
- satellite-imagery
- geospatial
source: bellingcat-toolkit
lastVerified: '2026-07-23'
enrichment: full
---

# NASA Worldview

> NASA's daily full-Earth satellite browser: pick a location and a date and see near-real-time (or historical) imagery — ideal for dating events like fires, floods, smoke, and large-scale change.

## When to use
You have a `geolocation` and a date (or date range) and want to see what a place looked like from orbit at that time. Reach for Worldview to corroborate the timing of large events — wildfires, floods, dust/smoke plumes, ice/algae, big construction or destruction — or to establish "on date X, this area showed Y". It is daily, global, and date-selectable, which is its strength; its weakness is resolution (moderate, not street-level), so it's for landscape-scale, not identifying individuals or vehicles.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://worldview.earthdata.nasa.gov/ and navigate/search to your location.
2. Set the date with the timeline slider (imagery goes back years for many layers, up to near-real-time).
3. Toggle layers — true-colour (MODIS/VIIRS), fires/thermal anomalies (FIRMS), aerosols, etc. — to match your question.
4. Compare dates to see change; use the snapshot/download tool to export the image for your report.
5. Pivot: fire detections feed `[[nasa-firms]]`/`[[firms]]`; for higher resolution on a confirmed area, move to commercial/other satellite sources.

## Inputs → Outputs
- **In:** `geolocation`/`address` + a date
- **Out:** date-stamped satellite imagery layers of that area (a `geolocation`-anchored view), downloadable
- **Empty/negative result looks like:** cloud cover obscuring the ground, or a resolution too coarse to show the feature you need — the data exists but can't answer a street-level question.

## Gotchas & OpSec
- Moderate resolution: great for landscape/event scale, useless for identifying people, vehicles, or small structures.
- Clouds frequently block optical layers; try adjacent dates or non-optical layers.
- OpSec: passive; browsing public imagery exposes nothing.

## Overlaps ("do both")
- Pairs with `[[nasa-firms]]`/`[[firms]]` for fire-detection points and `[[nasa-earthdata-search]]` for the underlying granules; use higher-resolution satellite/aerial sources when Worldview is too coarse. Combine with historical-map tools for before/after context.

## Trust & verifiability
`trust: trusted` — authoritative NASA/EOSDIS imagery; the data is reliable, and the interpretive step (what a plume or change *is*, exact timing given clouds) is yours to confirm across dates and layers.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nasa-worldview |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation, address → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
