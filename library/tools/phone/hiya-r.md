---
id: hiya-r
name: Hiya (R$)
description: Spam classification and caller-ID enrichment on mobile workflows
url: https://www.hiya.com/
category: phone
path:
- phone
bestFor: Spam classification and caller-ID enrichment on mobile workflows
input: Phone number
output: Caller identity signals, spam ratings, and reputation context
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
opsec: passive
opsecNote: Most checks are service-mediated; advanced features may still be account-tracked.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: high
coverage: []
auth: account
api: true
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

# Hiya (R$)

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.hiya.com/
- **Best for:** Spam classification and caller-ID enrichment on mobile workflows
- **Input → Output:** Phone number → Caller identity signals, spam ratings, and reputation context
- **OpSec:** passive. Most checks are service-mediated; advanced features may still be account-tracked.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
