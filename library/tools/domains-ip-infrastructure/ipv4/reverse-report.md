---
id: reverse-report
name: Reverse.report
description: Reverse IP and domain lookups
url: https://reverse.report/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- ipv4
bestFor: Reverse IP and domain lookups
input: IP address or domain
output: Associated domains, subdomains, history
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
opsec: passive
opsecNote: Passive lookup of DNS and WHOIS data.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: low
coverage: []
auth: account
api: false
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

# Reverse.report

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://reverse.report/
- **Best for:** Reverse IP and domain lookups
- **Input → Output:** IP address or domain → Associated domains, subdomains, history
- **OpSec:** passive. Passive lookup of DNS and WHOIS data.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
