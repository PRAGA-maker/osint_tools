---
id: recover-fb-account
name: Recover FB Account
description: Validating whether a target email or phone is tied to a Facebook account
url: https://www.facebook.com/login/identify?ctx=recover
category: social-networks
path:
- social-networks
- facebook
- search
bestFor: Validating whether a target email or phone is tied to a Facebook account
input: Email address or phone number
output: Account match confirmation and available recovery paths
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: No login required, but submitted identifiers are sent directly to Facebook.
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

# Recover FB Account

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.facebook.com/login/identify?ctx=recover
- **Best for:** Validating whether a target email or phone is tied to a Facebook account
- **Input → Output:** Email address or phone number → Account match confirmation and available recovery paths
- **OpSec:** passive. No login required, but submitted identifiers are sent directly to Facebook.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
