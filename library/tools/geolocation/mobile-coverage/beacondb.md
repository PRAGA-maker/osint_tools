---
id: beacondb
name: beaconDB
description: Beacon and AP-based geolocation without major platform lock-in
url: https://beacondb.net/
category: geolocation
path:
- geolocation
- mobile-coverage
bestFor: Beacon and AP-based geolocation without major platform lock-in
input: BSSID/cell IDs or coordinates
output: Geolocated beacon and network records
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Uses open-source mapping/geospatial data and does not directly interact with the target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: high
coverage: []
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases: []
tags: []
source: arf-seed
lastVerified: ''
enrichment: stub
---

# beaconDB

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://beacondb.net/
- **Best for:** Beacon and AP-based geolocation without major platform lock-in
- **Input → Output:** BSSID/cell IDs or coordinates → Geolocated beacon and network records
- **OpSec:** passive. Uses open-source mapping/geospatial data and does not directly interact with the target.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
