---
id: btcbook-guarda-com
name: btcbook.guarda.com
description: Use when you have a Bitcoin `crypto-wallet` address or transaction ID and want its on-chain activity — returns balance, transaction history, and linked `crypto-wallet` addresses.
url: https://btcbook.guarda.com/
category: financial-crypto
path:
- financial-crypto
bestFor: Quick Bitcoin block-explorer lookups — inspect an address's balance, transactions, and counterparties.
selectorsIn:
- crypto-wallet
selectorsOut:
- crypto-wallet
status: live
pricing: free
costNote: Free block explorer operated by Guarda Wallet; no account needed to view chain data.
opsec: passive
opsecNote: Reading the public Bitcoin blockchain is passive and invisible to the address owner. Guarda logs your lookups to their servers, so if the query is sensitive use a clean browser/VPN; consider a self-hosted explorer for maximum privacy.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Explorer run by Guarda (an established non-custodial wallet vendor); chain data itself is authoritative, but it is a commercial front-end with wallet/exchange upsells.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Guarda BTC explorer
- btcbook
tags:
- cryptosites
- bitcoin
- block-explorer
source: uk-osint
lastVerified: '2026-07-19'
enrichment: full
---

# btcbook.guarda.com

> Guarda's Bitcoin block explorer — paste an address or txid to see balance, history, and the addresses it transacted with.

## When to use
You have a Bitcoin `crypto-wallet` address (or a transaction ID) tied to a subject — from a ransom note, a donation page, a marketplace, a breach — and want to see whether it holds funds, how active it is, and which other addresses it moved coins to/from as pivot points.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://btcbook.guarda.com/.
2. Paste the BTC address or transaction hash into the search box.
3. Read the output: current/total balance, number of transactions, and a chronological list of inputs/outputs with counterparty addresses and amounts.
4. Pivot: follow counterparty `crypto-wallet` addresses to map fund flow; cluster/attribute with a dedicated analytics tool and check exchange-linked addresses.

## Inputs → Outputs
- **In:** a Bitcoin `crypto-wallet` address or transaction ID
- **Out:** balance, transaction history, and linked counterparty `crypto-wallet` addresses
- **Empty/negative result looks like:** "address not found" / zero transactions means the address has never appeared on-chain (freshly generated or mistyped) — re-check the string; BTC addresses are case-sensitive.

## Gotchas & OpSec
- Bitcoin-only — it will not resolve Ethereum, Tron, or other chains; use a chain-appropriate explorer for those.
- It shows raw chain data, not identity; attribution to a person requires linking the address to an exchange/KYC event or off-chain leak.
- Human-in-the-loop: none.
- OpSec: passive; only Guarda sees your lookups.

## Overlaps ("do both")
- Do both with a second explorer (e.g. mempool.space/blockchair) — cross-check balances and use the other's richer clustering; explorers occasionally lag or differ on unconfirmed data.

## Trust & verifiability
`trust: community` — the underlying blockchain data is authoritative and independently verifiable on any explorer; treat the vendor's UI as convenience, and confirm critical figures on a second explorer.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | btcbook-guarda-com |
| category | financial-crypto |
| selectorsIn → selectorsOut | crypto-wallet → crypto-wallet |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
