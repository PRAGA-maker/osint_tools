---
id: ads-b-nl
name: ADS-B.NL
description: European and military aircraft movement monitoring
url: https://www.ads-b.nl/index.php?pageno=9999
category: transportation
path:
- transportation
- air-traffic-records
bestFor: European and military aircraft movement monitoring
input: Aircraft registration, military callsign, or track query
output: Flight traces, movement history, and aircraft classification context
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Aggregates publicly broadcast ADS-B data in a read-only interface.
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

# ADS-B.NL

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.ads-b.nl/index.php?pageno=9999
- **Best for:** European and military aircraft movement monitoring
- **Input → Output:** Aircraft registration, military callsign, or track query → Flight traces, movement history, and aircraft classification context
- **OpSec:** passive. Aggregates publicly broadcast ADS-B data in a read-only interface.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
