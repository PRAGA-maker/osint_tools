---
id: google-safe-browsing-api
name: Google Safe Browsing API
description: Malware and phishing URL detection
url: https://developers.google.com/safe-browsing/?csw=1
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- reputation
bestFor: Malware and phishing URL detection
input: URL or domain
output: Safe/unsafe classification, threat type
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Free for non-commercial use; commercial use requires Web Risk API (paid)
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

# Google Safe Browsing API

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://developers.google.com/safe-browsing/?csw=1
- **Best for:** Malware and phishing URL detection
- **Input → Output:** URL or domain → Safe/unsafe classification, threat type
- **OpSec:** passive. Free for non-commercial use; commercial use requires Web Risk API (paid)

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
