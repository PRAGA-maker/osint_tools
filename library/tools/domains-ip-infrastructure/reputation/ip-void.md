---
id: ip-void
name: IP Void
description: Check IP reputation and blacklist status
url: https://www.ipvoid.com/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- reputation
bestFor: Check IP reputation and blacklist status
input: IP address
output: Threat score, blacklist status, reports
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
opsec: passive
opsecNote: Passive reputation lookup; account needed for full data.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: low
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

# IP Void

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.ipvoid.com/
- **Best for:** Check IP reputation and blacklist status
- **Input → Output:** IP address → Threat score, blacklist status, reports
- **OpSec:** passive. Passive reputation lookup; account needed for full data.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
