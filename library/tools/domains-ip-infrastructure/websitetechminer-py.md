---
id: websitetechminer-py
name: WebsiteTechMiner.py
description: Use when you have a `domain` (or a CSV of domains) and want its technology stack from BuiltWith + Wappalyzer in bulk — returns per-domain tech-stack rows; requires your own API keys.
url: https://github.com/cybersader/WebsiteTechMiner-py
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Bulk technographic profiling of one or many domains, pulling BuiltWith + Wappalyzer tech data into a CSV.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: The script is free and open source (MIT-style GitHub project). It calls the BuiltWith and Wappalyzer APIs, which require your own API keys — those services have their own free/paid tiers, so cost depends on your key.
opsec: passive
opsecNote: Detection is fetched via the BuiltWith/Wappalyzer APIs from their databases, so your machine does not crawl the target directly and the target's server sees nothing from you. Your query footprint sits with those API providers under your key — use a dedicated account/key, not one tied to your identity.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: community
trustNote: Small open-source GitHub tool (cybersader); auditable code, but it is a thin wrapper whose data quality is entirely BuiltWith's and Wappalyzer's.
missingPersonsRelevance: low
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: true
aliases:
- WebsiteTechMiner
- WebsiteTechMiner-py
tags:
- website-technology
- tech-stack
- bulk-lookup
- domain-and-ip-research
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# WebsiteTechMiner.py

> A CLI batch profiler: feed it one domain or a CSV of domains and it pulls technology-stack data from BuiltWith and Wappalyzer into a single CSV — bring your own API keys.

## When to use
You have a `domain` — or a whole list of them — and need their technology stacks side by side, for example to cluster a target's properties by shared/unusual technologies or to enrich a set of discovered domains at once. Where a browser checker does one site at a time, this automates the same BuiltWith/Wappalyzer lookups over a CSV, which is the practical way to profile dozens of domains in a pass.

## How to use it (`bestInteractionPattern`: cli)
1. Clone the repo: `git clone https://github.com/cybersader/WebsiteTechMiner-py` and install its Python requirements.
2. Obtain API keys from BuiltWith and Wappalyzer and add them to the tool's JSON config.
3. Single domain: `python WebsiteTechMiner.py -s example.com`. Bulk: point it at a CSV of domains.
4. Read the output CSV — per row: domain, detection source, technology category, technology name, description (`selectorsOut`).

## Inputs → Outputs
- **In:** `domain` (single via `-s`, or many via CSV)
- **Out:** `domain` rows annotated with technology category/name/description from BuiltWith + Wappalyzer
- **Empty/negative result looks like:** blank/error rows when a domain is unreachable or your API key is missing/rate-limited — check key quota rather than assuming the site has no tech.

## Gotchas & OpSec
- Human-in-the-loop: you must register for BuiltWith and Wappalyzer API keys before it runs (`api-key`).
- OpSec: passive toward the target — lookups go through the two APIs' databases, not a direct crawl. Your usage is logged under your API keys, so isolate those from your identity.
- Data quality is inherited: it's only as accurate/current as BuiltWith and Wappalyzer; cross-source disagreements are normal.

## Overlaps ("do both")
- Pairs with browser-based checkers like [[snov-io-technology-checker]] and Wappalyzer/BuiltWith directly — use this for *bulk* runs and the browser tools for one-off checks or when you lack API keys.

## Trust & verifiability
`trust: community` — an open-source wrapper you can audit, but its findings are entirely BuiltWith's and Wappalyzer's; treat conflicting or thin results as an artifact of those upstream sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | websitetechminer-py |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (api-key) |
