---
id: occrp-aleph
name: OCCRP Aleph
description: Cross-referencing persons and companies across public records, leaks, and investigative datasets
url: https://aleph.occrp.org/
category: public-records
path:
- public-records
- beneficial-ownership-lookup
bestFor: Cross-referencing persons and companies across public records, leaks, and investigative datasets
input: Person name, company name, or document keywords
output: Entity profiles, linked datasets, document matches, and relationship mappings
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Registration required for full access; queries are logged by OCCRP but subjects are not notified.
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

# OCCRP Aleph

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://aleph.occrp.org/
- **Best for:** Cross-referencing persons and companies across public records, leaks, and investigative datasets
- **Input → Output:** Person name, company name, or document keywords → Entity profiles, linked datasets, document matches, and relationship mappings
- **OpSec:** passive. Registration required for full access; queries are logged by OCCRP but subjects are not notified.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
