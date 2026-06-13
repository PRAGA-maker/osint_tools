---
id: urlscan-io
name: urlscan.io
description: Investigating suspicious URLs with scan snapshots and indicators
url: https://urlscan.io/search/#*
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- discovery
bestFor: Investigating suspicious URLs with scan snapshots and indicators
input: URL or domain
output: Scan reports including redirects, requests, domains, IPs, and screenshots
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
opsec: passive
opsecNote: Analysis runs on urlscan infrastructure; target contact is performed from their scanners.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: low
coverage: []
auth: account
api: true
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

# urlscan.io

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://urlscan.io/search/#*
- **Best for:** Investigating suspicious URLs with scan snapshots and indicators
- **Input → Output:** URL or domain → Scan reports including redirects, requests, domains, IPs, and screenshots
- **OpSec:** passive. Analysis runs on urlscan infrastructure; target contact is performed from their scanners.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
