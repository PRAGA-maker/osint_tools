---
id: subgraph-os
name: Subgraph OS
description: High-security threat model; adversary resistance; encrypted communications
url: https://subgraph.com/index.en.html
category: ai-analysis-automation
path:
- ai-analysis-automation
- virtual-machines
bestFor: High-security threat model; adversary resistance; encrypted communications
input: N/A (OS distribution)
output: Hardened Linux environment with Tor integration
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: active
opsecNote: Default Tor routing; kernel hardening (grsecurity, PaX); AppArmor profiles; Oz sandboxing
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

# Subgraph OS

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://subgraph.com/index.en.html
- **Best for:** High-security threat model; adversary resistance; encrypted communications
- **Input → Output:** N/A (OS distribution) → Hardened Linux environment with Tor integration
- **OpSec:** active. Default Tor routing; kernel hardening (grsecurity, PaX); AppArmor profiles; Oz sandboxing

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
