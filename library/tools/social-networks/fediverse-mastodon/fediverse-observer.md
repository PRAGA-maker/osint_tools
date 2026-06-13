---
id: fediverse-observer
name: Fediverse Observer
description: Discovering and mapping Fediverse instances by software, country, or size
url: https://fediverse.observer/
category: social-networks
path:
- social-networks
- fediverse-mastodon
bestFor: Discovering and mapping Fediverse instances by software, country, or size
input: Search filters (software type, country, language, instance name)
output: Instance list with user counts, uptime, software version, registration status, and geographic location
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Queries the Fediverse Observer database, not individual instances; no contact with target servers.
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

# Fediverse Observer

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://fediverse.observer/
- **Best for:** Discovering and mapping Fediverse instances by software, country, or size
- **Input → Output:** Search filters (software type, country, language, instance name) → Instance list with user counts, uptime, software version, registration status, and geographic location
- **OpSec:** passive. Queries the Fediverse Observer database, not individual instances; no contact with target servers.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
