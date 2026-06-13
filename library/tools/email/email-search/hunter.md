---
id: hunter
name: Hunter
description: Business email discovery, email verification
url: https://hunter.io/
category: email
path:
- email
- email-search
bestFor: Business email discovery, email verification
input: Domain name, person name, or company info
output: Verified business email addresses
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
opsec: passive
opsecNote: Queries Hunter's database of public emails; does not contact targets.
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

# Hunter

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://hunter.io/
- **Best for:** Business email discovery, email verification
- **Input → Output:** Domain name, person name, or company info → Verified business email addresses
- **OpSec:** passive. Queries Hunter's database of public emails; does not contact targets.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
