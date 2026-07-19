---
id: arkham-intelligence
name: Arkham Intelligence
description: Use when you have a `crypto-wallet` or entity `name` and want labelled entity mapping and fund-flow analysis — returns entity profiles, address labels, counterparties and transaction graphs.
url: https://intel.arkm.com/
category: financial-crypto
path:
- financial-crypto
- mixer-tracking
bestFor: De-anonymising and mapping crypto activity — turning an address or entity name into labelled owners, counterparties, and visual fund-flow graphs.
selectorsIn:
- crypto-wallet
- name
selectorsOut:
- crypto-wallet
- associate
- employer-org
status: live
pricing: freemium
costNote: Free to create an account and use the core Explorer (entity profiles, labels, transaction graphs); advanced/enterprise features and higher API limits are paid.
opsec: active
opsecNote: Requires registration, so your queries are tied to an account — use a sock-puppet email/identity. Searching an address on Arkham does not notify the wallet owner, but Arkham logs what you look up; keep case-linked searches on a dedicated account.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A widely used crypto-intelligence platform with government/institutional adoption; its entity labels blend algorithmic attribution and human input, so high-confidence labels are strong leads but should be corroborated on-chain before you rely on them.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
aliases:
- Arkham
- intel.arkm.com
tags:
- crypto
- blockchain-analysis
- entity-mapping
source: arf-seed
lastVerified: '2026-07-19'
enrichment: full
---

# Arkham Intelligence

> A crypto-intelligence Explorer that attaches real-world entity labels to blockchain addresses and visualises fund flows — one of the strongest free tools for turning a `crypto-wallet` into named owners and counterparties.

## When to use
You are tracing a `crypto-wallet` (BTC, ETH, and many chains) or investigating a named entity/exchange and want to know who is behind an address, which exchange deposit addresses funds reach, and who the counterparties are. Arkham's labelled entity graph can convert a bare address into an exchange, service, or named individual/organisation, and its visualiser maps the flow between them — invaluable when following stolen/laundered funds or linking a wallet to a person or business.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register a (sock-puppet) account at https://intel.arkm.com/ and open the Explorer.
2. Search the `crypto-wallet` address or an entity `name`.
3. Read the entity profile: attached labels, associated addresses, balances, and known real-world identity if attributed.
4. Use the visualiser to trace fund flow to/from counterparties — watch for exchange deposit addresses (which can be subpoenaed) and mixer entries.
5. Note the confidence/source of each label; corroborate high-value attributions directly on-chain.
6. Pivot: an exchange deposit address → legal-process lead; named `associate`/`employer-org` counterparties → conventional OSINT on those identities.

## Inputs → Outputs
- **In:** `crypto-wallet` address or entity `name`
- **Out:** labelled entity profiles, associated addresses, `associate`/counterparty and `employer-org` (exchange/service) mapping, transaction-flow graphs
- **Empty/negative result looks like:** an address with no labels and only raw transactions — attribution unknown (common for fresh or privacy-conscious wallets). Absence of a label is not proof of anything; keep tracing counterparties.

## Gotchas & OpSec
- Labels mix algorithmic and crowd/human attribution and can be wrong — treat them as leads and verify on-chain before acting.
- Registration ties queries to you; use a dedicated sock-puppet account for case work.
- Free tier covers the Explorer; heavy API/advanced use is paid.

## Overlaps ("do both")
- Pairs with block explorers and other analytics (e.g. mixer-tracking tools) — Arkham's labels/graphs orient the investigation, while raw explorers let you verify every hop independently.

## Trust & verifiability
`trust: community` — a reputable, institutionally adopted platform, but attribution labels are probabilistic; corroborate any identity-critical label with the underlying on-chain evidence.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | arkham-intelligence |
| category | financial-crypto |
| selectorsIn → selectorsOut | crypto-wallet, name → crypto-wallet, associate, employer-org |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
