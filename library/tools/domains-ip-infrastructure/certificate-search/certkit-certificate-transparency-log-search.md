---
id: certkit-certificate-transparency-log-search
name: CertKit - Certificate Transparency Log Search
description: CT certificate search, subdomain enumeration, certificate misuse detection
url: https://www.certkit.io/tools/ct-logs/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- certificate-search
bestFor: CT certificate search, subdomain enumeration, certificate misuse detection
input: Domain name
output: List of certificates with issuance dates, expiry dates, and Subject Alternative Names
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Queries public Certificate Transparency logs; does not contact the target.
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

# CertKit - Certificate Transparency Log Search

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.certkit.io/tools/ct-logs/
- **Best for:** CT certificate search, subdomain enumeration, certificate misuse detection
- **Input → Output:** Domain name → List of certificates with issuance dates, expiry dates, and Subject Alternative Names
- **OpSec:** passive. Queries public Certificate Transparency logs; does not contact the target.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
