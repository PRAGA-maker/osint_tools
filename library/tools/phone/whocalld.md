---
id: whocalld
name: WhoCalld
description: Historical reference only (defunct per project guidance)
url: https://whocalld.com/
category: phone
path:
- phone
bestFor: Historical reference only (defunct per project guidance)
input: Phone number
output: Previously provided caller identity and spam context
selectorsIn: []
selectorsOut: []
status: down
pricing: freemium
opsec: unknown
opsecNote: Marked defunct per CEO guidance; reliability and operational behavior are not trusted.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: high
coverage: []
auth: account
api: true
localInstall: false
registration: true
invitationOnly: false
deprecated: true
relatedTools: []
aliases: []
tags: []
source: arf-seed
lastVerified: ''
enrichment: stub
---

# WhoCalld

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://whocalld.com/
- **Best for:** Historical reference only (defunct per project guidance)
- **Input → Output:** Phone number → Previously provided caller identity and spam context
- **OpSec:** unknown. Marked defunct per CEO guidance; reliability and operational behavior are not trusted.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
