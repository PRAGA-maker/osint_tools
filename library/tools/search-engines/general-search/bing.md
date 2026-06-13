---
id: bing
name: Bing
description: Alternative to Google, regional results, academic content, supplementary searches
url: https://www.bing.com/
category: search-engines
path:
- search-engines
- general-search
bestFor: Alternative to Google, regional results, academic content, supplementary searches
input: Keywords, search operators (site:, intitle:, filetype:, inurl:, AND, NOT, etc.)
output: Ranked web pages, images, news, videos, answers
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Passive OSINT; Bing Search API is being retired by Microsoft on August 11, 2026; limited future API availability
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

# Bing

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.bing.com/
- **Best for:** Alternative to Google, regional results, academic content, supplementary searches
- **Input → Output:** Keywords, search operators (site:, intitle:, filetype:, inurl:, AND, NOT, etc.) → Ranked web pages, images, news, videos, answers
- **OpSec:** passive. Passive OSINT; Bing Search API is being retired by Microsoft on August 11, 2026; limited future API availability

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
