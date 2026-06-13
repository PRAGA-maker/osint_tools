---
id: google-safe-browsing
name: Google Safe Browsing
description: Reporting malicious sites to Google and checking URL safety status
url: https://safebrowsing.google.com/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- report-malicious-sites
bestFor: Reporting malicious sites to Google and checking URL safety status
input: URLs
output: Safety status and submission confirmation
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Google-tracked; searches and submissions aggregated at scale
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: low
coverage: []
auth: none
api: true
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

# Google Safe Browsing

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://safebrowsing.google.com/
- **Best for:** Reporting malicious sites to Google and checking URL safety status
- **Input → Output:** URLs → Safety status and submission confirmation
- **OpSec:** passive. Google-tracked; searches and submissions aggregated at scale

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
