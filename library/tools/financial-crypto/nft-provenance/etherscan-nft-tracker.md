---
id: etherscan-nft-tracker
name: Etherscan NFT Tracker
description: Use when you have a `crypto-wallet` address or NFT contract and want its Ethereum NFT transfers and holdings — returns counterparty `crypto-wallet` addresses and collection activity.
url: https://etherscan.io/nft
category: financial-crypto
path:
- financial-crypto
- nft-provenance
bestFor: Tracing NFT transfers, holdings, and mint/trade history for an Ethereum address or collection.
selectorsIn:
- crypto-wallet
selectorsOut:
- crypto-wallet
status: live
pricing: freemium
costNote: Free to browse in the web explorer; programmatic access needs a free Etherscan API key (rate-limited free tier).
opsec: passive
opsecNote: Passive — you read the public Ethereum ledger via Etherscan; the wallet owner is not notified and on-chain reads leave no trace on the target. Etherscan sees your web/API requests; use a clean session for sensitive investigations.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party Etherscan explorer view; the underlying data is the public Ethereum blockchain, so it is authoritative for on-chain facts.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- etherscan
- etherscan-io
aliases:
- Etherscan NFT
- Etherscan NFT transfers
tags:
- ethereum
- nft
- blockchain
- crypto
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# Etherscan NFT Tracker

> The NFT lens of Etherscan's block explorer — see which NFTs a wallet holds and traded, and follow the transfer trail between addresses.

## When to use
You have a `crypto-wallet` address (or a specific NFT contract) tied to a subject and want the NFT side of their on-chain activity: what collections they hold, what they minted or traded, and the counterparty addresses. Useful for building a financial/behavioral picture and for pivoting a wallet to other wallets, marketplaces, or an ENS/social handle that a subject has publicly linked to their address.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://etherscan.io/nft (top NFTs) or paste a wallet address into Etherscan's main search and select the **NFT Transfers** / **ERC-721/1155** tab on the address page.
2. Review the wallet's NFT holdings and its chronological transfer log: mints, buys, sells, and transfers with timestamps and counterparties.
3. Click through a transfer to see the sending/receiving `crypto-wallet` addresses and the transaction; click a collection to see holders and volume.
4. Pivot: counterparty wallets extend the graph; a wallet often resolves to an ENS name or a marketplace profile that a subject has tied to a `username` / `social-profile`.

## Inputs → Outputs
- **In:** `crypto-wallet` address (or NFT contract address / collection).
- **Out:** NFT holdings and transfer history, plus counterparty `crypto-wallet` addresses, timestamps, and collection stats.
- **Empty/negative result looks like:** an address with no ERC-721/1155 activity (no NFT transfers) — meaning the wallet simply hasn't touched NFTs, not that it's inactive overall.

## Gotchas & OpSec
- Ethereum L1 only: this covers Ethereum mainnet; NFTs on Polygon, Solana, etc. need the equivalent explorer for that chain.
- Pseudonymity: addresses aren't identities — attribution requires linking the wallet to an ENS name, exchange KYC, or a self-disclosed handle.
- Rate limits/API: heavy or automated pulls need a free API key and respect its limits.
- OpSec: passive; reading the chain never alerts the wallet owner.

## Overlaps ("do both")
- Pairs with `[[etherscan]]` / `[[etherscan-io]]` — those give the full token/transaction view of the same address, while this focuses on the NFT holdings and provenance trail.

## Trust & verifiability
`trust: trusted` — Etherscan is the first-party Ethereum explorer and the data is the public blockchain itself, so on-chain facts are authoritative; only the *attribution* of an address to a person is uncertain.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | etherscan-nft-tracker |
| category | financial-crypto |
| selectorsIn → selectorsOut | crypto-wallet → crypto-wallet |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
