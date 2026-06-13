---
id: follow-that-page
name: Follow That Page
description: Tracking updates on specific web pages by keyword
url: https://www.followthatpage.com/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- change-detection
bestFor: Tracking updates on specific web pages by keyword
input: Target page URL and optional keyword filters
output: Email alerts showing detected page changes
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
opsec: passive
opsecNote: Monitoring requests are performed by Follow That Page infrastructure rather than directly from the investigator's workstation.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: low
coverage: []
auth: account
api: false
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

# Follow That Page

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.followthatpage.com/
- **Best for:** Tracking updates on specific web pages by keyword
- **Input → Output:** Target page URL and optional keyword filters → Email alerts showing detected page changes
- **OpSec:** passive. Monitoring requests are performed by Follow That Page infrastructure rather than directly from the investigator's workstation.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
