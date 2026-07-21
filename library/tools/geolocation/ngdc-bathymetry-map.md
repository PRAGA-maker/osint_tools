---
id: ngdc-bathymetry-map
name: NGDC Bathymetry map
description: Use when you have a marine/coastal `geolocation` or a water-scene `image` and want seafloor depth and coastal relief to test plausibility — returns bathymetric depth data by location.
url: https://maps.ngdc.noaa.gov/viewers/bathymetry/
category: geolocation
path:
- geolocation
bestFor: Checking seafloor depth and coastal/marine relief for a location to corroborate maritime imagery or claims.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: Free official NOAA/NCEI viewer; underlying datasets are public and downloadable at no cost.
opsec: passive
opsecNote: Querying a government bathymetry viewer discloses nothing about your subject — you are reading public geophysical data. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by NOAA's National Centers for Environmental Information (former NGDC) — authoritative, government-maintained bathymetric data.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- NOAA bathymetry viewer
- NCEI bathymetry map
tags:
- Maps, Geolocation and Transport
- Nature
- bathymetry
source: cyb-detective
lastVerified: '2026-07-21'
enrichment: full
relatedTools:
- ncei-noaa-gov
- nexrad-data-inventory-search
- noaa-data-access-viewer
- noaa-fisheries-vessel-search
---

# NGDC Bathymetry map

> NOAA/NCEI's interactive bathymetry viewer — authoritative worldwide seafloor-depth and coastal-relief data for testing marine and coastal geolocation claims.

## When to use
You have a marine or coastal `geolocation`, or a photo/video shot on/near the water, and you need seafloor depth or coastal relief to test whether a claim is plausible — e.g. could a vessel be at anchor here, does the depth match a diving/fishing account, is a "deep-water" claim consistent with the location. This is a niche corroboration tool for maritime/coastal scenarios, not a people-finder.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://maps.ngdc.noaa.gov/viewers/bathymetry/.
2. Navigate/zoom to your candidate coordinates or place.
3. Read the bathymetric depth at the point of interest and inspect the surrounding relief.
4. Compare against the claim/imagery (depth, distance-to-shore, shelf vs. deep water).
5. Pivot: a confirmed marine location feeds vessel-tracking, coastal-webcam, or satellite tools; a depth mismatch flags a claim as suspect.

## Inputs → Outputs
- **In:** a marine/coastal `geolocation` (coordinates or place)
- **Out:** seafloor depth and coastal relief at that `geolocation`
- **Empty/negative result looks like:** sparse/coarse data in poorly-surveyed regions — a gap in survey coverage, not a zero-depth reading; note the resolution before drawing conclusions.

## Gotchas & OpSec
- Purpose-specific: this measures water depth/relief only — no people, vessels, or activity data.
- Survey resolution varies enormously; open-ocean and remote areas are coarse. Don't over-read fine detail where none exists.
- Low direct missing-persons value; use it only for maritime/coastal corroboration.
- OpSec: fully passive.

## Overlaps ("do both")
- Pairs with NOAA data viewers ([[noaa-data-access-viewer]], [[ncei-noaa-gov]]) and vessel-tracking — bathymetry sets the physical stage, while those add environmental data and ship movements.

## Trust & verifiability
`trust: trusted` — NOAA/NCEI is an authoritative government source; the depth data is reliable, bounded only by each region's survey resolution.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ngdc-bathymetry-map |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
