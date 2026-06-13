---
id: dehashed
name: DeHashed
description: Breach searching, credential lookup, historical breach analysis
url: https://dehashed.com/
category: email
path:
- email
- breach-data
bestFor: Breach searching, credential lookup, historical breach analysis
input: Email, username, password, domain, phone, or IP
output: Breach records, exposed credentials, breach dates
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
opsec: passive
opsecNote: Searches aggregated public breach databases.
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

# DeHashed

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://dehashed.com/
- **Best for:** Breach searching, credential lookup, historical breach analysis
- **Input → Output:** Email, username, password, domain, phone, or IP → Breach records, exposed credentials, breach dates
- **OpSec:** passive. Searches aggregated public breach databases.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
