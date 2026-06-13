---
id: google-finance
name: Google Finance
description: Quick financial overview, stock data, and news for public companies
url: https://www.google.com/finance/
category: public-records
path:
- public-records
- general-info-and-news
bestFor: Quick financial overview, stock data, and news for public companies
input: Company name or stock ticker
output: Stock price, financial summaries, news, and related companies
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: All queries routed through Google; no direct interaction with target company.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: medium
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

# Google Finance

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.google.com/finance/
- **Best for:** Quick financial overview, stock data, and news for public companies
- **Input → Output:** Company name or stock ticker → Stock price, financial summaries, news, and related companies
- **OpSec:** passive. All queries routed through Google; no direct interaction with target company.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
