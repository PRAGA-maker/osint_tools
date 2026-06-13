---
id: s3scanner
name: S3Scanner
description: Validating bucket exposure and permissions across S3-compatible targets
url: https://github.com/sa7mon/s3scanner
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- s3-blob-storage
bestFor: Validating bucket exposure and permissions across S3-compatible targets
input: Bucket names, generated candidates, or wordlist-driven targets
output: Bucket existence and permission states (list/read/write/public indicators)
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: active
opsecNote: Actively queries cloud storage endpoints and leaves provider-side request logs.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: unverified
trustNote: ''
missingPersonsRelevance: low
coverage: []
auth: none
api: false
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

# S3Scanner

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://github.com/sa7mon/s3scanner
- **Best for:** Validating bucket exposure and permissions across S3-compatible targets
- **Input → Output:** Bucket names, generated candidates, or wordlist-driven targets → Bucket existence and permission states (list/read/write/public indicators)
- **OpSec:** active. Actively queries cloud storage endpoints and leaves provider-side request logs.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
