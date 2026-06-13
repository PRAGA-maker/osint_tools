---
id: us-patent-office-search
name: US Patent Office Search
description: US patent search
url: https://www.uspto.gov/patents/search
category: public-records
path:
- public-records
- patent-records
bestFor: US patent search
input: Patent number, inventor name, keyword
output: Patent documents, claims, assignee info
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Official USPTO database
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

# US Patent Office Search

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.uspto.gov/patents/search
- **Best for:** US patent search
- **Input → Output:** Patent number, inventor name, keyword → Patent documents, claims, assignee info
- **OpSec:** passive. Official USPTO database

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
