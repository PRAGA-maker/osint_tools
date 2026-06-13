---
id: common-crawl
name: Common Crawl
description: Large-scale historical web content mining and corpus analysis
url: https://commoncrawl.org/
category: archives-cache
path:
- archives-cache
- web
bestFor: Large-scale historical web content mining and corpus analysis
input: CC index query, URL, domain, or WARC request
output: Raw crawl records, metadata indexes, and extracted web content
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Reads published crawl datasets and indexes; no direct interaction with target systems.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: medium
coverage: []
auth: none
api: true
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

# Common Crawl

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://commoncrawl.org/
- **Best for:** Large-scale historical web content mining and corpus analysis
- **Input → Output:** CC index query, URL, domain, or WARC request → Raw crawl records, metadata indexes, and extracted web content
- **OpSec:** passive. Reads published crawl datasets and indexes; no direct interaction with target systems.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
