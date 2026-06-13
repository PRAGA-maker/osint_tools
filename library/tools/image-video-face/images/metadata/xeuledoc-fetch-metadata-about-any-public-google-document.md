---
id: xeuledoc-fetch-metadata-about-any-public-google-document
name: xeuledoc - Fetch metadata about any public Google document
description: Google document attribution and metadata extraction
url: https://github.com/Malfrats/xeuledoc
category: image-video-face
path:
- image-video-face
- images
- metadata
bestFor: Google document attribution and metadata extraction
input: Public Google document URLs
output: Owner identifiers, account metadata, and document context
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Reads only public docs without authentication bypass, but still queries Google infrastructure.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: high
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

# xeuledoc - Fetch metadata about any public Google document

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://github.com/Malfrats/xeuledoc
- **Best for:** Google document attribution and metadata extraction
- **Input → Output:** Public Google document URLs → Owner identifiers, account metadata, and document context
- **OpSec:** passive. Reads only public docs without authentication bypass, but still queries Google infrastructure.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
