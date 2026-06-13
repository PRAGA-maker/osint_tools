---
id: ofac-sanctions-list-search
name: OFAC Sanctions List Search
description: Checking individuals or entities against U.S. sanctions programs
url: https://sanctionssearch.ofac.treas.gov/
category: public-records
path:
- public-records
- sanctions-screening
bestFor: Checking individuals or entities against U.S. sanctions programs
input: Name, address, entity type, ID number, or sanctions program
output: Matched records with name, sanctions program, list designation, and confidence score
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Public U.S. government search tool; queries are submitted to a federal server and may be logged.
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
- **Best for:** Checking individuals or entities against U.S. sanctions programs
- **Input → Output:** Name, address, entity type, ID number, or sanctions program → Matched records with name, sanctions program, list designation, and confidence score
- **OpSec:** passive. Public U.S. government search tool; queries are submitted to a federal server and may be logged.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
