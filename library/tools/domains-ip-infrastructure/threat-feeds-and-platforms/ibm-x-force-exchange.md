---
id: ibm-x-force-exchange
name: IBM X-Force Exchange
description: Malware and threat intelligence
url: https://exchange.xforce.ibmcloud.com/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- threat-feeds-and-platforms
bestFor: Malware and threat intelligence
input: IOC, domain, or malware sample
output: Threat analysis and intelligence reports
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
opsec: passive
opsecNote: Passive querying of threat database
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

# IBM X-Force Exchange

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://exchange.xforce.ibmcloud.com/
- **Best for:** Malware and threat intelligence
- **Input → Output:** IOC, domain, or malware sample → Threat analysis and intelligence reports
- **OpSec:** passive. Passive querying of threat database

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
