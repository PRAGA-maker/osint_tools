---
id: inspy
name: InSpy
description: Employee and email pattern discovery
url: https://github.com/jobroche/InSpy
category: social-networks
path:
- social-networks
- linkedin
bestFor: Employee and email pattern discovery
input: Company name and domain context
output: Employee candidates with associated role and email pattern hints
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: active
opsecNote: Enumeration and enrichment workflows can expose investigator infrastructure.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: cli
trust: unverified
trustNote: ''
missingPersonsRelevance: high
coverage: []
auth: account
api: true
localInstall: true
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

# InSpy

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://github.com/jobroche/InSpy
- **Best for:** Employee and email pattern discovery
- **Input → Output:** Company name and domain context → Employee candidates with associated role and email pattern hints
- **OpSec:** active. Enumeration and enrichment workflows can expose investigator infrastructure.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
