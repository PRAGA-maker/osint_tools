---
id: gobuster
name: Gobuster
description: Fast DNS and vhost brute-force enumeration
url: https://github.com/OJ/gobuster
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- subdomains
bestFor: Fast DNS and vhost brute-force enumeration
input: Domain, wordlist, and optional resolver/thread settings
output: Discovered subdomains, vhosts, or directories with response details
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: active
opsecNote: Sends direct DNS/HTTP probes and can generate noisy traffic patterns.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
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

# Gobuster

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://github.com/OJ/gobuster
- **Best for:** Fast DNS and vhost brute-force enumeration
- **Input → Output:** Domain, wordlist, and optional resolver/thread settings → Discovered subdomains, vhosts, or directories with response details
- **OpSec:** active. Sends direct DNS/HTTP probes and can generate noisy traffic patterns.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
