---
id: domain-dossier
name: Domain Dossier
description: Quick domain and IP reconnaissance with DNS and WHOIS data
url: https://centralops.net/co/DomainDossier.aspx
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- whois-records
bestFor: Quick domain and IP reconnaissance with DNS and WHOIS data
input: Domain name or IP address
output: WHOIS records, DNS records, IP information, registration details
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Queries public WHOIS and DNS records; does not contact the target domain directly.
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

# Domain Dossier

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://centralops.net/co/DomainDossier.aspx
- **Best for:** Quick domain and IP reconnaissance with DNS and WHOIS data
- **Input → Output:** Domain name or IP address → WHOIS records, DNS records, IP information, registration details
- **OpSec:** passive. Queries public WHOIS and DNS records; does not contact the target domain directly.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
