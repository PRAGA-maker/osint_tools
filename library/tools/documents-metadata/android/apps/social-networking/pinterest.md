---
id: pinterest
name: Pinterest
description: Interest profiling, location discovery, lifestyle analysis, image reverse search
url: https://www.pinterest.com/
category: documents-metadata
path:
- documents-metadata
- android
- apps
- social-networking
bestFor: Interest profiling, location discovery, lifestyle analysis, image reverse search
input: Usernames, pins, boards, images
output: User profiles, boards, pins, location metadata, follower networks
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Passive reconnaissance; less aggressively monitored than Facebook or LinkedIn
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

# Pinterest

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.pinterest.com/
- **Best for:** Interest profiling, location discovery, lifestyle analysis, image reverse search
- **Input → Output:** Usernames, pins, boards, images → User profiles, boards, pins, location metadata, follower networks
- **OpSec:** passive. Passive reconnaissance; less aggressively monitored than Facebook or LinkedIn

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
