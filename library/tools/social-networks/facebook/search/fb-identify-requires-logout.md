---
id: fb-identify-requires-logout
name: FB Identify (Requires Logout)
description: Account discovery checks through Facebook identify flow
url: https://www.facebook.com/login/identify
category: social-networks
path:
- social-networks
- facebook
- search
bestFor: Account discovery checks through Facebook identify flow
input: Email address, phone number, or profile identifier
output: Potential account matches and recovery prompts
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Requires interacting with Facebook recovery interfaces and may produce different results when authenticated.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: high
coverage: []
auth: none
api: false
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

# FB Identify (Requires Logout)

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.facebook.com/login/identify
- **Best for:** Account discovery checks through Facebook identify flow
- **Input → Output:** Email address, phone number, or profile identifier → Potential account matches and recovery prompts
- **OpSec:** passive. Requires interacting with Facebook recovery interfaces and may produce different results when authenticated.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
