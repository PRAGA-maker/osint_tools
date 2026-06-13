---
id: browser-leaks
name: Browser Leaks
description: Deep browser fingerprint analysis, identifying all data leak vectors before OSINT operations
url: https://browserleaks.com/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
- anonymous-browsing
bestFor: Deep browser fingerprint analysis, identifying all data leak vectors before OSINT operations
input: No input required (automatic browser analysis)
output: Detailed reports on WebRTC, canvas, WebGL, fonts, plugins, and all other browser identifiers
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: active
opsecNote: Sends comprehensive fingerprint data to their servers; use to audit your anonymization setup but not during live operations.
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

# Browser Leaks

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://browserleaks.com/
- **Best for:** Deep browser fingerprint analysis, identifying all data leak vectors before OSINT operations
- **Input → Output:** No input required (automatic browser analysis) → Detailed reports on WebRTC, canvas, WebGL, fonts, plugins, and all other browser identifiers
- **OpSec:** active. Sends comprehensive fingerprint data to their servers; use to audit your anonymization setup but not during live operations.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
