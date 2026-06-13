---
id: whatsmyname
name: WhatsMyName
description: Username enumeration using community-maintained site detection data
url: https://github.com/WebBreacher/WhatsMyName
category: username
path:
- username
- username-search-engines
bestFor: Username enumeration using community-maintained site detection data
input: Username
output: List of sites where the username exists, based on HTTP response pattern matching
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: active
opsecNote: Makes HTTP requests to each target site to check for username existence.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
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

# WhatsMyName

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://github.com/WebBreacher/WhatsMyName
- **Best for:** Username enumeration using community-maintained site detection data
- **Input → Output:** Username → List of sites where the username exists, based on HTTP response pattern matching
- **OpSec:** active. Makes HTTP requests to each target site to check for username existence.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
