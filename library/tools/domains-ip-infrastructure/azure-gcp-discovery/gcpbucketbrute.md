---
id: gcpbucketbrute
name: GCPBucketBrute
description: Enumerating likely GCS bucket names at scale
url: https://github.com/RhinoSecurityLabs/GCPBucketBrute
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- azure-gcp-discovery
bestFor: Enumerating likely GCS bucket names at scale
input: Target company names, domains, and custom wordlists
output: Valid bucket names with access status and findings
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: active
opsecNote: Performs direct requests against GCS endpoints and can be detected in provider logs.
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

# GCPBucketBrute

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://github.com/RhinoSecurityLabs/GCPBucketBrute
- **Best for:** Enumerating likely GCS bucket names at scale
- **Input → Output:** Target company names, domains, and custom wordlists → Valid bucket names with access status and findings
- **OpSec:** active. Performs direct requests against GCS endpoints and can be detected in provider logs.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
