---
id: napalm-ftp
name: Napalm FTP
description: Large-scale FTP file discovery across hundreds of indexed public servers
url: https://www.searchftps.net/
category: search-engines
path:
- search-engines
- ftp-search
bestFor: Large-scale FTP file discovery across hundreds of indexed public servers
input: Filename, file type, or keyword
output: Matching files with FTP server address, path, file size, and date
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Searches Napalm FTP's index; no direct connection to target FTP servers during search.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: medium
coverage: []
auth: none
api: false
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

# Napalm FTP

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.searchftps.net/
- **Best for:** Large-scale FTP file discovery across hundreds of indexed public servers
- **Input → Output:** Filename, file type, or keyword → Matching files with FTP server address, path, file size, and date
- **OpSec:** passive. Searches Napalm FTP's index; no direct connection to target FTP servers during search.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
