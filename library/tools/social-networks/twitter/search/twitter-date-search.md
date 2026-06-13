---
id: twitter-date-search
name: Twitter Date Search
description: Timeline reconstruction and historical tweet collection
url: https://twitter.com/search?q=SearchTerm%20since:2016-03-01%20until:2016-03-02
category: social-networks
path:
- social-networks
- twitter
- search
bestFor: Timeline reconstruction and historical tweet collection
input: Keywords plus `since:` and `until:` date operators
output: Tweets posted within the requested date range
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Relies on platform search indexing and public content availability.
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

# Twitter Date Search

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://twitter.com/search?q=SearchTerm%20since:2016-03-01%20until:2016-03-02
- **Best for:** Timeline reconstruction and historical tweet collection
- **Input → Output:** Keywords plus `since:` and `until:` date operators → Tweets posted within the requested date range
- **OpSec:** passive. Relies on platform search indexing and public content availability.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
