---
id: microburst
name: MicroBurst
description: Azure subscription and service-level exposure testing
url: https://github.com/NetSPI/MicroBurst
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- azure-gcp-discovery
bestFor: Azure subscription and service-level exposure testing
input: Azure tenant/subscription context and optional credentials
output: Recon data and security findings for Azure resources
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: active
opsecNote: Runs active checks against Azure control/data plane endpoints.
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

# MicroBurst

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://github.com/NetSPI/MicroBurst
- **Best for:** Azure subscription and service-level exposure testing
- **Input → Output:** Azure tenant/subscription context and optional credentials → Recon data and security findings for Azure resources
- **OpSec:** active. Runs active checks against Azure control/data plane endpoints.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
