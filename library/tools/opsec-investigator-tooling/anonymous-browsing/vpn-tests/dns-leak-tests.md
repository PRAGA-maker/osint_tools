---
id: dns-leak-tests
name: DNS Leak Tests
description: Secondary DNS leak verification, cross-checking VPN DNS configuration
url: https://dnsleak.com/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
- anonymous-browsing
- vpn-tests
bestFor: Secondary DNS leak verification, cross-checking VPN DNS configuration
input: No input required (automatic detection)
output: DNS server IPs, provider names, and country locations for all resolving servers
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: active
opsecNote: Sends DNS probe queries that can be logged; use as part of pre-operation anonymization verification.
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

# DNS Leak Tests

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://dnsleak.com/
- **Best for:** Secondary DNS leak verification, cross-checking VPN DNS configuration
- **Input → Output:** No input required (automatic detection) → DNS server IPs, provider names, and country locations for all resolving servers
- **OpSec:** active. Sends DNS probe queries that can be logged; use as part of pre-operation anonymization verification.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
