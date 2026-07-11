---
id: celltowermaps-com
name: celltowermaps.com
description: Use when you have a `geolocation`/`address` (or a carrier) and want the cell towers serving it — returns tower locations, callsigns, carrier and band data (`geolocation` + `metadata-exif`-style RF detail).
url: https://www.celltowermaps.com/
category: phone
path:
- phone
bestFor: Mapping US cell-tower locations by area or carrier from FCC data.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
- metadata-exif
status: live
pricing: free
costNote: Free. Maps ~2.8M US tower locations from public FCC database records; no account or payment.
opsec: passive
opsecNote: You query a static map of infrastructure, not a person or their device. Nothing reaches any subject. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party visualiser of public FCC tower registrations. The underlying FCC data is authoritative; tower-to-coverage inference (which tower actually served a call) is not something this tool can prove.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- cellmapper
- fcc-io
aliases:
- Cell Tower Maps
- celltowermaps.com
tags:
- mobilephone
- Mobile & Phone Related
- cell-tower
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# celltowermaps.com

> A free map of ~2.8 million US cell towers from FCC records — see which carriers' towers (and what generation/bands) serve any address or area.

## When to use
You have a `geolocation`/`address` tied to a subject (a last-known location, a place in a photo, or coordinates from other evidence) and want to understand the cellular infrastructure there: which carriers have towers nearby, tower callsigns/coordinates, structure heights, and 2G/3G/4G/5G coverage. Useful for reasoning about signal/coverage in an area, corroborating which carrier a subject likely uses, or identifying a tower/mast visible in imagery.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.celltowermaps.com/.
2. Search by `address`, city, or ZIP, or click the interactive map to drop a pin (or filter by carrier).
3. Read the tower markers: colour-coded by generation (5G/4G/2-3G/broadcast), with callsign, coordinates, band, power, and antenna height.
4. Note the carriers and towers serving the target area.
5. Pivot: carrier presence narrows which network a subject's `phone` uses; a tower's coordinates/height can match a mast seen in a photo; cross-check registrations via `[[fcc-io]]` and compare with `[[cellmapper]]`.

## Inputs → Outputs
- **In:** `geolocation` / `address` (or a carrier name)
- **Out:** tower `geolocation`s + RF/technical detail (`metadata-exif`-style: callsign, bands, height, power, carrier)
- **Empty/negative result looks like:** sparse or no towers in a rural area, or gaps where the FCC record is incomplete — means limited registered infrastructure/data, not necessarily no coverage.

## Gotchas & OpSec
- Human-in-the-loop: none; interactive map.
- OpSec: **passive** — infrastructure data only; no person or device is queried.
- It maps *registered tower structures*, which doesn't tell you which tower actually handled a specific call, nor anything about a subscriber. Treat it as coverage/infrastructure context, not call-detail evidence. US-only.

## Overlaps ("do both")
- Pairs with `[[cellmapper]]` (crowd-sourced cell/coverage data with cell IDs) and `[[fcc-io]]` (device/registration lookups) — celltowermaps is the FCC-structures view; CellMapper adds live crowd-sourced cell detail. Cross-reference for a fuller picture of an area's cellular environment.

## Trust & verifiability
`trust: community` — a solid visualiser of authoritative FCC tower data. The tower locations are reliable; any inference about which tower served a device, or about a person, is beyond what the tool can substantiate.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | celltowermaps-com |
| category | phone |
| selectorsIn → selectorsOut | geolocation, address → geolocation, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
