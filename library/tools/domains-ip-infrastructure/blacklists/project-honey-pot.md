---
id: project-honey-pot
name: Project Honey Pot
description: Check IP for spam and attack history
url: https://www.projecthoneypot.org/list_of_ips.php
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- blacklists
bestFor: Check IP for spam and attack history
input: IP address
output: Threat score, spam reports, attack activity
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
opsec: passive
opsecNote: Passive lookup of honeypot-collected threat data.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: low
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

# Project Honey Pot

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.projecthoneypot.org/list_of_ips.php
- **Best for:** Check IP for spam and attack history
- **Input → Output:** IP address → Threat score, spam reports, attack activity
- **OpSec:** passive. Passive lookup of honeypot-collected threat data.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
