---
id: github-user
name: Github User
description: Enumerating a GitHub user's recent public activity and repository interactions
url: https://api.github.com/users/%3Cusername%3E/events/public
category: username
path:
- username
- specific-sites
bestFor: Enumerating a GitHub user's recent public activity and repository interactions
input: GitHub username (inserted into URL path)
output: JSON array of public events (pushes, PRs, issues, comments) with timestamps and repo details
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Unauthenticated API call; GitHub rate-limits by IP (60 req/hr) but does not notify the target user.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: high
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

# Github User

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://api.github.com/users/%3Cusername%3E/events/public
- **Best for:** Enumerating a GitHub user's recent public activity and repository interactions
- **Input → Output:** GitHub username (inserted into URL path) → JSON array of public events (pushes, PRs, issues, comments) with timestamps and repo details
- **OpSec:** passive. Unauthenticated API call; GitHub rate-limits by IP (60 req/hr) but does not notify the target user.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
