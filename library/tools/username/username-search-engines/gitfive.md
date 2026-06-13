---
id: gitfive
name: GitFive
description: Deep investigation of GitHub user profiles and email-to-account mapping
url: https://github.com/mxrch/GitFive
category: username
path:
- username
- username-search-engines
bestFor: Deep investigation of GitHub user profiles and email-to-account mapping
input: GitHub username or email address
output: Profile history, linked emails, SSH keys, repository analysis, JSON export
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: active
opsecNote: Queries GitHub API directly; developer recommends using a secondary GitHub account.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: cli
trust: unverified
trustNote: ''
missingPersonsRelevance: high
coverage: []
auth: account
api: false
localInstall: true
registration: true
invitationOnly: false
deprecated: false
relatedTools: []
aliases: []
tags: []
source: arf-seed
lastVerified: ''
enrichment: stub
---

# GitFive

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://github.com/mxrch/GitFive
- **Best for:** Deep investigation of GitHub user profiles and email-to-account mapping
- **Input → Output:** GitHub username or email address → Profile history, linked emails, SSH keys, repository analysis, JSON export
- **OpSec:** active. Queries GitHub API directly; developer recommends using a secondary GitHub account.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
