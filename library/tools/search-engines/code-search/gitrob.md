---
id: gitrob
name: Gitrob
description: GitHub organization reconnaissance for exposed secrets and sensitive files in commit history
url: https://github.com/michenriksen/gitrob
category: search-engines
path:
- search-engines
- code-search
bestFor: GitHub organization reconnaissance for exposed secrets and sensitive files in commit history
input: GitHub username or organization name
output: List of potentially sensitive files and paths found across repositories
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: active
opsecNote: Directly queries the GitHub API and clones repositories; API activity is logged and may alert security monitoring.
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

# Gitrob

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://github.com/michenriksen/gitrob
- **Best for:** GitHub organization reconnaissance for exposed secrets and sensitive files in commit history
- **Input → Output:** GitHub username or organization name → List of potentially sensitive files and paths found across repositories
- **OpSec:** active. Directly queries the GitHub API and clones repositories; API activity is logged and may alert security monitoring.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
