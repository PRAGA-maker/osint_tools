---
id: dnsrecon
name: dnsrecon
description: Detailed DNS reconnaissance and validation
url: https://github.com/darkoperator/dnsrecon
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- saas-footprinting
bestFor: Detailed DNS reconnaissance and validation
input: Domain names, name servers, and optional DNS wordlists
output: DNS records, discovered hosts, and transfer/bruteforce findings
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: active
opsecNote: Performs direct DNS queries and active enumeration techniques against target infrastructure.
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

# dnsrecon

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://github.com/darkoperator/dnsrecon
- **Best for:** Detailed DNS reconnaissance and validation
- **Input → Output:** Domain names, name servers, and optional DNS wordlists → DNS records, discovered hosts, and transfer/bruteforce findings
- **OpSec:** active. Performs direct DNS queries and active enumeration techniques against target infrastructure.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
