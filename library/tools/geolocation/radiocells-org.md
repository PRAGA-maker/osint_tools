---
id: radiocells-org
name: Radiocells.org
description: Use when you have a WiFi BSSID (`mac-address`) or a cell-tower ID and want its physical location — returns `geolocation` from a community-collected radio-cell database.
url: https://radiocells.org/
category: geolocation
path:
- geolocation
bestFor: Resolving a WiFi access point (BSSID) or cell tower to map coordinates using open crowd-sourced data.
selectorsIn:
- mac-address
- device-id
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free and open data — cell data under CC BY-SA 3.0, WiFi data under ODbL; the whole database can be downloaded for offline use.
opsec: passive
opsecNote: You query a static crowd-sourced database, not the access point or the target's device, so nothing is transmitted to the subject. The database is contributed by volunteers wardriving with scanner apps.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A volunteer project (formerly openBmap, since 2009) with ~700k cell and ~10M WiFi locations; coverage is uneven and dated in places, so a single fix should be corroborated.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- Radiocells
- openBmap
- radiocells.org
tags:
- geolocation
- wifi-geolocation
- cell-tower
source: osint4all
lastVerified: '2026-08-04'
enrichment: full
---

# Radiocells.org

> An open, crowd-sourced database of WiFi access points and cell towers with locations — turn a BSSID or cell ID into map coordinates, offline or online, without Google/Apple's proprietary services.

## When to use
You have a radio identifier tied to your subject — a WiFi router's BSSID (`mac-address`) recovered from device logs/EXIF/network data, or a cell-tower identifier (MCC/MNC/LAC/CID) — and want the physical `geolocation` it maps to. Radiocells.org resolves these against volunteer-collected data, a free alternative to WiGLE/OpenCelliD for placing a network or tower on a map.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://radiocells.org/ and use the map/search, or query via its API / downloadable offline database for bulk work.
2. Enter the WiFi BSSID or the cell-tower identifiers to look up their recorded position.
3. Read the returned coordinates; note how many observations back the fix (a single sighting is weaker than many).
4. Pivot: cross-check the coordinates against `[[wigle]]`/OpenCelliD and satellite/street imagery before treating the location as confirmed.

## Inputs → Outputs
- **In:** WiFi BSSID (`mac-address`) or cell-tower ID (`device-id`)
- **Out:** `geolocation` (coordinates) for the network/tower
- **Empty/negative result looks like:** "not found" — the AP/tower simply isn't in this volunteer dataset (very common outside well-mapped regions); absence is not evidence the device doesn't exist.

## Gotchas & OpSec
- Human-in-the-loop: none for a lookup.
- OpSec: passive — you read a static database; the subject's router/device is never contacted.
- Coverage/currency: crowd-sourced and patchy, with some data years old; routers move and towers change, so always corroborate a fix.

## Overlaps ("do both")
- Pairs with `[[wigle]]` and OpenCelliD because each database was collected by different contributors — a BSSID/tower missing here may be present there; agreement across them strengthens a location.

## Trust & verifiability
`trust: community` — open volunteer data with no completeness guarantee; use it as one geolocation source and confirm coordinates against an independent database and imagery.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
