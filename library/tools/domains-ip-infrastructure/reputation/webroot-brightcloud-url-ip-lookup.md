---
id: webroot-brightcloud-url-ip-lookup
name: Webroot BrightCloud URL/IP Lookup
description: URL/IP reputation lookup, web classification, threat intelligence, web categorization
url: https://www.brightcloud.com/tools/url-ip-lookup.php
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- reputation
bestFor: URL/IP reputation lookup, web classification, threat intelligence, web categorization
input: URL or IP address
output: Threat assessment, content category, reputation score, WHOIS data, risk level
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Queries BrightCloud's reputation database without directly contacting the target.
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

# Webroot BrightCloud URL/IP Lookup

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.brightcloud.com/tools/url-ip-lookup.php
- **Best for:** URL/IP reputation lookup, web classification, threat intelligence, web categorization
- **Input → Output:** URL or IP address → Threat assessment, content category, reputation score, WHOIS data, risk level
- **OpSec:** passive. Queries BrightCloud's reputation database without directly contacting the target.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
