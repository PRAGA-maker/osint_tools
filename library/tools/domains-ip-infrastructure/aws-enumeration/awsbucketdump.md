---
id: awsbucketdump
name: AWSBucketDump
description: Targeted S3 bucket discovery and object collection
url: https://github.com/jordanpotti/AWSBucketDump
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- aws-enumeration
bestFor: Targeted S3 bucket discovery and object collection
input: AWS account naming patterns, keywords, and optional wordlists
output: Discovered bucket names and downloadable object listings/files
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: active
opsecNote: Actively sends requests to S3 endpoints and can download objects.
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

# AWSBucketDump

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://github.com/jordanpotti/AWSBucketDump
- **Best for:** Targeted S3 bucket discovery and object collection
- **Input → Output:** AWS account naming patterns, keywords, and optional wordlists → Discovered bucket names and downloadable object listings/files
- **OpSec:** active. Actively sends requests to S3 endpoints and can download objects.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
