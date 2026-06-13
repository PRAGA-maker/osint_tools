---
id: dilisense
name: dilisense
description: Commercial AML/KYC sanctions screening and PEP checks
url: https://dilisense.com/en
category: public-records
path:
- public-records
- sanctions-screening
bestFor: Commercial AML/KYC sanctions screening and PEP checks
input: Name, date of birth, citizenship, or other identifying information
output: Match results with entity details, list sources, and confidence scores
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
opsec: passive
opsecNote: Queries sent to dilisense servers; registration required so searches are tied to an account.
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

# dilisense

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://dilisense.com/en
- **Best for:** Commercial AML/KYC sanctions screening and PEP checks
- **Input → Output:** Name, date of birth, citizenship, or other identifying information → Match results with entity details, list sources, and confidence scores
- **OpSec:** passive. Queries sent to dilisense servers; registration required so searches are tied to an account.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
