---
id: hunting-new-registered-domains
name: Hunting-New-Registered-Domains
description: Phishing domain detection and brand threat monitoring
url: https://github.com/gfek/Hunting-New-Registered-Domains
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- tools
bestFor: Phishing domain detection and brand threat monitoring
input: Domain patterns or keywords
output: List of newly registered matching domains
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: WHOIS queries may create observable patterns; otherwise passive
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: unverified
trustNote: ''
missingPersonsRelevance: low
coverage: []
auth: none
api: true
localInstall: true
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

# Hunting-New-Registered-Domains

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://github.com/gfek/Hunting-New-Registered-Domains
- **Best for:** Phishing domain detection and brand threat monitoring
- **Input → Output:** Domain patterns or keywords → List of newly registered matching domains
- **OpSec:** passive. WHOIS queries may create observable patterns; otherwise passive

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
