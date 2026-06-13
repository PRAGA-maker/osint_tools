---
id: twitter-location-search
name: Twitter Location Search
description: Finding public tweets associated with specific coordinates and radius
url: https://twitter.com/search?q=geocode%3A36.1143855%2C-115.1727518%2C1km&src=typd
category: social-networks
path:
- social-networks
- twitter
- search
bestFor: Finding public tweets associated with specific coordinates and radius
input: Latitude/longitude plus radius in search query
output: Tweets matching the configured location filter
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Searches public indexed content; no outbound contact to targets beyond normal platform queries.
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

# Twitter Location Search

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://twitter.com/search?q=geocode%3A36.1143855%2C-115.1727518%2C1km&src=typd
- **Best for:** Finding public tweets associated with specific coordinates and radius
- **Input → Output:** Latitude/longitude plus radius in search query → Tweets matching the configured location filter
- **OpSec:** passive. Searches public indexed content; no outbound contact to targets beyond normal platform queries.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
