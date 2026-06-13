---
id: github-dorks
name: Github-Dorks
description: Finding exposed credentials and sensitive files on GitHub via advanced search dorks
url: https://github.com/techgaun/github-dorks
category: search-engines
path:
- search-engines
- code-search
bestFor: Finding exposed credentials and sensitive files on GitHub via advanced search dorks
input: Target username, organization, or domain
output: GitHub search results matching dork patterns for sensitive data exposure
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: active
opsecNote: Queries the GitHub search API; activity is logged by GitHub and may trigger alerts for repository owners.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: unverified
trustNote: ''
missingPersonsRelevance: medium
coverage: []
auth: none
api: false
localInstall: true
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

# Github-Dorks

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://github.com/techgaun/github-dorks
- **Best for:** Finding exposed credentials and sensitive files on GitHub via advanced search dorks
- **Input → Output:** Target username, organization, or domain → GitHub search results matching dork patterns for sensitive data exposure
- **OpSec:** active. Queries the GitHub search API; activity is logged by GitHub and may trigger alerts for repository owners.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
