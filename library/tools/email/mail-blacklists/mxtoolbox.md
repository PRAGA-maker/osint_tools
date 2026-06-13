---
id: mxtoolbox
name: MxToolbox
description: Email server diagnostics, deliverability testing, DNS validation
url: https://mxtoolbox.com/
category: email
path:
- email
- mail-blacklists
bestFor: Email server diagnostics, deliverability testing, DNS validation
input: Domain name or email address
output: MX records, SPF/DKIM/DMARC status, blacklist info
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Public DNS lookups and SMTP diagnostics without target alerting.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: high
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

# MxToolbox

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://mxtoolbox.com/
- **Best for:** Email server diagnostics, deliverability testing, DNS validation
- **Input → Output:** Domain name or email address → MX records, SPF/DKIM/DMARC status, blacklist info
- **OpSec:** passive. Public DNS lookups and SMTP diagnostics without target alerting.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
