---
id: ship-ais
name: Ship AIS
description: UK maritime activity monitoring and vessel identification
url: https://shipais.uk/
category: transportation
path:
- transportation
- marine-records
bestFor: UK maritime activity monitoring and vessel identification
input: Vessel name, MMSI, or local waterway context
output: Current position, movement track, vessel details, and nearby traffic
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Reads public AIS transmissions via community infrastructure.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: medium
coverage: []
auth: none
api: false
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

# Ship AIS

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://shipais.uk/
- **Best for:** UK maritime activity monitoring and vessel identification
- **Input → Output:** Vessel name, MMSI, or local waterway context → Current position, movement track, vessel details, and nearby traffic
- **OpSec:** passive. Reads public AIS transmissions via community infrastructure.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
