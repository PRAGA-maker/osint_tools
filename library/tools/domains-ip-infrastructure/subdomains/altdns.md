---
id: altdns
name: AltDNS
description: Discovering likely subdomain variants through permutations
url: https://github.com/infosec-au/altdns
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- subdomains
bestFor: Discovering likely subdomain variants through permutations
input: Known subdomains, wordlist, and target domain
output: Resolved alternative subdomains and permutation results
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: active
opsecNote: Performs direct DNS resolution on generated permutations, creating active query footprints.
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

# AltDNS

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://github.com/infosec-au/altdns
- **Best for:** Discovering likely subdomain variants through permutations
- **Input → Output:** Known subdomains, wordlist, and target domain → Resolved alternative subdomains and permutation results
- **OpSec:** active. Performs direct DNS resolution on generated permutations, creating active query footprints.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
