---
id: voter-registration-data
name: Voter Registration Data
description: Voter registration verification
url: https://www.sos.secretary.state.gov/
category: public-records
path:
- public-records
- us-voter-records
bestFor: Voter registration verification
input: Name, state, county
output: Registration status, voting history
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: State-specific access and restrictions vary
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: medium
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

# Voter Registration Data

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.sos.secretary.state.gov/
- **Best for:** Voter registration verification
- **Input → Output:** Name, state, county → Registration status, voting history
- **OpSec:** passive. State-specific access and restrictions vary

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
