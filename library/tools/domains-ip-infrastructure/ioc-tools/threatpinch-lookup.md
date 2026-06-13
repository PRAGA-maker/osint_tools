---
id: threatpinch-lookup
name: ThreatPinch Lookup
description: Indicator enrichment
url: https://github.com/cloudtracer/ThreatPinchLookup
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- ioc-tools
bestFor: Indicator enrichment
input: IOC or domain/IP/hash
output: Enriched threat intelligence from multiple sources
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Passive lookup of public threat intel APIs
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: low
coverage: []
auth: none
api: true
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

# ThreatPinch Lookup

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://github.com/cloudtracer/ThreatPinchLookup
- **Best for:** Indicator enrichment
- **Input → Output:** IOC or domain/IP/hash → Enriched threat intelligence from multiple sources
- **OpSec:** passive. Passive lookup of public threat intel APIs

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
