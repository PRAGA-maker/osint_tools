---
id: windows-defender-security-intelligence-wdsi
name: Windows Defender Security Intelligence (WDSI)
description: Reporting malicious sites to Microsoft and checking URL threat status
url: https://www.microsoft.com/en-us/wdsi
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- report-malicious-sites
bestFor: Reporting malicious sites to Microsoft and checking URL threat status
input: URLs
output: Threat status and submission confirmation
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Microsoft-tracked; submissions aggregated for threat intelligence
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: low
coverage: []
auth: none
api: true
localInstall: false
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

# Windows Defender Security Intelligence (WDSI)

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.microsoft.com/en-us/wdsi
- **Best for:** Reporting malicious sites to Microsoft and checking URL threat status
- **Input → Output:** URLs → Threat status and submission confirmation
- **OpSec:** passive. Microsoft-tracked; submissions aggregated for threat intelligence

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
