---
id: osint-cryptocurrencies
name: Aware Online — Cryptocurrency OSINT Tools
description: Use when you have a `crypto-wallet`/transaction and want a curated, explained directory of crypto-investigation tools — returns a vetted starting list of explorers and tracing services.
url: https://www.aware-online.com/en/osint-tools/cryptocurrency-tools/
category: financial-crypto
path:
- financial-crypto
bestFor: A curated, briefly-explained directory of cryptocurrency OSINT tools (explorers, tracers, address checkers).
selectorsIn:
- crypto-wallet
selectorsOut:
- crypto-wallet
status: live
pricing: free
costNote: Free resource page from Aware Online (a Dutch OSINT training company); the tools it links have their own pricing.
opsec: passive
opsecNote: Reading the directory is passive. The tools it points to vary — most blockchain lookups are passive (public ledger), but note each linked tool's own OpSec before use.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Maintained by Aware Online, an established OSINT training provider; a curated guide rather than a tool itself, so its value is editorial and its links can age.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Aware Online crypto tools
tags:
- crypto
- tool-directory
- resource-guide
source: osint4all
lastVerified: '2026-07-29'
enrichment: full
---

# Aware Online — Cryptocurrency OSINT Tools

> A curated, explained directory of cryptocurrency-investigation tools — the orientation page to consult before diving into wallet tracing.

## When to use
You're starting a crypto investigation (a `crypto-wallet` address, a suspected scam, a ransom payment) and want a vetted, briefly-explained list of the right tools — block explorers, address-reputation checkers, transaction tracers, exchange identifiers — rather than assembling one blindly. Aware Online's page curates and describes these, so it's a jump-off/reference, not a lookup engine itself.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the Aware Online cryptocurrency-tools page.
2. Read the categorized entries to pick the tool matching your task (explore an address, trace flows, check an address against scam reports).
3. Follow the link to the chosen tool and run your actual `crypto-wallet` lookup there.
4. Pivot: use the directory to move from explorer → tracer → exchange-attribution as your investigation deepens.

## Inputs → Outputs
- **In:** the intent to investigate a `crypto-wallet` (you bring the address to the linked tools)
- **Out:** a curated shortlist of crypto OSINT tools → the linked tools return the actual `crypto-wallet`/flow data
- **Empty/negative result looks like:** a linked tool is dead or moved (link rot) — pick another from the list or search for a current equivalent.

## Gotchas & OpSec
- It's a **directory, not a tool** — it returns no wallet data itself; the work happens in the tools it links.
- Curated pages age: verify a linked tool is still live and free before relying on it.
- **Passive** to read; check each downstream tool's OpSec (most on-chain lookups are safe/public).

## Overlaps ("do both")
- Pairs with `[[blockexplorer]]` and `[[bitcoin-forums-search-engine]]` — this page orients you; those do the on-chain tracing and persona-linking.

## Trust & verifiability
`trust: community` — a reputable training provider's curated guide; reliable as an editorial starting point, with the usual link-rot caveat for any directory.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osint-cryptocurrencies |
