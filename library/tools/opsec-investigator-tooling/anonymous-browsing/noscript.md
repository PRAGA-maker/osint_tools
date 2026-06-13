---
id: noscript
name: NoScript
description: Browser hardening, preventing JavaScript-based fingerprinting and tracking during OSINT
url: https://noscript.net/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
- anonymous-browsing
bestFor: Browser hardening, preventing JavaScript-based fingerprinting and tracking during OSINT
input: Browser extension installation
output: Selective script blocking with per-site whitelist control
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Reduces active fingerprinting surface significantly; some OSINT tools require JavaScript and may need temporary whitelisting.
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

# NoScript

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://noscript.net/
- **Best for:** Browser hardening, preventing JavaScript-based fingerprinting and tracking during OSINT
- **Input → Output:** Browser extension installation → Selective script blocking with per-site whitelist control
- **OpSec:** passive. Reduces active fingerprinting surface significantly; some OSINT tools require JavaScript and may need temporary whitelisting.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
