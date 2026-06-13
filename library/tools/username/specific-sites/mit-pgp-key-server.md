---
id: mit-pgp-key-server
name: MIT PGP Key Server
description: Looking up PGP public keys associated with a username or email address
url: https://pgp.mit.edu/
category: username
path:
- username
- specific-sites
bestFor: Looking up PGP public keys associated with a username or email address
input: Name, email address, or key ID
output: PGP public key data, key fingerprints, associated UIDs/email addresses, and key metadata
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Public key server query; no authentication required and target is not notified of lookups.
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

# MIT PGP Key Server

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://pgp.mit.edu/
- **Best for:** Looking up PGP public keys associated with a username or email address
- **Input → Output:** Name, email address, or key ID → PGP public key data, key fingerprints, associated UIDs/email addresses, and key metadata
- **OpSec:** passive. Public key server query; no authentication required and target is not notified of lookups.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
