---
id: google
name: Google
description: General web OSINT, historical information via cache, broad searches with operators
url: https://www.google.com/?gws_rd=ssl
category: search-engines
path:
- search-engines
- general-search
bestFor: General web OSINT, historical information via cache, broad searches with operators
input: Keywords, search operators (site:, intitle:, inurl:, filetype:, cache:, etc.)
output: Ranked web pages, snippets, images, news, cached pages
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Passive reconnaissance technique; widely monitored by targets; Google tracks all searches if logged in; extensively documented for OSINT use
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

# Google

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.google.com/?gws_rd=ssl
- **Best for:** General web OSINT, historical information via cache, broad searches with operators
- **Input → Output:** Keywords, search operators (site:, intitle:, inurl:, filetype:, cache:, etc.) → Ranked web pages, snippets, images, news, cached pages
- **OpSec:** passive. Passive reconnaissance technique; widely monitored by targets; Google tracks all searches if logged in; extensively documented for OSINT use

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
