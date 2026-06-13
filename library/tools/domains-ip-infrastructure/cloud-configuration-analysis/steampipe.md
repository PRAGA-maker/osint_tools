---
id: steampipe
name: Steampipe
description: SQL-driven cloud inventory and security query workflows
url: https://github.com/turbot/steampipe
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- cloud-configuration-analysis
bestFor: SQL-driven cloud inventory and security query workflows
input: SQL queries and plugin connections to cloud/provider APIs
output: Tabular query results from live cloud metadata
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
opsec: active
opsecNote: Executes API-backed queries against connected cloud accounts.
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

# Steampipe

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://github.com/turbot/steampipe
- **Best for:** SQL-driven cloud inventory and security query workflows
- **Input → Output:** SQL queries and plugin connections to cloud/provider APIs → Tabular query results from live cloud metadata
- **OpSec:** active. Executes API-backed queries against connected cloud accounts.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
