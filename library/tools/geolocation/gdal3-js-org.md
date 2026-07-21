---
id: gdal3-js-org
name: gdal3.js
description: Use when you have geospatial data (`geolocation`) in one format and need it in another — returns the same data converted between GeoJSON, KML, Shapefile, GPKG and more, entirely in-browser.
url: https://gdal3.js.org/
category: geolocation
path:
- geolocation
bestFor: Converting geospatial files between formats (GeoJSON, KML, Shapefile, GeoPackage, etc.) without installing GDAL.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free and open source (GDAL compiled to WebAssembly); no account or payment.
opsec: passive
opsecNote: Conversion runs client-side in your browser via WebAssembly — your files are not uploaded to a server, so sensitive geodata stays local. Still, verify you are on the genuine site before loading confidential data.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Open-source browser port of GDAL, the standard geospatial data library; the underlying engine is authoritative, the web wrapper is community-maintained.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- gdal3.js
- gdal3.js.org
- browser GDAL
tags:
- Maps, Geolocation and Transport
- Tools
- geodata-conversion
source: cyb-detective
lastVerified: '2026-07-21'
enrichment: full
---

# gdal3.js

> GDAL — the industry-standard geospatial data toolkit — running entirely in your browser, so you can convert map-data formats without installing anything.

## When to use
A utility for the geospatial side of an investigation. When you obtain location data in an awkward format — a Shapefile bundle, a GeoPackage, a KML from Google Earth, a GeoJSON export — and your next tool wants a different format, gdal3.js converts it in-browser. Use it to make a `.shp` viewable, turn coordinates into KML for mapping, or normalize disparate geodata into one format for analysis.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://gdal3.js.org/.
2. Load your input geospatial file(s) into the page (drag/drop or file picker). Shapefiles need their sidecar files (`.shp/.shx/.dbf/.prj`).
3. Choose the target output format (GeoJSON, KML, GPKG, CSV, etc.).
4. Run the conversion and download the result — all processed locally in the browser.
5. Pivot: feed the converted `geolocation` layer into a mapping tool, Google Earth, or a GIS viewer for analysis.

## Inputs → Outputs
- **In:** a geospatial file / `geolocation` dataset in some source format
- **Out:** the same `geolocation` data re-encoded in your chosen format
- **Empty/negative result looks like:** a conversion error — usually a missing Shapefile sidecar, an unsupported driver, or a malformed source file, not a data-absent result.

## Gotchas & OpSec
- Shapefiles are multi-file; supply the whole set or projection/attributes are lost.
- It converts formats, it does not geocode or fetch data — you must already have the geodata.
- OpSec: strong — processing is client-side WASM, so files never leave your machine; ideal for sensitive location data.

## Overlaps ("do both")
- Pairs with desktop GDAL/QGIS for heavy batch work — gdal3.js is the zero-install option for a quick one-off conversion in the field.

## Trust & verifiability
`trust: community` — it wraps GDAL, the authoritative open-source geospatial library, in WebAssembly; conversions are as correct as GDAL itself, with a community-maintained front-end.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gdal3-js-org |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
