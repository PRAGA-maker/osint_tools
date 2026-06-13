---
id: whatsapp-osint
name: WhatsApp-OSINT
description: Rapid WhatsApp account reconnaissance and metadata checks
url: https://github.com/kinghacker0/WhatsApp-OSINT
category: messaging
path:
- messaging
- whatsapp
bestFor: Rapid WhatsApp account reconnaissance and metadata checks
input: Phone numbers or WhatsApp account identifiers
output: Enriched account metadata and reconnaissance results
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
opsec: active
opsecNote: Direct API-driven lookups against messaging infrastructure may be logged by providers.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: cli
trust: unverified
trustNote: ''
missingPersonsRelevance: high
coverage: []
auth: account
api: true
localInstall: true
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

# WhatsApp-OSINT

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://github.com/kinghacker0/WhatsApp-OSINT
- **Best for:** Rapid WhatsApp account reconnaissance and metadata checks
- **Input → Output:** Phone numbers or WhatsApp account identifiers → Enriched account metadata and reconnaissance results
- **OpSec:** active. Direct API-driven lookups against messaging infrastructure may be logged by providers.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
