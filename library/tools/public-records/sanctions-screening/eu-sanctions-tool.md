---
id: eu-sanctions-tool
name: EU Sanctions Tool
description: Checking individuals or entities against EU sanctions regimes
url: https://sanctions-tool.ec.europa.eu
category: public-records
path:
- public-records
- sanctions-screening
bestFor: Checking individuals or entities against EU sanctions regimes
input: Person or entity name
output: Matches against EU consolidated sanctions list with designation details
selectorsIn: []
selectorsOut: []
status: degraded
pricing: free
opsec: passive
opsecNote: Public EU government search tool; queries are submitted to an EU server and may be logged.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: low
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

# EU Sanctions Tool

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://sanctions-tool.ec.europa.eu
- **Best for:** Checking individuals or entities against EU sanctions regimes
- **Input → Output:** Person or entity name → Matches against EU consolidated sanctions list with designation details
- **OpSec:** passive. Public EU government search tool; queries are submitted to an EU server and may be logged.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
