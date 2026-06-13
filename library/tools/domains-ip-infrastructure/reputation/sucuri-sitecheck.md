---
id: sucuri-sitecheck
name: Sucuri SiteCheck
description: Website malware scanning, vulnerability detection, security assessment
url: https://sitecheck.sucuri.net/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- reputation
bestFor: Website malware scanning, vulnerability detection, security assessment
input: Website URL
output: Security scan report, malware detection, blacklist status, vulnerable plugin/CMS details
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: active
opsecNote: Remotely visits the website to check source code and security; may be detectable by WAF/IDS.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: low
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

# Sucuri SiteCheck

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://sitecheck.sucuri.net/
- **Best for:** Website malware scanning, vulnerability detection, security assessment
- **Input → Output:** Website URL → Security scan report, malware detection, blacklist status, vulnerable plugin/CMS details
- **OpSec:** active. Remotely visits the website to check source code and security; may be detectable by WAF/IDS.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
