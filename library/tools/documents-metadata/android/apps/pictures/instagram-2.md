---
id: instagram-2
name: Instagram
description: Visual reconnaissance, metadata analysis, location tracking via geotagging, relationship mapping
url: https://www.instagram.com/
category: documents-metadata
path:
- documents-metadata
- android
- apps
- pictures
bestFor: Visual reconnaissance, metadata analysis, location tracking via geotagging, relationship mapping
input: Usernames, hashtags, locations, profile URLs
output: User profiles, photos, videos, captions, location data, follower networks
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: active
opsecNote: Instagram aggressively blocks scraping tools; bulk data collection easily detected
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

# Instagram

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.instagram.com/
- **Best for:** Visual reconnaissance, metadata analysis, location tracking via geotagging, relationship mapping
- **Input → Output:** Usernames, hashtags, locations, profile URLs → User profiles, photos, videos, captions, location data, follower networks
- **OpSec:** active. Instagram aggressively blocks scraping tools; bulk data collection easily detected

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
