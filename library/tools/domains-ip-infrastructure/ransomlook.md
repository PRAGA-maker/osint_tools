---
id: ransomlook
name: RansomLook
description: Use when you have an `employer-org`/`domain` and want to know if it appears as a ransomware victim, or want to profile a ransomware group — returns victim listings, leak-site posts, ransom notes and crypto-wallet indicators.
url: https://www.ransomlook.io/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Checking whether an organisation has been named on a ransomware leak site, and tracking ransomware groups, markets and their crypto wallets.
selectorsIn:
- employer-org
- domain
selectorsOut:
- employer-org
- domain
- crypto-wallet
status: live
pricing: free
costNote: Free and open-source; a public API (Swagger) is available for programmatic access.
opsec: passive
opsecNote: You query RansomLook's own aggregated index, so you never visit the actual (often .onion) leak sites yourself — a big OpSec win. Your queries are seen by RansomLook only.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Well-regarded open-source ransomware tracker, live since 2022, indexing 500+ groups. It mirrors what leak sites claim; victim listings are the actors' assertions, not verified fact.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- ransomlook.io
tags:
- Domain/IP/Links
- Databases of domains
- ransomware
source: cyb-detective
lastVerified: '2026-07-28'
enrichment: full
---

# RansomLook

> An open-source ransomware-intelligence aggregator — search whether an organisation appears on any leak site, and profile the groups, markets and crypto wallets behind them, all without touching the .onion sites yourself.

## When to use
You have an `employer-org` or `domain` and want to know if it has been claimed as a ransomware victim, or you're profiling a ransomware group/market. RansomLook pulls together leak-site posts, ransom notes and associated `crypto-wallet` addresses into one searchable, clearnet index. Peripheral to missing-persons work; core for cybercrime/infrastructure investigations and for safely reading what would otherwise require dark-web access.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.ransomlook.io/.
2. Search for the target `employer-org`/`domain`, or browse by group/market.
3. Read the matched entries: which group posted the victim, dates, sample data claims, ransom notes.
4. Note associated `crypto-wallet` addresses for chain-analysis pivots.
5. For automation, use the Swagger API at `/doc/`.

## Inputs → Outputs
- **In:** `employer-org` / `domain` (victim search) or a group name
- **Out:** victim listings, leak-site posts, ransom notes, and `crypto-wallet` addresses → chain-analysis and group-attribution pivots
- **Empty/negative result looks like:** no hits for an org — it hasn't been publicly named by a tracked group (not proof it wasn't breached). Absence of a wallet just means none was captured for that entry.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: **passive** — you read RansomLook's mirror, never the actor's .onion site. This is the safe way to consume leak-site intel.
- Victim claims are the attackers' assertions and can be false, inflated, or recycled; treat as leads, corroborate before reporting.

## Overlaps ("do both")
- Feed captured `crypto-wallet` addresses into a blockchain-explorer/chain-analysis tool, and cross-check victim claims against breach-notification and news sources.

## Trust & verifiability
`trust: community` — a respected open-source tracker; reliable as an index of what leak sites publish, but the underlying victim claims originate with the threat actors, not with RansomLook.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ransomlook |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | employer-org, domain → employer-org, domain, crypto-wallet |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
