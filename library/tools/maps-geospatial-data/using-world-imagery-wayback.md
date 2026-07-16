---
id: using-world-imagery-wayback
name: Using World Imagery Wayback
description: Use when you have a `geolocation`/`address` and want to see how that spot looked in past satellite imagery — returns dated historical `geolocation` imagery for change analysis.
url: https://www.esri.com/arcgis-blog/products/arcgis-living-atlas/mapping/using-world-imagery-wayback
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Browsing Esri's archive of past World Imagery basemap versions to see a location at different points in time.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free to use via the Living Atlas Wayback app; no ArcGIS account required for basic browsing/comparison.
opsec: passive
opsecNote: You are viewing pre-captured satellite basemaps hosted by Esri; nothing is sent to or about the subject, so it is fully passive. Queries go to Esri's servers like any web map — standard hygiene suffices.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Esri's official World Imagery Wayback service (part of ArcGIS Living Atlas); imagery is authoritative commercial/aerial source data, with dozens of archived captures per area.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- esri
aliases:
- World Imagery Wayback
- ArcGIS Wayback
tags:
- maps
- satellite-imagery
- historical-imagery
source: metaosint
lastVerified: '2026-07-16'
enrichment: full
---

# Using World Imagery Wayback

> Esri's time-machine for satellite imagery — step back through dozens of archived captures of a location to see what changed, and when.

## When to use
You have a `geolocation` or `address` and need to see how it looked at earlier dates: to date a structure, spot a vehicle/object that appeared or vanished, corroborate when someone was present, or match a background in a photo to a specific time window. Historical imagery turns "where" into "where *and when*", which is often the crux of a missing-persons timeline.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the Wayback app (linked from this Esri guide: livingatlas.arcgis.com/wayback).
2. Navigate/search to the `geolocation` or `address` of interest.
3. Use the version list (left panel) to step through archived World Imagery captures; only versions where the local imagery actually changed are highlighted.
4. Compare captures to find when a feature (building, road, vehicle) appeared or disappeared; note the capture date of each relevant version.
5. Pivot: pin the change to a date to tighten a timeline; combine with Google Earth history and Sentinel/Planet imagery for denser temporal coverage.

## Inputs → Outputs
- **In:** `geolocation` (lat/long) or `address`
- **Out:** dated historical satellite imagery of that spot across multiple captures (`geolocation` context over time)
- **Empty/negative result looks like:** few or no distinct versions for a rural/low-interest area, or all captures look identical — imagery refresh cadence is sparse there; switch to another historical-imagery source.

## Gotchas & OpSec
- Capture dates are irregular and area-dependent — dense over cities, sparse over remote areas; the "date" is when Esri's basemap updated, not necessarily a precise acquisition date.
- Resolution/quality varies by version and region; a change you see may reflect a new imagery source, not a real-world change.
- This URL is the *guide*; the actual tool is the Wayback web app it links to.

## Overlaps ("do both")
- Pairs with `[[esri]]` and with Google Earth's historical imagery slider — each archive has different dates; cross-reference to maximize temporal coverage of one location.

## Trust & verifiability
`trust: trusted` — Esri's first-party imagery archive; the captures are authoritative, but always read the per-version capture date and corroborate a key change against a second imagery archive.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | using-world-imagery-wayback |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation, address → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
