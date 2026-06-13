---
id: mapquest
name: MapQuest
description: Route analysis and multi-stop planning
url: https://www.mapquest.com/
category: geolocation
path:
- geolocation
bestFor: Route analysis and multi-stop planning
input: Origin, destination, and stop list
output: Turn-by-turn routes and distance metrics
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

# MapQuest

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.mapquest.com/
- **Best for:** Route analysis and multi-stop planning
- **Input → Output:** Origin, destination, and stop list → Turn-by-turn routes and distance metrics
- **OpSec:** passive. Uses open-source mapping/geospatial data and does not directly interact with the target.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
