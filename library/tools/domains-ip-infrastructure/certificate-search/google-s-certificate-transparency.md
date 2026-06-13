---
id: google-s-certificate-transparency
name: Google's Certificate Transparency
description: Certificate discovery, unauthorized cert detection, domain monitoring
url: https://www.certificate-transparency.org/known-logs
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- certificate-search
bestFor: Certificate discovery, unauthorized cert detection, domain monitoring
input: Domain name or certificate fingerprint
output: List of CT logs and certificates issued for the specified domain
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Queries public certificate logs without contacting the target domain.
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

# Google's Certificate Transparency

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.certificate-transparency.org/known-logs
- **Best for:** Certificate discovery, unauthorized cert detection, domain monitoring
- **Input → Output:** Domain name or certificate fingerprint → List of CT logs and certificates issued for the specified domain
- **OpSec:** passive. Queries public certificate logs without contacting the target domain.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
