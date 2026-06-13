---
id: ofac-sanctions-list-search-2
name: OFAC Sanctions List Search
description: Checking against U.S. government sanctions list (SDN and consolidated lists)
url: https://sanctionssearch.ofac.treas.gov/
category: financial-crypto
path:
- financial-crypto
- mixer-tracking
bestFor: Checking against U.S. government sanctions list (SDN and consolidated lists)
input: Individual or entity name (fuzzy-matched), alias variations
output: SDN list matches, alternate names, addresses, dates of birth (when available), designation details
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Official government database; searches are not logged against user identity but accessing the government website may be monitored.
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

# OFAC Sanctions List Search

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://sanctionssearch.ofac.treas.gov/
- **Best for:** Checking against U.S. government sanctions list (SDN and consolidated lists)
- **Input → Output:** Individual or entity name (fuzzy-matched), alias variations → SDN list matches, alternate names, addresses, dates of birth (when available), designation details
- **OpSec:** passive. Official government database; searches are not logged against user identity but accessing the government website may be monitored.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
