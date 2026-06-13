---
id: burp-suite
name: Burp Suite
description: Web application penetration testing
url: https://portswigger.net/burp
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- tools
bestFor: Web application penetration testing
input: Web applications and URLs
output: Security findings, intercepted traffic, and vulnerability reports
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
opsec: active
opsecNote: Full active scanning; generates extensive server logs and may trigger WAF/IDS alerts
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: unverified
trustNote: ''
missingPersonsRelevance: low
coverage: []
auth: none
api: true
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

# Burp Suite

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://portswigger.net/burp
- **Best for:** Web application penetration testing
- **Input → Output:** Web applications and URLs → Security findings, intercepted traffic, and vulnerability reports
- **OpSec:** active. Full active scanning; generates extensive server logs and may trigger WAF/IDS alerts

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
