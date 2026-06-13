---
id: roadtools
name: ROADtools
description: Enumerating Azure AD objects and privilege relationships
url: https://github.com/dirkjanm/roadtools
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- azure-gcp-discovery
bestFor: Enumerating Azure AD objects and privilege relationships
input: Azure AD tenant context and authentication tokens/credentials
output: Users, groups, applications, roles, and privilege mappings
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: active
opsecNote: Interacts directly with Microsoft Graph and Azure AD endpoints.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
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

# ROADtools

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://github.com/dirkjanm/roadtools
- **Best for:** Enumerating Azure AD objects and privilege relationships
- **Input → Output:** Azure AD tenant context and authentication tokens/credentials → Users, groups, applications, roles, and privilege mappings
- **OpSec:** active. Interacts directly with Microsoft Graph and Azure AD endpoints.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
