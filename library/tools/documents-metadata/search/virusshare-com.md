---
id: virusshare-com
name: VirusShare.com
description: Bulk access to malware sample collections for research and analysis
url: https://virusshare.com/
category: documents-metadata
path:
- documents-metadata
- search
bestFor: Bulk access to malware sample collections for research and analysis
input: MD5 hash, account credentials
output: Malware sample files (zip archives, password protected), related IOCs
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Registration required; no direct execution occurs; passive hash lookup available
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: low
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

# VirusShare.com

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://virusshare.com/
- **Best for:** Bulk access to malware sample collections for research and analysis
- **Input → Output:** MD5 hash, account credentials → Malware sample files (zip archives, password protected), related IOCs
- **OpSec:** passive. Registration required; no direct execution occurs; passive hash lookup available

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
