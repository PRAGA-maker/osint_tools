---
id: blockchain-info
name: Blockchain.info
description: Use when you have a Bitcoin `crypto-wallet` address or transaction ID and want its balance, history and linked addresses — returns on-chain activity (now via blockchain.com/explorer).
url: https://blockchain.info
category: financial-crypto
path:
- financial-crypto
bestFor: Looking up a Bitcoin address or transaction: balance, inputs/outputs, and transaction graph.
selectorsIn:
- crypto-wallet
selectorsOut:
- crypto-wallet
status: live
pricing: free
costNote: Free public block explorer (blockchain.info now redirects to blockchain.com/explorer); no account needed to browse. A paid data API exists for bulk use.
opsec: passive
opsecNote: You query a public block explorer, not the wallet owner — fully passive, no signal to the subject. Note the explorer operator can log your search terms; use a VPN/Tor for sensitive lookups.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: One of the oldest and most widely-used Bitcoin explorers (Blockchain.com); reflects authoritative on-chain data straight from the ledger.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- blockchain.com explorer
- Blockchain.com
tags:
- financial-crypto
- bitcoin
- blockchain-explorer
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# Blockchain.info

> The classic Bitcoin block explorer (now Blockchain.com/explorer) — resolve an address or txid into balances, transaction history, and the flow of funds.

## When to use
You have a Bitcoin `crypto-wallet` address or a transaction ID surfaced in an investigation (a ransom note, a donation address, a marketplace payment) and want to see its on-chain behaviour: current/total balance, number of transactions, counterparties, and timing. A starting point for tracing funds and clustering related addresses.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://blockchain.info (redirects to https://www.blockchain.com/explorer).
2. Paste the BTC address or transaction hash into the search box.
3. Read the result: balance, total received/sent, and a list of transactions with input/output addresses and timestamps.
4. Pivot: follow input/output `crypto-wallet` addresses to map fund flow; feed addresses into clustering/attribution tools and sanctions/known-address lists.

## Inputs → Outputs
- **In:** BTC `crypto-wallet` address or transaction ID
- **Out:** balance, transaction history, and linked `crypto-wallet` addresses (fund flow)
- **Empty/negative result looks like:** "address not found" / zero transactions — the address has never been used on-chain, or you have a non-BTC/typo'd address (this explorer is Bitcoin-centric).

## Gotchas & OpSec
- Bitcoin-focused; for Ethereum/other chains use the relevant explorer (Etherscan, etc.).
- On-chain data is pseudonymous — an address is not an identity until you attribute it via off-chain data (exchange KYC, leaks, forum posts).
- The explorer can log your queries; use a VPN/Tor for sensitive traces.

## Overlaps ("do both")
- Pairs with address-attribution and clustering services — this shows the raw on-chain activity; those add owner/entity labels and risk scoring.

## Trust & verifiability
`trust: trusted` — a long-established explorer reading directly from the Bitcoin ledger, so the transaction data is authoritative; only the *attribution* of addresses to people requires external corroboration.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | blockchain-info |
| category | financial-crypto |
| selectorsIn → selectorsOut | crypto-wallet → crypto-wallet |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
