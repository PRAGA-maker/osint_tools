---
id: orbit
name: Orbit
description: Use when you have a Bitcoin `crypto-wallet` address and want to map the wallets it transacts with as a graph — returns `crypto-wallet`, `associate`.
url: https://github.com/s0md3v/Orbit
category: financial-crypto
path:
- financial-crypto
- bitcoin
bestFor: Recursively crawling a Bitcoin address's transaction network and visualising related wallets as a graph.
selectorsIn:
- crypto-wallet
selectorsOut:
- crypto-wallet
- associate
status: live
pricing: free
costNote: Free and open-source (Python CLI); you run it yourself, so no cost beyond your own compute.
opsec: active
opsecNote: Orbit queries public blockchain data over the network from your machine, so your IP hits those endpoints — route through a VPN/sock-puppet. The graph file you generate reveals your investigation's scope, so store and share it carefully.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: A popular open-source tool by a well-known author (s0md3v, ~600+ stars); functional and widely used, but wallet clustering is heuristic — links are leads, not proof of shared ownership.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- photon
- striker
- zen
- zen-github-com
aliases:
- s0md3v/Orbit
tags:
- bitcoin
- blockchain
- graph-analysis
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# Orbit

> A Python CLI that recursively crawls a Bitcoin address's transaction history and renders the wallet network as an interactive graph — turning one `crypto-wallet` into a map of who it moves funds with.

## When to use
You have a Bitcoin `crypto-wallet` address tied to your subject (from a ransom note, a donation page, a marketplace, a scam report) and you want to see the wallets it transacts with and how funds flow. Orbit expands outward level-by-level, so you can spot hubs, exchanges, and clusters that suggest the same actor or their counterparties. Relevant to a missing-persons or fraud case where a Bitcoin address is a lead and you need to identify associated wallets to pivot toward a cash-out point or a known service.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `git clone https://github.com/s0md3v/Orbit && cd Orbit && pip install -r requirements.txt` (Python 3).
2. Run against a seed address: `python3 orbit.py -s <bitcoin_address>`.
3. Tune the crawl: `-d` depth (default 3), `-l` transaction limit per wallet (default 50), `-t` top-N wallets per level, `-o` output format (GraphML/JSON).
4. Read the output: it opens an interactive graph (`quark.html`) — nodes are wallets, edges are fund flows; dense hubs are often exchanges/mixers.
5. Pivot: feed high-value related wallets into a blockchain explorer / attribution service to check for exchange or known-entity labels, which is where a wallet can tie back to a real identity.

## Inputs → Outputs
- **In:** `crypto-wallet` (one or more comma-separated Bitcoin addresses)
- **Out:** `crypto-wallet` (related addresses), `associate` (transacting counterparties as graph nodes)
- **Empty/negative result looks like:** a graph with only the seed node and a couple of edges — the address has few transactions or you set depth/limits too low; increase `-d`/`-l` or confirm the address is actually used.

## Gotchas & OpSec
- Human-in-the-loop: none, but large depth/limit values explode the graph and the request count — start small.
- OpSec: **active** — queries originate from your host against blockchain data endpoints; use a VPN and don't run from an attributable IP. The output graph leaks your investigative scope; protect it.
- Heuristic clustering: a shared edge means a transaction, not shared ownership. Do not assert two wallets are the same person from the graph alone — corroborate with an attribution service.

## Overlaps ("do both")
- Pairs with blockchain explorers and wallet-attribution/labelling services — Orbit reveals the *shape* of the network fast, while a labelled explorer tells you *which* nodes are exchanges or known entities. Do both to turn a cluster into a cash-out lead.

## Trust & verifiability
`trust: community` — a widely-used open-source tool from a reputable author; reliable for graphing public on-chain data, but its wallet relationships are inferential leads to verify, not ownership proof.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | orbit |
| category | financial-crypto |
| selectorsIn → selectorsOut | crypto-wallet → crypto-wallet, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
