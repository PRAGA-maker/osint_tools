---
id: scoutsuite
name: ScoutSuite
description: Snapshot-style multi-cloud security posture reviews
url: https://github.com/nccgroup/ScoutSuite
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- cloud-configuration-analysis
bestFor: Snapshot-style multi-cloud security posture reviews
input: Cloud account credentials and provider-specific profile configuration
output: Interactive audit report with categorized misconfiguration findings
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: active
opsecNote: Collects cloud metadata directly from provider APIs using granted credentials.
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

# ScoutSuite

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://github.com/nccgroup/ScoutSuite
- **Best for:** Snapshot-style multi-cloud security posture reviews
- **Input → Output:** Cloud account credentials and provider-specific profile configuration → Interactive audit report with categorized misconfiguration findings
- **OpSec:** active. Collects cloud metadata directly from provider APIs using granted credentials.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
