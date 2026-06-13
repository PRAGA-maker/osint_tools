---
id: locabrowser-com
name: LocaBrowser.com
description: Testing browser geolocation exposure, verifying location permission settings
url: https://www.locabrowser.com/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
- anonymous-browsing
bestFor: Testing browser geolocation exposure, verifying location permission settings
input: No input required (requests browser geolocation permission)
output: Latitude, longitude, and accuracy of browser-reported geolocation
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: active
opsecNote: Requests and logs your browser’s geolocation; verify location masking is working before conducting location-sensitive OSINT.
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

# LocaBrowser.com

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.locabrowser.com/
- **Best for:** Testing browser geolocation exposure, verifying location permission settings
- **Input → Output:** No input required (requests browser geolocation permission) → Latitude, longitude, and accuracy of browser-reported geolocation
- **OpSec:** active. Requests and logs your browser’s geolocation; verify location masking is working before conducting location-sensitive OSINT.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
