---
id: seclists-dns-subdomains
name: SecLists DNS Subdomains
description: Supplying high-quality DNS wordlists for enumeration tools
url: https://github.com/danielmiessler/SecLists/tree/master/Discovery/DNS
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- subdomains
bestFor: Supplying high-quality DNS wordlists for enumeration tools
input: Domain and chosen wordlist file used in external tooling
output: Wordlist candidates for subdomain brute-force and permutation attacks
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Repository itself is passive; OPSEC impact depends on how the lists are used.
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

# SecLists DNS Subdomains

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://github.com/danielmiessler/SecLists/tree/master/Discovery/DNS
- **Best for:** Supplying high-quality DNS wordlists for enumeration tools
- **Input → Output:** Domain and chosen wordlist file used in external tooling → Wordlist candidates for subdomain brute-force and permutation attacks
- **OpSec:** passive. Repository itself is passive; OPSEC impact depends on how the lists are used.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
