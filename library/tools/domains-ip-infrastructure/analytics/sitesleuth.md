---
id: sitesleuth
name: SiteSleuth
description: Tracking code intelligence and related domain discovery
url: https://www.sitesleuth.io/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- analytics
bestFor: Tracking code intelligence and related domain discovery
input: Domain, Google Analytics ID, AdSense ID, or Stripe key
output: List of associated domains and tracking codes
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Passive intelligence from indexed tracking identifiers; no direct queries to targets
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

# SiteSleuth

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.sitesleuth.io/
- **Best for:** Tracking code intelligence and related domain discovery
- **Input → Output:** Domain, Google Analytics ID, AdSense ID, or Stripe key → List of associated domains and tracking codes
- **OpSec:** passive. Passive intelligence from indexed tracking identifiers; no direct queries to targets

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
