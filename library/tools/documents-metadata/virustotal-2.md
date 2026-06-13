---
id: virustotal-2
name: virustotal
description: Multi-engine malware scanning and URL reputation lookup
url: https://www.virustotal.com/gui/home/upload
category: documents-metadata
path:
- documents-metadata
bestFor: Multi-engine malware scanning and URL reputation lookup
input: Files, URLs, domains, IP addresses, file hashes
output: Detection results from 70+ AV engines, behavioral analysis, file insights, related samples
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
opsec: passive
opsecNote: File uploads are indexed and visible to other users; hash-only queries are private
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: low
coverage: []
auth: account
api: true
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

# virustotal

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.virustotal.com/gui/home/upload
- **Best for:** Multi-engine malware scanning and URL reputation lookup
- **Input → Output:** Files, URLs, domains, IP addresses, file hashes → Detection results from 70+ AV engines, behavioral analysis, file insights, related samples
- **OpSec:** passive. File uploads are indexed and visible to other users; hash-only queries are private

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
