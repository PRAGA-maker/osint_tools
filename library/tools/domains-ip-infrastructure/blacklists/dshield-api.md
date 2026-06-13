---
id: dshield-api
name: DShield API
description: Query IPs involved in attacks
url: https://isc.sans.edu/api/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- blacklists
bestFor: Query IPs involved in attacks
input: IP address
output: Attack reports, threat activity
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Passive threat intelligence from SANS monitored networks.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: low
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

# DShield API

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://isc.sans.edu/api/
- **Best for:** Query IPs involved in attacks
- **Input → Output:** IP address → Attack reports, threat activity
- **OpSec:** passive. Passive threat intelligence from SANS monitored networks.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
