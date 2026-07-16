---
id: blockchair
name: Blockchair
description: Use when you have a `crypto-wallet` address or transaction hash and want its full history across many blockchains — returns transaction, balance and counterparty leads.
url: https://blockchair.com/
category: financial-crypto
path:
- financial-crypto
- chain-analysis-platforms
bestFor: Multi-chain block explorer and search for tracing a wallet's balance, transactions, and counterparties across 20+ blockchains.
selectorsIn:
- crypto-wallet
selectorsOut:
- crypto-wallet
- document-id
status: live
pricing: freemium
costNote: Free web explorer and search across Bitcoin, Ethereum, and 20+ chains; no account needed. Bulk data, exports, and heavy API use are paid.
opsec: passive
opsecNote: Blockchain data is public; querying an address does not alert its owner. Blockchair is reachable over Tor and requires no login, so you can research addresses without tying the lookup to yourself — still use Tor/VPN for sensitive tracing.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Well-established multi-chain explorer widely used in crypto investigations; on-chain data it shows is authoritative because it comes from the blockchains themselves.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- blockchair.com
tags:
- crypto
- blockchain-explorer
- transaction-tracing
source: arf-seed
lastVerified: '2026-07-16'
enrichment: full
relatedTools:
- bitcoin-explorer
- blockchair-com
- zcash-block-explorer
---

# Blockchair

> A privacy-friendly, multi-chain block explorer: search a wallet address, transaction hash, or block across 20+ blockchains and read its full on-chain history.

## When to use
You have a `crypto-wallet` address or a transaction hash tied to a subject — from a ransom demand, a marketplace listing, a donation link, or a breach — and want to trace it. Blockchair shows the address's balance, every transaction, and the counterparty addresses it interacted with, across Bitcoin, Ethereum, and many other chains from one interface. Those counterparty addresses and exchange-deposit patterns are the leads that push an investigation toward attribution.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://blockchair.com/ (also reachable over Tor).
2. Paste the `crypto-wallet` address, transaction hash, or block into search; pick the right chain if prompted.
3. Read the address page: current/historic balance, full transaction list, and counterparties (senders/receivers).
4. Use the advanced/SQL-like query and filters to slice by amount, date, or tag; follow flows to/from known exchange or service clusters.
5. Pivot: counterparty addresses → further tracing; a deposit to a known exchange address → a potential KYC subpoena point; transaction `document-id`s → timeline corroboration.

## Inputs → Outputs
- **In:** `crypto-wallet` address, transaction hash, or block (multi-chain)
- **Out:** balance/transaction history, counterparty `crypto-wallet` addresses, and transaction hashes (`document-id`).
- **Empty/negative result looks like:** an address with zero transactions / not found on the selected chain — it was never used, or you're on the wrong blockchain; re-check the chain and address format.

## Gotchas & OpSec
- On-chain data shows *addresses*, not identities — attribution requires linking an address to an exchange/KYC event or off-chain leak, not the explorer alone.
- Make sure you're querying the correct chain; the same-looking string can be valid on multiple networks.
- Mixers, privacy coins, and CoinJoin break naive "follow the money" — flag but don't overclaim through them.

## Overlaps ("do both")
- Pairs with `[[bitcoin-explorer]]` and other chain explorers, plus address-attribution/tagging services — Blockchair gives the raw multi-chain history, attribution tools add known-entity labels.

## Trust & verifiability
`trust: trusted` — a mature, widely used explorer; the on-chain data it displays is authoritative (straight from the blockchains), while any behavioural interpretation is yours to verify.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | blockchair |
| category | financial-crypto |
| selectorsIn → selectorsOut | crypto-wallet → crypto-wallet, document-id |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
