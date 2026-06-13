---
id: baidu-maps
name: Baidu Maps
description: Geolocation and POI discovery in mainland China
url: https://map.baidu.com/
category: geolocation
path:
- geolocation
bestFor: Geolocation and POI discovery in mainland China
input: Address, place name, or coordinates
output: Map layers, routes, POIs, and location context
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
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

# Baidu Maps

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://map.baidu.com/
- **Best for:** Geolocation and POI discovery in mainland China
- **Input → Output:** Address, place name, or coordinates → Map layers, routes, POIs, and location context
- **OpSec:** passive. Uses open-source mapping/geospatial data and does not directly interact with the target.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
