---
id: opencellid
name: OpenCelliD
description: Cell tower identification and approximate location triangulation
url: https://opencellid.org/
category: geolocation
path:
- geolocation
- mobile-coverage
bestFor: Cell tower identification and approximate location triangulation
input: Cell identifiers or coordinates
output: Cell tower records and geographic positions
selectorsIn: []
selectorsOut: []
status: live
pricing: free
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

# OpenCelliD

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://opencellid.org/
- **Best for:** Cell tower identification and approximate location triangulation
- **Input → Output:** Cell identifiers or coordinates → Cell tower records and geographic positions
- **OpSec:** passive. Uses open-source mapping/geospatial data and does not directly interact with the target.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
