---
id: theharvester
name: theHarvester
description: Email harvesting, subdomain enumeration, passive recon
url: https://github.com/laramies/theHarvester
category: email
path:
- email
- email-search
bestFor: Email harvesting, subdomain enumeration, passive recon
input: Domain name
output: Email addresses, subdomains, IPs, URLs
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Queries third-party search engines and APIs. Does not contact the target directly.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: unverified
trustNote: ''
missingPersonsRelevance: high
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

# theHarvester

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://github.com/laramies/theHarvester
- **Best for:** Email harvesting, subdomain enumeration, passive recon
- **Input → Output:** Domain name → Email addresses, subdomains, IPs, URLs
- **OpSec:** passive. Queries third-party search engines and APIs. Does not contact the target directly.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
