---
id: bluecoat-webpulse
name: BlueCoat WebPulse
description: URL categorization, website reputation filtering, malicious link detection
url: https://sitereview.bluecoat.com/sitereview.jsp
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- reputation
bestFor: URL categorization, website reputation filtering, malicious link detection
input: Website URL
output: URL category, reputation rating, threat indicators, web content classification
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Queries Blue Coat's cloud-based URL reputation database without directly probing targets.
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

# BlueCoat WebPulse

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://sitereview.bluecoat.com/sitereview.jsp
- **Best for:** URL categorization, website reputation filtering, malicious link detection
- **Input → Output:** Website URL → URL category, reputation rating, threat indicators, web content classification
- **OpSec:** passive. Queries Blue Coat's cloud-based URL reputation database without directly probing targets.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
