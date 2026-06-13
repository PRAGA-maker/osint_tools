---
id: read-notify
name: Read Notify
description: Email delivery confirmation, read receipt tracking
url: https://www.readnotify.com/
category: email
path:
- email
- email-verification
bestFor: Email delivery confirmation, read receipt tracking
input: Email address
output: Delivery and read status
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
opsec: active
opsecNote: Sends tracking pixels; may alert targets to monitoring.
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

# Read Notify

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.readnotify.com/
- **Best for:** Email delivery confirmation, read receipt tracking
- **Input → Output:** Email address → Delivery and read status
- **OpSec:** active. Sends tracking pixels; may alert targets to monitoring.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
