---
id: netr-online
name: NETR Online
description: County property records aggregation
url: https://publicrecords.netronline.com/
category: public-records
path:
- public-records
- financial-tax-resources
bestFor: County property records aggregation
input: Address, county name, owner name
output: Property deeds, tax records, assessments
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Links to county systems; coverage varies
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: medium
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

# NETR Online

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://publicrecords.netronline.com/
- **Best for:** County property records aggregation
- **Input → Output:** Address, county name, owner name → Property deeds, tax records, assessments
- **OpSec:** passive. Links to county systems; coverage varies

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
