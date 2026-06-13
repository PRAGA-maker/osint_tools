---
id: goblob
name: goblob
description: Enumerating Azure blob container exposure quickly
url: https://github.com/Macmod/goblob
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- s3-blob-storage
bestFor: Enumerating Azure blob container exposure quickly
input: Target naming patterns and optional custom wordlists
output: Discovered blob storage endpoints and access results
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: active
opsecNote: Sends direct requests to Azure storage endpoints during enumeration.
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

# goblob

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://github.com/Macmod/goblob
- **Best for:** Enumerating Azure blob container exposure quickly
- **Input → Output:** Target naming patterns and optional custom wordlists → Discovered blob storage endpoints and access results
- **OpSec:** active. Sends direct requests to Azure storage endpoints during enumeration.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
