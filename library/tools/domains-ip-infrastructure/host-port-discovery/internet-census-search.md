---
id: internet-census-search
name: Internet Census Search
description: Search open services and devices
url: https://www.exfiltrated.com/querystart.php
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- host-port-discovery
bestFor: Search open services and devices
input: Service type, IP range, port
output: List of exposed services and IPs
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Passive data search of known internet census.
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

# Internet Census Search

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.exfiltrated.com/querystart.php
- **Best for:** Search open services and devices
- **Input → Output:** Service type, IP range, port → List of exposed services and IPs
- **OpSec:** passive. Passive data search of known internet census.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
