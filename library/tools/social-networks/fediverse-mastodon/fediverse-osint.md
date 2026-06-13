---
id: fediverse-osint
name: Fediverse_OSINT
description: Cross-instance Fediverse user and content search
url: https://github.com/cyfinoid/fediverse_osint
category: social-networks
path:
- social-networks
- fediverse-mastodon
bestFor: Cross-instance Fediverse user and content search
input: Username or search terms
output: User profiles and posts found across Fediverse instances
selectorsIn: []
selectorsOut: []
status: degraded
pricing: free
opsec: active
opsecNote: Queries multiple Fediverse instances directly; requests may be logged by instance administrators.
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

# Fediverse_OSINT

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://github.com/cyfinoid/fediverse_osint
- **Best for:** Cross-instance Fediverse user and content search
- **Input → Output:** Username or search terms → User profiles and posts found across Fediverse instances
- **OpSec:** active. Queries multiple Fediverse instances directly; requests may be logged by instance administrators.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
