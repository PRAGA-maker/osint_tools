---
id: certgraph
name: certgraph
description: Certificate mapping, domain relationship discovery, hostname enumeration via SSL certificates
url: https://github.com/lanrat/certgraph
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- certificate-search
bestFor: Certificate mapping, domain relationship discovery, hostname enumeration via SSL certificates
input: Hostname or domain name
output: Directed graph showing domain nodes and certificate alternative name connections between domains
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Default HTTPS driver can make connections to hosts; alternative drivers query CT logs passively. Use CT drivers for stealth.
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

# certgraph

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://github.com/lanrat/certgraph
- **Best for:** Certificate mapping, domain relationship discovery, hostname enumeration via SSL certificates
- **Input → Output:** Hostname or domain name → Directed graph showing domain nodes and certificate alternative name connections between domains
- **OpSec:** passive. Default HTTPS driver can make connections to hosts; alternative drivers query CT logs passively. Use CT drivers for stealth.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
