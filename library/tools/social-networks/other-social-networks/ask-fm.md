---
id: ask-fm
name: Ask FM
description: Finding Ask FM profiles by username
url: https://ask.fm/%3Cusername%3E
category: social-networks
path:
- social-networks
- other-social-networks
bestFor: Finding Ask FM profiles by username
input: Ask FM username
output: Public profile, Q&A history, followers, and profile metadata
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Standard web request to Ask FM public profile; profile views are not logged to target users.
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

# Ask FM

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://ask.fm/%3Cusername%3E
- **Best for:** Finding Ask FM profiles by username
- **Input → Output:** Ask FM username → Public profile, Q&A history, followers, and profile metadata
- **OpSec:** passive. Standard web request to Ask FM public profile; profile views are not logged to target users.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
