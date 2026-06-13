---
id: line
name: LINE
description: Asian market user discovery, profile analysis, account verification
url: https://line.me/
category: documents-metadata
path:
- documents-metadata
- android
- apps
- instant-messaging
bestFor: Asian market user discovery, profile analysis, account verification
input: User IDs, phone numbers, LINE accounts
output: User profiles, status messages, timeline data, friends list
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Public profile search available; varies by region and privacy settings
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: cli
trust: unverified
trustNote: ''
missingPersonsRelevance: medium
coverage: []
auth: account
api: true
localInstall: true
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

# LINE

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://line.me/
- **Best for:** Asian market user discovery, profile analysis, account verification
- **Input → Output:** User IDs, phone numbers, LINE accounts → User profiles, status messages, timeline data, friends list
- **OpSec:** passive. Public profile search available; varies by region and privacy settings

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
