---
id: crt-sh-certificate-search
name: crt.sh - Certificate Search
description: Certificate search, subdomain discovery via CT logs, detecting unauthorized certificates
url: https://crt.sh/?
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- certificate-search
bestFor: Certificate search, subdomain discovery via CT logs, detecting unauthorized certificates
input: Domain name (with or without wildcard)
output: List of certificates issued to the domain with Subject Alternative Names and issue/expiry dates
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Queries public Certificate Transparency logs; does not contact the target domain.
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

# crt.sh - Certificate Search

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://crt.sh/?
- **Best for:** Certificate search, subdomain discovery via CT logs, detecting unauthorized certificates
- **Input → Output:** Domain name (with or without wildcard) → List of certificates issued to the domain with Subject Alternative Names and issue/expiry dates
- **OpSec:** passive. Queries public Certificate Transparency logs; does not contact the target domain.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
