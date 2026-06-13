---
id: federal-inmate-locator
name: Federal Inmate Locator
description: Federal inmate location and release dates
url: https://www.bop.gov/inmateloc/
category: public-records
path:
- public-records
- court-criminal-records
bestFor: Federal inmate location and release dates
input: Name or BOP register number
output: Inmate location, facility, release date
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Official federal database, daily updates
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

# Federal Inmate Locator

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.bop.gov/inmateloc/
- **Best for:** Federal inmate location and release dates
- **Input → Output:** Name or BOP register number → Inmate location, facility, release date
- **OpSec:** passive. Official federal database, daily updates

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
