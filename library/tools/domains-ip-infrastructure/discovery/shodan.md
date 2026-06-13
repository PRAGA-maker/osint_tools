---
id: shodan
name: Shodan
description: Finding exposed services and infrastructure risk indicators
url: https://www.shodan.io/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- discovery
bestFor: Finding exposed services and infrastructure risk indicators
input: IP, domain, ASN, organization, or filter-based search query
output: Service banners, open ports, geolocation, vulnerabilities, and host metadata
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
opsec: passive
opsecNote: Uses Shodan indexed scan data; target systems are not probed from your local host.
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
- **Best for:** Finding exposed services and infrastructure risk indicators
- **Input → Output:** IP, domain, ASN, organization, or filter-based search query → Service banners, open ports, geolocation, vulnerabilities, and host metadata
- **OpSec:** passive. Uses Shodan indexed scan data; target systems are not probed from your local host.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
