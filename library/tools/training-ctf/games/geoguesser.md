---
id: geoguesser
name: GeoGuesser
description: Geolocation skills, visual intelligence analysis, landmark identification
url: https://www.geoguessr.com/
category: training-ctf
path:
- training-ctf
- games
bestFor: Geolocation skills, visual intelligence analysis, landmark identification
input: Street View imagery, map interface
output: Accuracy score, location guess feedback, player rankings
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
opsec: passive
opsecNote: No active reconnaissance; purely observational gameplay using public imagery.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: low
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

# GeoGuesser

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.geoguessr.com/
- **Best for:** Geolocation skills, visual intelligence analysis, landmark identification
- **Input → Output:** Street View imagery, map interface → Accuracy score, location guess feedback, player rankings
- **OpSec:** passive. No active reconnaissance; purely observational gameplay using public imagery.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
