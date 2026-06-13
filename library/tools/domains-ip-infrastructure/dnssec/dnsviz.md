---
id: dnsviz
name: DNSViz
description: Visual DNSSEC validation and DNS misconfiguration analysis
url: https://dnsviz.net/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- dnssec
bestFor: Visual DNSSEC validation and DNS misconfiguration analysis
input: Domain name
output: DNS resolution graphs, DNSSEC status, and validation diagnostics
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Analysis runs against public DNS infrastructure without direct interaction with domain owners.
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

# DNSViz

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://dnsviz.net/
- **Best for:** Visual DNSSEC validation and DNS misconfiguration analysis
- **Input → Output:** Domain name → DNS resolution graphs, DNSSEC status, and validation diagnostics
- **OpSec:** passive. Analysis runs against public DNS infrastructure without direct interaction with domain owners.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
