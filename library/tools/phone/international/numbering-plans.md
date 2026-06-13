---
id: numbering-plans
name: Numbering Plans
description: Telephony standards and numbering-plan validation
url: https://www.numberingplans.com/?page=analysis&sub=phonenr
category: phone
path:
- phone
- international
bestFor: Telephony standards and numbering-plan validation
input: Country code, number range, or prefix
output: Numbering-plan structure, carrier/routing metadata, and dialing references
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Reference lookup against published numbering data; no interaction with the target number.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: high
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

# Numbering Plans

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.numberingplans.com/?page=analysis&sub=phonenr
- **Best for:** Telephony standards and numbering-plan validation
- **Input → Output:** Country code, number range, or prefix → Numbering-plan structure, carrier/routing metadata, and dialing references
- **OpSec:** passive. Reference lookup against published numbering data; no interaction with the target number.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
