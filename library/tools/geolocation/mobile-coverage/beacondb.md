---
id: beacondb
name: beaconDB
description: Use when you have a WiFi BSSID, cell-tower ID, or Bluetooth beacon identifier and want to estimate its physical coordinates from a free, open, privacy-friendly geolocation database.
url: https://beacondb.net/
category: geolocation
path:
- geolocation
- mobile-coverage
bestFor: Resolving WiFi/cell/Bluetooth network identifiers to approximate coordinates via an open, MLS-compatible API.
selectorsIn: [mac-address, device-id, ip-address]
selectorsOut: [geolocation]
status: live
pricing: free
costNote: Free and public-domain; the geolocate API is open. No payment; contributors run apps to crowdsource data.
opsec: passive
opsecNote: Querying the database is a server-side lookup that does not touch the target's network or device. The API requires you to set a descriptive User-Agent identifying your client.
humanInLoop: false
humanInLoopReason: [api-key]
bestInteractionPattern: api
trust: community
trustNote: Open-source, public-domain successor to Mozilla Location Service; ethically/crowdsourced and explicitly experimental — coverage is sparse and results may be inaccurate, so corroborate.
missingPersonsRelevance: medium
coverage: [global]
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: [antennasearch, cellmapper-net, celltowermaps-com]
aliases: [beacondb-net]
tags: [wifi, bssid, cell-tower, bluetooth, geolocation, mls]
source: arf-seed
lastVerified: '2026-06-13'
enrichment: full
---

# beaconDB

> A free, public-domain, crowdsourced wireless-geolocation database (WiFi BSSIDs, cell towers, Bluetooth beacons) with an MLS/Ichnaea-compatible API that turns a network identifier into approximate coordinates.

## When to use
You have a network identifier — a WiFi `mac-address` (BSSID), a cell-tower ID, or a Bluetooth beacon `device-id`, perhaps pulled from a device, a screenshot, or logs — and want to estimate where that network physically is. It fills the role Mozilla Location Service used to, as a privacy-friendly, open alternative to Google/Apple geolocation. Useful for placing a device or confirming an area when GPS isn't available.

## How to use it (`bestInteractionPattern`: api)
1. Query the geolocate endpoint: `https://api.beacondb.net/v1/geolocate` (the request/response format is compatible with MLS/Ichnaea).
2. Send a POST with the network details you have (WiFi access points by BSSID, cell tower info, and/or Bluetooth beacons) and **set a descriptive User-Agent** identifying your client (required).
3. Read the JSON response: an estimated latitude/longitude (`geolocation`) and accuracy radius.
4. Confirm against another source before trusting it — coverage is patchy.
5. Pivot: drop the returned coordinate into `[[antennasearch]]` (for nearby registered towers) or a map tool; compare with `[[cellmapper-net]]` for cell-ID coverage.

## Inputs -> Outputs
- **In:** `mac-address` (WiFi BSSID), `device-id` (cell/Bluetooth IDs), `ip-address` (fallback context)
- **Out:** `geolocation` (estimated coordinates + accuracy radius)
- **Empty/negative result looks like:** no match / no position returned — the identifier simply isn't in the crowdsourced dataset yet (very common, since coverage is limited), not proof it doesn't exist.

## Gotchas & OpSec
- **Experimental & sparse:** the project itself warns it may be inaccurate/unreliable and that WiFi coverage is thin in most areas. A miss means "not in DB," not "nowhere."
- You must send a real, identifying User-Agent; anonymous/blank clients may be rejected.
- BSSIDs can move (routers relocate) — a hit reflects where the network was last seen by contributors, which may be stale.
- Treat any single fix as a lead and corroborate with a second method.

## Overlaps ("do both")
- Pairs with `[[antennasearch]]` and `[[celltowermaps-com]]` when your identifier is a cell tower — combine crowdsourced position with registered-tower/coverage data.
- Pairs with `[[cellmapper-net]]` to cross-check cell-ID locations.

## Trust & verifiability
`trust: community` — open-source, public-domain, MLS-compatible and transparently sourced (code on Codeberg), but explicitly experimental with limited coverage. Reliable in method, uneven in data; always corroborate a returned position.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | beacondb |
| category | geolocation |
| selectorsIn → selectorsOut | mac-address, device-id, ip-address → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | api |
| opsec | passive |
| human-in-loop | no |
