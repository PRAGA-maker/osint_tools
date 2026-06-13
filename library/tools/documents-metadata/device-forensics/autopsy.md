---
id: autopsy
name: Autopsy
description: Mobile forensic artifact extraction, database analysis, file system recovery, evidence analysis
url: https://www.autopsy.com/
category: documents-metadata
path:
- documents-metadata
- device-forensics
bestFor: Mobile forensic artifact extraction, database analysis, file system recovery, evidence analysis
input: Device backups, disk images, app databases, file systems
output: SQLite databases, app data, deleted files, timeline analysis, forensic artifacts
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Works on forensic images and backups; no interaction with live devices
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: medium
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

# Autopsy

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.autopsy.com/
- **Best for:** Mobile forensic artifact extraction, database analysis, file system recovery, evidence analysis
- **Input → Output:** Device backups, disk images, app databases, file systems → SQLite databases, app data, deleted files, timeline analysis, forensic artifacts
- **OpSec:** passive. Works on forensic images and backups; no interaction with live devices

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
