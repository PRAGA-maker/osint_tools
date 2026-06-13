---
id: databases-today
name: Databases.Today
description: Identifying whether target identifiers appear in known breach dumps
url: https://databases.today/
category: archives-cache
path:
- archives-cache
- data-leaks
bestFor: Identifying whether target identifiers appear in known breach dumps
input: Email, username, domain, or keyword
output: Indexed breach hit results and source references
selectorsIn: []
selectorsOut: []
status: degraded
pricing: freemium
opsec: active
opsecNote: Operational status requires verification; querying breach portals can create attribution and compliance risk.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: medium
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

# Databases.Today

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://databases.today/
- **Best for:** Identifying whether target identifiers appear in known breach dumps
- **Input → Output:** Email, username, domain, or keyword → Indexed breach hit results and source references
- **OpSec:** active. Operational status requires verification; querying breach portals can create attribution and compliance risk.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
