---
id: checkov
name: Checkov
description: Shift-left cloud misconfiguration detection in IaC repositories
url: https://github.com/bridgecrewio/checkov
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- cloud-configuration-analysis
bestFor: Shift-left cloud misconfiguration detection in IaC repositories
input: IaC source files, templates, and configuration manifests
output: Policy violations with severity and remediation context
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Analyzes local code/config files without probing target cloud environments directly.
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

# Checkov

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://github.com/bridgecrewio/checkov
- **Best for:** Shift-left cloud misconfiguration detection in IaC repositories
- **Input → Output:** IaC source files, templates, and configuration manifests → Policy violations with severity and remediation context
- **OpSec:** passive. Analyzes local code/config files without probing target cloud environments directly.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
