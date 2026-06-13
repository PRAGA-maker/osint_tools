---
id: netlas-io
name: Netlas.io
description: Internet reconnaissance, DNS and WHOIS lookups, attack surface discovery, vulnerability research
url: https://app.netlas.io/whois_domains/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- whois-records
bestFor: Internet reconnaissance, DNS and WHOIS lookups, attack surface discovery, vulnerability research
input: Domain name, IP address, ASN, DNS records
output: DNS records, WHOIS data, open ports, SSL certificates, service information, historical data
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
opsec: passive
opsecNote: Queries cached internet scanning data; free tier available with 50 daily requests.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: low
coverage: []
auth: none
api: true
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

# Netlas.io

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://app.netlas.io/whois_domains/
- **Best for:** Internet reconnaissance, DNS and WHOIS lookups, attack surface discovery, vulnerability research
- **Input → Output:** Domain name, IP address, ASN, DNS records → DNS records, WHOIS data, open ports, SSL certificates, service information, historical data
- **OpSec:** passive. Queries cached internet scanning data; free tier available with 50 daily requests.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
