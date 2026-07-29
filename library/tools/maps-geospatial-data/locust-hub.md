---
id: locust-hub
name: Locust Hub
description: Use when you have a `geolocation` in the desert-locust belt and want FAO survey/swarm data and maps for tracking infestations — returns geolocation and metadata-exif (survey record) leads.
url: https://locust-hub-hqfao.hub.arcgis.com/
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: FAO desert-locust survey, swarm, hopper-band and control data as interactive maps and downloadable GIS datasets.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
- metadata-exif
status: live
pricing: free
costNote: Free public FAO ArcGIS Hub; no account required to view maps or download open datasets.
opsec: passive
opsecNote: Fully passive — a public FAO data portal. Viewing or downloading reveals nothing about any person; it concerns insect/agricultural monitoring, not individuals.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official FAO (UN Food and Agriculture Organization) Locust Hub; authoritative for desert-locust survey and control data.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- FAO Locust Hub
- Desert Locust Hub
tags:
- bellingcat-toolkit
- environment-wildlife
- fao
source: bellingcat-toolkit
lastVerified: '2026-07-29'
enrichment: full
---

# Locust Hub

> The FAO's open desert-locust data portal — survey observations, swarms, hopper bands and control operations as interactive maps and downloadable GIS layers across the affected region.

## When to use
You have a `geolocation` within the desert-locust belt (North/East Africa, the Middle East, South Asia) and need FAO's ground-truth locust data for that area: where surveys were done, where swarms/hopper bands were recorded, dates, and control interventions. Relevant for agricultural/food-security investigations, environmental monitoring, or corroborating on-the-ground conditions (e.g. why a region is under stress) at a point in time. It's geospatial insect-monitoring data, not people data.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://locust-hub-hqfao.hub.arcgis.com/.
2. Browse the interactive maps/dashboards; pan/zoom to your `geolocation` and filter by data type (adults, hoppers, bands, swarms, control) and date.
3. Click features for the survey record (date, stage, location, source).
4. Download the underlying datasets (via the Hub's open-data/API endpoints) for offline GIS analysis.
5. Pivot: a survey point's date/location → correlate with satellite imagery or field reports for that area and time.

## Inputs → Outputs
- **In:** a `geolocation` / area + date range
- **Out:** locust survey/swarm/band records with coordinates and dates (`geolocation` + record `metadata-exif`), downloadable GIS layers
- **Empty/negative result looks like:** no records for an area/date — either no survey occurred there or it's outside the locust range; absence means no FAO observation, not necessarily no locusts.

## Gotchas & OpSec
- Coverage is limited to the desert-locust affected region and to where surveys were actually conducted.
- Data reflects reported observations — gaps are common in insecure or remote areas.
- OpSec: fully passive public data portal.

## Overlaps ("do both")
- Complements satellite/NDVI vegetation tools and general GIS/mapping resources — the Locust Hub gives the ground observations; imagery gives the environmental context.

## Trust & verifiability
`trust: trusted` — official FAO data hub; authoritative for desert-locust survey and control information.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | locust-hub |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation → geolocation, metadata-exif |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
