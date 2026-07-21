---
id: bitinfocharts-com
name: bitinfocharts.com
description: Use when you have a `crypto-wallet` address (or a name/exchange label) and want its balance, transaction activity, wealth rank, and public owner tags — returns crypto-wallet intelligence across 13 major coins.
url: https://bitinfocharts.com/
category: financial-crypto
path:
- financial-crypto
bestFor: Looking up a crypto address's balance/history and reading community-submitted owner tags, plus rich-list ranking.
selectorsIn:
- crypto-wallet
- name
selectorsOut:
- crypto-wallet
status: live
pricing: free
costNote: Free explorer, charts, rich lists, and address monitoring; no account required for lookups.
opsec: passive
opsecNote: Blockchain data is public and queries hit bitinfocharts, not the wallet owner — nothing alerts the subject. Do NOT add a public tag/comment to an address you're investigating; that is active and would tip off anyone watching the address.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A long-running third-party analytics site; on-chain figures are reliable, but the crowd-sourced address "tags/comments" are user-submitted and must be corroborated.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- BitInfoCharts
- bitinfocharts explorer
tags:
- cryptosites
- CryptoCurrency Related Sites
- blockchain-explorer
- rich-list
source: uk-osint
lastVerified: '2026-07-21'
enrichment: full
---

# bitinfocharts.com

> A multi-coin blockchain explorer with rich lists and crowd-sourced address tags — turns a wallet address into balance, activity, wealth ranking, and any public owner attribution.

## When to use
You have a `crypto-wallet` address tied to a subject (from a ransom note, a profile, a paste, a scam report) and want to characterize it: how much it holds, how active it is, where it ranks among top holders, and whether the community has publicly tagged it as belonging to an exchange, service, or named individual. Also useful in reverse — browsing rich lists or searching a `name`/label to find addresses others have attributed to an exchange or entity.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://bitinfocharts.com and pick the coin (BTC, ETH, XRP, LTC, BCH, DOGE, XMR-note, DASH, ZEC, ETC, BSV, BTG, VTC).
2. Paste the `crypto-wallet` address into the explorer, or open the coin's **rich list** to browse top holders.
3. Read the address page: current balance, first/last activity, transaction count, and the **tags/comments** section where users attribute addresses to exchanges, services, or people.
4. Pivot: an exchange tag tells you where to send a legal request; a first-seen date anchors a timeline; counterparties in the transaction history are `crypto-wallet` leads for graph analysis in a dedicated tracer.

## Inputs → Outputs
- **In:** `crypto-wallet` address (or a `name`/label to search attributions)
- **Out:** `crypto-wallet` intelligence — balance, activity, wealth rank, counterparties, and public owner tags
- **Empty/negative result looks like:** an address with zero/near-zero balance and no tags — real but uncharacterized. No tag is not proof of anonymity, just that no one has publicly attributed it.

## Gotchas & OpSec
- Coverage is the 13 listed chains only; other coins/tokens aren't here. Privacy coins like Monero expose little on-chain by design.
- The tags/comments are user-submitted — treat an "owner" label as a lead to verify, not fact; adversaries can plant misleading tags.
- OpSec: passive for lookups. Never post a tag/comment on a target address.

## Overlaps ("do both")
- Pairs with dedicated tracing tools (e.g. block explorers per chain, and clustering/attribution services) — bitinfocharts is fast for balance/tags/rich-list, while a tracer follows the money graph and clusters related addresses.

## Trust & verifiability
`trust: unverified` — the on-chain metrics are sourced from the public ledger and are dependable, but the site is a third-party aggregator and its crowd-sourced attributions are not authoritative. Verify owner claims against primary evidence before acting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bitinfocharts-com |
| category | financial-crypto |
| selectorsIn → selectorsOut | crypto-wallet, name → crypto-wallet |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
