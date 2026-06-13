---
id: public-buckets
name: Public Buckets
description: Investigating exposed bucket contents without running local scanners
url: https://buckets.grayhatwarfare.com/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- s3-blob-storage
bestFor: Investigating exposed bucket contents without running local scanners
input: Keywords, domains, filenames, and object metadata filters
output: Indexed public bucket/object matches with downloadable links
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
opsec: passive
opsecNote: Queries an existing index rather than probing target infrastructure directly.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: low
coverage: []
auth: account
api: false
localInstall: false
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

# Public Buckets

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://buckets.grayhatwarfare.com/
- **Best for:** Investigating exposed bucket contents without running local scanners
- **Input → Output:** Keywords, domains, filenames, and object metadata filters → Indexed public bucket/object matches with downloadable links
- **OpSec:** passive. Queries an existing index rather than probing target infrastructure directly.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
