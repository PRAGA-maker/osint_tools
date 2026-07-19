---
id: bitcoin-org
name: bitcoin.org
description: Use when you need a vetted jumping-off directory of Bitcoin block explorers, mempool/on-chain analysis tools, and learning resources — returns links to the actual tracing tools, not lookups itself.
url: https://bitcoin.org/en/resources
category: financial-crypto
path:
- financial-crypto
bestFor: Finding trustworthy starting-point tools (block explorers, mempool.space, on-chain analytics, glossaries) when beginning a Bitcoin investigation.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: The page and everything it links are free/open-source; bitcoin.org is community-funded and asks only for donations.
opsec: passive
opsecNote: This is a static resource-directory page — reading it discloses nothing about a target. The tools it links to (e.g. block explorers) have their own OpSec considerations; treat those separately.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: bitcoin.org is a long-standing community-maintained educational hub (historically the reference site for the Bitcoin project); it is a curated link directory, not a data source, so trust flows to the tools it points at.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- bitcoin.org resources
tags:
- cryptosites
- CryptoCurrency Related Sites
- directory
source: uk-osint
lastVerified: '2026-07-19'
enrichment: full
---

# bitcoin.org

> A curated directory of Bitcoin resources — the front door to the block explorers and on-chain tools you'll actually trace wallets with.

## When to use
You are starting a Bitcoin angle on a case (a `crypto-wallet` address surfaced, or a subject is tied to crypto) and want a vetted list of the real investigative tools — block explorers, mempool viewers, on-chain analytics — rather than guessing at random sites. This page is a *signpost*: it doesn't look anything up, it tells you which tools to open next.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://bitcoin.org/en/resources.
2. Skim the sections — **Charts & Tools** (block explorers, mempool.space, CheckOnChain), **Learning Resources** (Learn Me A Bitcoin, Bitcoin Wiki), **Developer Resources**.
3. Click through to the explorer/analytics tool you need and run the actual address lookup there.
4. Use the Learning Resources to decode unfamiliar terms (UTXO, change address, coinjoin) before interpreting transaction graphs.
5. Pivot: paste your `crypto-wallet` address into a linked explorer (or a dedicated library entry like `[[blockchain-com-explorer]]`) to see balances and transaction flows.

## Inputs → Outputs
- **In:** none (it's a directory — you bring the intent, not a selector)
- **Out:** links to block explorers, mempool/on-chain analysis tools, and reference material
- **Empty/negative result looks like:** the page never "fails," but it also never returns wallet data itself — if you expected a lookup, you're on the wrong tool; follow one of its links instead.

## Gotchas & OpSec
- Human-in-the-loop: none for the page itself.
- This is a gateway, not an analyzer — don't record "checked bitcoin.org" as having traced anything; log the explorer you actually used.
- Vet each linked third-party tool's own trust/OpSec before submitting an address to it.

## Overlaps ("do both")
- Feeds into any block-explorer entry in the library (e.g. `[[blockchain-com-explorer]]`, `[[mempool-space]]`) — bitcoin.org points you there, those do the actual `crypto-wallet` tracing.

## Trust & verifiability
`trust: community` — bitcoin.org is a well-known community-maintained educational site; because it only curates links, its usefulness depends on independently vetting each tool it recommends before relying on that tool's output.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bitcoin-org |
| category | financial-crypto |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
