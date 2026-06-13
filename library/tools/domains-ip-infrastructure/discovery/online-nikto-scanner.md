---
id: online-nikto-scanner
name: Online Nikto scanner
description: Web server vulnerability scanning
url: https://nikto.online/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- discovery
bestFor: Web server vulnerability scanning
input: URLs
output: Vulnerability and misconfiguration reports
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: active
opsecNote: Generates noisy scan traffic visible in target server logs; likely to trigger WAF/IDS alerts
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: low
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

# Online Nikto scanner

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://nikto.online/
- **Best for:** Web server vulnerability scanning
- **Input → Output:** URLs → Vulnerability and misconfiguration reports
- **OpSec:** active. Generates noisy scan traffic visible in target server logs; likely to trigger WAF/IDS alerts

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
