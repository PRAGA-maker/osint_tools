---
id: whatsmyname-web
name: WhatsMyName Web
description: Quick web-based username enumeration across social media, forums, gaming platforms, and professional networks
url: https://whatsmyname.app/
category: username
path:
- username
- username-search-engines
bestFor: Quick web-based username enumeration across social media, forums, gaming platforms, and professional networks
input: Username
output: List of sites where the username exists with direct profile links
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: active
opsecNote: Makes HTTP requests to each target site to check for username existence, however it does it from WhatsMyName infrastructure.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: high
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

# WhatsMyName Web

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://whatsmyname.app/
- **Best for:** Quick web-based username enumeration across social media, forums, gaming platforms, and professional networks
- **Input → Output:** Username → List of sites where the username exists with direct profile links
- **OpSec:** active. Makes HTTP requests to each target site to check for username existence, however it does it from WhatsMyName infrastructure.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
