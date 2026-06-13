---
id: urlcrazy
name: URLCrazy
description: Typosquatting domain discovery
url: https://www.morningstarsecurity.com/research/urlcrazy
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- typosquatting
bestFor: Typosquatting domain discovery
input: Domain name
output: Domain variant list, registration status
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: active
opsecNote: Generates 2000+ variants requiring DNS queries for availability checking
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: unverified
trustNote: ''
missingPersonsRelevance: low
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

# URLCrazy

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.morningstarsecurity.com/research/urlcrazy
- **Best for:** Typosquatting domain discovery
- **Input → Output:** Domain name → Domain variant list, registration status
- **OpSec:** active. Generates 2000+ variants requiring DNS queries for availability checking

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
