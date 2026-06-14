---
id: skyfi-com-satellite-open-data
name: SkyFi.com - Satellite Open Data
description: Use when you need to find or order higher-resolution open and commercial satellite scenes for a specific area and date.
url: https://app.skyfi.com/explore/open
category: geolocation
path:
- geolocation
bestFor: Marketplace/explorer to search open and commercial satellite scenes for an AOI and order imagery.
input: AOI, date range, and scene filters
output: Scene search results with preview and ordering options
selectorsIn: [geolocation, address]
selectorsOut: [geolocation, metadata]
status: live
pricing: freemium
costNote: Open-data scene browsing/preview is free; ordering commercial high-resolution imagery is paid.
opsec: passive
opsecNote: Imagery search reveals nothing about a target; ordering imagery requires an account and payment, which ties activity to you.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: Commercial satellite-imagery marketplace (SkyFi); legitimate aggregator of providers, but high-res scenes are paid and account-gated.
missingPersonsRelevance: high
coverage: [global]
auth: account
api: true
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools: [sentinel-hub]
aliases: [SkyFi]
tags: []
source: arf-seed
lastVerified: ''
enrichment: full
---

# SkyFi.com - Satellite Open Data

> A satellite-imagery marketplace and explorer for searching open and commercial scenes over an area of interest and ordering imagery — including higher resolution than free viewers.

## When to use
You have a `geolocation`/`address` and a date window and need imagery beyond what free 10 m viewers provide — e.g. higher-resolution scenes to inspect a remote site, vehicle, or structure near a last-known location, or to find any scene captured around the time of a disappearance. The open-data explorer surfaces free scenes; the marketplace lets you order commercial high-res when justified.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://app.skyfi.com/explore/open and draw or enter your AOI.
2. Set a date range and scene filters (resolution, cloud cover, provider).
3. Browse results with previews (`geolocation` + `metadata`: date, sensor, resolution); use free open-data scenes directly.
4. To order commercial imagery, sign in and purchase. Pivot: analyze downloaded scenes in `[[qgis]]`; cross-check free dated imagery in `[[sentinel-hub]]`.

## Inputs → Outputs
- **In:** `geolocation`/`address` (AOI), date range, filters
- **Out:** scene search results with previews and `metadata` (date, sensor, resolution); orderable imagery
- **Empty/negative result looks like:** no scenes for the AOI/date — common for narrow date windows or low-revisit areas; widen the range.

## Gotchas & OpSec
- Human-in-the-loop: account login to use fully; ordering high-res imagery hits a payment wall.
- OpSec: searching is passive and reveals nothing about a target, but ordering ties the request to your account and payment.
- Free open-data scenes are the same archives as elsewhere; the paid value is high-res/tasking.

## Overlaps ("do both")
- Pairs with `[[sentinel-hub]]` (free dated medium-res) — use SkyFi when you need higher resolution or commercial scenes, then analyze in `[[qgis]]`.

## Trust & verifiability
`trust: community` — a legitimate commercial imagery marketplace aggregating multiple providers. Open-data browsing is free; high-res is paid and account-gated.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | skyfi-com-satellite-open-data |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → geolocation, metadata |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
