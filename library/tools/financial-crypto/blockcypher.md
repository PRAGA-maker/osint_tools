---
id: blockcypher
name: Blockcypher
description: Use when you have a `crypto-wallet` address or transaction hash and want to trace it — returns balances, transaction history, and linked `crypto-wallet` addresses.
url: https://live.blockcypher.com/
category: financial-crypto
path:
- financial-crypto
bestFor: Exploring Bitcoin/Ethereum/Litecoin/Dogecoin addresses and transactions in a web block explorer.
selectorsIn:
- crypto-wallet
- document-id
selectorsOut:
- crypto-wallet
status: live
pricing: freemium
costNote: The web explorer is free with no account; the developer API is freemium (free tier with rate limits, paid tiers for higher volume).
opsec: passive
opsecNote: Passive — blockchain data is public and you query BlockCypher's index, not the wallet owner, so no signal reaches the target. Your lookups are logged by BlockCypher; use a puppet session if the address under investigation is sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Established blockchain-infrastructure provider; the explorer reflects on-chain data, which is independently verifiable against the public ledgers.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- BlockCypher
- live.blockcypher.com
tags:
- blockchain-explorer
- crypto
- bitcoin
source: osint4all
lastVerified: '2026-07-28'
enrichment: full
---

# Blockcypher

> A multi-chain block explorer (Bitcoin, Ethereum, Litecoin, Dogecoin, and testnets) — look up any address or transaction and trace the flow of funds.

## When to use
You have a `crypto-wallet` address or a transaction hash (`document-id`) — from a ransom note, a scam report, a marketplace, a donation page — and want to see its balance, its transaction history, and the counterpart addresses it has sent to or received from. Following those counterparts is the core of crypto tracing.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://live.blockcypher.com/ and pick the chain (BTC, ETH, LTC, DOGE).
2. Paste the `crypto-wallet` address or transaction hash into the search box.
3. Read the results: current/total balance, number of transactions, and each transaction's inputs/outputs.
4. Follow the money: click counterpart addresses to walk the graph forward/backward; note clustering (multiple inputs in one tx usually share an owner).
5. Pivot: repeated counterpart addresses feed exchange-attribution and clustering tools; a tx timestamp anchors an event in time.

## Inputs → Outputs
- **In:** `crypto-wallet` address or transaction hash (`document-id`)
- **Out:** balances, transaction history, and linked counterpart `crypto-wallet` addresses
- **Empty/negative result looks like:** a valid-but-empty address (zero balance, no transactions) — real but unused; an invalid string returns no result at all.

## Gotchas & OpSec
- Explorers show *addresses*, not identities — attribution to a person requires off-chain data (exchange KYC, leaks, forum posts).
- Only the chains BlockCypher supports; for others (Monero, most tokens) use a chain-specific explorer.
- Free API tiers are rate-limited — for bulk tracing, plan around quotas or use another explorer to cross-check.
- Address clustering heuristics are probabilistic; don't treat co-spending as certain shared ownership without corroboration.

## Overlaps ("do both")
- Pairs with dedicated crypto-attribution/clustering tools — BlockCypher gives the raw transaction graph, while attribution services label addresses with known exchanges/entities.

## Trust & verifiability
`trust: trusted` — reflects public on-chain data that anyone can independently verify against the ledger; the explorer itself is a reliable, long-standing service.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | blockcypher |
| category | financial-crypto |
| selectorsIn → selectorsOut | crypto-wallet, document-id → crypto-wallet |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
