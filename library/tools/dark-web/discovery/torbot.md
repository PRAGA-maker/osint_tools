---
id: torbot
name: TorBot
description: Automated dark web crawling and onion link collection
url: https://github.com/DedSecInside/TorBot
category: dark-web
path:
- dark-web
- discovery
bestFor: Automated dark web crawling and onion link collection
input: Seed onion links and crawl configuration
output: Crawled onion pages, discovered links, and metadata
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: active
opsecNote: Crawling generates repeated target requests that can be detected by destination services.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: medium
coverage: []
auth: none
api: true
localInstall: true
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

# TorBot

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://github.com/DedSecInside/TorBot
- **Best for:** Automated dark web crawling and onion link collection
- **Input → Output:** Seed onion links and crawl configuration → Crawled onion pages, discovered links, and metadata
- **OpSec:** active. Crawling generates repeated target requests that can be detected by destination services.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
