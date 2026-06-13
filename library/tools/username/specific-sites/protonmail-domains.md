---
id: protonmail-domains
name: ProtonMail Domains
description: Checking if an email address on a custom domain is hosted on ProtonMail
url: https://api.protonmail.ch/pks/lookup?op=index&search=<email_address>
category: username
path:
- username
- specific-sites
bestFor: Checking if an email address on a custom domain is hosted on ProtonMail
input: Full email address (any domain that may be hosted on ProtonMail)
output: PGP key index with public key fingerprint, algorithm, creation timestamp, and email UID
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Unauthenticated public HKP endpoint. Target is not notified. Can reveal whether a custom domain uses ProtonMail.
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

# ProtonMail Domains

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://api.protonmail.ch/pks/lookup?op=index&search=<email_address>
- **Best for:** Checking if an email address on a custom domain is hosted on ProtonMail
- **Input → Output:** Full email address (any domain that may be hosted on ProtonMail) → PGP key index with public key fingerprint, algorithm, creation timestamp, and email UID
- **OpSec:** passive. Unauthenticated public HKP endpoint. Target is not notified. Can reveal whether a custom domain uses ProtonMail.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
