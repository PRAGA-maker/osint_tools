---
id: url-void
name: URL Void
description: Website reputation checking, malware/phishing detection, threat analysis
url: https://www.urlvoid.com/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- reputation
bestFor: Website reputation checking, malware/phishing detection, threat analysis
input: Website URL
output: Safety report from 30+ blocklists, IP details, domain age, server location, threat indicators
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Queries blocklist and reputation services; does not directly visit or probe the target.
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

# URL Void

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.urlvoid.com/
- **Best for:** Website reputation checking, malware/phishing detection, threat analysis
- **Input → Output:** Website URL → Safety report from 30+ blocklists, IP details, domain age, server location, threat indicators
- **OpSec:** passive. Queries blocklist and reputation services; does not directly visit or probe the target.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
