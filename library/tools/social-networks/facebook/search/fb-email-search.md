---
id: fb-email-search
name: FB Email Search
description: Quick Facebook account existence checks from an email identifier
url: https://www.facebook.com/public?query=email@gmail.com&nomc=0
category: social-networks
path:
- social-networks
- facebook
- search
bestFor: Quick Facebook account existence checks from an email identifier
input: Email address (replace the query value in the URL)
output: Facebook public search results that may include matching profile records
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Uses Facebook web search endpoints without authentication, but query terms are visible in browser/network logs.
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

# FB Email Search

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.facebook.com/public?query=email@gmail.com&nomc=0
- **Best for:** Quick Facebook account existence checks from an email identifier
- **Input → Output:** Email address (replace the query value in the URL) → Facebook public search results that may include matching profile records
- **OpSec:** passive. Uses Facebook web search endpoints without authentication, but query terms are visible in browser/network logs.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
