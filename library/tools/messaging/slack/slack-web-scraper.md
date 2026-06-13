---
id: slack-web-scraper
name: slack-web-scraper
description: Archiving Slack channel content for offline analysis
url: https://github.com/iulspop/slack-web-scraper
category: messaging
path:
- messaging
- slack
bestFor: Archiving Slack channel content for offline analysis
input: Slack-authenticated browser/session context
output: Scraped channel messages and related metadata exports
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: active
opsecNote: Direct scraping activity against Slack endpoints may be logged and rate-limited.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: cli
trust: unverified
trustNote: ''
missingPersonsRelevance: high
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

# slack-web-scraper

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://github.com/iulspop/slack-web-scraper
- **Best for:** Archiving Slack channel content for offline analysis
- **Input → Output:** Slack-authenticated browser/session context → Scraped channel messages and related metadata exports
- **OpSec:** active. Direct scraping activity against Slack endpoints may be logged and rate-limited.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
