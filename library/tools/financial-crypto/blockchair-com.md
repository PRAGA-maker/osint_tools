---
id: blockchair-com
name: blockchair.com
description: Use when you have a `crypto-wallet` address or transaction hash and want to trace it — returns balances, transaction history, and counterparties across 15+ blockchains.
url: https://blockchair.com/
category: financial-crypto
path:
- financial-crypto
bestFor: Multi-blockchain explorer — look up a wallet's balance and transaction history across Bitcoin, Ethereum, and many other chains from one search box.
selectorsIn:
- crypto-wallet
selectorsOut:
- crypto-wallet
status: live
pricing: freemium
costNote: Free web explorer and search; a paid API/data-dumps tier exists for bulk/programmatic use, but interactive lookups are free.
opsec: passive
opsecNote: Blockchain data is public and Blockchair reads its own indexed copy — you don't touch the wallet owner and no one is alerted. Passive. (Blockchair sees your queries; use a clean browser for sensitive tracing.)
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Well-established multi-chain blockchain explorer widely used in crypto research; data comes directly from the public blockchains it indexes.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- bitcoin-explorer
- blockchain-explorer
- etherscan
aliases:
- Blockchair
- blockchair.com
tags:
- cryptosites
- CryptoCurrency Related Sites
- blockchain-explorer
source: uk-osint
lastVerified: '2026-07-17'
enrichment: full
---

# blockchair.com

> A universal blockchain explorer and search engine — trace a wallet or transaction across 15+ chains (Bitcoin, Ethereum, and more) from a single interface.

## When to use
You have a `crypto-wallet` address or a transaction hash tied to a case — a ransom demand, a scam, a subject's known wallet — and want to see its activity: balance, inflows/outflows, counterparties, and timing. Blockchair's strength is breadth: it indexes many chains at once and offers a powerful search/filter, so it's a strong first stop for following crypto money. (Direct missing-persons relevance is usually low unless finances/extortion are involved.)

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://blockchair.com/ and paste the wallet address or transaction hash into the universal search (it auto-detects the chain).
2. On an address page, read current balance, total received/sent, and the full transaction list.
3. Follow transactions to counterparties; use filters/exports to map flows over time.
4. For a specific chain, prefix the URL (e.g. `blockchair.com/bitcoin/address/<addr>`).
5. Pivot: counterparty addresses → repeat the trace; exchange-linked addresses → point where a legal request could unmask an identity; cross-check on the chain's native explorer (`[[etherscan]]` for Ethereum).

## Inputs → Outputs
- **In:** a `crypto-wallet` address or transaction hash
- **Out:** balance, transaction history, counterparties, timestamps (`crypto-wallet` links)
- **Empty/negative result looks like:** address not found / zero activity — the address is unused, on a chain Blockchair doesn't index, or mistyped; try the chain's native explorer.

## Gotchas & OpSec
- Blockchain analysis shows addresses, not identities — attributing a wallet to a person needs off-chain links (exchange KYC, reused addresses, posts). Don't overclaim.
- Privacy coins and mixers break tracing; large exchanges pool funds, so a hop into an exchange usually ends the on-chain trail.
- Free interactive use is fine; bulk/automated pulls need the paid API.

## Overlaps ("do both")
- Pairs with `[[etherscan]]` (and other native explorers) — Blockchair is multi-chain and great for a first look; native explorers give chain-specific depth (tokens, contracts). Cross-check.
- Pairs with `[[bitcoin-explorer]]` for a second Bitcoin-specific view.

## Trust & verifiability
`trust: trusted` — an established explorer reading directly from public blockchains, so the on-chain data is authoritative and independently verifiable on any other explorer. Attribution to a real person is the hard part and always needs corroboration.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | blockchair-com |
| category | financial-crypto |
| selectorsIn → selectorsOut | crypto-wallet → crypto-wallet |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
