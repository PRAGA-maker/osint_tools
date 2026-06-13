---
id: firehol-ip-lists
name: FireHOL IP Lists
description: Block malicious/spam IP sources
url: https://iplists.firehol.org/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- blacklists
bestFor: Block malicious/spam IP sources
input: IP address or list download
output: Blacklist membership status
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Passive lookup of public IP reputation lists.
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

# FireHOL IP Lists

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://iplists.firehol.org/
- **Best for:** Block malicious/spam IP sources
- **Input → Output:** IP address or list download → Blacklist membership status
- **OpSec:** passive. Passive lookup of public IP reputation lists.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
