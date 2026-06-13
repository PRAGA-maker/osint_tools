---
id: blocklist-de
name: Blocklist.de
description: Check IP blacklist status
url: https://www.blocklist.de/en/index.html
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- blacklists
bestFor: Check IP blacklist status
input: IP address
output: Blacklist status, attack types logged
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Passive lookup of community blocklist.
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

# Blocklist.de

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.blocklist.de/en/index.html
- **Best for:** Check IP blacklist status
- **Input → Output:** IP address → Blacklist status, attack types logged
- **OpSec:** passive. Passive lookup of community blocklist.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
