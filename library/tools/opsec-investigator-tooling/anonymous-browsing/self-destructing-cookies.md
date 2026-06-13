---
id: self-destructing-cookies
name: Self-Destructing Cookies
description: Automatic cookie cleanup to prevent cross-session tracking
url: https://addons.mozilla.org/en-US/firefox/addon/self-destructing-cookies/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
- anonymous-browsing
bestFor: Automatic cookie cleanup to prevent cross-session tracking
input: Firefox extension installation
output: Automatic cookie deletion on tab close with per-site whitelist support
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Reduces cookie-based tracking; modern Firefox’s built-in cookie management may provide equivalent protection.
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

# Self-Destructing Cookies

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://addons.mozilla.org/en-US/firefox/addon/self-destructing-cookies/
- **Best for:** Automatic cookie cleanup to prevent cross-session tracking
- **Input → Output:** Firefox extension installation → Automatic cookie deletion on tab close with per-site whitelist support
- **OpSec:** passive. Reduces cookie-based tracking; modern Firefox’s built-in cookie management may provide equivalent protection.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
