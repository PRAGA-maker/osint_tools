---
id: steamosint
name: SteamOSINT
description: Steam account investigation and user profile analysis
url: https://github.com/Frontline-Femmes/Steam-OSINT
category: social-networks
path:
- social-networks
- steam-discord-and-gaming-networks
bestFor: Steam account investigation and user profile analysis
input: Steam username or profile URL
output: User profile details, games library, playtime, achievements, trade history, and public friend lists
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: active
opsecNote: Queries Steam's public API and web interface; requests are visible in Steam community logs.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: unverified
trustNote: ''
missingPersonsRelevance: high
coverage: []
auth: none
api: true
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

# SteamOSINT

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://github.com/Frontline-Femmes/Steam-OSINT
- **Best for:** Steam account investigation and user profile analysis
- **Input → Output:** Steam username or profile URL → User profile details, games library, playtime, achievements, trade history, and public friend lists
- **OpSec:** active. Queries Steam's public API and web interface; requests are visible in Steam community logs.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
