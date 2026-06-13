---
id: deteque
name: Deteque
description: Domain/IP threat intelligence, malware tracking, botnet detection, abuse data
url: https://www.deteque.com/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- passivedns
bestFor: Domain/IP threat intelligence, malware tracking, botnet detection, abuse data
input: Domain, IP, URL, file hash, or AS number
output: Threat classification, malware associations, botnet data, historical records (up to 12 months)
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
opsec: passive
opsecNote: Queries threat intelligence database; does not contact or probe the target.
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

# Deteque

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.deteque.com/
- **Best for:** Domain/IP threat intelligence, malware tracking, botnet detection, abuse data
- **Input → Output:** Domain, IP, URL, file hash, or AS number → Threat classification, malware associations, botnet data, historical records (up to 12 months)
- **OpSec:** passive. Queries threat intelligence database; does not contact or probe the target.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
