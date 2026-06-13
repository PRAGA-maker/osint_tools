---
id: ip-dns-leak-detection
name: IP / DNS Leak Detection
description: Verifying VPN effectiveness, detecting IP and DNS leaks before OSINT operations
url: https://ipleak.net/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
- anonymous-browsing
- vpn-tests
bestFor: Verifying VPN effectiveness, detecting IP and DNS leaks before OSINT operations
input: No input required (automatically tests current connection)
output: Detected IP, DNS servers, WebRTC leaks, and geolocation data
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: active
opsecNote: Connecting to this service reveals your current IP and DNS to their servers; use only to test anonymization setup before operations.
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

# IP / DNS Leak Detection

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://ipleak.net/
- **Best for:** Verifying VPN effectiveness, detecting IP and DNS leaks before OSINT operations
- **Input → Output:** No input required (automatically tests current connection) → Detected IP, DNS servers, WebRTC leaks, and geolocation data
- **OpSec:** active. Connecting to this service reveals your current IP and DNS to their servers; use only to test anonymization setup before operations.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
