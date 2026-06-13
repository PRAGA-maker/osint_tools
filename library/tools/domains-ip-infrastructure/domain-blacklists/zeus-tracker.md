---
id: zeus-tracker
name: ZeuS Tracker
description: Zeus botnet tracking and blocking
url: https://zeustracker.abuse.ch/blocklist.php
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- domain-blacklists
bestFor: Zeus botnet tracking and blocking
input: None (blocklist provider)
output: Domain blocklist, IP blocklist, Snort rules, Squid format
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Public tracker; passive monitoring of Zeus C2 activity
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

# ZeuS Tracker

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://zeustracker.abuse.ch/blocklist.php
- **Best for:** Zeus botnet tracking and blocking
- **Input → Output:** None (blocklist provider) → Domain blocklist, IP blocklist, Snort rules, Squid format
- **OpSec:** passive. Public tracker; passive monitoring of Zeus C2 activity

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
