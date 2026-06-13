---
id: twitwork
name: TwitWork
description: Electron/Node.js desktop app to monitor a live Twitter stream.
url: https://github.com/atmoner/TwitWork
category: social-networks
path:
- social-networks
bestFor: Real-time monitoring of Twitter/X activity for keywords or accounts
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- username
status: unknown
pricing: free
opsec: passive
opsecNote: ''
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: community
trustNote: 272 stars; relies on the legacy Twitter API which may be deprecated/paywalled post-2023 changes.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: true
registration: true
aliases: []
tags:
- twitter
- x
- stream-monitoring
- social
source: gh-topic-intelligence-gathering
lastVerified: ''
enrichment: full
---

# TwitWork

> Electron/Node.js desktop app to monitor a live Twitter stream.

- **URL:** https://github.com/atmoner/TwitWork
- **Best for:** Real-time monitoring of Twitter/X activity for keywords or accounts
- **Source:** harvested from `gh-topic-intelligence-gathering`

Monitors Twitter streams from a desktop Electron app. Useful for watching a person's social activity, but Twitter/X API access changes since 2023 likely break or paywall functionality. Requires Twitter API keys.

_Enrichment: full. If stub, complete per `schema/templates/tool.template.md`._
