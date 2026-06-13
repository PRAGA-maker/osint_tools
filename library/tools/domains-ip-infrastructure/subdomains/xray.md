---
id: xray
name: XRay
description: Automated subdomain discovery with banner grabbing, open port enumeration, Shodan integration
url: https://github.com/evilsocket/xray
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- subdomains
bestFor: Automated subdomain discovery with banner grabbing, open port enumeration, Shodan integration
input: Domain name, subdomain wordlist, Shodan API key (optional), ViewDNS API key (optional)
output: Enumerated subdomains, open ports, banner information, historical data, web-based results UI
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: active
opsecNote: Performs DNS brute force for subdomain enumeration and makes banner grabbing connections to discovered services.
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

# XRay

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://github.com/evilsocket/xray
- **Best for:** Automated subdomain discovery with banner grabbing, open port enumeration, Shodan integration
- **Input → Output:** Domain name, subdomain wordlist, Shodan API key (optional), ViewDNS API key (optional) → Enumerated subdomains, open ports, banner information, historical data, web-based results UI
- **OpSec:** active. Performs DNS brute force for subdomain enumeration and makes banner grabbing connections to discovered services.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
