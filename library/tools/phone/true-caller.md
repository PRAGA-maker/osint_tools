---
id: true-caller
name: True Caller
description: Caller-ID enrichment and spam reputation checks
url: https://www.truecaller.com/
category: phone
path:
- phone
bestFor: Caller-ID enrichment and spam reputation checks
input: Phone number
output: Caller profile signals, spam labels, and identity hints
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
opsec: passive
opsecNote: Lookups are mediated by the platform; typical usage does not directly notify the target.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: high
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

# True Caller

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.truecaller.com/
- **Best for:** Caller-ID enrichment and spam reputation checks
- **Input → Output:** Phone number → Caller profile signals, spam labels, and identity hints
- **OpSec:** passive. Lookups are mediated by the platform; typical usage does not directly notify the target.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
