---
id: truecaller
name: Truecaller
description: Phone number verification, caller ID lookup, spam detection, contact validation
url: https://www.truecaller.com/
category: documents-metadata
path:
- documents-metadata
- android
- apps
bestFor: Phone number verification, caller ID lookup, spam detection, contact validation
input: Phone numbers, contact names
output: Caller name, carrier info, location data, spam reports, contact validation
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
opsec: passive
opsecNote: Requires app or web access; limited free tier for bulk lookups
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: cli
trust: unverified
trustNote: ''
missingPersonsRelevance: medium
coverage: []
auth: account
api: false
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

# Truecaller

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.truecaller.com/
- **Best for:** Phone number verification, caller ID lookup, spam detection, contact validation
- **Input → Output:** Phone numbers, contact names → Caller name, carrier info, location data, spam reports, contact validation
- **OpSec:** passive. Requires app or web access; limited free tier for bulk lookups

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
