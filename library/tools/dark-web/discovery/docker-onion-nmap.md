---
id: docker-onion-nmap
name: docker-onion-nmap
description: Containerized port enumeration of hidden services
url: https://github.com/milesrichardson/docker-onion-nmap
category: dark-web
path:
- dark-web
- discovery
bestFor: Containerized port enumeration of hidden services
input: .onion hosts
output: Network scan results and open-port findings
selectorsIn: []
selectorsOut: []
status: degraded
pricing: free
opsec: active
opsecNote: Port scanning is high-signal active probing and is likely visible to target operators.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: unverified
trustNote: ''
missingPersonsRelevance: medium
coverage: []
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: true
relatedTools: []
aliases: []
tags: []
source: arf-seed
lastVerified: ''
enrichment: stub
---

# docker-onion-nmap

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://github.com/milesrichardson/docker-onion-nmap
- **Best for:** Containerized port enumeration of hidden services
- **Input → Output:** .onion hosts → Network scan results and open-port findings
- **OpSec:** active. Port scanning is high-signal active probing and is likely visible to target operators.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
