---
id: autoref-eu
name: AutoRef (EU)
description: EU vehicle specification lookup and plate-to-VIN workflows
url: https://www.autoref.eu/en
category: transportation
path:
- transportation
- vehicle-records
bestFor: EU vehicle specification lookup and plate-to-VIN workflows
input: European VIN or license plate number
output: Vehicle make, model, engine, registration, and technical profile data
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
opsec: passive
opsecNote: Passive web queries with quota limits on the free tier.
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

# AutoRef (EU)

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.autoref.eu/en
- **Best for:** EU vehicle specification lookup and plate-to-VIN workflows
- **Input → Output:** European VIN or license plate number → Vehicle make, model, engine, registration, and technical profile data
- **OpSec:** passive. Passive web queries with quota limits on the free tier.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
