---
id: hivemapper
name: Hivemapper
description: Street-level imagery in areas with limited mainstream coverage
url: https://hivemapper.com/
category: geolocation
path:
- geolocation
bestFor: Street-level imagery in areas with limited mainstream coverage
input: Location query
output: Crowdsourced map and imagery tiles
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
opsec: passive
opsecNote: Uses open-source mapping/geospatial data and does not directly interact with the target.
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

# Hivemapper

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://hivemapper.com/
- **Best for:** Street-level imagery in areas with limited mainstream coverage
- **Input → Output:** Location query → Crowdsourced map and imagery tiles
- **OpSec:** passive. Uses open-source mapping/geospatial data and does not directly interact with the target.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
