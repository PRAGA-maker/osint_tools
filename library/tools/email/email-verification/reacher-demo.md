---
id: reacher-demo
name: Reacher Demo
description: Email verification testing, demonstration
url: https://reacher.email
category: email
path:
- email
- email-verification
bestFor: Email verification testing, demonstration
input: Email address
output: Deliverability status, bounce information
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Passive MTA-based verification without sending emails.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: high
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

# Reacher Demo

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://reacher.email
- **Best for:** Email verification testing, demonstration
- **Input → Output:** Email address → Deliverability status, bounce information
- **OpSec:** passive. Passive MTA-based verification without sending emails.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
