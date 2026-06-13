---
id: datasploit
name: DataSploit
description: Multi-target reconnaissance (domain/email/username/phone aggregation)
url: https://github.com/datasploit/datasploit/
category: ai-analysis-automation
path:
- ai-analysis-automation
- osint-automation
bestFor: Multi-target reconnaissance (domain/email/username/phone aggregation)
input: Domain, email address, username, phone number, Bitcoin addresses
output: HTML, JSON, and text reports aggregating findings
selectorsIn: []
selectorsOut: []
status: down
pricing: free
opsec: active
opsecNote: Performs active reconnaissance; relies on external API availability
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
deprecated: true
relatedTools: []
aliases: []
tags: []
source: arf-seed
lastVerified: ''
enrichment: stub
---

# DataSploit

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://github.com/datasploit/datasploit/
- **Best for:** Multi-target reconnaissance (domain/email/username/phone aggregation)
- **Input → Output:** Domain, email address, username, phone number, Bitcoin addresses → HTML, JSON, and text reports aggregating findings
- **OpSec:** active. Performs active reconnaissance; relies on external API availability

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
