---
id: opencellid-database-of-cell-towers
name: 'OpenCelliD: Database of Cell Towers'
description: Use when you have a cell-tower identifier (MCC/MNC/LAC/CellID) and want its physical location — returns tower coordinates, operator, and coverage, i.e. a `geolocation` for the tower.
url: https://opencellid.org/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- wireless-network-info
bestFor: Resolving a cell-tower ID to map coordinates and operator, for coarse device geolocation.
selectorsIn:
- device-id
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free community database; an API key (free registration via the dashboard) is required for programmatic lookups and bulk data.
opsec: passive
opsecNote: Passive — you look up a tower ID in a public crowdsourced database; nothing is sent to the tower, the carrier, or any device. Registering for the API ties an email to your usage, so use a research address.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: web-manual
trust: community
trustNote: Community-contributed database maintained by Unwired Labs; the largest open cell-tower dataset, but coverage/accuracy vary by region and contributions.
missingPersonsRelevance: medium
coverage:
- global
auth: api-key
api: true
localInstall: false
registration: true
relatedTools:
- opencellid
aliases:
- OpenCelliD
- opencellid.org
tags:
- cell-tower
- geolocation
- wireless
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# OpenCelliD: Database of Cell Towers

> The largest open, crowdsourced database of cell-tower locations — turn a tower identifier (MCC/MNC/LAC/CellID) into map coordinates and an operator.

## When to use
You have a cell-tower identifier — from a phone's engineering/field-test screen, call-detail records, an IoT/GSM device log, or metadata that includes MCC/MNC/LAC/CellID — and you want to place it on a map. Reach for OpenCelliD to resolve that tower ID to coordinates and a carrier, giving a *coarse* geolocation of a device that was connected to it. It is the go-to for cell-based location when you don't have GPS.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://opencellid.org/ and register for a free account to obtain an API key.
2. Gather the tower's identifiers: MCC (country), MNC (operator), LAC/TAC, and CellID.
3. Query via the site's map/search or the API (e.g. `/cell/get?...&mcc=&mnc=&lac=&cellid=`) with your key.
4. Read the returned coordinates, operator, and estimated range/coverage — this is the tower's location, and thus roughly where the connected device was.
5. Pivot: plot the tower(s) on a map; multiple towers over time sketch a movement pattern. Combine with GPS/Wi-Fi geolocation for precision.

## Inputs → Outputs
- **In:** cell-tower identifiers (MCC/MNC/LAC/CellID) — a `device-id`-class network selector
- **Out:** tower `geolocation` (lat/lon), operator, coverage/range estimate
- **Empty/negative result looks like:** the tower ID isn't in the database (contribution gaps, rural/new towers) — no location returned; try a neighbouring cell or another source.

## Gotchas & OpSec
- Human-in-the-loop: an API key (free) is needed for automated lookups.
- Coverage is crowdsourced and uneven — dense in some countries, sparse in others; a tower gives *cell-level*, not GPS-level, precision (hundreds of metres to kilometres).
- OpSec: passive; you never touch the network or device.

## Overlaps ("do both")
- Pairs with Wi-Fi/BSSID geolocation (e.g. WiGLE) and GPS EXIF — cell towers give coarse location, Wi-Fi/GPS refine it. Use OpenCelliD when only cellular identifiers are available.

## Trust & verifiability
`trust: community` — a large, reputable crowdsourced dataset (Unwired Labs); locations are estimates aggregated from contributor measurements, so treat a single tower fix as approximate and corroborate movement with multiple cells.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | opencellid-database-of-cell-towers |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | device-id → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (api-key) |
