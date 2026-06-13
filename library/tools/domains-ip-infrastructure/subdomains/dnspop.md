---
id: dnspop
name: dnspop
description: Command-line DNS recon and record analysis
url: https://github.com/bitquark/dnspop
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- subdomains
bestFor: Command-line DNS recon and record analysis
input: Domain and optional scan parameters
output: DNS records, discovered hosts, and recon findings
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: active
opsecNote: Performs direct DNS queries against resolvers and target-associated records.
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

# dnspop

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://github.com/bitquark/dnspop
- **Best for:** Command-line DNS recon and record analysis
- **Input → Output:** Domain and optional scan parameters → DNS records, discovered hosts, and recon findings
- **OpSec:** active. Performs direct DNS queries against resolvers and target-associated records.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
