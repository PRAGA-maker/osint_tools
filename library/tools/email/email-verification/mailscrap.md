---
id: mailscrap
name: MailScrap
description: Email validation, list cleaning, disposable email detection
url: https://mailscrap.com/
category: email
path:
- email
- email-verification
bestFor: Email validation, list cleaning, disposable email detection
input: Email addresses or email lists
output: Validation status, mailbox existence
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
opsec: passive
opsecNote: Connects to mail servers for verification without sending messages.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: high
coverage: []
auth: none
api: false
localInstall: false
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

# MailScrap

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://mailscrap.com/
- **Best for:** Email validation, list cleaning, disposable email detection
- **Input → Output:** Email addresses or email lists → Validation status, mailbox existence
- **OpSec:** passive. Connects to mail servers for verification without sending messages.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
