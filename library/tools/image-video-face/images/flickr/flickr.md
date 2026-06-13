---
id: flickr
name: Flickr
description: Image metadata and geolocation investigation
url: https://www.flickr.com/
category: image-video-face
path:
- image-video-face
- images
- flickr
bestFor: Image metadata and geolocation investigation
input: Usernames, tags, photo links, map regions
output: Public photos with metadata and account context
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
opsec: passive
opsecNote: Public browsing is generally low-risk; API and account use may be logged.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: high
coverage: []
auth: none
api: true
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

# Flickr

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.flickr.com/
- **Best for:** Image metadata and geolocation investigation
- **Input → Output:** Usernames, tags, photo links, map regions → Public photos with metadata and account context
- **OpSec:** passive. Public browsing is generally low-risk; API and account use may be logged.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
