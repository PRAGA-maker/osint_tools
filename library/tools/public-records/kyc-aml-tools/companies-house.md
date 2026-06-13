---
id: companies-house
name: Companies House
description: Looking up UK company details, officers, and filing history
url: https://find-and-update.company-information.service.gov.uk/
category: public-records
path:
- public-records
- kyc-aml-tools
bestFor: Looking up UK company details, officers, and filing history
input: Company name, company number, or officer name
output: Company profiles, registered addresses, officer appointments, filing history, and document images
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Public UK government service; searches are passive lookups against an open register.
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

# Companies House

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://find-and-update.company-information.service.gov.uk/
- **Best for:** Looking up UK company details, officers, and filing history
- **Input → Output:** Company name, company number, or officer name → Company profiles, registered addresses, officer appointments, filing history, and document images
- **OpSec:** passive. Public UK government service; searches are passive lookups against an open register.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
