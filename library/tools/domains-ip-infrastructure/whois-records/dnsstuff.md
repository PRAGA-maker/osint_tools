---
id: dnsstuff
name: DNSstuff
description: Quick DNS and WHOIS lookups, network diagnostics
url: https://www.dnsstuff.com/freetools
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- whois-records
bestFor: Quick DNS and WHOIS lookups, network diagnostics
input: Domain name, IP address
output: DNS records, WHOIS data, DNS propagation checks, nameserver information
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Queries public DNS and WHOIS servers; does not probe target infrastructure.
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

# DNSstuff

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.dnsstuff.com/freetools
- **Best for:** Quick DNS and WHOIS lookups, network diagnostics
- **Input → Output:** Domain name, IP address → DNS records, WHOIS data, DNS propagation checks, nameserver information
- **OpSec:** passive. Queries public DNS and WHOIS servers; does not probe target infrastructure.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
