---
id: infoflow-public-people-search-in-chilean
name: InfoFlow Public People Search In Chilean
description: Chilean public records and identity verification
url: https://infoflow.cloud/
category: people-search
path:
- people-search
- general-people-search
bestFor: Chilean public records and identity verification
input: Name, RUN (Chilean ID number), or vehicle plate
output: Personal identification data, vehicle registration, company records
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
opsec: active
opsecNote: Requires registration with Chilean RUT; queries may be logged.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: high
coverage: []
auth: account
api: false
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

# InfoFlow Public People Search In Chilean

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://infoflow.cloud/
- **Best for:** Chilean public records and identity verification
- **Input → Output:** Name, RUN (Chilean ID number), or vehicle plate → Personal identification data, vehicle registration, company records
- **OpSec:** active. Requires registration with Chilean RUT; queries may be logged.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
