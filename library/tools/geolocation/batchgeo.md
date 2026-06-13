---
id: batchgeo
name: Batchgeo
description: Use when you have a spreadsheet/list of addresses and want to drop them onto an interactive, shareable map fast — no GIS account or setup.
url: http://batchgeo.com
category: geolocation
path:
- geolocation
bestFor: Pasting an address spreadsheet and getting an interactive, shareable map with geocoded markers.
selectorsIn: [address]
selectorsOut: [geolocation, address]
status: live
pricing: freemium
costNote: Free tier maps a limited number of locations (with public/ad-supported maps); larger datasets, private maps, and extra features require a paid plan.
opsec: passive
opsecNote: You paste your own address list; it does not contact the target. On the free tier maps can be public — anyone with the link (or via search) may view them, so use paid/private maps for sensitive case data.
humanInLoop: false
humanInLoopReason: [payment-wall-partial]
bestInteractionPattern: web-manual
trust: community
trustNote: BatchGeo is a long-established commercial bulk-mapping service widely used for plotting spreadsheets; geocoding is solid but it's a convenience visualiser, not an authoritative data source.
missingPersonsRelevance: medium
coverage: [global]
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: [batch-geocoding, batch-reverse-geocoding, atlas, cartodb]
aliases: [batchgeo-com]
tags: [mapping, geocoding, spreadsheet, bulk]
source: awesome-osint
lastVerified: '2026-06-13'
enrichment: full
---

# Batchgeo

> Paste a spreadsheet of addresses and BatchGeo geocodes them and plots them on an interactive, shareable map — the quickest way to "see" a location list without GIS setup.

## When to use
You have a column of `address`es (locations from records, a sightings list, places associated with a person) and want them mapped together immediately so you can spot clusters and proximity. It's the low-friction visualiser: copy from Excel/Sheets, paste, get a map. Use it to make sense of an address list, not to look anyone up.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://batchgeo.com.
2. Copy your data (including a header row with an address/location column) from a spreadsheet and paste it into the box.
3. Confirm the column mapping (which column is the address) and generate the map.
4. View the interactive map with markers; group/colour by a data column; share or save the map link.
5. Pivot: read the clusters to prioritise a search area, then drill into a point with `[[bing-maps]]` imagery or move the dataset into `[[atlas]]`/`[[cartodb]]` for analysis.

## Inputs -> Outputs
- **In:** `address` (pasted spreadsheet rows)
- **Out:** `geolocation` (geocoded marker coordinates), `address` (validated/placed)
- **Empty/negative result looks like:** a row that fails to geocode shows no marker or lands in the wrong place — usually an ambiguous or malformed address; verify outliers manually.

## Gotchas & OpSec
- **Free maps can be public** and indexable — do not paste sensitive case addresses onto a free public map; use a paid private map for anything confidential.
- Free tier caps the number of locations; large datasets push you to a paid plan.
- Geocoding accuracy varies by address quality and region; markers are approximate.

## Overlaps ("do both")
- Pairs with `[[batch-geocoding]]` / `[[batch-reverse-geocoding]]` when you need the raw coordinates (or the reverse direction) rather than just a map.
- Pairs with `[[atlas]]` / `[[cartodb]]` when you outgrow simple plotting and need real spatial analysis.

## Trust & verifiability
`trust: community` — a well-known, reliable commercial bulk-mapping tool. It's a visualiser, so confirm placement of any critical marker against an authoritative source; don't treat geocoded pins as exact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | batchgeo |
| category | geolocation |
| selectorsIn → selectorsOut | address → geolocation, address |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no (partial paywall) |
