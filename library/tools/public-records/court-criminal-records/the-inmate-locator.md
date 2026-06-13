---
id: the-inmate-locator
name: The Inmate Locator
description: Federal inmate location
url: https://www.bop.gov/inmateloc/
category: public-records
path:
- public-records
- court-criminal-records
bestFor: Federal inmate location
input: Name or BOP register number
output: Location, release date, facility
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Official federal database
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: medium
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

# The Inmate Locator

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.bop.gov/inmateloc/
- **Best for:** Federal inmate location
- **Input → Output:** Name or BOP register number → Location, release date, facility
- **OpSec:** passive. Official federal database

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
