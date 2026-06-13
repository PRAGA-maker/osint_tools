---
id: fiddler
name: Fiddler
description: Network traffic analysis, web debugging, protocol inspection
url: https://www.telerik.com/download/fiddler
category: evidence-capture
path:
- evidence-capture
- web-browsing
bestFor: Network traffic analysis, web debugging, protocol inspection
input: HTTP/HTTPS traffic
output: Captured requests/responses, traffic logs, header analysis
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
opsec: active
opsecNote: Network-level traffic capture; may require target awareness and can trigger security alarms.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: cli
trust: unverified
trustNote: ''
missingPersonsRelevance: medium
coverage: []
auth: account
api: true
localInstall: true
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

# Fiddler

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.telerik.com/download/fiddler
- **Best for:** Network traffic analysis, web debugging, protocol inspection
- **Input → Output:** HTTP/HTTPS traffic → Captured requests/responses, traffic logs, header analysis
- **OpSec:** active. Network-level traffic capture; may require target awareness and can trigger security alarms.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
