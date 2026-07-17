---
id: metasleuth
name: MetaSleuth
description: Use when you have a `crypto-wallet` address or tx hash and want to trace fund flows across chains — returns linked `crypto-wallet`s, exchange endpoints and `associate` clusters.
url: https://metasleuth.io/
category: financial-crypto
path:
- financial-crypto
- mixer-tracking
bestFor: Visual cross-chain tracing of crypto fund movements, including mixer entry/exit and wallet clustering.
selectorsIn:
- crypto-wallet
selectorsOut:
- crypto-wallet
- associate
status: live
pricing: freemium
costNote: Free tier ("Get Started for Free") supports interactive tracing on supported chains; advanced features, deeper history and API/compliance tooling are paid. A login is required for full features.
opsec: active
opsecNote: You query a hosted investigation platform tied to your account; your searches are logged by the vendor (BlockSec). The blockchain itself is public, but do the lookups from a research account, not one linked to your identity or the case's principals.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Built by BlockSec, an established blockchain-security firm; widely used by compliance/security teams, and traces are auditable against the public chains.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools: []
aliases:
- MetaSleuth by BlockSec
- metasleuth.io
tags:
- crypto-tracing
- mixer-tracking
- blockchain-forensics
source: arf-seed
lastVerified: '2026-07-17'
enrichment: full
---

# MetaSleuth

> A visual crypto fund-tracing tool (by BlockSec) spanning 11+ chains — follow money from a `crypto-wallet` through hops, mixers and bridges to exchange deposit points, with automatic wallet clustering.

## When to use
You have a cryptocurrency address or transaction hash (from a scam, ransom, extortion, or a subject's disclosed wallet) and need to see where the funds came from or went — across Bitcoin, Ethereum, TRON, Solana, BSC and other supported chains. MetaSleuth draws the flow graph, flags mixer entry/exit and bridges, clusters addresses likely controlled by the same actor, and highlights known exchange/service endpoints where a real identity might be subpoenable. Use it to turn a lone wallet into a network and an off-ramp.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://metasleuth.io/ and sign in (free tier available).
2. Paste the `crypto-wallet` address or tx hash and pick the chain.
3. Explore the interactive graph: follow inbound/outbound hops, expand clustered addresses (`associate` wallets), and note labeled entities (exchanges, mixers, bridges).
4. Identify off-ramps — deposits into a known exchange are the strongest lead toward a real identity (via legal process).
5. Pivot: take exchange endpoints to compliance/subpoena channels; cross-check flows on a block explorer and correlate timing with other evidence.

## Inputs → Outputs
- **In:** `crypto-wallet` address or transaction hash
- **Out:** linked/clustered `crypto-wallet`s (`associate`s), labeled exchange/mixer/bridge endpoints, transaction timeline
- **Empty/negative result looks like:** a wallet with no meaningful flow (fresh/empty), or funds that vanish into a mixer/privacy chain with no traceable exit — tracing legitimately dead-ends there.

## Gotchas & OpSec
- Human-in-the-loop: account login required; the free tier is capped versus paid.
- OpSec: **active** in that queries are logged to your vendor account — keep it research-only.
- Clustering and entity labels are heuristics; a labeled "exchange" or linked wallet is a strong lead, not proof — corroborate on-chain.

## Overlaps ("do both")
- Pairs with block explorers and other tracers (Breadcrumbs, Arkham) — MetaSleuth's graph + clustering complements raw explorer data; cross-tool agreement strengthens a trace.

## Trust & verifiability
`trust: trusted` — from a reputable security firm; every hop it shows is on a public ledger, so a trace is independently verifiable on the corresponding block explorer.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | metasleuth |
| category | financial-crypto |
| selectorsIn → selectorsOut | crypto-wallet → crypto-wallet, associate |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
