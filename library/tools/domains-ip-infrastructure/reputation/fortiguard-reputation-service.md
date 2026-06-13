---
id: fortiguard-reputation-service
name: FortiGuard Reputation Service
description: IP reputation lookup, botnet/malware source identification, threat intelligence
url: https://fortiguard.com/iprep
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- reputation
bestFor: IP reputation lookup, botnet/malware source identification, threat intelligence
input: IP address or IP range
output: IP reputation score, threat categories, malware associations, botnet status
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Queries Fortinet's IP reputation database without contacting the target IP.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: low
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

# FortiGuard Reputation Service

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://fortiguard.com/iprep
- **Best for:** IP reputation lookup, botnet/malware source identification, threat intelligence
- **Input → Output:** IP address or IP range → IP reputation score, threat categories, malware associations, botnet status
- **OpSec:** passive. Queries Fortinet's IP reputation database without contacting the target IP.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
