---
id: slack-intelbot
name: slack-intelbot
description: In-channel IOC enrichment for threat intelligence triage
url: https://github.com/pun1sh3r/slack-intelbot
category: messaging
path:
- messaging
- slack
bestFor: In-channel IOC enrichment for threat intelligence triage
input: Indicators posted in Slack and configured API credentials
output: Automated enrichment responses with indicator context and reputation data
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Queries third-party intelligence APIs; no direct interaction with investigation targets by default.
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

# slack-intelbot

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://github.com/pun1sh3r/slack-intelbot
- **Best for:** In-channel IOC enrichment for threat intelligence triage
- **Input → Output:** Indicators posted in Slack and configured API credentials → Automated enrichment responses with indicator context and reputation data
- **OpSec:** passive. Queries third-party intelligence APIs; no direct interaction with investigation targets by default.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
