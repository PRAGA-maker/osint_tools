---
id: cellmapper
name: CellMapper
description: Use when you have a cell tower ID (CID/eNB), a carrier, or a geolocation and want to map cell towers, decode tower/sector IDs, and see coverage — returns geolocation for cell-network infrastructure.
url: https://www.cellmapper.net/map
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Mapping cell towers and decoding Cell/eNB IDs to physical tower locations worldwide.
selectorsIn:
- geolocation
- device-id
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free crowdsourced coverage map; a free account unlocks some filters/features, but browsing is open.
opsec: passive
opsecNote: A public crowdsourced map — you query CellMapper's data, not any target, so it's passive. Don't upload your own device's live measurements if that would reveal your location. Use a clean browser.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Crowdsourced by volunteers wardriving/logging towers; accuracy is high where coverage is dense and sparse elsewhere, and tower positions are estimated from measurements.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- cellmapper-net
aliases:
- cellmapper.net
tags:
- Maps, Geolocation and Transport
- Communications, Internet, Technologies
source: cyb-detective
lastVerified: '2026-08-05'
enrichment: full
---

# CellMapper

> A crowdsourced worldwide map of cellular towers with a Cell-ID calculator — turn a tower/sector identifier into a physical location, or survey the cell infrastructure around a place.

## When to use
Geospatial/technical investigations involving cellular data. If you have a cell identifier (`device-id`-adjacent: CID, eNB/gNB ID, LAC/TAC) from device logs, a photo of a tower, or metadata, CellMapper can place it on the map and decode the ID into a tower/sector location — helping corroborate where a device connected. Also useful to survey which carriers/towers serve a given `geolocation`.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.cellmapper.net/map.
2. Select the country + carrier (MCC/MNC), then navigate to your area of interest.
3. Use the Cell-ID calculator to convert a raw Cell/eNB ID into its tower/sector, or click towers to read their IDs, bands, and estimated positions.
4. Cross-reference a known cell ID from device data against the mapped tower to place a connection.
5. Pivot: a tower location → `geolocation` corroboration for where a device was; carrier/band info → phone-carrier reasoning.

## Inputs → Outputs
- **In:** a cell/tower ID (`device-id`-adjacent) or a `geolocation`/carrier
- **Out:** `geolocation` of towers/sectors and coverage context
- **Empty/negative result looks like:** an unmapped area or an ID with no logged tower — coverage is crowdsourced, so gaps mean "no one logged it," not "no tower."

## Gotchas & OpSec
- **Crowdsourced estimates:** tower positions are inferred from volunteer measurements and can be approximate or missing, especially in low-coverage regions.
- Correct MCC/MNC (country + carrier) selection is essential to resolve an ID.
- Passive to browse; don't contribute live measurements that would expose your own location.

## Overlaps ("do both")
- Pairs with coverage maps like `[[nperf-com-map]]` (operator coverage) — CellMapper pinpoints individual towers/IDs, coverage maps show the broader footprint.

## Trust & verifiability
`trust: community` — volunteer-sourced and generally reliable where data is dense; treat tower positions as estimates and corroborate a critical location fix with a second source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cellmapper |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | geolocation, device-id → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
