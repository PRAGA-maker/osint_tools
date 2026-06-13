---
id: email-domain-validation
name: Email Domain Validation
description: Email domain and mailbox verification
url: https://www.mailboxvalidator.com/domain
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- domain-blacklists
bestFor: Email domain and mailbox verification
input: Email domain or address
output: Domain validation report, MX records
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
opsec: active
opsecNote: Active mail server connectivity checks required for validation
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: low
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

# Email Domain Validation

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.mailboxvalidator.com/domain
- **Best for:** Email domain and mailbox verification
- **Input → Output:** Email domain or address → Domain validation report, MX records
- **OpSec:** active. Active mail server connectivity checks required for validation

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
