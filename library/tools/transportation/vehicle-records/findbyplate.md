---
id: findbyplate
name: FindByPlate
description: US license plate-based vehicle investigations
url: https://findbyplate.com/
category: transportation
path:
- transportation
- vehicle-records
bestFor: US license plate-based vehicle investigations
input: US license plate number and state
output: Vehicle make, model, year, and limited ownership hints
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
opsec: passive
opsecNote: Standard web lookup workflow without active interaction against the vehicle owner.
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

# FindByPlate

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://findbyplate.com/
- **Best for:** US license plate-based vehicle investigations
- **Input → Output:** US license plate number and state → Vehicle make, model, year, and limited ownership hints
- **OpSec:** passive. Standard web lookup workflow without active interaction against the vehicle owner.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
