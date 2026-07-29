---
id: wallet-labels
name: Wallet Labels
description: Use when you have a `crypto-wallet` address and want a human-readable label (exchange, whale, scammer, DAO, contract) for it — returns entity labels across major chains.
url: https://www.walletlabels.xyz/
category: financial-crypto
path:
- financial-crypto
bestFor: Attaching a known identity/category label to an on-chain wallet address.
selectorsIn:
- crypto-wallet
selectorsOut:
- crypto-wallet
- employer-org
status: degraded
pricing: freemium
costNote: Free-tier lookups planned (advertised ~1,000/month, no card); a paid API is "coming soon."
opsec: passive
opsecNote: Querying a label database does not touch the wallet owner or the blockchain, so nothing is alerted. It is a public-address lookup — still use a research browser/VPN for sensitive cases.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Early open-beta project with a hand-verified but currently very small label set (a handful of wallets at time of check); treat coverage as minimal and any label as a lead to corroborate.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- walletlabels.xyz
tags:
- Cryptocurrencies
- crypto-wallet
- attribution
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# Wallet Labels

> A hand-verified database of on-chain wallet identities — resolves a raw address into a human-readable label (exchange, DeFi protocol, whale, DAO, scammer, NFT contract) across several chains.

## When to use
You have a `crypto-wallet` address from a transaction trail and want to know *what* it is — a known exchange deposit address, a scam wallet, a team/VC wallet, a contract — so you can interpret the money flow around a subject. Note: this is an early open-beta with a **very small** label set right now, so expect most addresses to be unlabelled.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.walletlabels.xyz/ and browse or search the labelled-wallet database.
2. Enter or look up your address (Ethereum, Bitcoin, Solana, BNB, Arbitrum, Base, Polygon are in scope).
3. Read the label and category if present.
4. Because coverage is sparse, cross-check against a fuller labels source (block explorers' known-address tags, Arkham, Etherscan labels) before concluding.
5. Pivot: an exchange label points you toward a KYC-subpoena avenue; a scam/DAO label reframes the transaction's meaning.

## Inputs → Outputs
- **In:** `crypto-wallet` address
- **Out:** entity label / category (often an `employer-org`-type entity such as an exchange or protocol)
- **Empty/negative result looks like:** no label — common here given the tiny beta dataset; absence is not evidence the address is unknown elsewhere, so check other label sources.

## Gotchas & OpSec
- **Coverage is minimal (open beta)** — this is currently a weak primary source; use it as a supplement, not the authority.
- Labels are human-curated and can be wrong/outdated — corroborate before acting.
- OpSec: **passive**; a database lookup that touches neither the chain nor the owner.

## Overlaps ("do both")
- Do both with block-explorer address tags and larger attribution platforms (Etherscan labels, Arkham-class tools), which currently have far broader coverage.

## Trust & verifiability
`trust: unverified` — early-stage, small hand-curated set; every label should be independently confirmed against on-chain behaviour and a second labels source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wallet-labels |
| category | financial-crypto |
| selectorsIn → selectorsOut | crypto-wallet → crypto-wallet, employer-org |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
