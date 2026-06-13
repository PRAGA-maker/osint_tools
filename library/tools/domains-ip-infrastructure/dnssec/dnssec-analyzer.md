---
id: dnssec-analyzer
name: DNSSEC Analyzer
description: DNSSEC chain-of-trust validation
url: https://dnssec-analyzer.verisignlabs.com/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- dnssec
bestFor: DNSSEC chain-of-trust validation
input: Domain names
output: DNSSEC validation status and chain details
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: No identification risk; passive DNS lookup
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

# DNSSEC Analyzer

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://dnssec-analyzer.verisignlabs.com/
- **Best for:** DNSSEC chain-of-trust validation
- **Input → Output:** Domain names → DNSSEC validation status and chain details
- **OpSec:** passive. No identification risk; passive DNS lookup

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
