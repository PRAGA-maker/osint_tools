---
id: critical-stack-intel
name: Critical Stack Intel
description: Network IDS threat intelligence
url: https://intel.criticalstack.com/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- domain-blacklists
bestFor: Network IDS threat intelligence
input: Bro/Zeek intel format
output: Intel.log entries, network alerts
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Requires registration; polled hourly from curated threat intelligence feeds
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
localInstall: true
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

# Critical Stack Intel

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://intel.criticalstack.com/
- **Best for:** Network IDS threat intelligence
- **Input → Output:** Bro/Zeek intel format → Intel.log entries, network alerts
- **OpSec:** passive. Requires registration; polled hourly from curated threat intelligence feeds

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
