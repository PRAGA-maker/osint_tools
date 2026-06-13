---
id: vessel-finder
name: Vessel Finder
description: Worldwide ship tracking and port-call timeline analysis
url: https://www.vesselfinder.com/
category: transportation
path:
- transportation
- marine-records
bestFor: Worldwide ship tracking and port-call timeline analysis
input: Vessel name, IMO, MMSI, or geographic area
output: Live vessel tracks, destination status, and historical route context
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
opsec: passive
opsecNote: Passive maritime telemetry consumption through aggregated AIS feeds.
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

# Vessel Finder

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.vesselfinder.com/
- **Best for:** Worldwide ship tracking and port-call timeline analysis
- **Input → Output:** Vessel name, IMO, MMSI, or geographic area → Live vessel tracks, destination status, and historical route context
- **OpSec:** passive. Passive maritime telemetry consumption through aggregated AIS feeds.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
