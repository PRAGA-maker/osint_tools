---
id: vat-number-validation
name: VAT Number Validation
description: Validating EU VAT registration numbers and identifying registered businesses
url: https://ec.europa.eu/taxation_customs/vies/?locale=en
category: public-records
path:
- public-records
- additional-resources
bestFor: Validating EU VAT registration numbers and identifying registered businesses
input: EU VAT number (country code + number)
output: VAT registration validity, company name, and registered address
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Queries processed through the EU VIES system; no direct interaction with the target company.
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

# VAT Number Validation

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://ec.europa.eu/taxation_customs/vies/?locale=en
- **Best for:** Validating EU VAT registration numbers and identifying registered businesses
- **Input → Output:** EU VAT number (country code + number) → VAT registration validity, company name, and registered address
- **OpSec:** passive. Queries processed through the EU VIES system; no direct interaction with the target company.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
