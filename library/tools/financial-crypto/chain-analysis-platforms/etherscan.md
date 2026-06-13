---
id: etherscan
name: Etherscan
description: Ethereum and EVM transaction analysis, smart contract inspection, token tracking
url: https://etherscan.io/
category: financial-crypto
path:
- financial-crypto
- chain-analysis-platforms
bestFor: Ethereum and EVM transaction analysis, smart contract inspection, token tracking
input: Ethereum address, transaction hash, smart contract address, token contract
output: Transaction details, smart contract source code, token transfers, holder lists, gas analytics
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
opsec: passive
opsecNote: Query via web interface or free API (rate-limited); no registration required for basic lookup. API keys enable higher rate limits.
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

# Etherscan

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://etherscan.io/
- **Best for:** Ethereum and EVM transaction analysis, smart contract inspection, token tracking
- **Input → Output:** Ethereum address, transaction hash, smart contract address, token contract → Transaction details, smart contract source code, token transfers, holder lists, gas analytics
- **OpSec:** passive. Query via web interface or free API (rate-limited); no registration required for basic lookup. API keys enable higher rate limits.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
