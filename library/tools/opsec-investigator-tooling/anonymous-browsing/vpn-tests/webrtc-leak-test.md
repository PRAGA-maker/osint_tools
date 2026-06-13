---
id: webrtc-leak-test
name: WebRTC Leak Test
description: Detecting WebRTC IP leaks in browsers, verifying WebRTC disable effectiveness
url: https://www.perfect-privacy.com/webrtc-leaktest/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
- anonymous-browsing
- vpn-tests
bestFor: Detecting WebRTC IP leaks in browsers, verifying WebRTC disable effectiveness
input: No input required (automatic browser WebRTC detection)
output: Local IP, public IP via WebRTC, and VPN IP with leak assessment
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: active
opsecNote: Uses WebRTC in your browser to detect leaks; revealing your real IPs to the testing service is expected during this test.
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

# WebRTC Leak Test

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.perfect-privacy.com/webrtc-leaktest/
- **Best for:** Detecting WebRTC IP leaks in browsers, verifying WebRTC disable effectiveness
- **Input → Output:** No input required (automatic browser WebRTC detection) → Local IP, public IP via WebRTC, and VPN IP with leak assessment
- **OpSec:** active. Uses WebRTC in your browser to detect leaks; revealing your real IPs to the testing service is expected during this test.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
