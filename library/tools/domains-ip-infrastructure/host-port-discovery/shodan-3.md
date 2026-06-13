---
id: shodan-3
name: Shodan
description: Find exposed IoT and network services
url: https://www.shodan.io/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- host-port-discovery
bestFor: Find exposed IoT and network services
input: IP, port, service type
output: Service banners, open ports, vulnerabilities, location
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
opsec: passive
opsecNote: Passive data collection; InternetDB API free for non-commercial use.
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
localInstall: false
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

# Shodan

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.shodan.io/
- **Best for:** Find exposed IoT and network services
- **Input → Output:** IP, port, service type → Service banners, open ports, vulnerabilities, location
- **OpSec:** passive. Passive data collection; InternetDB API free for non-commercial use.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
