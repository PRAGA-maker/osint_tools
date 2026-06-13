---
id: memory-lol
name: memory.lol
description: Historical Twitter/X username and screen-name change history lookup.
url: https://memory.lol/app/
category: social-networks
path:
- social-networks
bestFor: Resolving old Twitter handles and tracking handle changes for an account
selectorsIn:
- username
selectorsOut:
- username
- social-profile
status: unknown
pricing: free
opsec: passive
opsecNote: ''
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Well-known handle-history tool (in the Social-Media-OSINT collection).
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases: []
tags:
- twitter
- handle-history
source: gh-topic-osint-resources
lastVerified: ''
enrichment: full
---

# memory.lol

> Historical Twitter/X username and screen-name change history lookup.

- **URL:** https://memory.lol/app/
- **Best for:** Resolving old Twitter handles and tracking handle changes for an account
- **Source:** harvested from `gh-topic-osint-resources`

Maps a current X account to its prior usernames - useful when a person renamed/abandoned an account.

_Enrichment: full. If stub, complete per `schema/templates/tool.template.md`._
