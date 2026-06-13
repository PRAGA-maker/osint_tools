---
id: autodna-vin-lookup
name: autoDNA VIN Lookup
description: VIN-based damage, ownership, and service history checks
url: https://www.autodna.com/
category: transportation
path:
- transportation
- vehicle-records
bestFor: VIN-based damage, ownership, and service history checks
input: 17-character VIN
output: Inspection, damage, repair, ownership, and mileage records
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
opsec: passive
opsecNote: Passive lookup model; full intelligence requires paid report access.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: medium
coverage: []
auth: account
api: false
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

# autoDNA VIN Lookup

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.autodna.com/
- **Best for:** VIN-based damage, ownership, and service history checks
- **Input → Output:** 17-character VIN → Inspection, damage, repair, ownership, and mileage records
- **OpSec:** passive. Passive lookup model; full intelligence requires paid report access.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
