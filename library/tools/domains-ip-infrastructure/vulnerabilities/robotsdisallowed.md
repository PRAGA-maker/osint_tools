---
id: robotsdisallowed
name: RobotsDisallowed
description: robots.txt enumeration and directory discovery
url: https://github.com/danielmiessler/RobotsDisallowed
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- vulnerabilities
bestFor: robots.txt enumeration and directory discovery
input: Used as wordlist input for directory brute-forcing
output: Directory path wordlist
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Passive wordlist only; no requests made to target during list use
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

# RobotsDisallowed

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://github.com/danielmiessler/RobotsDisallowed
- **Best for:** robots.txt enumeration and directory discovery
- **Input → Output:** Used as wordlist input for directory brute-forcing → Directory path wordlist
- **OpSec:** passive. Passive wordlist only; no requests made to target during list use

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
