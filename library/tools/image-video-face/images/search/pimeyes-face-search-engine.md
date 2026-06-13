---
id: pimeyes-face-search-engine
name: PimEyes Face Search Engine
description: High-coverage reverse face search investigations
url: https://pimeyes.com/en
category: image-video-face
path:
- image-video-face
- images
- search
bestFor: High-coverage reverse face search investigations
input: Face photo upload
output: Matched face thumbnails and source-page links
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
opsec: active
opsecNote: Face image is uploaded and processed by a third-party biometric search provider.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: high
coverage: []
auth: account
api: false
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

# PimEyes Face Search Engine

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://pimeyes.com/en
- **Best for:** High-coverage reverse face search investigations
- **Input → Output:** Face photo upload → Matched face thumbnails and source-page links
- **OpSec:** active. Face image is uploaded and processed by a third-party biometric search provider.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
