---
id: dns-twist
name: DNS Twist
description: Typosquatting and phishing domain detection
url: https://github.com/elceef/dnstwist
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- typosquatting
bestFor: Typosquatting and phishing domain detection
input: Domain name
output: Domain permutation list, DNS records, HTTP similarity
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: active
opsecNote: Active DNS queries required; queries can be resource-intensive (300K+ queries for google.com)
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

# DNS Twist

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://github.com/elceef/dnstwist
- **Best for:** Typosquatting and phishing domain detection
- **Input → Output:** Domain name → Domain permutation list, DNS records, HTTP similarity
- **OpSec:** active. Active DNS queries required; queries can be resource-intensive (300K+ queries for google.com)

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
