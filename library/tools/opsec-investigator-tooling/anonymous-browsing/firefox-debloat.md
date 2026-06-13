---
id: firefox-debloat
name: Firefox-debloat
description: Hardening Firefox for OSINT operations, reducing browser telemetry and tracking
url: https://github.com/amq/firefox-debloat
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
- anonymous-browsing
bestFor: Hardening Firefox for OSINT operations, reducing browser telemetry and tracking
input: Firefox configuration file (user.js or policies.json)
output: Hardened Firefox instance with reduced fingerprinting and telemetry
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Local configuration changes only; no data transmitted. Reduces but does not eliminate browser fingerprinting.
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

# Firefox-debloat

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://github.com/amq/firefox-debloat
- **Best for:** Hardening Firefox for OSINT operations, reducing browser telemetry and tracking
- **Input → Output:** Firefox configuration file (user.js or policies.json) → Hardened Firefox instance with reduced fingerprinting and telemetry
- **OpSec:** passive. Local configuration changes only; no data transmitted. Reduces but does not eliminate browser fingerprinting.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
