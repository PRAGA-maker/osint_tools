---
id: localfocus-nl-geokit
name: localfocus.nl/geokit
description: Use when you have a list of `address`es or raw coordinates and want to convert them into map-ready `geolocation` data — returns batch-geocoded coordinates, reprojected/converted formats, and admin-boundary joins.
url: https://www.localfocus.nl/geokit/
category: geolocation
path:
- geolocation
bestFor: Free browser GIS utilities for journalists — batch geocoding, coordinate reprojection, KML conversion, and spatial joins.
selectorsIn:
- address
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free, web-based, no download and no account required for the GeoKit tools.
opsec: passive
opsecNote: You paste address/coordinate lists into a browser tool that calls a geocoding backend; the subject is not contacted. Your pasted data is processed by LocalFocus/their geocoder, so don't paste sensitive victim addresses you wouldn't want a third party to handle — batch small, non-identifying sets or self-host geocoding for sensitive work.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Maintained by LocalFocus, a reputable data-journalism tooling company; conversions are deterministic GIS operations and geocoding quality depends on the underlying provider.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- localfocus
aliases:
- LocalFocus GeoKit
- geokit
tags:
- Maps, Geolocation and Transport
- Tools
- geocoding
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# localfocus.nl/geokit

> A free browser GIS toolkit for journalists: turn address lists into coordinates, reproject between coordinate systems, convert KML, and join points to administrative boundaries — the plumbing that gets messy location data onto a map.

## When to use
You have location data that isn't yet map-ready and need to normalise it: a spreadsheet of `address`es to batch-geocode into coordinates, raw coordinates in one system (e.g. Dutch Amersfoort/RD) that must become WGS84 lat/long, a KML file to flatten into a table, or a set of points you want tagged with the administrative region (municipality/county) they fall in. It's a preparation/enrichment step in a geolocation workflow, not a discovery tool.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.localfocus.nl/geokit/ and pick the tool you need (geocoder, coordinate converter, KML-to-table, boundary/spatial join, map styler).
2. Paste your data — an address list for the geocoder, or coordinate rows for the converter — following the on-page format.
3. Run the conversion; the tool returns coordinates / reprojected values / joined boundary names you can copy back out.
4. Sanity-check a few results against a map (geocoding can mis-hit ambiguous or partial addresses) before trusting the batch.
5. Pivot: clean `geolocation` coordinates feed mapping, radius/isochrone (e.g. [[smappen]]), and imagery tools; boundary joins help aggregate points by region.

## Inputs → Outputs
- **In:** `address` list or `geolocation` (coordinates/KML)
- **Out:** `geolocation` (batch-geocoded coordinates, reprojected values, boundary-tagged points)
- **Empty/negative result looks like:** a geocoder row returning no match or a low-confidence/centroid hit for a vague address — flag those and verify manually rather than treating every returned coordinate as exact.

## Gotchas & OpSec
- Human-in-the-loop: none; paste-and-run, no login.
- OpSec: **passive** toward the subject, but pasted data is processed server-side by LocalFocus's geocoder — keep sensitive victim addresses out of it, or geocode those with a self-hosted service.
- Accuracy: geocoding quality varies with address completeness and the backend provider; ambiguous inputs may snap to a city centroid. Always spot-check.

## Overlaps ("do both")
- Pairs with [[localfocus]] (the broader LocalFocus mapping suite) and with mapping/isochrone tools like [[smappen]] — GeoKit produces the clean coordinates those tools then visualise or analyse.

## Trust & verifiability
`trust: community` — LocalFocus is a well-regarded data-journalism outfit and the conversions are standard, inspectable GIS operations; the main variable is third-party geocoding accuracy, which you verify by spot-checking outputs on a map.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | localfocus-nl-geokit |
| category | geolocation |
| selectorsIn → selectorsOut | address, geolocation → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
