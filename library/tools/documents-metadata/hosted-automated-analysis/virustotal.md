---
id: virustotal
name: VirusTotal
description: Malware analysis, URL reputation, file hash lookups
url: https://www.virustotal.com/gui/
category: documents-metadata
path:
- documents-metadata
- hosted-automated-analysis
bestFor: Malware analysis, URL reputation, file hash lookups
input: File, file hash, URL, domain, IP address
output: Detection results, behavioral analysis, community comments, related indicators
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
opsec: passive
opsecNote: Uploaded files become visible to other VirusTotal users. Hash lookups are private.
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

# VirusTotal

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.virustotal.com/gui/
- **Best for:** Malware analysis, URL reputation, file hash lookups
- **Input → Output:** File, file hash, URL, domain, IP address → Detection results, behavioral analysis, community comments, related indicators
- **OpSec:** passive. Uploaded files become visible to other VirusTotal users. Hash lookups are private.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
