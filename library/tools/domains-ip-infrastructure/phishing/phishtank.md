---
id: phishtank
name: PhishTank
description: Phishing site verification
url: https://www.phishtank.com/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- phishing
bestFor: Phishing site verification
input: Phishing URL or suspected malicious site
output: Phishing status and community verification votes
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Passive lookup of community-reported database
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

# PhishTank

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.phishtank.com/
- **Best for:** Phishing site verification
- **Input → Output:** Phishing URL or suspected malicious site → Phishing status and community verification votes
- **OpSec:** passive. Passive lookup of community-reported database

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
