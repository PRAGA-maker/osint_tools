---
id: facebook
name: Facebook
description: Profile reconnaissance, relationship mapping, photo analysis, location tracking
url: https://www.facebook.com/
category: documents-metadata
path:
- documents-metadata
- android
- apps
- social-networking
bestFor: Profile reconnaissance, relationship mapping, photo analysis, location tracking
input: Usernames, profile URLs, phone numbers, email addresses
output: Profile data, friend networks, photos, location history, activity timeline
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: active
opsecNote: Facebook monitors and blocks suspicious activity patterns; tool-based scraping is easily detected
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

# Facebook

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.facebook.com/
- **Best for:** Profile reconnaissance, relationship mapping, photo analysis, location tracking
- **Input → Output:** Usernames, profile URLs, phone numbers, email addresses → Profile data, friend networks, photos, location history, activity timeline
- **OpSec:** active. Facebook monitors and blocks suspicious activity patterns; tool-based scraping is easily detected

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
