---
id: censys
name: Censys
description: Certificate discovery, host enumeration, exposure monitoring
url: https://censys.io/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- certificate-search
bestFor: Certificate discovery, host enumeration, exposure monitoring
input: Domain, IP, certificate fingerprint, search query
output: Host details, open ports, TLS certificates, service banners
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
opsec: passive
opsecNote: Queries pre-scanned data. Does not probe the target directly.
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

# Censys

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://censys.io/
- **Best for:** Certificate discovery, host enumeration, exposure monitoring
- **Input → Output:** Domain, IP, certificate fingerprint, search query → Host details, open ports, TLS certificates, service banners
- **OpSec:** passive. Queries pre-scanned data. Does not probe the target directly.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
