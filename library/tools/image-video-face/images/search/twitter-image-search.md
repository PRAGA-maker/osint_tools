---
id: twitter-image-search
name: Twitter Image Search
description: Finding image-containing tweets by keyword or operator
url: https://twitter.com/search?q=%3Csearchterm%3E&src=typd&vertical=default&f=images
category: image-video-face
path:
- image-video-face
- images
- search
bestFor: Finding image-containing tweets by keyword or operator
input: Edited URL query (keyword, account, and search operators)
output: Tweets and accounts with matching image/media posts
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Searches public timeline content; no direct engagement with targets.
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

# Twitter Image Search

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://twitter.com/search?q=%3Csearchterm%3E&src=typd&vertical=default&f=images
- **Best for:** Finding image-containing tweets by keyword or operator
- **Input → Output:** Edited URL query (keyword, account, and search operators) → Tweets and accounts with matching image/media posts
- **OpSec:** passive. Searches public timeline content; no direct engagement with targets.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
