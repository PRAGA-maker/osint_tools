---
id: noaa-data-access-viewer
name: NOAA Data Access Viewer
description: Use when you have a coastal U.S. `geolocation` and want authoritative imagery, land-cover, and lidar elevation data for it — returns downloadable geospatial imagery for that area.
url: https://coast.noaa.gov/dataviewer/#/
category: image-video-face
path:
- image-video-face
bestFor: Downloading authoritative aerial imagery, land-cover, and lidar elevation for coastal U.S. locations.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
- image
status: live
pricing: free
costNote: Free U.S. government (NOAA Office for Coastal Management) data portal; no account required.
opsec: passive
opsecNote: Passive — you browse and download public government geospatial datasets; nothing about a subject is submitted and no one is notified. NOAA logs standard web requests; use a clean session for sensitive investigations.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by NOAA (U.S. federal agency); the imagery, land-cover, and lidar are authoritative government sources.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- ncei-noaa-gov
- nexrad-data-inventory-search
- ngdc-bathymetry-map
- noaa-fisheries-vessel-search
aliases:
- NOAA Digital Coast Data Access Viewer
tags:
- Maps, Geolocation and Transport
- Satellite/aerial imagery
- lidar
source: cyb-detective
lastVerified: '2026-07-18'
enrichment: full
---

# NOAA Data Access Viewer

> NOAA's Digital Coast portal for downloading authoritative aerial imagery, land-cover, and lidar elevation data over coastal U.S. areas.

## When to use
A specialized geolocation/imagery aid for coastal U.S. cases: when you have a `geolocation` (a shoreline, waterway, or coastal parcel) and need authoritative aerial imagery, land-cover classification, or high-resolution lidar terrain — for verifying a location's appearance, elevation, and surroundings, or corroborating imagery-based geolocation. It's terrain/imagery data, not people data; use it to analyze a place, not to identify a person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://coast.noaa.gov/dataviewer/#/.
2. Navigate/zoom the map to your coastal `geolocation` of interest (or search a place/coordinates).
3. Draw an area of interest and browse the available datasets for that footprint: imagery, land cover, and lidar/elevation.
4. Customize (format, projection) and download the data for offline analysis in GIS or an image viewer.
5. Use the imagery/elevation to verify terrain features, confirm a geolocated photo's surroundings, or analyze access routes near a site.

## Inputs → Outputs
- **In:** a coastal U.S. `geolocation` / area of interest.
- **Out:** downloadable aerial `image`ry, land-cover layers, and lidar elevation for that footprint.
- **Empty/negative result looks like:** no datasets available for the drawn area — common inland or outside NOAA's coastal coverage.

## Gotchas & OpSec
- Coastal U.S. only: coverage is limited to U.S. coastal zones; inland/international areas aren't served here.
- Not real-time: datasets are periodic surveys, so imagery may be years old — check the collection date.
- Data, not identity: this characterizes terrain; pair with other tools for anything about people.
- OpSec: fully passive public government data.

## Overlaps ("do both")
- Pairs with `[[ncei-noaa-gov]]` and general satellite/aerial imagery tools — NOAA gives authoritative coastal lidar/land-cover, others give broader or more current overhead imagery.

## Trust & verifiability
`trust: trusted` — first-party NOAA government data; authoritative for coastal imagery and elevation, with survey dates published for each dataset.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | noaa-data-access-viewer |
| category | image-video-face |
| selectorsIn → selectorsOut | geolocation → geolocation, image |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
