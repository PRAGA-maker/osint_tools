---
id: alienvault-open-threat-exchange
name: AlienVault Open Threat Exchange
description: Community threat intelligence sharing
url: https://otx.alienvault.com/browse/pulses/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- reputation
bestFor: Community threat intelligence sharing
input: Domain, IP, URL, file hash
output: Threat pulses, reputation data, indicators
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Community-sourced intelligence; free API access with registration
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: low
coverage: []
auth: account
api: true
localInstall: false
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

# AlienVault Open Threat Exchange

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://otx.alienvault.com/browse/pulses/
- **Best for:** Community threat intelligence sharing
- **Input → Output:** Domain, IP, URL, file hash → Threat pulses, reputation data, indicators
- **OpSec:** passive. Community-sourced intelligence; free API access with registration

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
