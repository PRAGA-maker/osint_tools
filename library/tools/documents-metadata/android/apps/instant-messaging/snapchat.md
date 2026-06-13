---
id: snapchat
name: Snapchat
description: User verification, story analysis, location tracking via snap maps, relationship mapping
url: https://www.snapchat.com/
category: documents-metadata
path:
- documents-metadata
- android
- apps
- instant-messaging
bestFor: User verification, story analysis, location tracking via snap maps, relationship mapping
input: Usernames, Snapcodes, phone numbers
output: User profiles, story content, snap maps, friend networks
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: active
opsecNote: Snapchat actively detects and blocks third-party clients; API access is restricted
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

# Snapchat

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.snapchat.com/
- **Best for:** User verification, story analysis, location tracking via snap maps, relationship mapping
- **Input → Output:** Usernames, Snapcodes, phone numbers → User profiles, story content, snap maps, friend networks
- **OpSec:** active. Snapchat actively detects and blocks third-party clients; API access is restricted

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
