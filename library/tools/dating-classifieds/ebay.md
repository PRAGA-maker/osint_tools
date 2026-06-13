---
id: ebay
name: eBay
description: Seller profile research, username cross-referencing, item provenance tracking, fraud investigation
url: https://www.ebay.com/
category: dating-classifieds
path:
- dating-classifieds
bestFor: Seller profile research, username cross-referencing, item provenance tracking, fraud investigation
input: Username, item keywords, seller ID
output: Seller feedback history, active and completed listings, buyer/seller ratings, and account details
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Browsing seller profiles and listings is passive; account creation needed for full history access in some regions.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: high
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

# eBay

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.ebay.com/
- **Best for:** Seller profile research, username cross-referencing, item provenance tracking, fraud investigation
- **Input → Output:** Username, item keywords, seller ID → Seller feedback history, active and completed listings, buyer/seller ratings, and account details
- **OpSec:** passive. Browsing seller profiles and listings is passive; account creation needed for full history access in some regions.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
