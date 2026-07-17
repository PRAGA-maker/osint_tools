---
id: xmrchain-net-monero
name: XMRChain.net (Monero)
description: Use when you have a Monero transaction hash or block height (`crypto-wallet`) and want to confirm it on-chain — returns block/tx details (but not sender/receiver).
url: https://xmrchain.net/
category: financial-crypto
path:
- financial-crypto
- privacy-coin-analysis
bestFor: Confirming a Monero transaction exists and reading block/tx metadata on a privacy-respecting explorer.
selectorsIn:
- crypto-wallet
selectorsOut:
- metadata-exif
status: live
pricing: free
costNote: Free, open-source explorer (Onion Monero Blockchain Explorer); no account, and it runs no trackers.
opsec: passive
opsecNote: The explorer sets no cookies, runs no JavaScript/analytics and is reachable over Tor/I2P, so lookups leave a minimal footprint. Nothing you do reaches any counterparty. Note Monero's design means most transaction details are cryptographically hidden.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Runs the well-known open-source Onion Monero Blockchain Explorer; the on-chain data is verifiable, but by design it reveals little about participants.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- xmrchain-net
aliases:
- XMRChain
- xmrchain.net
tags:
- monero
- blockchain-explorer
- privacy-coin
source: arf-seed
lastVerified: '2026-07-17'
enrichment: full
---

# XMRChain.net (Monero)

> A privacy-focused Monero block explorer (no JS, no cookies, no trackers, Tor/I2P reachable) — use it to confirm a Monero transaction or block exists, while understanding Monero hides the things you usually want.

## When to use
You have a Monero transaction hash, block height, or block hash surfaced in an investigation and want to confirm it is real and read what little metadata is public: block time, fee, size, ring size, number of outputs, network stats. Unlike Bitcoin explorers, Monero is designed for privacy — amounts are hidden (RingCT), senders are obscured by ring signatures, and recipients by stealth addresses — so this **confirms existence and timing**, it does not deanonymise participants. Reach for it to timestamp/verify a Monero reference, not to trace funds to a person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://xmrchain.net/ (or its Tor/I2P mirror for extra anonymity).
2. Paste a transaction hash, block height or block hash into search.
3. Read the result: block timestamp (`metadata-exif`-style timing), confirmations, fee, output count and ring details.
4. Understand the limits: you will NOT see a real sender/receiver address or a plaintext amount — that is by Monero's design, not a tool limitation.
5. Pivot: if you also hold a transaction's private view key (e.g. supplied by a counterparty), the "prove/check" tools can confirm a payment to a specific address; otherwise treat Monero as an endpoint, not a trail.

## Inputs → Outputs
- **In:** `crypto-wallet` context — a Monero transaction hash, block height or block hash
- **Out:** `metadata-exif`-style block/tx metadata (timestamp, fee, size, ring size, output count); network statistics
- **Empty/negative result looks like:** "not found" — the hash is wrong/mistyped or not yet mined. A valid tx still shows **no** usable sender/amount; that is expected, not an error.

## Gotchas & OpSec
- OpSec: **passive** and low-footprint (no cookies/JS; Tor/I2P available).
- Fundamental limit: Monero deliberately hides amounts and participants; do not expect address-level tracing from any explorer.
- Timestamps are block times, not exact submission times.

## Overlaps ("do both")
- Pairs with `[[xmrchain-net]]` (same explorer entry) and general crypto tooling — but for privacy coins, confirmation/timing is usually all any explorer can give.

## Trust & verifiability
`trust: community` — an instance of a reputable open-source explorer; on-chain facts are independently verifiable by running your own node/explorer, which the project explicitly encourages.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | xmrchain-net-monero |
| category | financial-crypto |
| selectorsIn → selectorsOut | crypto-wallet → metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
