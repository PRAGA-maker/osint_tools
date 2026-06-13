---
id: whatsapp-messenger
name: WhatsApp Messenger
description: User verification, profile discovery, status updates, contact verification
url: https://www.whatsapp.com/
category: documents-metadata
path:
- documents-metadata
- android
- apps
- instant-messaging
bestFor: User verification, profile discovery, status updates, contact verification
input: Phone numbers, WhatsApp IDs
output: User profiles, status messages, profile pictures, last-seen timestamps, online status
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: No official API for OSINT; third-party tools easily detected and account-banned
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

# WhatsApp Messenger

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.whatsapp.com/
- **Best for:** User verification, profile discovery, status updates, contact verification
- **Input → Output:** Phone numbers, WhatsApp IDs → User profiles, status messages, profile pictures, last-seen timestamps, online status
- **OpSec:** passive. No official API for OSINT; third-party tools easily detected and account-banned

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
