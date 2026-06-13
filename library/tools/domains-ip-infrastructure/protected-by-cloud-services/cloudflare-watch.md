---
id: cloudflare-watch
name: CloudFlare Watch
description: Identify Cloudflare-protected sites
url: https://www.crimeflare.com/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- protected-by-cloud-services
bestFor: Identify Cloudflare-protected sites
input: Domain or IP
output: Cloudflare status, origin IP (if discoverable)
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Passive lookup of Cloudflare configurations.
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

# CloudFlare Watch

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.crimeflare.com/
- **Best for:** Identify Cloudflare-protected sites
- **Input → Output:** Domain or IP → Cloudflare status, origin IP (if discoverable)
- **OpSec:** passive. Passive lookup of Cloudflare configurations.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
