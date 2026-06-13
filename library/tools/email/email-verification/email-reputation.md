---
id: email-reputation
name: Email Reputation
description: Email reputation checking, risk assessment
url: https://emailrep.io/
category: email
path:
- email
- email-verification
bestFor: Email reputation checking, risk assessment
input: Email address
output: Reputation score, risk level, breach history
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Passive database lookup without target contact.
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

# Email Reputation

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://emailrep.io/
- **Best for:** Email reputation checking, risk assessment
- **Input → Output:** Email address → Reputation score, risk level, breach history
- **OpSec:** passive. Passive database lookup without target contact.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
