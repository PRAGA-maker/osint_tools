---
id: burp-suite-2
name: Burp Suite
description: Web application security testing, vulnerability discovery, traffic analysis
url: https://portswigger.net/burp/download.html
category: evidence-capture
path:
- evidence-capture
- web-browsing
bestFor: Web application security testing, vulnerability discovery, traffic analysis
input: Web application traffic
output: Security scan results, vulnerability reports, request/response logs
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
opsec: active
opsecNote: Active security testing tool; generates traffic and may trigger security alarms on target systems.
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

# Burp Suite

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://portswigger.net/burp/download.html
- **Best for:** Web application security testing, vulnerability discovery, traffic analysis
- **Input → Output:** Web application traffic → Security scan results, vulnerability reports, request/response logs
- **OpSec:** active. Active security testing tool; generates traffic and may trigger security alarms on target systems.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
