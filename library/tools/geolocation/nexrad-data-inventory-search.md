---
id: nexrad-data-inventory-search
name: NEXRAD Data Inventory Search
description: Locating radar archives for weather-event correlation
url: https://www.ncdc.noaa.gov/nexradinv/
category: geolocation
path:
- geolocation
bestFor: Locating radar archives for weather-event correlation
input: Radar station, date, and query filters
output: Inventory records and radar dataset references
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Uses open-source mapping/geospatial data and does not directly interact with the target.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: high
coverage: []
auth: account
api: true
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools: []
aliases: []
tags: []
source: arf-seed
lastVerified: ''
enrichment: stub
---

# NEXRAD Data Inventory Search

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.ncdc.noaa.gov/nexradinv/
- **Best for:** Locating radar archives for weather-event correlation
- **Input → Output:** Radar station, date, and query filters → Inventory records and radar dataset references
- **OpSec:** passive. Uses open-source mapping/geospatial data and does not directly interact with the target.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
