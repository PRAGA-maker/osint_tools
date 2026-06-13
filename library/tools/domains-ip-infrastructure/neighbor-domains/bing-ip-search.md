---
id: bing-ip-search
name: Bing IP Search
description: Find domains on IP using Bing index
url: https://www.bing.com/search?q=ip%3A8.8.8.8
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- neighbor-domains
bestFor: Find domains on IP using Bing index
input: IP address
output: Domains indexed by Bing on that IP
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Passive search using Bing's public index.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: low
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

# Bing IP Search

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.bing.com/search?q=ip%3A8.8.8.8
- **Best for:** Find domains on IP using Bing index
- **Input → Output:** IP address → Domains indexed by Bing on that IP
- **OpSec:** passive. Passive search using Bing's public index.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
