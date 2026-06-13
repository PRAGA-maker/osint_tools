---
id: burner-email-providers
name: Burner Email Providers
description: Identifying burner email providers for integration into custom investigation tools
url: https://github.com/wesbos/burner-email-providers
category: email
path:
- email
- email-verification
bestFor: Identifying burner email providers for integration into custom investigation tools
input: Email domain
output: Match result against known burner/temporary email providers
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Local list comparison; MIT licensed for integration use.
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

# Burner Email Providers

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://github.com/wesbos/burner-email-providers
- **Best for:** Identifying burner email providers for integration into custom investigation tools
- **Input → Output:** Email domain → Match result against known burner/temporary email providers
- **OpSec:** passive. Local list comparison; MIT licensed for integration use.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
