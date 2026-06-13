---
id: gitleaks
name: GitLeaks
description: Scanning git repositories for hardcoded secrets, API keys, and leaked credentials
url: https://github.com/gitleaks/gitleaks
category: search-engines
path:
- search-engines
- code-search
bestFor: Scanning git repositories for hardcoded secrets, API keys, and leaked credentials
input: Git repository path, remote URL, or file system path
output: Report of detected secrets with file location, matched rule, commit hash, and line context
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: active
opsecNote: Remote scans require cloning the target repository; clone activity may be logged by the hosting platform.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
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

# GitLeaks

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://github.com/gitleaks/gitleaks
- **Best for:** Scanning git repositories for hardcoded secrets, API keys, and leaked credentials
- **Input → Output:** Git repository path, remote URL, or file system path → Report of detected secrets with file location, matched rule, commit hash, and line context
- **OpSec:** active. Remote scans require cloning the target repository; clone activity may be logged by the hosting platform.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
