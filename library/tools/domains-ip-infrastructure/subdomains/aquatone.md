---
id: aquatone
name: Aquatone
description: Visual subdomain reconnaissance, HTTP service discovery, attack surface mapping
url: https://github.com/michenriksen/aquatone
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- subdomains
bestFor: Visual subdomain reconnaissance, HTTP service discovery, attack surface mapping
input: Domain name
output: Discovered subdomains, open ports, HTTP screenshots, consolidated reconnaissance report
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: active
opsecNote: Makes HTTP requests to discovered hosts to capture screenshots and fingerprint services; supports integration with passive enumeration tools.
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

# Aquatone

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://github.com/michenriksen/aquatone
- **Best for:** Visual subdomain reconnaissance, HTTP service discovery, attack surface mapping
- **Input → Output:** Domain name → Discovered subdomains, open ports, HTTP screenshots, consolidated reconnaissance report
- **OpSec:** active. Makes HTTP requests to discovered hosts to capture screenshots and fingerprint services; supports integration with passive enumeration tools.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
