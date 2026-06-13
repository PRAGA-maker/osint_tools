---
id: viewdns-info
name: ViewDNS.info
description: DNS reconnaissance, reverse IP and reverse WHOIS lookups, historical DNS tracking
url: https://viewdns.info/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- whois-records
bestFor: DNS reconnaissance, reverse IP and reverse WHOIS lookups, historical DNS tracking
input: Domain name, IP address, registrant name/email, nameserver
output: DNS records, WHOIS information, reverse lookups, IP hosting, historical DNS changes
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Queries public DNS and WHOIS data; does not perform active probing of targets.
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

# ViewDNS.info

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://viewdns.info/
- **Best for:** DNS reconnaissance, reverse IP and reverse WHOIS lookups, historical DNS tracking
- **Input → Output:** Domain name, IP address, registrant name/email, nameserver → DNS records, WHOIS information, reverse lookups, IP hosting, historical DNS changes
- **OpSec:** passive. Queries public DNS and WHOIS data; does not perform active probing of targets.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
