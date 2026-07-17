---
id: bitref
name: BitRef
description: Use when you have a Bitcoin `crypto-wallet` address and want its balance and transaction history — returns balance, tx history, and linked-address leads.
url: https://bitref.com/
category: financial-crypto
path:
- financial-crypto
- bitcoin
bestFor: Quick Bitcoin address balance and transaction lookup, plus watch-address monitoring, from a clean web interface.
selectorsIn:
- crypto-wallet
selectorsOut:
- crypto-wallet
status: live
pricing: freemium
costNote: Free to look up any address, transaction, or block; no account needed. Optional paid/watch features exist but aren't required.
opsec: passive
opsecNote: The blockchain is public; querying an address via BitRef reveals nothing to the wallet's owner. BitRef sees the address you look up and your IP — use a clean browser/VPN if you don't want the lookup linked to you.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-standing Bitcoin balance/explorer service; data is derived from the public blockchain and cross-checkable against any other explorer.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- BitRef
- bitref.com
tags: []
source: arf-seed
lastVerified: '2026-07-17'
enrichment: full
---

# BitRef

> A no-frills Bitcoin explorer — paste an address to see its live balance and full transaction history, and optionally watch it for new activity.

## When to use
You have a Bitcoin `crypto-wallet` address (from a ransom note, a scam, a marketplace listing, a donation page, or a subject's disclosed wallet) and want to know: how much it holds, whether it's active, and where funds moved. Balance + transaction history is the first step in tracing crypto flows, establishing whether an address is in use, and finding counterparty addresses to follow.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://bitref.com/ and paste the Bitcoin address (also accepts a transaction ID or block hash).
2. Read the current balance, total received/sent, and the transaction list with timestamps and amounts.
3. Click transactions to see input/output addresses — the counterparties funds came from or went to.
4. Optionally "watch" the address to be alerted to new activity.
5. Pivot: counterparty addresses feed further tracing (and clustering tools); a busy address with exchange-linked flows may point to a KYC'd off-ramp to pursue lawfully.

## Inputs → Outputs
- **In:** `crypto-wallet` (Bitcoin address), or a tx ID / block hash
- **Out:** `crypto-wallet` linkage — balance, transaction history, and the counterparty addresses in each transaction.
- **Empty/negative result looks like:** zero balance and no transactions — the address was never used (or you have a typo/wrong network); an unused address isn't evidence of anything.

## Gotchas & OpSec
- Bitcoin only — not Ethereum or other chains; use the right explorer per asset.
- BitRef shows on-chain data but not identity; attributing an address to a person needs off-chain links (exchange KYC, forum posts, reuse).
- For serious tracing, use dedicated clustering/analytics tools; BitRef is the fast first look.
- OpSec: passive; the chain is public, but mask your own IP for sensitive lookups.

## Overlaps ("do both")
- Complements full blockchain analytics and other explorers (Blockchain.com, mempool.space) — BitRef is the quick balance/history check; cross-verify data on a second explorer and cluster with a dedicated tracer.

## Trust & verifiability
`trust: community` — data comes straight from the public Bitcoin blockchain and is verifiable on any other explorer, so the figures are reliable; only the identity attribution is up to you.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bitref |
| category | financial-crypto |
| selectorsIn → selectorsOut | crypto-wallet → crypto-wallet |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
