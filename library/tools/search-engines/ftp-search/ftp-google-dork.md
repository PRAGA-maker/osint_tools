---
id: ftp-google-dork
name: FTP Google Dork
description: Discovering publicly indexed FTP server directories and files via Google dorking
url: https://www.google.com/search?q=inurl%3Aftp+-inurl%3Ahttp+-inurl%3Ahttps+ftpsearchterm
category: search-engines
path:
- search-engines
- ftp-search
bestFor: Discovering publicly indexed FTP server directories and files via Google dorking
input: Search term appended to the dork URL
output: Google search results showing indexed FTP server directories
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Searches are routed through Google; no direct contact with target FTP servers.
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

# FTP Google Dork

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.google.com/search?q=inurl%3Aftp+-inurl%3Ahttp+-inurl%3Ahttps+ftpsearchterm
- **Best for:** Discovering publicly indexed FTP server directories and files via Google dorking
- **Input → Output:** Search term appended to the dork URL → Google search results showing indexed FTP server directories
- **OpSec:** passive. Searches are routed through Google; no direct contact with target FTP servers.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
