---
id: copernicus-browser-formerly-sentinel-hub-playground-eo-browser
name: Copernicus Browser (formerly Sentinel Hub Playground, EO Browser)
description: Use when you have a `geolocation`/`address` and want recent satellite imagery of it — returns free Sentinel/Copernicus imagery by location and date for verification and change detection.
url: https://browser.dataspace.copernicus.eu/
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Viewing and downloading free Sentinel satellite imagery of a location across dates for change detection.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free via the Copernicus Data Space Ecosystem; a free account unlocks full features (downloads, statistical/analysis tools).
opsec: passive
opsecNote: You browse public satellite archives, not the subject — fully passive, no target signal. Register with a sock-puppet account if you want to keep saved analyses separate.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official ESA/European Commission Copernicus platform; imagery is authoritative satellite data straight from the Sentinel missions.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
aliases:
- Copernicus Browser
- EO Browser
- Sentinel Hub
tags:
- maps-geospatial-data
- satellite
- imagery
- geolocation
- verification
source: bellingcat-toolkit
lastVerified: '2026-07-23'
enrichment: full
---

# Copernicus Browser (formerly Sentinel Hub Playground, EO Browser)

> Free access to ESA's Sentinel satellite imagery — pick a location and date and pull recent, medium-resolution imagery for verification, change detection, and dating events.

## When to use
You have a `geolocation`/`address` and need overhead imagery: to verify a scene, detect change over time (construction, fire, flooding, military movement), or corroborate/date a ground-level photo. Sentinel-2 optical (~10m) and Sentinel-1 radar imagery refresh every few days, so you can build a time series of a spot for free.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://browser.dataspace.copernicus.eu/ and register a free account (needed for full features/downloads).
2. Navigate/search to the `geolocation`/`address`; draw an area of interest.
3. Pick a satellite (Sentinel-2 optical, Sentinel-1 radar), date, and visualization (true colour, NDVI, false colour, etc.); step through dates to compare.
4. Download imagery or run built-in analysis. Pivot: confirmed features/dates feed chronogeolocation (`[[peakvisor]]`), and change detection corroborates event timelines.

## Inputs → Outputs
- **In:** `geolocation`/`address` (+ date, satellite, band selection)
- **Out:** satellite imagery of that `geolocation` across dates
- **Empty/negative result looks like:** cloud-covered or no acquisition for your date — step to nearby dates or switch to Sentinel-1 radar (sees through cloud); very small features may be below ~10m resolution.

## Gotchas & OpSec
- Resolution is medium (~10m optical) — good for landscape/large-feature change, not for reading small objects (use commercial hi-res for that).
- Cloud cover frequently blocks optical passes; radar (S1) is the workaround.
- Full features/downloads need the (free) account.

## Overlaps ("do both")
- Complements Google Earth/hi-res commercial imagery — Copernicus gives free, frequent, dated coverage for change detection; hi-res sources add detail on a specific date.

## Trust & verifiability
`trust: trusted` — the official Copernicus/ESA platform; the imagery is authoritative satellite data, ideal as primary evidence for geospatial verification.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | copernicus-browser-formerly-sentinel-hub-playground-eo-browser |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation, address → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
