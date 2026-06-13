---
id: cloud-custodian
name: Cloud Custodian
description: Automated cloud governance and continuous configuration enforcement
url: https://github.com/cloud-custodian/cloud-custodian
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- cloud-configuration-analysis
bestFor: Automated cloud governance and continuous configuration enforcement
input: Cloud account credentials and YAML policy definitions
output: Matched resources, policy findings, and optional remediation actions
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: active
opsecNote: Uses cloud APIs directly and can trigger enforcement actions when configured.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: unverified
trustNote: ''
missingPersonsRelevance: low
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

# Cloud Custodian

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://github.com/cloud-custodian/cloud-custodian
- **Best for:** Automated cloud governance and continuous configuration enforcement
- **Input → Output:** Cloud account credentials and YAML policy definitions → Matched resources, policy findings, and optional remediation actions
- **OpSec:** active. Uses cloud APIs directly and can trigger enforcement actions when configured.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
