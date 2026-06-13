---
id: whois-arin
name: Whois ARIN
description: IP address and ASN registration data, North American internet resource tracking
url: https://whois.arin.net/ui/advanced.jsp
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- whois-records
bestFor: IP address and ASN registration data, North American internet resource tracking
input: IP address, ASN, organization name, contact information
output: IP ownership, organization details, Points of Contact (POCs), ASN information
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Queries official ARIN database; does not contact targets or perform active scanning.
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

# Whois ARIN

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://whois.arin.net/ui/advanced.jsp
- **Best for:** IP address and ASN registration data, North American internet resource tracking
- **Input → Output:** IP address, ASN, organization name, contact information → IP ownership, organization details, Points of Contact (POCs), ASN information
- **OpSec:** passive. Queries official ARIN database; does not contact targets or perform active scanning.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
