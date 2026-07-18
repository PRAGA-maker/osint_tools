---
id: blockonomics
name: Blockonomics
description: Use when you have a Bitcoin `crypto-wallet` address and want its balance and transaction history — returns balance, transactions, and counterparty `crypto-wallet` addresses.
url: https://www.blockonomics.co/
category: financial-crypto
path:
- financial-crypto
- bitcoin
bestFor: Looking up a Bitcoin address's balance and transaction history (and optional monitoring/alerts).
selectorsIn:
- crypto-wallet
selectorsOut:
- crypto-wallet
status: live
pricing: freemium
costNote: Free web block explorer and basic address lookups; the merchant/payment API and monitoring features need an API key (and are paid at volume).
opsec: passive
opsecNote: Passive — you read the public Bitcoin blockchain; the wallet owner is not notified. Basic lookups need no account; the monitoring/webhook features require an API key, so those tie activity to your account.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: An established Bitcoin payment/explorer service; block-explorer data is the public chain (authoritative), while its higher-level features are a commercial product.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- blockchain-explorer
- blockchair
aliases:
- blockonomics.co
tags:
- bitcoin
- blockchain
- crypto
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# Blockonomics

> A Bitcoin block explorer and payment service — look up any BTC address's balance and transaction history, or set up monitoring/alerts on it.

## When to use
You have a Bitcoin `crypto-wallet` address tied to a subject (from a ransom note, a donation page, a marketplace, a leaked profile) and want to see its balance, activity, and the addresses it transacts with. Beyond one-off lookups, you can register the address for balance/transaction alerts to watch it going forward — useful for tracking whether a wallet is still active.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.blockonomics.co/ and use the block explorer (or the search box) with the BTC `crypto-wallet` address.
2. Review the address page: current balance, full transaction list, and the counterparty addresses on each transaction.
3. Follow counterparty `crypto-wallet` addresses to extend the transaction graph.
4. (Optional) With an API key, configure webhook/email monitoring to get alerts on future activity for the address.
5. Pivot: clustered addresses and exchange-linked transactions can, with additional tools, move toward attribution.

## Inputs → Outputs
- **In:** a Bitcoin `crypto-wallet` address.
- **Out:** balance, transaction history, and counterparty `crypto-wallet` addresses (plus optional alerts).
- **Empty/negative result looks like:** an address with zero balance and no transactions — meaning it was never used (or only just created), not an error.

## Gotchas & OpSec
- Bitcoin only: for other chains use their respective explorers.
- Pseudonymity: addresses aren't identities — attribution needs exchange/KYC or self-disclosure links.
- Feature split: explorer lookups are free/no-account; monitoring/webhooks need an API key.
- OpSec: reading the chain is passive and never alerts the owner.

## Overlaps ("do both")
- Pairs with `[[blockchair]]` and other BTC explorers — cross-check balances/history and use whichever offers better clustering/labels for a given address.

## Trust & verifiability
`trust: community` — a commercial service, but its explorer reflects the public Bitcoin blockchain, so the on-chain facts are authoritative; only address-to-person attribution is uncertain.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | blockonomics |
| category | financial-crypto |
| selectorsIn → selectorsOut | crypto-wallet → crypto-wallet |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
