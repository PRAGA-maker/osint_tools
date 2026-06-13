---
id: have-i-been-pwned
name: Have I been pwned?
description: Breach detection, credential exposure checks
url: https://haveibeenpwned.com/
category: email
path:
- email
- breach-data
bestFor: Breach detection, credential exposure checks
input: Email address, phone number, password hash
output: Breach names, breach dates, exposed data types
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
opsec: passive
opsecNote: Queries breach database via API. Target is not notified of lookups.
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

# Have I been pwned?

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://haveibeenpwned.com/
- **Best for:** Breach detection, credential exposure checks
- **Input → Output:** Email address, phone number, password hash → Breach names, breach dates, exposed data types
- **OpSec:** passive. Queries breach database via API. Target is not notified of lookups.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
