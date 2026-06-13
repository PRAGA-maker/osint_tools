---
id: celltower-locator
name: CellTower Locator
description: Use when you have raw cell identifiers (MCC/MNC/LAC/CID, or SID/NID/BID) and need to convert them to approximate GPS coordinates for a phone's serving cell.
url: http://www.cell2gps.com/
category: phone
path:
- phone
bestFor: Convert cell tower IDs (MCC/MNC/LAC/CID or SID/NID/BID) to approximate GPS coordinates.
selectorsIn:
- device-id
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: Free web converter; backed by public cell databases (OpenCellID / Mozilla Location Service style data). Some richer APIs/databases require keys/credits.
opsec: passive
opsecNote: Looks up tower IDs in a database; does not ping a handset or network. The input itself reveals you hold cell-trace data — handle that data carefully.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Community/third-party converter over crowd-sourced cell databases; accuracy is tower-area-level and depends on database coverage for that cell.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- cell2gps
- cell2gps.com
- cell2gps.net
tags:
- phone
- cell-tower
- geolocation
source: osint4all
lastVerified: '2026-06-13'
enrichment: full
---

# CellTower Locator (cell2gps)

> Converts raw cell-tower identifiers into approximate GPS coordinates — feed it MCC/MNC/LAC/CID (GSM/LTE) or SID/NID/BID (CDMA) and it returns a lat/long for the serving cell.

## When to use
You have raw cell parameters as `device-id` data (from a device's serving-cell readout, call-detail records, or a forensic extraction) and need to turn them into a map location. Use it to ground a phone's approximate `geolocation` at the time a given cell was serving it — area-level, not pinpoint.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://www.cell2gps.com/.
2. Enter the network identifiers: MCC (country), MNC (operator), LAC (location area), CID (cell) for GSM/WCDMA/LTE; or SID/NID/BID for CDMA.
3. Read the result: latitude/longitude of the tower/cell and a map pin (`geolocation`). More towers in the area generally means a tighter result.
4. Pivot: drop the coordinates into a map and overlay `[[cellmapper-net]]` to see the surrounding tower grid and coverage footprint.

## Inputs → Outputs
- **In:** `device-id` (MCC/MNC/LAC/CID or SID/NID/BID)
- **Out:** `geolocation` (approximate tower coordinates)
- **Empty/negative result looks like:** "not found"/no coordinates — the cell isn't in the database (common for rural or newly-deployed cells); absence ≠ invalid cell.

## Gotchas & OpSec
- Result is the tower/cell area, not the phone's exact position — a cell can cover many square km.
- Accuracy depends on database coverage for that specific cell; sparse areas return nothing or a stale location.
- Verify the MNC/operator and country to avoid mapping the wrong network's cell.
- OpSec: passive database lookup; no contact with handset or network. Treat the cell-trace input as sensitive.

## Overlaps ("do both")
- Pairs with `[[cellmapper-net]]` — cell2gps gives the point coordinate, CellMapper shows the carrier's tower grid and coverage around it for sanity-checking.

## Trust & verifiability
`trust: community` — a third-party converter over crowd-sourced cell databases (OpenCellID/MLS-style); reliable to tower-area precision where the cell is well-mapped, unreliable where it isn't. Corroborate before drawing conclusions.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | celltower-locator |
| category | phone |
| selectorsIn → selectorsOut | device-id (cell IDs) → geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
