---
id: mnemonic
name: Mnemonic
description: Passive DNS lookups, historical domain resolutions, DNS reconnaissance
url: https://passivedns.mnemonic.no/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- passivedns
bestFor: Passive DNS lookups, historical domain resolutions, DNS reconnaissance
input: Domain or IP address
output: DNS query history with timestamps, associated IPs, and historical resolutions
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Queries a passive database of DNS records; does not contact the target domain.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: low
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

# Mnemonic

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://passivedns.mnemonic.no/
- **Best for:** Passive DNS lookups, historical domain resolutions, DNS reconnaissance
- **Input → Output:** Domain or IP address → DNS query history with timestamps, associated IPs, and historical resolutions
- **OpSec:** passive. Queries a passive database of DNS records; does not contact the target domain.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
