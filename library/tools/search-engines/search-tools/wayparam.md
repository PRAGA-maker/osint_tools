---
id: wayparam
name: wayparam
description: Use when you have a `domain` and want its historical URLs and parameterized endpoints from the Wayback Machine — returns domain endpoints for recon.
url: https://github.com/aleff-github/wayparam
category: search-engines
path:
- search-engines
- search-tools
bestFor: Mining the Internet Archive's Wayback CDX index for a domain's historical URLs and query parameters (a modern ParamSpider-style endpoint harvester).
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free and open-source; pip-installable, no account or key required.
opsec: passive
opsecNote: It queries the Internet Archive's public Wayback CDX API, not the target site, so the domain owner is not contacted or alerted. Purely archive-side reconnaissance.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: A focused open-source recon utility; data comes straight from the Wayback CDX API, so results are only as complete as the Archive's crawl of that domain.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- aleff-github/wayparam
tags:
- wayback
- web-recon
- parameters
source: arf-seed
lastVerified: '2026-07-17'
enrichment: full
---

# wayparam

> A Wayback-CDX harvester that pulls a domain's historical URLs and normalizes their query parameters into fuzzable endpoints.

## When to use
You're profiling a `domain` (in an infrastructure or web-app recon step tied to an investigation) and want the URLs it has exposed over time — especially parameterized endpoints. wayparam queries the Internet Archive's Wayback CDX API, strips static assets, and replaces parameter values with a placeholder (default `FUZZ`), giving a clean list of historical endpoints without ever touching the live site.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install wayparam`.
2. Run against one domain: `wayparam -d example.com` (or a list: `wayparam -l domains.txt`).
3. Add `--include-subdomains` for breadth and `--rps 1` to stay polite; use `--stdout --no-files` to pipe results.
4. Read the output: normalized URLs with masked parameters, written to `results/` or streamed as text/JSONL.
5. Pivot: the recovered endpoints/hostnames map a domain's historical surface — feed hosts into subdomain/WHOIS tooling and archived pages into the Wayback Machine for content.

## Inputs → Outputs
- **In:** a `domain` (or list of domains), optional date range
- **Out:** normalized historical URLs and parameterized `domain` endpoints
- **Empty/negative result looks like:** no archived URLs — the Wayback Machine has little/no crawl of that domain, not that the site had no endpoints.

## Gotchas & OpSec
- Coverage is bounded by the **Internet Archive's crawl** of the domain; sparsely-archived sites yield little.
- Output is historical, so endpoints may be dead now — useful for recon, not a live-site map.
- It's a web-app/infra recon tool; its missing-persons relevance is indirect (via a subject's domain).

## Overlaps ("do both")
- Pairs with the Wayback Machine itself and subdomain-enumeration tools — wayparam lists the parameterized URLs, the Wayback UI serves the archived content, subdomain tools widen the host set.

## Trust & verifiability
`trust: community` — a small open-source utility over the public Wayback CDX API; results are archive-sourced and reproducible, so verifiable, but only as complete as the Archive's coverage.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wayparam |
| category | search-engines |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
