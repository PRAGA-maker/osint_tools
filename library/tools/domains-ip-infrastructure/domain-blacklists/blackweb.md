---
id: blackweb
name: Blackweb
description: Squid proxy malware filtering
url: https://github.com/maravento/blackweb
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- domain-blacklists
bestFor: Squid proxy malware filtering
input: None (aggregated blocklist)
output: Squid-compatible blocklist format
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Aggregates existing public blacklist sources; requires DNS verification
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: low
coverage: []
auth: none
api: false
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

# Blackweb

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://github.com/maravento/blackweb
- **Best for:** Squid proxy malware filtering
- **Input → Output:** None (aggregated blocklist) → Squid-compatible blocklist format
- **OpSec:** passive. Aggregates existing public blacklist sources; requires DNS verification

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
