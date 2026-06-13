---
id: pagodo-passive-google-dork
name: pagodo - Passive Google Dork
description: Automated passive Google dork enumeration from GHDB
url: https://github.com/opsdisk/pagodo
category: search-engines
path:
- search-engines
- search-tools
bestFor: Automated passive Google dork enumeration from GHDB
input: GHDB dork categories, target domain
output: Google search result URLs matching dork patterns
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Queries public Google search only; supports proxy configuration to reduce exposure. No direct target system contact.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: unverified
trustNote: ''
missingPersonsRelevance: medium
coverage: []
auth: none
api: false
localInstall: true
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

# pagodo - Passive Google Dork

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://github.com/opsdisk/pagodo
- **Best for:** Automated passive Google dork enumeration from GHDB
- **Input → Output:** GHDB dork categories, target domain → Google search result URLs matching dork patterns
- **OpSec:** passive. Queries public Google search only; supports proxy configuration to reduce exposure. No direct target system contact.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
