---
id: disposable-email-domains
name: Disposable Email Domains
description: Detecting disposable and temporary email addresses during verification
url: https://github.com/disposable-email-domains/disposable-email-domains
category: email
path:
- email
- email-verification
bestFor: Detecting disposable and temporary email addresses during verification
input: Domain name to check against the blocklist
output: Match result against the disposable email domain blocklist
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Local list comparison; no external requests made during lookup.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: unverified
trustNote: ''
missingPersonsRelevance: high
coverage: []
auth: none
api: false
localInstall: true
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

# Disposable Email Domains

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://github.com/disposable-email-domains/disposable-email-domains
- **Best for:** Detecting disposable and temporary email addresses during verification
- **Input → Output:** Domain name to check against the blocklist → Match result against the disposable email domain blocklist
- **OpSec:** passive. Local list comparison; no external requests made during lookup.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
