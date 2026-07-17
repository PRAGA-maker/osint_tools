---
id: start-me
name: start.me
description: Use when you have a `crypto-wallet` or a crypto-investigation goal and want a curated directory of blockchain/crypto OSINT tools — returns pointers to wallet-tracing resources.
url: https://start.me/p/Bnmdyv/crypto-resources
category: financial-crypto
path:
- financial-crypto
bestFor: A curated start.me link hub of cryptocurrency/blockchain OSINT resources — explorers, tracing tools and reference sites — to pick the right tool for a wallet trace.
selectorsIn:
- crypto-wallet
- name
selectorsOut:
- crypto-wallet
status: live
pricing: free
costNote: Free public start.me curated page; no account needed to view.
opsec: passive
opsecNote: A read-only link directory; you view a static curated page, nothing is sent to any subject. The linked tools have their own opsec profiles — check each before use.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community-curated start.me board (not an official index); link quality depends on the curator and links can rot, so treat it as a jumping-off point, not an authority.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- cse-utopia
- geoint
- osint-assassin
- socmint
aliases:
- start.me crypto resources
tags:
- cryptosites
- CryptoCurrency Related Sites
- curated-directory
source: uk-osint
lastVerified: '2026-07-17'
enrichment: full
---

# start.me

> A curated start.me board of cryptocurrency/blockchain OSINT resources — a directory to find the right explorer or tracing tool, not a lookup itself.

## When to use
You're starting a crypto trace (you have a `crypto-wallet`, exchange, or transaction to investigate) and want a hand-picked menu of blockchain explorers, wallet-attribution and tracing tools, and reference material rather than searching blind. Use this board to choose the tool, then run the actual lookup in that tool. It's a resource hub, so it points you at pivots — it doesn't return wallet data on its own.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://start.me/p/Bnmdyv/crypto-resources.
2. Browse the categorized link sections (explorers, address/wallet tracing, exchanges, reference).
3. Pick the tool matching your input — e.g. a chain explorer for the wallet's network, or an attribution service.
4. Open that linked tool and run the real query there.
5. Pivot: feed your `crypto-wallet` into the chosen explorer/tracing tool; bring any attributed identity back into people-search.

## Inputs → Outputs
- **In:** an investigation need (e.g. a `crypto-wallet`/`name` to trace)
- **Out:** curated pointers to crypto OSINT tools that themselves return wallet/transaction intel
- **Empty/negative result looks like:** a link that 404s or a section that doesn't cover your chain — curated boards rot, so verify each link and don't assume the board is exhaustive.

## Gotchas & OpSec
- This is a **directory, not a tool** — it never returns wallet data itself; the value is curation.
- Links decay over time; some entries may be dead or superseded.
- Each linked tool has its own trust/opsec profile — vet them individually before running a trace.

## Overlaps ("do both")
- Pairs with the concrete crypto tools already in this library — use the board to discover, then run the actual explorer/tracer for results.

## Trust & verifiability
`trust: community` — a single curator's start.me board; useful as a starting map of the crypto-OSINT landscape, but confirm each linked tool independently and expect some rot.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | start-me |
| category | financial-crypto |
| selectorsIn → selectorsOut | crypto-wallet, name → crypto-wallet |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
