---
id: facecheck-facial-recognition-search
name: FaceCheck Facial Recognition Search
description: Finding public social profiles by face image
url: https://facecheck.id/
category: image-video-face
path:
- image-video-face
- images
- search
bestFor: Finding public social profiles by face image
input: Face photo upload
output: Potential face matches with source links and similarity scoring
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
opsec: active
opsecNote: Uploads target imagery to a third-party face-search service; treat as active collection.
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

# FaceCheck Facial Recognition Search

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://facecheck.id/
- **Best for:** Finding public social profiles by face image
- **Input → Output:** Face photo upload → Potential face matches with source links and similarity scoring
- **OpSec:** active. Uploads target imagery to a third-party face-search service; treat as active collection.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
