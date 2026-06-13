---
id: exonerator
name: ExoneraTor
description: Verify Tor relay membership by date
url: https://exonerator.torproject.org/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- reputation
bestFor: Verify Tor relay membership by date
input: IP address and date
output: Tor exit/entry node status confirmation
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Passive historical Tor relay lookup from public archives.
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

# ExoneraTor

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://exonerator.torproject.org/
- **Best for:** Verify Tor relay membership by date
- **Input → Output:** IP address and date → Tor exit/entry node status confirmation
- **OpSec:** passive. Passive historical Tor relay lookup from public archives.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
