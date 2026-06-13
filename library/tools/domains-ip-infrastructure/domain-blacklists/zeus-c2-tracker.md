---
id: zeus-c2-tracker
name: Zeus C2 Tracker
description: Zeus botnet C2 blocking
url: https://zeustracker.abuse.ch/blocklist.php?download=domainblocklist
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- domain-blacklists
bestFor: Zeus botnet C2 blocking
input: None (blocklist provider)
output: Domain/IP blocklist, Snort rules, Squid format
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Queries public Zeus tracker database; no active scanning
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: low
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

# Zeus C2 Tracker

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://zeustracker.abuse.ch/blocklist.php?download=domainblocklist
- **Best for:** Zeus botnet C2 blocking
- **Input → Output:** None (blocklist provider) → Domain/IP blocklist, Snort rules, Squid format
- **OpSec:** passive. Queries public Zeus tracker database; no active scanning

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
