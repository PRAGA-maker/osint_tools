---
id: bitquery-explorer
name: Bitquery Explorer
description: Use when you have a `crypto-wallet` address across chains and want deep, queryable on-chain data — returns transactions, token transfers, and DEX trades over 40+ blockchains.
url: https://explorer.bitquery.io/
category: financial-crypto
path:
- financial-crypto
- multi-chain-explorers
bestFor: Cross-chain blockchain data querying — following an address's transfers, token flows, and DEX activity across many chains from one interface (or GraphQL API).
selectorsIn:
- crypto-wallet
selectorsOut:
- crypto-wallet
status: live
pricing: freemium
costNote: Free web explorer and a free API tier (rate-limited, needs a free API key); high-volume/GraphQL streaming use is paid.
opsec: passive
opsecNote: Passive — you query public on-chain data via Bitquery's servers; the wallet owner sees nothing. API use ties queries to your (sock-puppet) account and key; the web explorer needs no login for lookups.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: An established blockchain-data provider indexing 40+ chains; its data derives from the public ledgers and is checkable against each chain's native explorer.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- Bitquery
- explorer.bitquery.io
tags:
- crypto
- blockchain
- multi-chain
- graphql
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# Bitquery Explorer

> A cross-chain blockchain explorer and query engine — trace an address's activity across dozens of chains at once, and (via GraphQL) ask far more precise questions than a single-chain explorer allows.

## When to use
You have a `crypto-wallet` address (or want to follow token/DEX activity) and the trail spans multiple chains — the subject moved funds across Ethereum, BSC, Polygon, Solana, Tron, Bitcoin, and others. Bitquery indexes 40+ blockchains behind one interface, so you can see an entity's footprint without hopping between per-chain explorers, and its GraphQL layer lets you filter transfers, trades, and counterparties programmatically for deeper analysis.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://explorer.bitquery.io/ and search an address, transaction, token, or contract.
2. Review the cross-chain activity: transaction history, token-transfer flows, and DEX trades tied to the address.
3. For precise/bulk analysis, use the GraphQL API (create a free account for an API key) to query specific transfers, time windows, or counterparties, or to stream real-time events.
4. Identify counterparties and endpoints (exchanges, bridges, services) that could de-anonymize the owner.
5. Pivot: cross-chain hops feed a fuller entity map; a bridge/exchange endpoint feeds legal process; specific flows feed visual tracing in `[[breadcrumbs-app]]`.

## Inputs → Outputs
- **In:** a `crypto-wallet` address (or token/tx/contract) on any supported chain
- **Out:** cross-chain transaction history, token transfers, DEX trades, and connected `crypto-wallet` counterparties
- **Empty/negative result looks like:** an inactive address, or a chain outside its coverage, returns little/nothing; funds through mixers/bridges fragment the trail — the tool shows what's on-chain, not what privacy tooling hid.

## Gotchas & OpSec
- **API-first depth:** the richest querying is via GraphQL and needs a free key (rate-limited); the no-login web explorer is fine for lookups but limited for heavy analysis.
- Coverage is broad but not universal — confirm a specific chain is indexed before trusting a "no activity" read.
- Cross-reference decisive findings against the chain's native explorer (e.g. `[[etherscan-io]]`), since Bitquery is an indexer atop the same public data.

## Overlaps ("do both")
- Pairs with `[[etherscan-io]]` / `[[blockscan]]` (authoritative per-chain / multichain views) and `[[breadcrumbs-app]]` (visual tracing) — Bitquery's strength is precise cross-chain querying that stitches those single-chain views together.

## Trust & verifiability
`trust: community` — a reputable data provider indexing public ledgers; its output is derived, so verify a critical result against the native chain explorer, which is the ground truth.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bitquery-explorer |
| category | financial-crypto |
| selectorsIn → selectorsOut | crypto-wallet → crypto-wallet |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
