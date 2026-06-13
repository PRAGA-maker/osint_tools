---
id: recondog
name: ReconDog
description: Multi-function passive reconnaissance with modular capabilities
url: https://github.com/s0md3v/ReconDog
category: ai-analysis-automation
path:
- ai-analysis-automation
- osint-automation
bestFor: Multi-function passive reconnaissance with modular capabilities
input: Domain names, IP addresses
output: Subdomain lists, CMS identification, technology stacks, honeypot detection results
selectorsIn: []
selectorsOut: []
status: degraded
pricing: free
opsec: passive
opsecNote: Queries Censys and Shodan; traffic appears as API lookups rather than direct reconnaissance
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: cli
trust: unverified
trustNote: ''
missingPersonsRelevance: low
coverage: []
auth: account
api: false
localInstall: true
registration: true
invitationOnly: false
deprecated: true
relatedTools: []
aliases: []
tags: []
source: arf-seed
lastVerified: ''
enrichment: stub
---

# ReconDog

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://github.com/s0md3v/ReconDog
- **Best for:** Multi-function passive reconnaissance with modular capabilities
- **Input → Output:** Domain names, IP addresses → Subdomain lists, CMS identification, technology stacks, honeypot detection results
- **OpSec:** passive. Queries Censys and Shodan; traffic appears as API lookups rather than direct reconnaissance

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
