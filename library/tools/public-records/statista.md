---
id: statista
name: Statista
description: Use when you need statistics/market data on a topic, industry, country or demographic to add context to a case — returns charts, figures and sourced datasets, not person-level records.
url: https://www.statista.com
category: public-records
path:
- public-records
bestFor: Quick sourced statistics and market/industry/demographic figures to contextualise an investigation or report.
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
costNote: Headline figures and many charts are free to view; full datasets, downloads and detailed studies sit behind paid subscription accounts.
opsec: passive
opsecNote: Passive reference reading — you query topics, not a target. No subject data is disclosed. Standard sock-puppet browsing hygiene applies.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Statista (Hamburg); a widely-cited commercial statistics aggregator that attributes underlying sources, though it is a secondary aggregator, not the primary data collector.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Statista.com
tags:
- data-and-statistics
source: awesome-osint
lastVerified: '2026-08-04'
enrichment: full
---

# Statista

> A large commercial statistics portal — background/context data for a report or case, not a source of records about a specific person.

## When to use
You need a sourced statistic or market/industry/demographic figure to frame an investigation or brief — e.g. base rates, industry size, adoption numbers, country demographics. It is contextual reference material; it holds no person-level records and will not identify anyone.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.statista.com and search your topic, industry, or country.
2. Browse the free headline charts/figures; note the cited underlying source shown with each statistic.
3. Where possible, follow that citation to the primary source rather than relying on Statista's aggregation.
4. Detailed datasets, downloads, and full studies require a paid account — treat the free view as a pointer.

## Inputs → Outputs
- **In:** a topic/industry/geography (not a personal selector)
- **Out:** statistics, charts, and cited datasets for context
- **Empty/negative result looks like:** only teaser figures behind a paywall, or no coverage of a niche topic — pivot to the primary statistical agency instead.

## Gotchas & OpSec
- Human-in-the-loop: none for browsing; full data is gated behind a subscription.
- OpSec: passive; nothing about a subject is entered.
- It is a secondary aggregator — always chase the cited primary source before quoting a figure as fact.

## Overlaps ("do both")
- Complements official statistics portals (census bureaus, World Bank): use Statista to find a figure fast, then the primary agency to verify and cite it.

## Trust & verifiability
`trust: trusted` — a reputable, widely-cited aggregator that attributes sources; still a secondary layer, so verify against the primary dataset for anything load-bearing.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | statista |
| category | public-records |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
