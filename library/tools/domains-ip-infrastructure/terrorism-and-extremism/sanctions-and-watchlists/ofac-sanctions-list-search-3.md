---
id: ofac-sanctions-list-search-3
name: OFAC Sanctions List Search
description: Sanctions list lookups
url: https://sanctionssearch.ofac.treas.gov/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- terrorism-and-extremism
- sanctions-and-watchlists
bestFor: Sanctions list lookups
input: Person or entity name
output: Sanctions status and entity information
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Government database lookup with approximate matching
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

# OFAC Sanctions List Search

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://sanctionssearch.ofac.treas.gov/
- **Best for:** Sanctions list lookups
- **Input → Output:** Person or entity name → Sanctions status and entity information
- **OpSec:** passive. Government database lookup with approximate matching

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
