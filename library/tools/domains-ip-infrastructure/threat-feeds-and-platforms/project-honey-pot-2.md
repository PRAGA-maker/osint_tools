---
id: project-honey-pot-2
name: Project Honey Pot
description: Spam and harvester tracking
url: https://www.projecthoneypot.org/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- threat-feeds-and-platforms
bestFor: Spam and harvester tracking
input: IP address or email domain
output: Harvester and spam activity records
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Passive honeypot intelligence
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

# Project Honey Pot

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.projecthoneypot.org/
- **Best for:** Spam and harvester tracking
- **Input → Output:** IP address or email domain → Harvester and spam activity records
- **OpSec:** passive. Passive honeypot intelligence

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
