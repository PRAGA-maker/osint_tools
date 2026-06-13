---
id: ip2proxy
name: IP2Proxy
description: Checking if your VPN/proxy IP is flagged, verifying anonymization infrastructure quality
url: https://www.ip2proxy.com/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
- anonymous-browsing
- proxy-tests
bestFor: Checking if your VPN/proxy IP is flagged, verifying anonymization infrastructure quality
input: IP address
output: Proxy type classification (VPN/TOR/hosting/residential), ISP, and country
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
opsec: passive
opsecNote: Passive IP lookup; useful for checking if your exit node IPs are flagged in commercial proxy databases before conducting operations.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: medium
coverage: []
auth: none
api: true
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

# IP2Proxy

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.ip2proxy.com/
- **Best for:** Checking if your VPN/proxy IP is flagged, verifying anonymization infrastructure quality
- **Input → Output:** IP address → Proxy type classification (VPN/TOR/hosting/residential), ISP, and country
- **OpSec:** passive. Passive IP lookup; useful for checking if your exit node IPs are flagged in commercial proxy databases before conducting operations.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
