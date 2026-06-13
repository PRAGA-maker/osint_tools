---
id: bing-maps
name: Bing Maps
description: General geolocation and route context with Microsoft map data
url: https://www.bing.com/maps
category: geolocation
path:
- geolocation
bestFor: General geolocation and route context with Microsoft map data
input: Address, place name, or coordinates
output: Map views, routes, and nearby POI results
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

# Bing Maps

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.bing.com/maps
- **Best for:** General geolocation and route context with Microsoft map data
- **Input → Output:** Address, place name, or coordinates → Map views, routes, and nearby POI results
- **OpSec:** passive. Uses open-source mapping/geospatial data and does not directly interact with the target.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
