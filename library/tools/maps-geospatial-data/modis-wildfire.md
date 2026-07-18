---
id: modis-wildfire
name: MODIS Wildfire
description: Use when you have a `geolocation` and want recent satellite-detected active fires there — returns geolocated fire/thermal-anomaly points with detection times.
url: https://www.arcgis.com/apps/dashboards/bf5df3a49a624521844a2e5e1ec7df05
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Checking whether NASA's MODIS satellite detected active fires/thermal anomalies at a location and time.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: Free ArcGIS dashboard over NASA MODIS/FIRMS fire-detection data; no account to view. Bulk FIRMS data is also free but may need a NASA Earthdata login.
opsec: passive
opsecNote: Passive — you view a public satellite-fire dashboard; nothing about your query is exposed. It maps thermal anomalies, not people, so there is no subject to alert.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Underlying data is NASA MODIS/FIRMS active-fire detections (authoritative satellite science); the ArcGIS dashboard is a third-party presentation layer over that data.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- nasa-firms
- earth-engine-dataset
aliases:
- MODIS fire map
- MODIS thermal anomalies
tags:
- Maps, Geolocation and Transport
- wildfire
- satellite
source: osint4all
lastVerified: '2026-07-18'
enrichment: full
---

# MODIS Wildfire

> An ArcGIS dashboard over NASA MODIS satellite fire detections — see where active fires and thermal anomalies were spotted, and when.

## When to use
You have a `geolocation` and want to know whether satellites detected active fires or heat anomalies there around a given time. It maps NASA's MODIS active-fire product (thermal detections from orbit). In an investigation this is niche context: corroborating that a wildfire/burn was occurring at a location and date (relevant to a disappearance in a fire-affected area, verifying imagery/claims of a fire, or timelining an evacuation), rather than anything about a specific person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the dashboard at the ArcGIS URL.
2. Pan/zoom to the `geolocation` of interest.
3. Read the fire-detection points: each is a satellite thermal-anomaly hit with an acquisition date/time and confidence.
4. Use any time filter to bound detections to your window of interest.
5. Pivot: confirmed fire timing/location corroborates other evidence; for rigorous work, cross-check NASA FIRMS directly and note MODIS's coarse resolution.

## Inputs → Outputs
- **In:** `geolocation` (+ optional time window)
- **Out:** geolocated active-fire/thermal-anomaly detections with timestamps (`geolocation` context layer)
- **Empty/negative result looks like:** no detections in the area/window — either no fire large/hot enough for MODIS to catch, cloud cover blocked the view, or it fell between satellite passes; absence does NOT prove there was no fire.

## Gotchas & OpSec
- MODIS resolution is coarse (~1 km) and it only sees fires during satellite overpasses — small, brief, or cloud-covered fires are missed.
- Detections are thermal anomalies (could be industrial heat/flares), not confirmed wildfires; treat as a signal to verify.
- It maps environmental events, not people — no personal data here.
- OpSec: fully passive.

## Overlaps ("do both")
- Pairs with `[[nasa-firms]]` (the authoritative NASA fire-data source, including higher-resolution VIIRS) and `[[earth-engine-dataset]]` (for deeper geospatial/temporal analysis) — use this dashboard for a quick look and those for rigor.

## Trust & verifiability
`trust: trusted` — the fire detections are authoritative NASA satellite science; the dashboard is just a viewer, so for anything critical confirm against NASA FIRMS and account for MODIS's known resolution/timing limits.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | modis-wildfire |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
