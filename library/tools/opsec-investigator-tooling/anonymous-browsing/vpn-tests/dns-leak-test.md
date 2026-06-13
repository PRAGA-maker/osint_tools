---
id: dns-leak-test
name: DNS leak test
description: Verifying DNS query routing through VPN, detecting ISP DNS exposure
url: https://www.dnsleaktest.com/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
- anonymous-browsing
- vpn-tests
bestFor: Verifying DNS query routing through VPN, detecting ISP DNS exposure
input: No input required (runs standard and extended DNS leak tests)
output: List of DNS servers handling your queries with ISP and location details
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: active
opsecNote: Test queries reveal which DNS servers handle your lookups; reveals real DNS servers to the testing service.
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

# DNS leak test

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.dnsleaktest.com/
- **Best for:** Verifying DNS query routing through VPN, detecting ISP DNS exposure
- **Input → Output:** No input required (runs standard and extended DNS leak tests) → List of DNS servers handling your queries with ISP and location details
- **OpSec:** active. Test queries reveal which DNS servers handle your lookups; reveals real DNS servers to the testing service.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
