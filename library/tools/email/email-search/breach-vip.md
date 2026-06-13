---
id: breach-vip
name: breach.vip
description: Breach database search, credential lookup
url: https://breach.vip/
category: email
path:
- email
- email-search
bestFor: Breach database search, credential lookup
input: Email, domain, Discord ID, or phone number
output: Breach records, leaked credentials
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Queries aggregated public breach databases.
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

# breach.vip

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://breach.vip/
- **Best for:** Breach database search, credential lookup
- **Input → Output:** Email, domain, Discord ID, or phone number → Breach records, leaked credentials
- **OpSec:** passive. Queries aggregated public breach databases.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
