---
id: cloudfail
name: CloudFail
description: Bypass Cloudflare to find origin IP
url: https://github.com/m0rtem/CloudFail
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- protected-by-cloud-services
bestFor: Bypass Cloudflare to find origin IP
input: Domain protected by Cloudflare
output: Origin IP address (if discoverable)
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: active
opsecNote: Uses active enumeration and DNS history techniques.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: unverified
trustNote: ''
missingPersonsRelevance: low
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

# CloudFail

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://github.com/m0rtem/CloudFail
- **Best for:** Bypass Cloudflare to find origin IP
- **Input → Output:** Domain protected by Cloudflare → Origin IP address (if discoverable)
- **OpSec:** active. Uses active enumeration and DNS history techniques.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
