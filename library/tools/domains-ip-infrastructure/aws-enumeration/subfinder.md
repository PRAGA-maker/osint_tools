---
id: subfinder
name: Subfinder
description: Passive subdomain enumeration for cloud asset inventorying
url: https://github.com/projectdiscovery/subfinder
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- aws-enumeration
bestFor: Passive subdomain enumeration for cloud asset inventorying
input: Domain name and optional API credentials for data sources
output: Resolved and unresolved subdomain candidates
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Uses third-party data sources by default and avoids active probing unless paired with other tools.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: cli
trust: unverified
trustNote: ''
missingPersonsRelevance: low
coverage: []
auth: account
api: true
localInstall: true
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

# Subfinder

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://github.com/projectdiscovery/subfinder
- **Best for:** Passive subdomain enumeration for cloud asset inventorying
- **Input → Output:** Domain name and optional API credentials for data sources → Resolved and unresolved subdomain candidates
- **OpSec:** passive. Uses third-party data sources by default and avoids active probing unless paired with other tools.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
