---
id: amazon-usernames
name: Amazon Usernames
description: Finding Amazon public profiles, wishlists, and review activity by username
url: https://www.google.com/search?q=site:amazon.com+%3Cusername%3E
category: username
path:
- username
- specific-sites
bestFor: Finding Amazon public profiles, wishlists, and review activity by username
input: Username (inserted into Google search query)
output: Google search results linking to Amazon pages mentioning the username
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Query goes to Google, not Amazon directly. Google may log the search but the target is not alerted.
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

# Amazon Usernames

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.google.com/search?q=site:amazon.com+%3Cusername%3E
- **Best for:** Finding Amazon public profiles, wishlists, and review activity by username
- **Input → Output:** Username (inserted into Google search query) → Google search results linking to Amazon pages mentioning the username
- **OpSec:** passive. Query goes to Google, not Amazon directly. Google may log the search but the target is not alerted.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
