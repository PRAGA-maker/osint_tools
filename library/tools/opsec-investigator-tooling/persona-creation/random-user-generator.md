---
id: random-user-generator
name: Random User Generator
description: Bulk persona generation, test account data, application seeding
url: https://randomuser.me/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
- persona-creation
bestFor: Bulk persona generation, test account data, application seeding
input: Nationality, gender, quantity, and field filters via API or web
output: JSON user objects with name, location, email, phone, photo, DOB, and login data
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: API-based generation with no data retention; all output is synthetic.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: medium
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

# Random User Generator

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://randomuser.me/
- **Best for:** Bulk persona generation, test account data, application seeding
- **Input → Output:** Nationality, gender, quantity, and field filters via API or web → JSON user objects with name, location, email, phone, photo, DOB, and login data
- **OpSec:** passive. API-based generation with no data retention; all output is synthetic.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
