---
id: earthexplorer
name: EarthExplorer
description: Use when you have an area of interest and need historical or multispectral satellite/aerial imagery for a specific date to corroborate timeline or terrain.
url: https://earthexplorer.usgs.gov/
category: geolocation
path:
- geolocation
bestFor: Downloading dated historical and multispectral satellite/aerial scenes for an area of interest.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
- image
- metadata-exif
status: live
pricing: free
costNote: Free; requires a no-cost USGS ERS account to download scenes.
opsec: passive
opsecNote: Queries the public USGS archive; no contact with the target. Requires a logged-in account, so use a research identity, not a personal one tied to the case.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the U.S. Geological Survey; authoritative government source for Landsat, aerial photography, and other earth-observation archives.
missingPersonsRelevance: high
coverage:
- global
- us
auth: account
api: true
localInstall: false
registration: true
aliases:
- USGS EarthExplorer
tags:
- geospatial-research-and-mapping-tools
source: arf-seed
lastVerified: ''
enrichment: full
---

# EarthExplorer

> USGS's public portal for searching and downloading dated satellite and aerial imagery — the canonical source for historical earth-observation scenes.

## When to use
You have a `geolocation` or `address` and need imagery from a particular time window: confirming whether a structure, vehicle, or feature existed on a given date, checking seasonal terrain (snow, foliage, flooding) along a last-known route, or sourcing multispectral data. Especially useful when consumer maps only show current imagery and you need the past.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register a free USGS ERS account and log in at https://earthexplorer.usgs.gov/.
2. **Search Criteria** tab: draw a polygon, drop a point, or enter coordinates/place; set a date range.
3. **Data Sets** tab: pick a collection (Landsat, Aerial Photography, Sentinel, etc.).
4. **Results** tab: preview footprints, then download the scene (some require an order/processing step).
5. Pivot: open the scene in `[[google-earth-pro]]` or GIS to overlay against other layers; cross-check against `[[google-maps]]` current imagery.

## Inputs → Outputs
- **In:** `geolocation`/`address` + date range + dataset.
- **Out:** downloadable `image` scenes with acquisition `metadata-exif` (date, sensor, resolution), tied to `geolocation`.
- **Empty/negative result looks like:** no footprints intersect your AOI/date — widen the date range or switch datasets (coverage and cadence vary by sensor and region).

## Gotchas & OpSec
- Human-in-the-loop: a free account login is required to download (browsing the catalog is possible without it).
- Resolution and revisit frequency vary widely; consumer aerial may be sharper than free Landsat for a single date.
- OpSec: passive against the target; use a dedicated research account, since downloads are logged to your profile.

## Overlaps ("do both")
- Pairs with `[[google-earth-pro]]`, which has a friendly historical-imagery slider but a narrower archive than USGS's raw catalog.

## Trust & verifiability
`trust: trusted` — authoritative U.S. Geological Survey data with documented acquisition metadata for every scene.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | earthexplorer |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → image, metadata-exif |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
