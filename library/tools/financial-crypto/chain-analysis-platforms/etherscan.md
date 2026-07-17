---
id: etherscan
name: Etherscan
description: Use when you have a `crypto-wallet` (Ethereum address), transaction hash, or contract address and want to trace balances, transfers, and counterparties — returns crypto-wallet links and associate leads.
url: https://etherscan.io/
category: financial-crypto
path:
- financial-crypto
- chain-analysis-platforms
bestFor: Tracing Ethereum/EVM wallet activity, token holdings, and transaction counterparties.
selectorsIn:
- crypto-wallet
selectorsOut:
- crypto-wallet
- associate
status: live
pricing: freemium
costNote: Web explorer and public API are free with rate limits; a free API key raises limits, paid API tiers add throughput. No payment needed for interactive lookups.
opsec: passive
opsecNote: Reads a public blockchain via Etherscan's servers; you never touch the target's wallet, and the subject gets no notification. Etherscan sees your IP/API key, so use a clean IP for sensitive work. Nothing you do here is visible on-chain.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Etherscan is the de-facto reference Ethereum block explorer; on-chain data is verifiable against the ledger itself.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- etherscan-io
- etherscan-nft-tracker
aliases:
- etherscan.io
- Ethereum block explorer
tags:
- crypto
- blockchain
- ethereum
- chain-analysis
source: arf-seed
lastVerified: '2026-07-17'
enrichment: full
---

# Etherscan

> The reference Ethereum/EVM block explorer, used to turn a wallet address into a full history of who paid whom, when, and in what token.

## When to use
You have a `crypto-wallet` (an Ethereum `0x…` address) tied to a subject — from a ransom note, a marketplace listing, a donation page, a leaked profile — and you want to see its balance, transaction history, and the addresses it interacts with. Counterparty addresses become new `crypto-wallet` selectors, and exchange-deposit addresses are the pivot toward a subpoena-able identity.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://etherscan.io/ and paste the `0x…` address (or a transaction hash / contract address) into the search bar.
2. On the address page read: current ETH balance, total sent/received, and the **Transactions** tab for a timestamped ledger of counterparties.
3. Check the **Token Transfers (ERC-20 / ERC-721)** tabs to see stablecoin/NFT movement, which often reveals more activity than raw ETH.
4. Click any counterparty address to recurse; addresses labeled with an exchange name (e.g. "Binance", "Coinbase") are custodial deposit points — the endpoint where an off-ramp KYC identity may exist.
5. For bulk work, request a free API key (Account → API Keys) and query `https://api.etherscan.io/api?module=account&action=txlist&address=0x…`.

## Inputs → Outputs
- **In:** `crypto-wallet` (Ethereum address), transaction hash, or contract address
- **Out:** `crypto-wallet` counterparties, `associate` leads (repeated counterparties, exchange deposit addresses), balances, token holdings, timestamps
- **Empty/negative result looks like:** "There are no matching entries" / zero transactions — a valid but unused (or freshly generated) address, or you are on the wrong EVM chain (try Polygonscan, BscScan, Arbiscan for the same address).

## Gotchas & OpSec
- Etherscan only indexes Ethereum mainnet; the same address may be active on other EVM chains — check the sister explorers before concluding it is dormant.
- Exchange/mixer labels are Etherscan's own tagging and are not exhaustive; absence of a label is not proof funds never touched an exchange.
- OpSec: fully **passive** — blockchain reads generate no alert to the wallet owner. Your only exposure is to Etherscan (IP/API key); use a clean session for sensitive investigations.

## Overlaps ("do both")
- Pairs with `[[etherscan-nft-tracker]]` for NFT-centric pivots and `[[etherscan-io]]` as the same-provider suite — run the address through all so token and NFT activity aren't missed alongside raw ETH transfers.

## Trust & verifiability
`trust: trusted` — Etherscan mirrors the public Ethereum ledger, and any figure it shows can be independently re-derived from a node, so the underlying data is authoritative.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | etherscan |
| category | financial-crypto |
| selectorsIn → selectorsOut | crypto-wallet → crypto-wallet, associate |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
