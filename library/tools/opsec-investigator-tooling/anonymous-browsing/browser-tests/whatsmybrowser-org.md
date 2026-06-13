---
id: whatsmybrowser-org
name: WhatsMyBrowser.org
description: Verifying browser fingerprint, checking what browser version appears to websites
url: https://www.whatsmybrowser.org/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
- anonymous-browsing
- browser-tests
bestFor: Verifying browser fingerprint, checking what browser version appears to websites
input: No input required (detects current browser)
output: Browser name, version, OS, screen resolution, and shareable detection URL
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: active
opsecNote: Collects and stores browser fingerprint data; use only to verify anonymization effectiveness, not during live operations.
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

# WhatsMyBrowser.org

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.whatsmybrowser.org/
- **Best for:** Verifying browser fingerprint, checking what browser version appears to websites
- **Input → Output:** No input required (detects current browser) → Browser name, version, OS, screen resolution, and shareable detection URL
- **OpSec:** active. Collects and stores browser fingerprint data; use only to verify anonymization effectiveness, not during live operations.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
