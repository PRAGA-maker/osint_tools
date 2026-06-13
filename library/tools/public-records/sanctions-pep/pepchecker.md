---
id: pepchecker
name: PepChecker
description: Screening individuals against PEP lists and international sanctions databases
url: https://pepchecker.com
category: public-records
path:
- public-records
- sanctions-pep
bestFor: Screening individuals against PEP lists and international sanctions databases
input: Person name
output: PEP match results, sanctions list matches, risk indicators, and political exposure details
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
opsec: passive
opsecNote: Web-based queries; registration required for workspace features. Subjects are not notified.
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

# PepChecker

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://pepchecker.com
- **Best for:** Screening individuals against PEP lists and international sanctions databases
- **Input → Output:** Person name → PEP match results, sanctions list matches, risk indicators, and political exposure details
- **OpSec:** passive. Web-based queries; registration required for workspace features. Subjects are not notified.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
