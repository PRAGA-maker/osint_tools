---
id: autoosint
name: AutoOSINT
description: Automated domain/email reconnaissance with report generation
url: https://github.com/bharshbarger/AutOSINT
category: ai-analysis-automation
path:
- ai-analysis-automation
- osint-automation
bestFor: Automated domain/email reconnaissance with report generation
input: Domain names, dorks, client names
output: Word (docx) reports with aggregated OSINT results
selectorsIn: []
selectorsOut: []
status: down
pricing: free
opsec: active
opsecNote: API-dependent modules (Shodan, HIBP) require keys; public searches passive
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: cli
trust: unverified
trustNote: ''
missingPersonsRelevance: low
coverage: []
auth: account
api: true
localInstall: true
registration: true
invitationOnly: false
deprecated: true
relatedTools: []
aliases: []
tags: []
source: arf-seed
lastVerified: ''
enrichment: stub
---

# AutoOSINT

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://github.com/bharshbarger/AutOSINT
- **Best for:** Automated domain/email reconnaissance with report generation
- **Input → Output:** Domain names, dorks, client names → Word (docx) reports with aggregated OSINT results
- **OpSec:** active. API-dependent modules (Shodan, HIBP) require keys; public searches passive

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
