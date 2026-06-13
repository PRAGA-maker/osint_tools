---
id: criminal-ip-search
name: Criminal IP Search
description: Threat-focused lookup of internet-facing assets and exposures
url: https://www.criminalip.io/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- discovery
bestFor: Threat-focused lookup of internet-facing assets and exposures
input: IP, domain, ASN, CVE, or filter-based threat query
output: Asset details, risk scores, service fingerprints, and vulnerability context
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
opsec: passive
opsecNote: Searches provider datasets rather than scanning targets directly from analyst infrastructure.
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

# Criminal IP Search

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.criminalip.io/
- **Best for:** Threat-focused lookup of internet-facing assets and exposures
- **Input → Output:** IP, domain, ASN, CVE, or filter-based threat query → Asset details, risk scores, service fingerprints, and vulnerability context
- **OpSec:** passive. Searches provider datasets rather than scanning targets directly from analyst infrastructure.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
