---
id: tinfoleak-web
name: Tinfoleak Web
description: Twitter profile and timeline intelligence
url: https://tinfoleak.com/
category: social-networks
path:
- social-networks
- twitter
- analytics
bestFor: Twitter profile and timeline intelligence
input: Twitter/X username or profile URL
output: Profile details, tweet history views, and account activity context
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
opsec: active
opsecNote: Queries are sent to third-party service infrastructure and may be logged.
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

# Tinfoleak Web

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://tinfoleak.com/
- **Best for:** Twitter profile and timeline intelligence
- **Input → Output:** Twitter/X username or profile URL → Profile details, tweet history views, and account activity context
- **OpSec:** active. Queries are sent to third-party service infrastructure and may be logged.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
