---
id: gdns
name: gdns
description: Quick DNS enumeration via Google DNS services
url: https://github.com/hrbrmstr/gdns
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- subdomains
bestFor: Quick DNS enumeration via Google DNS services
input: Domain and query options
output: Resolved DNS records and related lookup results
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: active
opsecNote: Issues active DNS lookup requests that may be observable at resolver level.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: unverified
trustNote: ''
missingPersonsRelevance: low
coverage: []
auth: none
api: false
localInstall: true
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

# gdns

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://github.com/hrbrmstr/gdns
- **Best for:** Quick DNS enumeration via Google DNS services
- **Input → Output:** Domain and query options → Resolved DNS records and related lookup results
- **OpSec:** active. Issues active DNS lookup requests that may be observable at resolver level.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
