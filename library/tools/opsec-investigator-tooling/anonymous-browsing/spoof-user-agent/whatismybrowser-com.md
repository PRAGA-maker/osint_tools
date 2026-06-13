---
id: whatismybrowser-com
name: WhatIsMyBrowser.com
description: Verifying browser fingerprint and user-agent visibility during OSINT sessions
url: https://www.whatismybrowser.com/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
- anonymous-browsing
- spoof-user-agent
bestFor: Verifying browser fingerprint and user-agent visibility during OSINT sessions
input: No input required (detects current browser automatically)
output: Browser name, version, OS, plugins, and shareable detection link
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: active
opsecNote: Visiting this site sends your real browser data to their servers; use only to test anonymization setups.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: medium
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

# WhatIsMyBrowser.com

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.whatismybrowser.com/
- **Best for:** Verifying browser fingerprint and user-agent visibility during OSINT sessions
- **Input → Output:** No input required (detects current browser automatically) → Browser name, version, OS, plugins, and shareable detection link
- **OpSec:** active. Visiting this site sends your real browser data to their servers; use only to test anonymization setups.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
