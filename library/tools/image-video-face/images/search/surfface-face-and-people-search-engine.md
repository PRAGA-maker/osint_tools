---
id: surfface-face-and-people-search-engine
name: Surfface Face & People Search Engine
description: Identity correlation from face imagery
url: https://surfface.com/
category: image-video-face
path:
- image-video-face
- images
- search
bestFor: Identity correlation from face imagery
input: Face photo and optional identifying context
output: Candidate profile matches from publicly available web sources
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
opsec: active
opsecNote: Submits facial data to vendor infrastructure for matching against indexed sources.
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

# Surfface Face & People Search Engine

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://surfface.com/
- **Best for:** Identity correlation from face imagery
- **Input → Output:** Face photo and optional identifying context → Candidate profile matches from publicly available web sources
- **OpSec:** active. Submits facial data to vendor infrastructure for matching against indexed sources.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
