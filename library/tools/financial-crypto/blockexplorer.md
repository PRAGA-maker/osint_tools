---
id: blockexplorer
name: BlockExplorer
description: Use when you have a `crypto-wallet` address or transaction ID and want to trace its on-chain activity — returns balances, transaction history, and linked counterparty `crypto-wallet`s.
url: https://blockexplorer.com/
category: financial-crypto
path:
- financial-crypto
bestFor: Looking up a Bitcoin (and multi-chain) address or transaction to map balances, flows, and counterparties.
selectorsIn:
- crypto-wallet
- document-id
selectorsOut:
- crypto-wallet
- associate
status: live
pricing: free
costNote: Free public block explorer; no account.
opsec: passive
opsecNote: Blockchains are public; querying an address here reveals nothing to its owner and leaves no trace with them. Do the lookup from sock-puppet egress purely to keep it out of your own attributable history — the target cannot see the query.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-standing public block explorer (originally by theymos); it reflects on-chain data faithfully, but attribution of an address to a person is analyst inference, not data the explorer provides.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- blockexplorer.com
tags:
- bellingcat-toolkit
- companies-finance
- blockchain
- crypto
source: bellingcat-toolkit
lastVerified: '2026-07-29'
enrichment: full
---

# BlockExplorer

> A public blockchain explorer — paste a wallet address or transaction ID to read its full on-chain history and follow the money to counterparty addresses.

## When to use
You have a `crypto-wallet` address or a transaction ID (`document-id`) tied to a subject — from a ransom note, a scam listing, a forum signature, a donation page — and want to see its balance, transaction history, and where funds moved. On-chain flows expose counterparties, timing, and cluster relationships that can corroborate or break an attribution.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open blockexplorer.com and paste the address or transaction hash into search (it covers Bitcoin and other major chains).
2. Read the record: current/historical balance, inbound/outbound transactions, timestamps, and the counterparty addresses on each side.
3. Follow high-value or repeated counterparties to build a flow graph; note deposits to known exchange addresses (a lead for a subpoena/attribution).
4. Pivot: counterparty `crypto-wallet`s feed clustering/attribution tools; an exchange-linked deposit feeds legal-process leads; a wallet seen in a forum feeds `[[bitcoin-forums-search-engine]]`.

## Inputs → Outputs
- **In:** `crypto-wallet` address or transaction `document-id`
- **Out:** balance + transaction history, linked counterparty `crypto-wallet`s (`associate` in the money-flow sense)
- **Empty/negative result looks like:** "address not found / 0 transactions" — a valid-but-unused address, a typo, or the wrong chain (verify the address format matches the network).

## Gotchas & OpSec
- **Addresses ≠ identities:** the chain shows flows, not names. Attribution requires off-chain data (exchange KYC, a doxed post); never assert ownership from on-chain data alone.
- Wrong-chain lookups silently return nothing — confirm you're querying the network the address belongs to.
- **Passive**: fully public data; the owner cannot detect your lookup.

## Overlaps ("do both")
- Pairs with `[[bitcoin-forums-search-engine]]` (tie the wallet to a forum persona) and dedicated chain-analytics/clustering tools — the explorer gives raw flows; those add heuristics and known-entity labels for attribution.

## Trust & verifiability
`trust: community` — a faithful mirror of public ledger data; reliable for the transactions themselves, with attribution left to the analyst.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | blockexplorer |
