---
id: grey-noise
name: Grey Noise
description: Distinguish malicious from benign internet activity
url: https://viz.greynoise.io/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- reputation
bestFor: Distinguish malicious from benign internet activity
input: IP address
output: Classification, scanner type, threat assessment
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
opsec: passive
opsecNote: Passive threat intelligence; free tier available.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: low
coverage: []
auth: account
api: true
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools: []
aliases: []
tags: []
source: arf-seed
lastVerified: ''
enrichment: stub
---

# Grey Noise

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://viz.greynoise.io/
- **Best for:** Distinguish malicious from benign internet activity
- **Input → Output:** IP address → Classification, scanner type, threat assessment
- **OpSec:** passive. Passive threat intelligence; free tier available.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
