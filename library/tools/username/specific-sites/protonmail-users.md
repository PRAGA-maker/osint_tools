---
id: protonmail-users
name: ProtonMail users
description: Confirming whether a ProtonMail username exists and retrieving its PGP public key
url: https://api.protonmail.ch/pks/lookup?op=index&search=<username>@protonmail.com
category: username
path:
- username
- specific-sites
bestFor: Confirming whether a ProtonMail username exists and retrieving its PGP public key
input: ProtonMail username (appended with @protonmail.com)
output: PGP key index with public key fingerprint, algorithm, creation timestamp, and email UID
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Unauthenticated API query to ProtonMail's public key server. Target user is not notified. Enables user enumeration.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: high
coverage: []
auth: none
api: true
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

# ProtonMail users

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://api.protonmail.ch/pks/lookup?op=index&search=<username>@protonmail.com
- **Best for:** Confirming whether a ProtonMail username exists and retrieving its PGP public key
- **Input → Output:** ProtonMail username (appended with @protonmail.com) → PGP key index with public key fingerprint, algorithm, creation timestamp, and email UID
- **OpSec:** passive. Unauthenticated API query to ProtonMail's public key server. Target user is not notified. Enables user enumeration.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
