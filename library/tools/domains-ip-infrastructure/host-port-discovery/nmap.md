---
id: nmap
name: Nmap
description: Network reconnaissance and port scanning
url: https://nmap.org/download.html
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- host-port-discovery
bestFor: Network reconnaissance and port scanning
input: IP range or hostname
output: Open ports, OS type, service versions, MAC addresses
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: active
opsecNote: Active scanning tool; generates network traffic.
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

# Nmap

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://nmap.org/download.html
- **Best for:** Network reconnaissance and port scanning
- **Input → Output:** IP range or hostname → Open ports, OS type, service versions, MAC addresses
- **OpSec:** active. Active scanning tool; generates network traffic.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
