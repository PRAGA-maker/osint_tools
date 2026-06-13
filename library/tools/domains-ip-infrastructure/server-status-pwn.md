---
id: server-status-pwn
name: server-status_PWN
description: Monitors public Apache /server-status pages to harvest URLs and request data for reconnaissance.
url: https://github.com/mazen160/server-status_PWN
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Scraping exposed Apache server-status for active request intel
selectorsIn:
- domain
- ip-address
selectorsOut:
- ip-address
- domain
status: unknown
pricing: free
opsec: active
opsecNote: ''
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: 443 stars; narrow infrastructure recon tool.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases: []
tags:
- apache
- recon
- infrastructure
source: gh-topic-intelligence-gathering
lastVerified: ''
enrichment: full
---

# server-status_PWN

> Monitors public Apache /server-status pages to harvest URLs and request data for reconnaissance.

- **URL:** https://github.com/mazen160/server-status_PWN
- **Best for:** Scraping exposed Apache server-status for active request intel
- **Source:** harvested from `gh-topic-intelligence-gathering`

Infrastructure reconnaissance only; no people-finding relevance.

_Enrichment: full. If stub, complete per `schema/templates/tool.template.md`._
