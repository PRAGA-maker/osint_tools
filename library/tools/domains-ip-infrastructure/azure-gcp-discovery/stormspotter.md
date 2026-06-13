---
id: stormspotter
name: Stormspotter
description: Visual analysis of Azure attack paths and privilege chains
url: https://github.com/Azure/Stormspotter
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- azure-gcp-discovery
bestFor: Visual analysis of Azure attack paths and privilege chains
input: Azure subscription/tenant metadata collected by collectors
output: Interactive graph of Azure identities, resources, and attack edges
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: active
opsecNote: Collection phase performs authenticated queries against Azure APIs.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: unverified
trustNote: ''
missingPersonsRelevance: low
coverage: []
auth: none
api: true
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

# Stormspotter

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://github.com/Azure/Stormspotter
- **Best for:** Visual analysis of Azure attack paths and privilege chains
- **Input → Output:** Azure subscription/tenant metadata collected by collectors → Interactive graph of Azure identities, resources, and attack edges
- **OpSec:** active. Collection phase performs authenticated queries against Azure APIs.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
