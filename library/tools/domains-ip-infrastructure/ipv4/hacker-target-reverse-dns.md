---
id: hacker-target-reverse-dns
name: Hacker Target - Reverse DNS
description: Reverse DNS lookup of IP addresses
url: https://hackertarget.com/reverse-dns-lookup/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- ipv4
bestFor: Reverse DNS lookup of IP addresses
input: IP address or range
output: Associated domains and PTR records
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
opsec: passive
opsecNote: Passive DNS lookup; includes free API tier.
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

# Hacker Target - Reverse DNS

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://hackertarget.com/reverse-dns-lookup/
- **Best for:** Reverse DNS lookup of IP addresses
- **Input → Output:** IP address or range → Associated domains and PTR records
- **OpSec:** passive. Passive DNS lookup; includes free API tier.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
