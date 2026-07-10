---
id: find-gsm-base-stations-cell-id-coordinates
name: Find GSM base stations cell id coordinates
description: Use when you have GSM cell identifiers (MCC/MNC/LAC/CID) and want the tower's approximate location — returns base-station coordinates plotted on a map.
url: https://cellidfinder.com/
category: phone
path:
- phone
bestFor: Converting GSM cell identifiers (MCC/MNC/LAC/CID) into approximate base-station GPS coordinates.
selectorsIn:
- device-id
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: Free nonprofit community project (CellIDFinder); results depend on crowd-sourced tower databases, so coverage varies by region.
opsec: passive
opsecNote: You look up tower identifiers in a public database — no query touches the target's phone or network, and nobody is notified. The identifiers themselves must come from a device you legitimately control or from lawful data; obtaining another person's live cell data is a separate legal matter this tool does not address.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A nonprofit crowd-sourced cell-tower locator; coordinates are approximate (tower location, not handset) and coverage/accuracy depend on community data density.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- CellIDFinder
- cellidfinder.com
- GSM base station locator
tags:
- cell-id
- gsm
- geolocation
- tower-lookup
source: osint4all
lastVerified: '2026-07-10'
enrichment: full
---

# Find GSM base stations cell id coordinates

> Turn raw GSM cell identifiers (MCC/MNC/LAC/CID) into an approximate tower location on a map — the base station a device was attached to, not the device itself.

## When to use
You have GSM network identifiers — MCC (country), MNC (operator), LAC (location area), and CID (cell) — recorded from a device (`device-id`-style network metadata), a network monitor app, or lawful data, and you want to know roughly where that cell tower is. Useful for placing a phone's last-known cell in a geographic area during a missing-person or timeline reconstruction, when GPS is unavailable but cell attachment is known.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://cellidfinder.com/.
2. Enter the four identifiers: MCC, MNC, LAC, and Cell ID.
3. Submit — the tool queries crowd-sourced tower databases and plots the base station's approximate coordinates on a Google map (averaging when multiple CIDs share a station).
4. Interpret the result as the **tower's** location and coverage area, not the phone's exact position — the handset is somewhere within that cell's range.
5. Pivot: cross-check against `[[opencellid]]`/OpenCelliD or operator maps; combine multiple cell hits over time to triangulate movement; feed the area into mapping/geolocation.

## Inputs → Outputs
- **In:** MCC + MNC + LAC + CID (`device-id`/network metadata)
- **Out:** approximate base-station `geolocation` (coordinates on a map)
- **Empty/negative result looks like:** "not found" — the tower isn't in the crowd-sourced database (common in low-coverage regions or for new/small cells), or an identifier is wrong. Absence means "not mapped here," not "no such tower."

## Gotchas & OpSec
- **Tower ≠ phone.** The coordinate is the base station; the device is within its cell radius (metres in dense urban areas, kilometres rurally). Never present it as a precise handset location.
- Coverage is crowd-sourced and uneven — cross-check with a second cell database before relying on a single hit.
- OpSec: **passive** database lookup. The identifiers must be lawfully obtained; this tool does not and cannot pull another person's live cell data.

## Overlaps ("do both")
- Pairs with OpenCelliD/`[[opencellid]]`, Mozilla Location Service-style databases, and operator coverage maps — different databases map different towers, so query several and reconcile the coordinates.

## Trust & verifiability
`trust: community` — a nonprofit crowd-sourced project; coordinates are approximate and coverage-dependent. Treat a single result as an area estimate and corroborate with another tower database.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | find-gsm-base-stations-cell-id-coordinates |
| category | phone |
| selectorsIn → selectorsOut | device-id → geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
