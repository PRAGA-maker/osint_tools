---
id: dns-dumpster
name: DNS Dumpster
description: Subdomain enumeration, DNS reconnaissance, infrastructure mapping
url: https://dnsdumpster.com/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- passivedns
bestFor: Subdomain enumeration, DNS reconnaissance, infrastructure mapping
input: Domain name
output: MX records, TXT records, Host records, subdomains, infrastructure map
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Passive DNS research without sending direct DNS requests or probing the target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: low
coverage: []
auth: none
api: false
localInstall: false
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

# DNS Dumpster

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://dnsdumpster.com/
- **Best for:** Subdomain enumeration, DNS reconnaissance, infrastructure mapping
- **Input → Output:** Domain name → MX records, TXT records, Host records, subdomains, infrastructure map
- **OpSec:** passive. Passive DNS research without sending direct DNS requests or probing the target.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
