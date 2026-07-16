---
id: gps-visualizer
name: GPS Visualizer
description: Use when you have an `address` or `geolocation` and want to convert between them or plot points on a map — returns latitude/longitude, addresses and map visualisations.
url: http://www.gpsvisualizer.com/geocode
category: geolocation
path:
- geolocation
bestFor: Free geocoding (address ↔ lat/long) and mapping of coordinate/point data.
selectorsIn:
- address
- geolocation
selectorsOut:
- geolocation
- address
status: live
pricing: free
costNote: Free web tool; bulk geocoding can require your own geocoding API key (Google/Bing/etc.) for large batches, but single lookups and mapping are free.
opsec: passive
opsecNote: You geocode/plot data locally against mapping providers — the subject is not contacted. Addresses you submit are sent to the chosen geocoding backend (Google/Bing/etc.) and may be logged there; avoid pasting sensitive location lists you must keep private. Use a sock-puppet browser.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-established free mapping/geocoding utility (Adam Schneider); reliable, but coordinates are only as accurate as the underlying geocoder and the input address.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- GPSVisualizer
- gpsvisualizer.com
tags:
- toddington
- curated-directory
- geo-location-mapping-tools
- geocoding
source: toddington-resources
lastVerified: '2026-07-10'
enrichment: full
relatedTools:
- gpsvisualizer
---

# GPS Visualizer

> A free geocoder and mapper — turn an address into coordinates (or back), and plot points/tracks on a map for spatial analysis.

## When to use
You have an `address` and need its latitude/longitude (or a `geolocation` you want reverse-geocoded to an address), or you have a set of points/coordinates you want to visualise on a map. Core to geolocation work: normalising addresses to coordinates so you can compare, cluster, or map locations tied to a subject (home, work, sightings, EXIF points).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.gpsvisualizer.com/geocode.
2. Paste one or more `address`es (or coordinates) into the input box.
3. Choose a geocoding source (Google/Bing/etc.) and run — it returns latitude/longitude for each address (or the nearest address for coordinates).
4. For visualisation, use the main GPS Visualizer map tools to plot the resulting points/tracks on a map or export to KML/GPX/GeoJSON.
5. Pivot: coordinates feed mapping and proximity analysis; normalise EXIF/`geolocation` from `[[reverse-image-search]]` results; compare a subject's addresses spatially.

## Inputs → Outputs
- **In:** `address` (to geocode) or `geolocation` (to reverse-geocode / plot)
- **Out:** `geolocation` (lat/long), matched `address`, and map/export files
- **Empty/negative result looks like:** "no match"/ambiguous geocode — a malformed, incomplete, or non-existent address, or a coordinate over featureless terrain. Ambiguous addresses may geocode to a city centroid; check the returned match, not just that a number came back.

## Gotchas & OpSec
- Accuracy depends on the **input and the geocoder** — vague addresses snap to centroids; verify the returned coordinate lands where you expect.
- Bulk geocoding may hit provider limits or need your own API key.
- OpSec: **passive**, but submitted addresses go to a third-party geocoder — don't paste sensitive location sets you must keep private.

## Overlaps ("do both")
- Pairs with mapping/imagery tools and EXIF extractors — GPS Visualizer normalises and plots the coordinates that reverse-image/EXIF and address records produce, so use it as the geocoding glue between them.

## Trust & verifiability
`trust: community` — a reputable free utility; output is deterministic geocoding, so verifiability rests on the input quality and the chosen provider. Confirm critical coordinates on satellite/street imagery.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gps-visualizer |
| category | geolocation |
| selectorsIn → selectorsOut | address, geolocation → geolocation, address |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
