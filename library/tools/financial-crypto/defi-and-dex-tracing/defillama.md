---
id: defillama
name: DefiLlama
description: Use when you have a `crypto-wallet` or protocol/token name in a DeFi trace and want to understand the platforms, chains and money-flows around it — returns protocol, chain and stablecoin context (not per-person data).
url: https://defillama.com/
category: financial-crypto
path:
- financial-crypto
- defi-and-dex-tracing
bestFor: Identifying which DeFi protocol, chain or bridge a flow of funds is interacting with, and its scale.
selectorsIn:
- crypto-wallet
selectorsOut:
- crypto-wallet
- domain
status: live
pricing: freemium
costNote: Dashboards, charts and the public API are free with no account. A paid "Pro" tier adds custom dashboards, higher API limits and LlamaAI; not needed for investigative use.
opsec: passive
opsecNote: You only read aggregate on-chain analytics; nothing is submitted about your target and the site does not know which wallet you are chasing. Fetching the public API from your own IP is fine, but route through a research VPN if you want to avoid tying analytics traffic to yourself.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Widely used, open-source-backed industry-standard DeFi data aggregator; its TVL/methodology is public and independently sanity-checkable against on-chain data.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- etherscan
- blockchair
- chainalysis
aliases:
- Defi Llama
- llama.fi
tags:
- defi
- tvl
- crypto
- chain-analysis
source: arf-seed
lastVerified: '2026-07-17'
enrichment: full
---

# DefiLlama

> The industry-standard DeFi analytics dashboard — used in a crypto trace to name the protocol/bridge behind a flow and gauge its scale, not to identify a person.

## When to use
You are following a `crypto-wallet` and its transactions touch a contract you don't recognise, or you need to know what a token, DEX, bridge or lending protocol actually is, which chains it spans, and how large/liquid it is. DefiLlama answers "what platform is this and how big is it?" — the context layer that turns raw addresses from `[[etherscan]]`/`[[blockchair]]` into a narrative (e.g. "funds moved into Protocol X's bridge to chain Y"). It does not resolve wallets to people; treat it as protocol/chain intelligence.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://defillama.com/ — no login needed.
2. Search the protocol or token name (or paste a contract address into the search) to reach its page with TVL, chains, and historical charts.
3. Use the section tabs for the specific flow you're tracing:
   - **Bridges** — which bridge moved value cross-chain and its volumes.
   - **Stablecoins** — supply/issuer context for a stablecoin in the flow.
   - **DEXes / Fees** — volumes and revenue for a trading venue.
4. For bulk/repeat work, hit the free public API (`https://api.llama.fi/`) instead of the UI.
5. Pivot: once you know the protocol and chain, go back to `[[etherscan]]` (or the relevant chain explorer) to follow specific transactions, and to `[[chainalysis]]` for attribution.

## Inputs → Outputs
- **In:** `crypto-wallet` / contract address, or a protocol/token name
- **Out:** protocol identity, chains it runs on, TVL/volume scale, associated `domain`s and related contract `crypto-wallet` addresses
- **Empty/negative result looks like:** a brand-new or obscure contract with no DefiLlama listing — absence here means "not a tracked protocol," not that the address is inactive. Confirm activity on the chain explorer.

## Gotchas & OpSec
- This is aggregate/protocol-level data. It will **not** tell you who controls a wallet — do not overstate its output as personal attribution.
- TVL and volumes are estimates that can be gamed by projects; corroborate large claims on-chain.
- Passive and account-free; the site never learns your target.

## Overlaps ("do both")
- Pairs with `[[etherscan]]` and `[[blockchair]]` — those give you the raw transactions and address balances; DefiLlama names and sizes the protocols those transactions interact with.
- Pairs with `[[chainalysis]]` for attribution once the protocol/flow is understood.

## Trust & verifiability
`trust: trusted` — DefiLlama is the most widely cited DeFi aggregator, its adapters/methodology are open, and every headline figure can be re-derived from public on-chain data.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | defillama |
| category | financial-crypto |
| selectorsIn → selectorsOut | crypto-wallet → crypto-wallet, domain |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
