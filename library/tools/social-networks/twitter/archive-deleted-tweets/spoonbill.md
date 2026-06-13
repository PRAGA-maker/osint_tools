---
id: spoonbill
name: Spoonbill
description: Monitoring profile change history
url: https://spoonbill.io/
category: social-networks
path:
- social-networks
- twitter
- archive-deleted-tweets
bestFor: Monitoring profile change history
input: Twitter/X usernames
output: Historical profile snapshots and change alerts
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
opsec: passive
opsecNote: Monitoring is indirect; investigator does not directly engage target accounts.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: high
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

# Spoonbill

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://spoonbill.io/
- **Best for:** Monitoring profile change history
- **Input → Output:** Twitter/X usernames → Historical profile snapshots and change alerts
- **OpSec:** passive. Monitoring is indirect; investigator does not directly engage target accounts.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
