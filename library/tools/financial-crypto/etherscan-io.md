---
id: etherscan-io
name: Etherscan
description: Use when you have an Ethereum `crypto-wallet` address and want its full on-chain history — returns balance, every transaction, token holdings, ENS name, and public labels.
url: https://etherscan.io/
category: financial-crypto
path:
- financial-crypto
bestFor: Inspecting any Ethereum address or transaction — balances, complete transfer history, tokens/NFTs, and community/exchange labels.
selectorsIn:
- crypto-wallet
selectorsOut:
- crypto-wallet
- social-profile
status: live
pricing: free
costNote: Free to browse all on-chain data; an optional API key (free tier) is needed only for programmatic access.
opsec: passive
opsecNote: Passive — you read public ledger data; the address owner cannot see you querying. No sock puppet needed for browsing, though an API key ties automated queries to an account.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The canonical, widely-trusted Ethereum block explorer; the raw chain data is authoritative, and it's the reference other Ethereum tools are checked against.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- etherscan
- etherscan-nft-tracker
aliases:
- etherscan.io
- Etherscan Ethereum explorer
tags:
- cryptosites
- CryptoCurrency Related Sites
- ethereum
- block-explorer
source: uk-osint
lastVerified: '2026-07-18'
enrichment: full
---

# Etherscan

> The definitive Ethereum block explorer — paste any address and get its balance, entire transaction history, tokens, NFTs, ENS identity, and any public labels, all free.

## When to use
You have an Ethereum (or EVM-compatible, via sibling explorers) `crypto-wallet` address tied to a subject — a ransom/scam address, a donation wallet, an exchange deposit, an NFT/DeFi account — and want to understand it fully: how much it holds, everywhere the money came from and went, which tokens/NFTs it touches, and whether the community or an exchange has labeled it. It's the starting point for any Ethereum financial trail and often reveals an ENS name or labeled counterparty that breaks pseudonymity.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://etherscan.io/ and paste the address (or a transaction hash / ENS name) into search.
2. Read the address page: ETH balance, transaction list (in/out, counterparties, timestamps), and the Token/NFT holdings tabs.
3. Check the **public name tag / labels** — Etherscan marks known exchanges, contracts, scams, and services; a labeled counterparty (e.g. a Binance deposit) is a pivot to a real-world entity.
4. Follow transactions to counterparties, especially deposits into labeled exchanges where legal process could unmask an owner.
5. Pivot: an ENS name feeds username/social lookups; a labeled exchange endpoint feeds a legal request; recurring counterparties feed clustering/tracing tools like `[[breadcrumbs-app]]`.

## Inputs → Outputs
- **In:** a `crypto-wallet` address (or tx hash / ENS name)
- **Out:** balance, full transaction history, token/NFT holdings, ENS identity, and public labels — potential `social-profile`/entity leads via ENS and tags
- **Empty/negative result looks like:** a fresh/unused address shows zero balance and no transactions; that's a real state, not an error. No label just means no one has tagged it.

## Gotchas & OpSec
- **Ethereum/EVM only:** use the matching explorer for other chains (Etherscan runs many, or use a multichain tool like `[[blockscan]]`).
- Labels are community/vendor-assigned and can be wrong or missing — treat a tag as a lead to verify, not proof.
- Everything is pseudonymous until a transaction touches a KYC'd service; on-chain data alone rarely names a person directly.

## Overlaps ("do both")
- Pairs with `[[breadcrumbs-app]]` (visual multi-hop tracing) and `[[blockscan]]` (cross-chain view) — Etherscan is the authoritative per-transaction record those tools build on.

## Trust & verifiability
`trust: trusted` — the canonical Ethereum explorer; its transaction data is the chain itself and independently verifiable, so it's the reference standard for on-chain investigation.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | etherscan-io |
| category | financial-crypto |
| selectorsIn → selectorsOut | crypto-wallet → crypto-wallet, social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
