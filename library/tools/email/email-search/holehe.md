---
id: holehe
name: Holehe
description: Email account enumeration, service detection
url: https://github.com/megadose/holehe
category: email
path:
- email
- email-search
bestFor: Email account enumeration, service detection
input: Email address
output: List of websites where email is registered
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Uses password-reset functionality without sending emails or alerting targets.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: unverified
trustNote: ''
missingPersonsRelevance: high
coverage: []
auth: none
api: false
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

# Holehe

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://github.com/megadose/holehe
- **Best for:** Email account enumeration, service detection
- **Input → Output:** Email address → List of websites where email is registered
- **OpSec:** passive. Uses password-reset functionality without sending emails or alerting targets.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
