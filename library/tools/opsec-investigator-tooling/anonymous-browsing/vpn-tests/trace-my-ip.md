---
id: trace-my-ip
name: Trace My IP
description: Verifying visible IP and geolocation before OSINT operations
url: https://www.tracemyip.org/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
- anonymous-browsing
- vpn-tests
bestFor: Verifying visible IP and geolocation before OSINT operations
input: No input required (detects current IP automatically)
output: IP address, ISP, country, region, city, coordinates, and connection type
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: active
opsecNote: Logs your IP on visit; use only for verifying anonymization setup before conducting actual OSINT work.
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

# Trace My IP

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.tracemyip.org/
- **Best for:** Verifying visible IP and geolocation before OSINT operations
- **Input → Output:** No input required (detects current IP automatically) → IP address, ISP, country, region, city, coordinates, and connection type
- **OpSec:** active. Logs your IP on visit; use only for verifying anonymization setup before conducting actual OSINT work.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
