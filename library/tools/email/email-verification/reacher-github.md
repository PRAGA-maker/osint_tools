---
id: reacher-github
name: Reacher Github
description: Email verification, bounce detection, list cleaning
url: https://github.com/reacherhq/check-if-email-exists
category: email
path:
- email
- email-verification
bestFor: Email verification, bounce detection, list cleaning
input: Email address
output: Deliverability status, MX records, bounce type
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Verifies email existence through MTA queries without sending mail.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: unverified
trustNote: ''
missingPersonsRelevance: high
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

# Reacher Github

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://github.com/reacherhq/check-if-email-exists
- **Best for:** Email verification, bounce detection, list cleaning
- **Input → Output:** Email address → Deliverability status, MX records, bounce type
- **OpSec:** passive. Verifies email existence through MTA queries without sending mail.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
