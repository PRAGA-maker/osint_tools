---
id: linkedint-linkedin-recon-tool
name: LinkedInt - LinkedIn Recon Tool
description: LinkedIn employee enumeration
url: https://github.com/vysecurity/LinkedInt
category: social-networks
path:
- social-networks
- linkedin
bestFor: LinkedIn employee enumeration
input: Company names, LinkedIn URLs, and search targets
output: Employee profile lists and organization intelligence leads
selectorsIn: []
selectorsOut: []
status: degraded
pricing: free
opsec: active
opsecNote: Automated LinkedIn collection can violate platform policy and trigger detection.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: cli
trust: unverified
trustNote: ''
missingPersonsRelevance: high
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

# LinkedInt - LinkedIn Recon Tool

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://github.com/vysecurity/LinkedInt
- **Best for:** LinkedIn employee enumeration
- **Input → Output:** Company names, LinkedIn URLs, and search targets → Employee profile lists and organization intelligence leads
- **OpSec:** active. Automated LinkedIn collection can violate platform policy and trigger detection.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
