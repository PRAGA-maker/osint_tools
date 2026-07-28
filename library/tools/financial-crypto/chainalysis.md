---
id: chainalysis
name: Chainalysis
description: Use when you have a `crypto-wallet` address and want to screen it against OFAC/UN/EU sanctions for free — full transaction-tracing (Reactor) is paid enterprise only.
url: https://www.chainalysis.com/free-cryptocurrency-sanctions-screening-tools/
category: financial-crypto
path:
- financial-crypto
bestFor: Free sanctions/OFAC screening of a crypto address; note that Chainalysis's investigation product is paid-only.
selectorsIn:
- crypto-wallet
selectorsOut: []
status: live
pricing: freemium
costNote: The sanctions-screening tools (API + on-chain oracle) are FREE with an API key. The investigative products (Reactor, KYT) are paid enterprise/government only — do not expect free wallet tracing here.
opsec: passive
opsecNote: Screening an address is a passive query against Chainalysis's sanctions data; the wallet owner isn't notified. You submit the address to a commercial provider, so use a sock-puppet API key/account for sensitive work.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: api
trust: trusted
trustNote: Chainalysis is a leading blockchain-analytics firm; its sanctions data draws on OFAC/UN/EU lists. The free tier is screening only — the rich attribution people associate with Chainalysis lives in the paid Reactor product.
missingPersonsRelevance: low
coverage:
- global
auth: api-key
api: true
localInstall: false
registration: true
aliases:
- Chainalysis sanctions screening
- Chainalysis free tools
tags:
- crypto
- sanctions
- screening
source: metaosint
lastVerified: '2026-07-28'
enrichment: full
---

# Chainalysis

> The industry-leading crypto-analytics firm. Its heavyweight tracing tool (Reactor) is paid enterprise/government only — but its **sanctions-screening tools are free**, which is the part an open-source investigator can actually use.

## When to use
You have a `crypto-wallet` address and want to check, for free, whether it is on (or connected to) OFAC/UN/EU sanctions lists — before transacting, or to flag a subject's address. That is what Chainalysis's free sanctions-screening tools do (a REST API for apps and an on-chain oracle for smart contracts). Do **not** come here expecting free graph-tracing of a wallet's flows — that capability is Reactor/KYT, which is paid and gated to enterprise/government. For free tracing, use a block explorer like `[[token-view]]` instead.

## How to use it (`bestInteractionPattern`: api)
1. Register for a free Chainalysis sanctions-screening API key at the free-tools page.
2. Call the screening API with the `crypto-wallet` address (or use the on-chain oracle from a contract).
3. Read the result: whether the address is sanctioned / linked to a sanctioned entity.
4. For a quick one-off, use a public free OFAC crypto-address checker built on the same lists.
5. Pivot: a flagged address feeds sanctions context (`[[sanctionsexplorer]]`); for actual flow-tracing, switch to a free explorer since Reactor is out of reach.

## Inputs → Outputs
- **In:** a `crypto-wallet` address
- **Out:** a sanctions-screening verdict (sanctioned / not) — no free transaction graph or attribution
- **Empty/negative result looks like:** "not sanctioned" — which only means not on the screened lists; it says nothing about other risk, and is not a tracing result.

## Gotchas & OpSec
- Scope trap: the free tier is **screening only**. The wallet-tracing/attribution Chainalysis is famous for is paid Reactor/KYT — don't record this as a free tracing tool.
- OpSec: passive, but you submit addresses to a commercial provider under an API key — sock-puppet it for sensitive cases.
- For free tracing, use block explorers (`[[token-view]]`) and clustering tools; use this purely for sanctions checks.

## Overlaps ("do both")
- Do both with `[[sanctionsexplorer]]` (person/entity sanctions detail) and `[[token-view]]` (free multi-chain tracing) — Chainalysis's free tool answers "is this address sanctioned," the others give the who and the money flow.

## Trust & verifiability
`trust: trusted` — a leading analytics firm using official sanctions data; reliable for screening, but recognise the free/paid boundary so you don't overstate what's available without a contract.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | chainalysis |
| category | financial-crypto |
| selectorsIn → selectorsOut | crypto-wallet → — |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | api |
| opsec | passive |
| human-in-loop | yes (api-key) |
