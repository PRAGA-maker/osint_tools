---
id: criminal-ip-search-2
name: Criminal IP Search
description: IP reputation and malicious activity analysis
url: https://www.criminalip.io/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- host-port-discovery
bestFor: IP reputation and malicious activity analysis
input: IP address
output: Threat reports, activity logs, attack types
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
opsec: passive
opsecNote: Passive threat intelligence lookup.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: low
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

# Criminal IP Search

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.criminalip.io/
- **Best for:** IP reputation and malicious activity analysis
- **Input → Output:** IP address → Threat reports, activity logs, attack types
- **OpSec:** passive. Passive threat intelligence lookup.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
