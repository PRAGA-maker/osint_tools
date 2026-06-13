---
id: myaccident-traffic-accident-map
name: MyAccident - traffic accident map
description: US accident history verification and claims investigations
url: https://myaccident.org/
category: transportation
path:
- transportation
- vehicle-records
bestFor: US accident history verification and claims investigations
input: Accident location, address, or basic vehicle details
output: Redacted accident reports, crash severity, and location data
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Read-only public database access; no direct contact with investigation targets.
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

# MyAccident - traffic accident map

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://myaccident.org/
- **Best for:** US accident history verification and claims investigations
- **Input → Output:** Accident location, address, or basic vehicle details → Redacted accident reports, crash severity, and location data
- **OpSec:** passive. Read-only public database access; no direct contact with investigation targets.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
