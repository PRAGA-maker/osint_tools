---
id: ipv6-leak-tests
name: IPv6 Leak Tests
description: Detecting IPv6 leaks through IPv4-only VPNs, dual-stack network verification
url: https://ipv6leak.com/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
- anonymous-browsing
- vpn-tests
bestFor: Detecting IPv6 leaks through IPv4-only VPNs, dual-stack network verification
input: No input required (automatic IPv6 detection)
output: IPv6 address if leaking, confirmation of leak status, and remediation guidance
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: active
opsecNote: May expose your real IPv6 address to the testing service; use before OSINT operations on dual-stack networks.
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

# IPv6 Leak Tests

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://ipv6leak.com/
- **Best for:** Detecting IPv6 leaks through IPv4-only VPNs, dual-stack network verification
- **Input → Output:** No input required (automatic IPv6 detection) → IPv6 address if leaking, confirmation of leak status, and remediation guidance
- **OpSec:** active. May expose your real IPv6 address to the testing service; use before OSINT operations on dual-stack networks.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
