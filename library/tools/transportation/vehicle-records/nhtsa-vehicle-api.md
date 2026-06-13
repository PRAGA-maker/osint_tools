---
id: nhtsa-vehicle-api
name: NHTSA Vehicle API
description: VIN decoding and US vehicle specification checks
url: https://vpic.nhtsa.dot.gov/api/
category: transportation
path:
- transportation
- vehicle-records
bestFor: VIN decoding and US vehicle specification checks
input: 17-character VIN (full or partial with wildcards)
output: Make, model, year, manufacturer, engine details, and related data
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Public government API endpoint with anonymous read access.
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

# NHTSA Vehicle API

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://vpic.nhtsa.dot.gov/api/
- **Best for:** VIN decoding and US vehicle specification checks
- **Input → Output:** 17-character VIN (full or partial with wildcards) → Make, model, year, manufacturer, engine details, and related data
- **OpSec:** passive. Public government API endpoint with anonymous read access.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
