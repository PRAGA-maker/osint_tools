---
id: geoplatform-portal
name: GeoPlatform Portal
description: Use when you have a `geolocation` or `address` and want authoritative U.S. federal geospatial layers — returns geolocation context (boundaries, imagery, infrastructure) plus metadata-exif-style dataset provenance.
url: https://www.geoplatform.gov/
category: geolocation
path:
- geolocation
bestFor: Pulling official U.S. federal map layers and datasets (imagery, boundaries, hydrology, infrastructure) for a location of interest.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
- metadata-exif
status: live
pricing: free
costNote: Free U.S. government geospatial catalog and viewer; no account needed to browse or download most public datasets.
opsec: passive
opsecNote: You browse and download public federal map data; no query concerns the subject and nothing is transmitted about them. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the U.S. Federal Geographic Data Committee; datasets are authoritative federal-agency sources.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: true
localInstall: false
registration: false
aliases:
- GeoPlatform
- geoplatform.gov
tags:
- geospatial
- government-records
- maps
- open-data
source: osint4all
lastVerified: '2026-07-20'
enrichment: full
---

# GeoPlatform Portal

> The U.S. federal geospatial catalog and map viewer — FGDC's hub for finding, viewing, and downloading authoritative government map layers.

## When to use
You have a `geolocation` or `address` and need authoritative context about that place: aerial/satellite imagery, administrative boundaries, hydrology, roads, land cover, or critical-infrastructure layers, all from official federal agencies. This is a context and corroboration tool for a location — not a person-finder — that helps you interpret coordinates, verify a terrain description, or overlay official data on a spot of interest.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.geoplatform.gov/ and use the map viewer or dataset catalog (search).
2. Navigate to your `geolocation`/`address` in the viewer, or search the catalog by theme (imagery, boundaries, transportation, hydrography).
3. Add layers to inspect the area; read each layer's metadata for source agency, date, and accuracy (`metadata-exif`-style provenance).
4. Download datasets or connect via the exposed OGC/REST services (API) for offline analysis.
5. Pivot: confirmed boundaries/imagery feed geolocation verification of a photo or a described location; jurisdiction data narrows which local records to pull next.

## Inputs → Outputs
- **In:** `geolocation` (coords) or `address`
- **Out:** `geolocation` context (official layers/boundaries/imagery), dataset `metadata-exif` (source, date, accuracy)
- **Empty/negative result looks like:** a location outside U.S. federal coverage returns sparse/no layers — this is a U.S.-centric resource; use it only for U.S. geography.

## Gotchas & OpSec
- Coverage is U.S. federal; non-U.S. locations are largely unsupported.
- It is a data catalog, not a live-tracking or people tool — value is corroborating a *place*, not finding a person.
- OpSec: fully passive; public open data.

## Overlaps ("do both")
- Complements street-view and satellite tools: use those for imagery of a spot, and GeoPlatform for the authoritative boundary/infrastructure/metadata layer over it.

## Trust & verifiability
`trust: trusted` — a first-party U.S. government portal aggregating authoritative federal-agency datasets; check each layer's own metadata for currency and accuracy.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | geoplatform-portal |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → geolocation, metadata-exif |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
