---
id: ads-b-exchange
name: ADS-B Exchange
description: Unfiltered aircraft tracking and historical flight pattern analysis
url: https://www.adsbexchange.com/
category: transportation
path:
- transportation
- air-traffic-records
bestFor: Unfiltered aircraft tracking and historical flight pattern analysis
input: Aircraft identifier, registration, hex code, or location
output: Live aircraft position, altitude, speed, and historical track data
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
opsec: passive
opsecNote: Consumes broadcast telemetry from receiver networks without active interaction.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: medium
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

# ADS-B Exchange

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.adsbexchange.com/
- **Best for:** Unfiltered aircraft tracking and historical flight pattern analysis
- **Input → Output:** Aircraft identifier, registration, hex code, or location → Live aircraft position, altitude, speed, and historical track data
- **OpSec:** passive. Consumes broadcast telemetry from receiver networks without active interaction.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
