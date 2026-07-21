---
id: gpx-file-editor
name: GPX File Editor
description: Use when you have a `.gpx`/`.kml` track file (with embedded `metadata-exif` timestamps) and want to view, edit and read the route, points and timings on a map — returns `geolocation`.
url: https://gpx.studio/
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Viewing, inspecting and editing GPS track files (GPX/KML) on an interactive map, including per-point coordinates and timestamps.
selectorsIn:
- metadata-exif
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free, open-source web app (gpx.studio); no account required for viewing/editing, runs in the browser.
opsec: passive
opsecNote: Files can be processed locally in your browser, but do not upload a subject's track to any cloud/sharing feature; keep the analysis offline on a controlled machine.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Open-source project (github.com/gpxstudio) maintained by a small team; it renders the file you give it, so there is no third-party data-quality risk — only tool availability.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- gps-visualizer
- qgis
- gridreferencefinder-com
aliases:
- gpx.studio
- GPX viewer/editor
tags:
- maps-geospatial-data
- gpx
- gps-track
- route-analysis
source: osint4all
lastVerified: '2026-07-21'
enrichment: full
---

# GPX File Editor

> The online GPX/KML editor — drop in a recorded GPS track and read every point's coordinates and timestamp on a map, or clean/trim a route for analysis.

## When to use
You have recovered a `.gpx` or `.kml` file — from a fitness app export, a device, a drone log, or a strava-style share — and need to see where the track went and *when*. Each trackpoint can carry a lat/long plus a timestamp, so a GPX file is effectively a movement history: last-seen locations, a commute pattern, a route to a specific address. Use this to visualise the path and extract the exact `geolocation` of start/stop/waypoints and their times.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://gpx.studio/ and load the file (File → Load, or drag-and-drop the `.gpx`/`.kml`).
2. The track renders on the map; hover or click points to read coordinates and elevation, and open the elevation/time panel to see timing.
3. Inspect start and end points and any pauses — these are candidate "last known location" and dwell points; copy the lat/long for pivoting.
4. If needed, edit/trim/split the track (remove noise, isolate a segment) and re-export a clean `.gpx`.
5. Pivot: drop extracted coordinates into `[[gps-visualizer]]` for alternative rendering, `[[qgis]]` for layered analysis, or a reverse-geocoder to turn coordinates into an `address`.

## Inputs → Outputs
- **In:** a `.gpx`/`.kml` track file carrying `metadata-exif`-style timestamps and `geolocation` points
- **Out:** `geolocation` — per-point coordinates, route shape, start/stop points and their times
- **Empty/negative result looks like:** a file that loads but shows no track (route-only with no timestamps), or a parse error on a malformed/empty file — meaning no usable movement data, not that the subject didn't travel.

## Gotchas & OpSec
- Human-in-the-loop: none for viewing; editing is manual.
- OpSec: passive — the tool renders locally; the risk is *you* leaking the file by using any share/upload feature. Never publish the loaded track.
- Not all GPX files contain time data — a "route" (planned) has coordinates but no timestamps, while a "track" (recorded) usually has both; only the latter proves movement.

## Overlaps ("do both")
- Pairs with `[[gps-visualizer]]` — that converts and maps many GPS formats and is handy for a second rendering or batch conversion, while this is the interactive editor.
- Pairs with `[[qgis]]` when you need to overlay the track on other geospatial layers.

## Trust & verifiability
`trust: community` — an open-source browser tool; it only displays the data you supply, so accuracy is entirely a property of the source file, not the tool.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gpx-file-editor |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | metadata-exif, geolocation → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
