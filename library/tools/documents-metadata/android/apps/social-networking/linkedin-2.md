---
id: linkedin-2
name: LinkedIn
description: Professional background verification, corporate reconnaissance, employment history research
url: https://www.linkedin.com/
category: documents-metadata
path:
- documents-metadata
- android
- apps
- social-networking
bestFor: Professional background verification, corporate reconnaissance, employment history research
input: Usernames, email domains, company names
output: Professional profiles, employment history, connections, company structure
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
opsec: active
opsecNote: LinkedIn actively blocks scraping tools and monitors for bulk data collection
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: cli
trust: unverified
trustNote: ''
missingPersonsRelevance: medium
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

# LinkedIn

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.linkedin.com/
- **Best for:** Professional background verification, corporate reconnaissance, employment history research
- **Input → Output:** Usernames, email domains, company names → Professional profiles, employment history, connections, company structure
- **OpSec:** active. LinkedIn actively blocks scraping tools and monitors for bulk data collection

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
