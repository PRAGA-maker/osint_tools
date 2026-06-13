---
id: telegram
name: Telegram
description: User discovery, channel monitoring, group reconnaissance, bot creation for data collection
url: https://telegram.org/
category: documents-metadata
path:
- documents-metadata
- android
- apps
- instant-messaging
bestFor: User discovery, channel monitoring, group reconnaissance, bot creation for data collection
input: Usernames, user IDs, chat links, phone numbers
output: User profiles, channel data, group membership, message history, media
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Public channels and users are accessible without authentication; bot development requires API key
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

# Telegram

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://telegram.org/
- **Best for:** User discovery, channel monitoring, group reconnaissance, bot creation for data collection
- **Input → Output:** Usernames, user IDs, chat links, phone numbers → User profiles, channel data, group membership, message history, media
- **OpSec:** passive. Public channels and users are accessible without authentication; bot development requires API key

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
