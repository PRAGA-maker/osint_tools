---
id: blockchain-explorer
name: Blockchain.com Explorer
description: Use when you have a `crypto-wallet` address or transaction hash and want its full on-chain history — balance, transactions and counterparties — returning linked `crypto-wallet` addresses to pivot on.
url: https://www.blockchain.com/explorer
category: financial-crypto
path:
- financial-crypto
bestFor: Free public lookup of Bitcoin/Ethereum addresses and transactions and their counterparties.
selectorsIn:
- crypto-wallet
selectorsOut:
- crypto-wallet
status: live
pricing: free
costNote: Free public block explorer; no account required to browse addresses, transactions or blocks.
opsec: passive
opsecNote: On-chain data is public; you're reading a ledger, not touching the target. But your queries go to blockchain.com over your IP — use a sock-puppet/VPN so a monitored address lookup isn't tied to you. Never send funds to a target address to "test" it.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: One of the oldest, most-used public block explorers; it renders authoritative on-chain data directly from the blockchain, though it doesn't attribute addresses to real identities.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- Blockchain.com Explorer
- blockchain.info explorer
tags:
- crypto
- bitcoin
- ethereum
- blockchain-explorer
source: osint4all
lastVerified: '2026-07-23'
enrichment: full
relatedTools:
---

# Blockchain.com Explorer

> Classic public block explorer: paste a wallet address or tx hash and read its entire Bitcoin/Ethereum history — balances, flows and counterparties.

## When to use
You have a `crypto-wallet` address (or a transaction hash) surfaced from a scam, ransom note, marketplace, or a subject's posts, and you want to trace it. The explorer shows the address's balance, total received/sent, and every transaction, letting you follow funds to and from other addresses (`crypto-wallet` pivots) and gauge activity level and timing — the starting point for any Bitcoin/Ethereum money-trail.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.blockchain.com/explorer.
2. Choose the chain (Bitcoin / Ethereum) and paste the `crypto-wallet` address or transaction hash into search.
3. Read the address page: current balance, total received/sent, transaction count, and first/last-seen timestamps.
4. Open individual transactions to see input and output addresses — the counterparties to pivot on.
5. Pivot: follow counterparty addresses to map flows; feed high-value/known addresses into attribution/clustering services and sanctions tools to attach identity or risk.

## Inputs → Outputs
- **In:** a `crypto-wallet` address or transaction hash (BTC/ETH)
- **Out:** balance, full transaction history, timestamps, and counterparty `crypto-wallet` addresses
- **Empty/negative result looks like:** "address not found" / zero transactions — the address has never transacted on this chain (or it's on a chain this explorer doesn't cover, e.g. a non-BTC/ETH network); check the correct chain's explorer.

## Gotchas & OpSec
- It shows the ledger, not identities — an address is not a person until you attribute it via clustering/exchange data.
- Only covers the chains it supports (primarily Bitcoin and Ethereum); use the right explorer for other networks.
- OpSec: passive (reading public data), but your lookups hit blockchain.com from your IP — use a sock-puppet/VPN for sensitive addresses and never transact with a target address.

## Overlaps ("do both")
- Pairs with dedicated clustering/attribution services — this explorer gives the raw on-chain trail, while attribution tools try to tie addresses to exchanges or real-world identities.

## Trust & verifiability
`trust: trusted` — a long-standing, widely-used explorer rendering authoritative data straight from the blockchain; the data is reliable, but identity attribution is not something it provides.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | blockchain-explorer |
| category | financial-crypto |
| selectorsIn → selectorsOut | crypto-wallet → crypto-wallet |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
