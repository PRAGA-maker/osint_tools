---
id: earthexplorer
name: EarthExplorer
description: Downloading historical and multispectral satellite datasets
url: https://earthexplorer.usgs.gov/
category: geolocation
path:
- geolocation
bestFor: Downloading historical and multispectral satellite datasets
input: AOI, date range, and dataset criteria
output: Search results with downloadable geospatial scenes
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Uses open-source mapping/geospatial data and does not directly interact with the target.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: high
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

# EarthExplorer

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://earthexplorer.usgs.gov/
- **Best for:** Downloading historical and multispectral satellite datasets
- **Input → Output:** AOI, date range, and dataset criteria → Search results with downloadable geospatial scenes
- **OpSec:** passive. Uses open-source mapping/geospatial data and does not directly interact with the target.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
