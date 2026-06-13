---
id: share-secret-feedback
name: Share Secret Feedback
description: Looking up Secreto profiles by username to find anonymous feedback pages
url: https://secreto.site/en/%3Cuser_id%3E
category: social-networks
path:
- social-networks
- other-social-networks
bestFor: Looking up Secreto profiles by username to find anonymous feedback pages
input: Secreto username or user ID
output: Public profile page and shareable feedback link for the target user
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Viewing a public Secreto profile page is a standard web request; does not notify the profile owner.
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

# Share Secret Feedback

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://secreto.site/en/%3Cuser_id%3E
- **Best for:** Looking up Secreto profiles by username to find anonymous feedback pages
- **Input → Output:** Secreto username or user ID → Public profile page and shareable feedback link for the target user
- **OpSec:** passive. Viewing a public Secreto profile page is a standard web request; does not notify the profile owner.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
