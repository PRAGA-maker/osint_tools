---
id: breadcrumbs-app
name: Breadcrumbs.app
description: Use when you have a `crypto-wallet` address and want to trace fund flows — returns an interactive transaction graph of connected addresses, in/out patterns, and balances.
url: https://www.breadcrumbs.app/
category: financial-crypto
path:
- financial-crypto
- mixer-tracking
bestFor: Visually tracing cryptocurrency fund flows from a wallet address to map connected addresses and follow the money.
selectorsIn:
- crypto-wallet
selectorsOut:
- crypto-wallet
status: live
pricing: freemium
costNote: Free tier (with a free account) allows building and viewing fund-flow graphs; advanced features, larger investigations, monitoring, and attribution data are paid.
opsec: passive
opsecNote: Passive — you analyze public on-chain data, which the wallet owner cannot see you querying. Note that saved/shared investigation graphs live on Breadcrumbs' servers; keep sensitive case graphs private and use a sock-puppet account.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A purpose-built blockchain-analytics platform reading public ledger data; the transaction graph is verifiable against any block explorer, though any attribution labels it adds are the vendor's assessment.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
relatedTools: []
aliases:
- Breadcrumbs
- breadcrumbs.app
tags:
- crypto
- blockchain
- fund-flow
- transaction-tracing
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# Breadcrumbs.app

> A visual blockchain-tracing workbench — paste a wallet address and follow the money across connected addresses on an interactive graph, without the heavyweight cost of enterprise chain-analysis suites.

## When to use
You have a `crypto-wallet` address (Bitcoin, Ethereum, and other supported chains) linked to a subject — a ransom demand, a scam payout, a donation address, an exchange deposit — and you want to see where funds came from and went. Breadcrumbs turns raw transactions into a navigable graph, letting you expand hops, spot clustering, and reach identifiable endpoints (exchanges, services). Valuable in financial-trail work where a wallet is the only handle you have.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register a (sock-puppet) free account at https://www.breadcrumbs.app/.
2. Enter the starting `crypto-wallet` address to seed a graph.
3. Expand incoming/outgoing edges to follow fund flow; the tool suggests related addresses and shows balances and transaction patterns.
4. Look for endpoints that break pseudonymity — deposits to a known exchange or service are where a subpoena/legal process could unmask the owner.
5. Pivot: an exchange-tagged endpoint feeds a legal request; clustered addresses feed further tracing; a reused address feeds cross-case correlation.

## Inputs → Outputs
- **In:** a `crypto-wallet` address
- **Out:** an interactive fund-flow graph — connected `crypto-wallet` addresses, in/out patterns, balances, and (paid) attribution labels
- **Empty/negative result looks like:** a brand-new or unused address shows no transactions; funds routed through a mixer/tumbler fragment the trail so downstream hops stop being meaningfully attributable — that's the tracing limit, not a tool error.

## Gotchas & OpSec
- **Account required:** the free tier needs a login — use a sock puppet; saved graphs sit on Breadcrumbs' servers, so keep sensitive investigations private.
- **Free-tier limits:** depth of tracing, monitoring, and attribution data are gated; the free graph is enough to scope a trail but not to run a large investigation.
- Attribution labels are the vendor's assessment — verify a claimed exchange/entity before acting on it; the raw transactions themselves are checkable on any block explorer.
- Mixers/privacy coins deliberately break the graph — treat a trail that enters a tumbler as lost, not merely hidden.

## Overlaps ("do both")
- Complements a plain block explorer and other chain-analysis tools — Breadcrumbs makes the relationships visual and navigable, while an explorer confirms each individual transaction independently.

## Trust & verifiability
`trust: community` — it reads public ledger data, so every edge in the graph is independently verifiable on-chain; only the value-added attribution labels rely on the vendor's own data and warrant corroboration.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | breadcrumbs-app |
| category | financial-crypto |
| selectorsIn → selectorsOut | crypto-wallet → crypto-wallet |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
