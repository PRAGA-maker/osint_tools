---
id: threads-dashboard
name: Threads Dashboard
description: Threads account analytics and engagement investigation
url: https://www.threadsdashboard.com/
category: social-networks
path:
- social-networks
- threads
bestFor: Threads account analytics and engagement investigation
input: Threads username or account URL
output: Audience demographics, engagement rates, posting frequency, optimal posting times, and historical data
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
opsec: passive
opsecNote: Retrieves data via Meta's official Threads API; no direct contact with the target account.
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
deprecated: false
relatedTools: []
aliases: []
tags: []
source: arf-seed
lastVerified: ''
enrichment: stub
---

# Threads Dashboard

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.threadsdashboard.com/
- **Best for:** Threads account analytics and engagement investigation
- **Input → Output:** Threads username or account URL → Audience demographics, engagement rates, posting frequency, optimal posting times, and historical data
- **OpSec:** passive. Retrieves data via Meta's official Threads API; no direct contact with the target account.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
