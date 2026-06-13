---
id: crunchbase
name: Crunchbase
description: Startup funding research, investor mapping, and executive tracking
url: https://www.crunchbase.com/#/home/index
category: public-records
path:
- public-records
- company-profiles
bestFor: Startup funding research, investor mapping, and executive tracking
input: Company name, person name, or investor name
output: Funding history, investors, acquisitions, team profiles, and news
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
opsec: passive
opsecNote: Queries processed through Crunchbase servers; aggregates from public and submitted data.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: medium
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

# Crunchbase

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.crunchbase.com/#/home/index
- **Best for:** Startup funding research, investor mapping, and executive tracking
- **Input → Output:** Company name, person name, or investor name → Funding history, investors, acquisitions, team profiles, and news
- **OpSec:** passive. Queries processed through Crunchbase servers; aggregates from public and submitted data.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
