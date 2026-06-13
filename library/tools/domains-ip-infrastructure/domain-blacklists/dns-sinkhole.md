---
id: dns-sinkhole
name: DNS Sinkhole
description: DNS-based malware blocking
url: https://malc0de.com/bl/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- domain-blacklists
bestFor: DNS-based malware blocking
input: DNS zone file
output: Malware domain sinkhole list
selectorsIn: []
selectorsOut: []
status: degraded
pricing: free
opsec: passive
opsecNote: Public malware database; Cloudflare CAPTCHA protection added
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

# DNS Sinkhole

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://malc0de.com/bl/
- **Best for:** DNS-based malware blocking
- **Input → Output:** DNS zone file → Malware domain sinkhole list
- **OpSec:** passive. Public malware database; Cloudflare CAPTCHA protection added

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
