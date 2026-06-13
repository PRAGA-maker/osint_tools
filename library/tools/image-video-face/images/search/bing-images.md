---
id: bing-images
name: Bing Images
description: Cropped reverse-image matching and visual component analysis
url: https://www.bing.com/images
category: image-video-face
path:
- image-video-face
- images
- search
bestFor: Cropped reverse-image matching and visual component analysis
input: Image upload, image URL, or cropped image region
output: Matching images, related pages, and object-level visual matches
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Performs web search queries without direct interaction with target identities.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: high
coverage: []
auth: none
api: false
localInstall: false
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

# Bing Images

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.bing.com/images
- **Best for:** Cropped reverse-image matching and visual component analysis
- **Input → Output:** Image upload, image URL, or cropped image region → Matching images, related pages, and object-level visual matches
- **OpSec:** passive. Performs web search queries without direct interaction with target identities.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
