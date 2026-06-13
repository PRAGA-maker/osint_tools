---
id: tinder-usernames
name: Tinder Usernames
description: Confirming existence of a Tinder profile and viewing public profile details
url: https://www.gotinder.com/@%3Cusername%3E
category: username
path:
- username
- specific-sites
bestFor: Confirming existence of a Tinder profile and viewing public profile details
input: Tinder username (appended to URL after @)
output: Public profile page with name, photo, and basic info if the user has web sharing enabled
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Simple HTTP GET to a public page; target is not notified of profile views via the web URL.
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

# Tinder Usernames

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.gotinder.com/@%3Cusername%3E
- **Best for:** Confirming existence of a Tinder profile and viewing public profile details
- **Input → Output:** Tinder username (appended to URL after @) → Public profile page with name, photo, and basic info if the user has web sharing enabled
- **OpSec:** passive. Simple HTTP GET to a public page; target is not notified of profile views via the web URL.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
