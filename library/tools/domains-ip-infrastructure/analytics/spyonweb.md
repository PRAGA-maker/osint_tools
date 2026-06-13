---
id: spyonweb
name: SpyOnWeb
description: Finding related infrastructure via shared IDs
url: https://www.spyonweb.com/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- analytics
bestFor: Finding related infrastructure via shared IDs
input: Domain or analytics/ad IDs
output: Related domains and shared identifier pivots
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
opsec: passive
opsecNote: Uses indexed identifier data and does not require active probing.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: low
coverage: []
auth: account
api: true
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

# SpyOnWeb

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.spyonweb.com/
- **Best for:** Finding related infrastructure via shared IDs
- **Input → Output:** Domain or analytics/ad IDs → Related domains and shared identifier pivots
- **OpSec:** passive. Uses indexed identifier data and does not require active probing.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
