---
id: slackpirate
name: SlackPirate
description: Slack workspace enumeration and sensitive data exposure assessment
url: https://github.com/emtunc/SlackPirate
category: messaging
path:
- messaging
- slack
bestFor: Slack workspace enumeration and sensitive data exposure assessment
input: Authenticated Slack session/token and workspace target
output: Channel/user inventory and extracted accessible Slack content
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: active
opsecNote: Interacts directly with Slack workspace APIs and can leave observable request activity.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: cli
trust: unverified
trustNote: ''
missingPersonsRelevance: high
coverage: []
auth: account
api: true
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

# SlackPirate

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://github.com/emtunc/SlackPirate
- **Best for:** Slack workspace enumeration and sensitive data exposure assessment
- **Input → Output:** Authenticated Slack session/token and workspace target → Channel/user inventory and extracted accessible Slack content
- **OpSec:** active. Interacts directly with Slack workspace APIs and can leave observable request activity.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
