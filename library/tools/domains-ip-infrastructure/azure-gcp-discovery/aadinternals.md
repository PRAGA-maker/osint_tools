---
id: aadinternals
name: AADInternals
description: Deep Azure AD reconnaissance and security assessment
url: https://github.com/Gerenios/AADInternals
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- azure-gcp-discovery
bestFor: Deep Azure AD reconnaissance and security assessment
input: Tenant identifiers, domain names, and account context
output: Tenant/user intelligence, configuration findings, and attack-path indicators
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: active
opsecNote: Queries Microsoft identity services directly and may generate tenant-visible activity.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: unverified
trustNote: ''
missingPersonsRelevance: low
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

# AADInternals

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://github.com/Gerenios/AADInternals
- **Best for:** Deep Azure AD reconnaissance and security assessment
- **Input → Output:** Tenant identifiers, domain names, and account context → Tenant/user intelligence, configuration findings, and attack-path indicators
- **OpSec:** active. Queries Microsoft identity services directly and may generate tenant-visible activity.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
