---
id: social-media-fingerprint
name: Social Media Fingerprint
description: Checking social media session exposure, verifying browser compartmentalization effectiveness
url: https://robinlinus.github.io/socialmedia-leak/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
- privacy-clean-up
bestFor: Checking social media session exposure, verifying browser compartmentalization effectiveness
input: No input required (automatic detection via browser)
output: List of social media platforms where active sessions are detected
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: active
opsecNote: Detects your active social media sessions locally in-browser; use to verify that OSINT browser profiles are properly isolated from personal accounts.
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

# Social Media Fingerprint

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://robinlinus.github.io/socialmedia-leak/
- **Best for:** Checking social media session exposure, verifying browser compartmentalization effectiveness
- **Input → Output:** No input required (automatic detection via browser) → List of social media platforms where active sessions are detected
- **OpSec:** active. Detects your active social media sessions locally in-browser; use to verify that OSINT browser profiles are properly isolated from personal accounts.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
