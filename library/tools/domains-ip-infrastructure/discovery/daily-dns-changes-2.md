---
id: daily-dns-changes-2
name: Daily DNS Changes
description: DNS change detection, subdomain discovery, infrastructure monitoring
url: https://dailychanges.domaintools.com/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- discovery
bestFor: DNS change detection, subdomain discovery, infrastructure monitoring
input: Domain name
output: New DNS records, nameserver changes, subdomain discoveries, historical DNS changes
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
opsec: passive
opsecNote: Monitors public DNS records for changes; no active scanning or direct contact.
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

# Daily DNS Changes

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://dailychanges.domaintools.com/
- **Best for:** DNS change detection, subdomain discovery, infrastructure monitoring
- **Input → Output:** Domain name → New DNS records, nameserver changes, subdomain discoveries, historical DNS changes
- **OpSec:** passive. Monitors public DNS records for changes; no active scanning or direct contact.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
