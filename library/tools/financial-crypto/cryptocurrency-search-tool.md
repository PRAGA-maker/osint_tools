---
id: cryptocurrency-search-tool
name: Cryptocurrency search tool
description: Use when you have a `crypto-wallet` address (or tx/block id) and want its history and web mentions — returns transaction history, balance, and links to `social-profile`/`name`.
url: https://www.aware-online.com/en/osint-tools/cryptocurrency-search-tool/
category: financial-crypto
path:
- financial-crypto
bestFor: A free hub that turns a crypto address, transaction, or block id into blockchain data plus a surface-web search for that address.
selectorsIn:
- crypto-wallet
selectorsOut:
- crypto-wallet
- social-profile
- name
status: live
pricing: free
costNote: Free tools page from Aware Online Academy; no login. Some buttons redirect you to third-party block explorers to complete the lookup.
opsec: passive
opsecNote: Blockchain queries hit public explorers and are passive toward the wallet owner (they can't see who looked). The "address web search" runs a Google-style search — normal search-engine logging applies, nothing reaches the target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Published by Aware Online, a Dutch OSINT training company; it's a convenience wrapper over public block explorers and search engines rather than a proprietary dataset.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Aware Online cryptocurrency search
- crypto address search
tags:
- cryptocurrency
- blockchain
- wallet-analysis
source: osint4all
lastVerified: '2026-07-28'
enrichment: full
---

# Cryptocurrency search tool

> Aware Online's free crypto page: paste a wallet address, transaction id, or block id and it fetches the on-chain data (history, balance, raw hex/JSON) and runs a surface-web search for the address.

## When to use
You have a `crypto-wallet` address linked to your subject — from a ransom note, a donation page, a marketplace profile, a screenshot — and you want two things at once: its blockchain activity (is it active, what's the balance, who did it transact with) and whether that exact address appears anywhere on the open web (forums, exchange KYC leaks, social posts, tip jars) tied to a `name` or `social-profile`. The web-search side is the OSINT value: an address reused in a public profile can de-anonymise the owner.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.aware-online.com/en/osint-tools/cryptocurrency-search-tool/.
2. Choose the function: **Address history** (balance, transactions, unspent outputs in JSON), **Transaction** (raw hex/JSON by tx id), **Block** (raw block data), or **Address web search**.
3. Paste the `crypto-wallet` address (or tx/block id) and submit — some options redirect you to a public block explorer to show the result.
4. For de-anonymisation, run **Address web search**: it Googles the exact address string across the surface web.
5. Pivot: a web hit tying the address to a handle feeds username/social search; on-chain counterparties feed further wallet-clustering tools.

## Inputs → Outputs
- **In:** `crypto-wallet` address (or transaction / block id)
- **Out:** transaction history + balance, and — from the web search — `social-profile`/`name` mentions of the address
- **Empty/negative result looks like:** a valid-but-empty address (zero balance, no transactions) and no web mentions — the address exists on-chain but isn't publicly attributed to anyone.

## Gotchas & OpSec
- Passive: you're reading public block explorers and running web searches; the wallet owner gets no signal.
- It supports the major chains (BTC, LTC, ETH, DOGE); an address on an unsupported chain won't resolve here.
- The "web search" is only as good as what search engines have indexed — absence of a hit is not proof the address is unattributed.

## Overlaps ("do both")
- Complements dedicated block explorers and clustering services — this is the quick triage/hub; use a full-featured explorer for deep transaction graphing.

## Trust & verifiability
`trust: community` — a training-org convenience tool that wraps authoritative public block explorers and standard search; the on-chain figures are verifiable directly against the explorer it links to.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cryptocurrency-search-tool |
| category | financial-crypto |
| selectorsIn → selectorsOut | crypto-wallet → crypto-wallet, social-profile, name |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
