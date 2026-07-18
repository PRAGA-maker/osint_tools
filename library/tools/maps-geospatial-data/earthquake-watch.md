---
id: earthquake-watch
name: Earthquake Watch
description: Use when you have a `geolocation` and want recent seismic events there — returns geolocated earthquakes with magnitude, depth, and time.
url: https://www.arcgis.com/apps/dashboards/c8af9c5411814584b460cc87cb7c3780
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Checking recent earthquakes near a location — magnitude, depth, and timing — as situational context.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: Free ArcGIS dashboard over public earthquake feeds (USGS-style seismic data); no account to view.
opsec: passive
opsecNote: Passive — you view a public seismic dashboard; nothing about your query is exposed and no subject is involved. It maps natural events, not people.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party ArcGIS dashboard presenting authoritative public seismic feeds; the underlying earthquake data is scientific, the dashboard is a community-built viewer.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- modis-wildfire
- nasa-firms
aliases:
- Earthquake dashboard
tags:
- Maps, Geolocation and Transport
- earthquake
- disaster
source: osint4all
lastVerified: '2026-07-18'
enrichment: full
---

# Earthquake Watch

> An ArcGIS dashboard of recent earthquakes — see seismic events near a location with magnitude, depth, and time.

## When to use
You have a `geolocation` and want to know whether recent earthquakes occurred there and how strong they were. Like other disaster-mapping tools, this is situational context: corroborating that a seismic event affected an area around a relevant date (relevant to a disappearance, evacuation, damage claim, or verifying reports/imagery of an earthquake), rather than anything about a specific person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the dashboard at the ArcGIS URL.
2. Pan/zoom to the `geolocation` of interest.
3. Read the plotted quakes: each point carries magnitude, depth, and origin time; use filters to bound the window.
4. Note the strongest/closest events relative to your date and place of interest.
5. Pivot: confirmed seismic timing/location corroborates a timeline; for rigorous work, verify against the USGS earthquake catalog directly.

## Inputs → Outputs
- **In:** `geolocation` (+ optional time window)
- **Out:** geolocated earthquake events with magnitude, depth, and timestamp (`geolocation` context layer)
- **Empty/negative result looks like:** no events in the area/window — no recorded seismicity there in that period; absence is normal for aseismic regions and is not evidence of anything about a person.

## Gotchas & OpSec
- Small quakes below the feed's magnitude threshold, or in poorly-instrumented regions, may be missing.
- It maps natural events, not people — no personal data.
- The dashboard is a third-party viewer; for authoritative figures, confirm against USGS.
- OpSec: fully passive.

## Overlaps ("do both")
- Pairs with `[[modis-wildfire]]` and `[[nasa-firms]]` — the same "what disaster context affected this place and when" question for fires; use the relevant hazard layer for your scenario.

## Trust & verifiability
`trust: community` — a community-built dashboard over authoritative seismic feeds; the earthquake data is scientific and reliable, but confirm critical figures against the USGS catalog.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | earthquake-watch |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
