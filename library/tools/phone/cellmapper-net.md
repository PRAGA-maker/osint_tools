---
id: cellmapper-net
name: cellmapper.net
description: Use when you have a cell tower ID / sector or a carrier and area and need tower locations and coverage to ground a phone's approximate location.
url: https://www.cellmapper.net/
category: phone
path:
- phone
bestFor: Crowd-sourced map of cell tower locations and coverage by carrier, searchable by tower/cell ID.
selectorsIn:
- geolocation
- device-id
selectorsOut:
- geolocation
- metadata-exif
status: live
pricing: free
costNote: Free to view the map and tower data; an account is only needed to edit/contribute data. Mobile apps available.
opsec: passive
opsecNote: Reads a crowd-sourced tower database; viewing does not transmit anything about the target. Logging your own device to contribute would expose your location — don't, for an investigation.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Crowd-sourced (volunteer-contributed) tower database; accuracy varies by area and contribution density, with verification flags on records.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- CellMapper
- cellmapper.net
tags:
- mobilephone
- Mobile & Phone Related
- cell-tower
- coverage
source: uk-osint
lastVerified: '2026-06-13'
enrichment: full
---

# cellmapper.net

> Crowd-sourced cell-tower map — view tower locations, sectors and coverage by carrier worldwide, searchable by tower/cell ID.

## When to use
You have a cell tower identifier, sector, or a carrier + area (e.g. from call-detail records, a device's serving cell, or a coverage question) and want to place it geographically: which towers a carrier operates in an area, where a specific cell is, and its coverage footprint. Use it to corroborate or contextualise an approximate `geolocation` for a phone, not to locate a live handset.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.cellmapper.net/ (no login needed to view).
2. Select the provider/network, then filter by frequency band or tower type; search by tower or by BSIC/PCI/PSC/cell `device-id` if you have it.
3. Read the result: tower coordinates, sectors/coverage, and technical specs (bands, bandwidth, verification status) — an approximate `geolocation` plus tower `metadata-exif`.
4. Pivot: overlay the tower/coverage on a map alongside other location signals; combine with `[[celltower-locator]]` to convert raw LAC/CID values into coordinates.

## Inputs → Outputs
- **In:** `geolocation` (area/carrier) or `device-id` (cell/tower ID)
- **Out:** `geolocation` (tower coordinates/coverage), `metadata-exif` (bands, sector, verification)
- **Empty/negative result looks like:** sparse or no towers in an area — common where few volunteers have mapped it; absence ≠ no coverage.

## Gotchas & OpSec
- Crowd-sourced: density and accuracy vary hugely by region; trust the verification flags.
- It maps infrastructure, not subscribers — it cannot tell you who is on a tower or locate a live phone.
- OpSec: viewing is passive. Do NOT log your own device to contribute during an investigation — that would upload your location.

## Overlaps ("do both")
- Pairs with `[[celltower-locator]]` (cell2gps) — cell2gps converts MCC/MNC/LAC/CID to coordinates, CellMapper shows the surrounding tower grid and coverage for context.

## Trust & verifiability
`trust: community` — volunteer/crowd-sourced tower data with per-record verification flags; reliable in well-mapped areas, thin elsewhere. Corroborate critical inferences.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cellmapper-net |
| category | phone |
| selectorsIn → selectorsOut | geolocation, device-id → geolocation, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
