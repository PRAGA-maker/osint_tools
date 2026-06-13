---
id: offvis
name: OffVis
description: Office binary file format analysis and exploit detection
url: https://download.microsoft.com/download/1/2/7/127ba59a-4fe1-4acd-ba47-513ceef85a85/OffVis.zip
category: documents-metadata
path:
- documents-metadata
- office-files
bestFor: Office binary file format analysis and exploit detection
input: Office binary files (.doc, .xls, .ppt, .pps, .pot)
output: File structure visualization, hex dump, object trees, vulnerability detection
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Local desktop application; no file uploads; Microsoft-provided tool
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

# OffVis

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://download.microsoft.com/download/1/2/7/127ba59a-4fe1-4acd-ba47-513ceef85a85/OffVis.zip
- **Best for:** Office binary file format analysis and exploit detection
- **Input → Output:** Office binary files (.doc, .xls, .ppt, .pps, .pot) → File structure visualization, hex dump, object trees, vulnerability detection
- **OpSec:** passive. Local desktop application; no file uploads; Microsoft-provided tool

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
