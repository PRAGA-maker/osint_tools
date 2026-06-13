---
id: instagram
name: Instagram
description: Social profiling and image discovery
url: https://www.instagram.com/
category: image-video-face
path:
- image-video-face
- images
- instagram
bestFor: Social profiling and image discovery
input: Usernames, hashtags, locations
output: Profiles, posts, location signals, and network context
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
opsec: passive
opsecNote: Viewing public content is low-friction, but platform telemetry and account controls still apply.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: high
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

# Instagram

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.instagram.com/
- **Best for:** Social profiling and image discovery
- **Input → Output:** Usernames, hashtags, locations → Profiles, posts, location signals, and network context
- **OpSec:** passive. Viewing public content is low-friction, but platform telemetry and account controls still apply.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
