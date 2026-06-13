---
id: signal-private-messenger
name: Signal Private Messenger
description: Identity verification, account discovery via phone/email, community research
url: https://signal.org/
category: documents-metadata
path:
- documents-metadata
- android
- apps
- instant-messaging
bestFor: Identity verification, account discovery via phone/email, community research
input: Phone numbers, email addresses, usernames
output: Account existence, profile names, avatar images
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Very limited information exposure; encrypted content not accessible
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

# Signal Private Messenger

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://signal.org/
- **Best for:** Identity verification, account discovery via phone/email, community research
- **Input → Output:** Phone numbers, email addresses, usernames → Account existence, profile names, avatar images
- **OpSec:** passive. Very limited information exposure; encrypted content not accessible

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
