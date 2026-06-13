---
id: zoomeye-ai
name: ZoomEye.ai
description: Internet device discovery, service enumeration, vulnerability mapping, attack surface assessment
url: https://www.zoomeye.org/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- discovery
bestFor: Internet device discovery, service enumeration, vulnerability mapping, attack surface assessment
input: Domain, IP, port, service, or natural language query
output: Device list, port data, banner info, vulnerability details, geographic distribution
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
opsec: passive
opsecNote: Queries ZoomEye's pre-scanned internet data; does not probe targets during search.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: low
coverage: []
auth: account
api: true
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools: []
aliases: []
tags: []
source: arf-seed
lastVerified: ''
enrichment: stub
---

# ZoomEye.ai

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.zoomeye.org/
- **Best for:** Internet device discovery, service enumeration, vulnerability mapping, attack surface assessment
- **Input → Output:** Domain, IP, port, service, or natural language query → Device list, port data, banner info, vulnerability details, geographic distribution
- **OpSec:** passive. Queries ZoomEye's pre-scanned internet data; does not probe targets during search.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
