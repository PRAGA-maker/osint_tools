---
id: companies-house-2
name: Companies House
description: UK company registration details, directors, and filed accounts
url: https://beta.companieshouse.gov.uk/
category: public-records
path:
- public-records
- company-profiles
bestFor: UK company registration details, directors, and filed accounts
input: Company name, registration number, or officer name
output: Company profile, registered officers, filing history, and charges
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Official government registry; queries do not interact with the target company.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: medium
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

# Companies House

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://beta.companieshouse.gov.uk/
- **Best for:** UK company registration details, directors, and filed accounts
- **Input → Output:** Company name, registration number, or officer name → Company profile, registered officers, filing history, and charges
- **OpSec:** passive. Official government registry; queries do not interact with the target company.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
