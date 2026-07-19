---
id: opensea
name: OpenSea
description: Use when you have a `crypto-wallet` address and want its NFT holdings and trading history — returns the wallet's owned/created NFTs, transfers, sales, and offers across multiple chains.
url: https://opensea.io/
category: financial-crypto
path:
- financial-crypto
- nft-provenance
bestFor: Viewing a wallet's NFT collection and trade history, and tracing NFT provenance between wallets.
selectorsIn:
- crypto-wallet
selectorsOut:
- crypto-wallet
- associate
status: live
pricing: freemium
costNote: Free to browse wallets, collections, and transaction/offer history without an account. Buying/selling needs a connected wallet; viewing does not.
opsec: passive
opsecNote: Browsing a wallet's public activity is passive — the owner isn't notified. Do NOT connect your own wallet when investigating (that links your identity to OpenSea and can leak your address); just view the public profile/URL.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: OpenSea is the largest, established NFT marketplace; on-chain data it surfaces is verifiable against the blockchain, so the trading history is authoritative (usernames/profiles are self-set).
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- opensea.io
- OpenSea NFT
tags:
- nft
- crypto
- provenance
- blockchain
source: arf-seed
lastVerified: '2026-07-19'
enrichment: full
---

# OpenSea

> The largest NFT marketplace — view a wallet's NFT holdings and trade history, and follow provenance from wallet to wallet.

## When to use
You have a `crypto-wallet` address (or an OpenSea username/ENS) tied to a subject and you want to see their NFT activity: what they own, what they created/minted, what they bought and sold, to whom, and when. NFT trades are public and on-chain, so this exposes counterparties (other wallets = potential `associate` leads), a timeline of activity, and links between wallets that suggest common ownership or transfers of value.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://opensea.io/ and go to the wallet's profile — `opensea.io/<address or ENS or username>` — **without connecting your own wallet**.
2. Review the tabs: Collected (holdings), Created (minted), Activity (transfers, sales, listings, offers) with dates and prices.
3. Follow counterparties in the Activity log — the wallet that bought/sold to your subject is a lead; recurring counterparties suggest a relationship or a second wallet of the same person.
4. Cross-check any on-chain claim against a block explorer (`[[etherscan]]`), since OpenSea usernames/avatars are self-chosen and not identity.
5. Pivot: counterparty wallets → further wallet tracing; an ENS name → ENS/social lookups; a mint/purchase timestamp → timeline.

## Inputs → Outputs
- **In:** `crypto-wallet` (address / ENS / OpenSea username)
- **Out:** NFT holdings, mints, and trade history with counterparties (`crypto-wallet`/`associate`), dates, and prices
- **Empty/negative result looks like:** an empty profile means no NFT activity on chains OpenSea indexes — the wallet may still be active in DeFi/token transfers (check a block explorer) or use a different marketplace; absence here isn't wallet inactivity.

## Gotchas & OpSec
- **Never connect your investigation to your own wallet** — viewing is fully public and passive; connecting links your identity and can expose your address.
- Usernames, avatars, and profile text are self-set and unverified; only the on-chain transfers are authoritative — confirm via a block explorer.
- Wash trading and self-transfers are common in NFTs; a "sale" between two wallets may be the same person moving assets, not a genuine counterparty.

## Overlaps ("do both")
- Pairs with a block explorer (`[[etherscan]]`) and wallet-analytics tools — OpenSea gives the human-readable NFT/marketplace view; the explorer gives the raw, complete on-chain record to verify and extend it.

## Trust & verifiability
`trust: trusted` — OpenSea is the leading NFT marketplace and its trade data reflects on-chain events you can independently verify on a block explorer; treat profile identity fields as unverified self-assertions.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | opensea |
| category | financial-crypto |
| selectorsIn → selectorsOut | crypto-wallet → crypto-wallet, associate |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
