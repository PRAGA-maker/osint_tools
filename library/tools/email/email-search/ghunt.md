---
id: ghunt
name: GHunt
description: Google account investigation, YouTube/Google Photos OSINT
url: https://github.com/mxrch/GHunt
category: email
path:
- email
- email-search
bestFor: Google account investigation, YouTube/Google Photos OSINT
input: Gmail address or GAIA ID
output: YouTube channels, Google Photos, Maps reviews, device info
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: active
opsecNote: Requires Google login via browser extension; may be detected by Google.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: unverified
trustNote: ''
missingPersonsRelevance: high
coverage: []
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases: []
tags: []
source: arf-seed
lastVerified: ''
enrichment: stub
---

# GHunt

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://github.com/mxrch/GHunt
- **Best for:** Google account investigation, YouTube/Google Photos OSINT
- **Input → Output:** Gmail address or GAIA ID → YouTube channels, Google Photos, Maps reviews, device info
- **OpSec:** active. Requires Google login via browser extension; may be detected by Google.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
