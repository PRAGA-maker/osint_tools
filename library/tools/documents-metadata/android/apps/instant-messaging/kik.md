---
id: kik
name: Kik
description: User discovery, profile analysis, public username search
url: https://www.kik.com/
category: documents-metadata
path:
- documents-metadata
- android
- apps
- instant-messaging
bestFor: User discovery, profile analysis, public username search
input: Usernames, user handles
output: User profiles, status, profile pictures, user discovery
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Public search available; less monitored than major platforms
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: cli
trust: unverified
trustNote: ''
missingPersonsRelevance: medium
coverage: []
auth: account
api: false
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

# Kik

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.kik.com/
- **Best for:** User discovery, profile analysis, public username search
- **Input → Output:** Usernames, user handles → User profiles, status, profile pictures, user discovery
- **OpSec:** passive. Public search available; less monitored than major platforms

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
