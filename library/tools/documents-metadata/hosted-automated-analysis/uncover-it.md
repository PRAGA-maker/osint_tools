---
id: uncover-it
name: Uncover It
description: Fast static malware configuration extraction
url: https://www.uncoverit.org/
category: documents-metadata
path:
- documents-metadata
- hosted-automated-analysis
bestFor: Fast static malware configuration extraction
input: Malware samples, executable files
output: Extracted configurations, C2 servers, encryption keys, behavioral indicators
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Static analysis only; no code execution; quick analysis without external dependencies
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

# Uncover It

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.uncoverit.org/
- **Best for:** Fast static malware configuration extraction
- **Input → Output:** Malware samples, executable files → Extracted configurations, C2 servers, encryption keys, behavioral indicators
- **OpSec:** passive. Static analysis only; no code execution; quick analysis without external dependencies

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
