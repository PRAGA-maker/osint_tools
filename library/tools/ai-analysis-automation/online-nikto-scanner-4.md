---
id: online-nikto-scanner-4
name: Online Nikto scanner
description: Web server vulnerability scanning, security assessment, SSL/TLS validation
url: https://nikto.online/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Web server vulnerability scanning, security assessment, SSL/TLS validation
input: Website URLs or domain names; configurable scan types
output: Vulnerability reports, CVE matching, server identification data, HTTP header analysis
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
opsec: active
opsecNote: Active vulnerability scanning; generates logs on target systems; creates measurable network activity
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

# Online Nikto scanner

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://nikto.online/
- **Best for:** Web server vulnerability scanning, security assessment, SSL/TLS validation
- **Input → Output:** Website URLs or domain names; configurable scan types → Vulnerability reports, CVE matching, server identification data, HTTP header analysis
- **OpSec:** active. Active vulnerability scanning; generates logs on target systems; creates measurable network activity

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
