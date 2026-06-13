---
id: zcash-block-explorer
name: Zcash Block Explorer
description: Zcash transparent transaction tracking (limited privacy-coin OSINT)
url: https://blockchair.com/zcash
category: financial-crypto
path:
- financial-crypto
- privacy-coin-analysis
bestFor: Zcash transparent transaction tracking (limited privacy-coin OSINT)
input: Zcash address (transparent), transaction hash, or block height
output: Transaction details, address balance (transparent addresses only), block information, mining statistics
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
opsec: passive
opsecNote: Only transparent Zcash transactions are traceable; shielded transactions provide privacy beyond analysis capability.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: medium
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

# Zcash Block Explorer

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://blockchair.com/zcash
- **Best for:** Zcash transparent transaction tracking (limited privacy-coin OSINT)
- **Input → Output:** Zcash address (transparent), transaction hash, or block height → Transaction details, address balance (transparent addresses only), block information, mining statistics
- **OpSec:** passive. Only transparent Zcash transactions are traceable; shielded transactions provide privacy beyond analysis capability.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
