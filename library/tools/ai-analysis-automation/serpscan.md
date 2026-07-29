---
id: serpscan
name: SerpScan
description: Use when you have a `domain` and want automated dorking + recon (subdomains, endpoints, JS, params) across multiple search engines — returns domain infrastructure and exposed paths.
url: https://github.com/Alaa-abdulridha/SerpScan
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Automated multi-engine dorking and attack-surface recon for a target domain.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: freemium
costNote: The tool is free/open-source, but it needs a SerpAPI key (free tier available) and external CLIs (subfinder, httpx, hakrawler) installed.
opsec: active
opsecNote: Mixed — dorking via SerpAPI is passive (queries search engines), but the crawling/probing tools it drives (httpx, hakrawler) send requests directly to the target's hosts and appear in their logs. Use a research IP and only run against authorised scope.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: unverified
trustNote: Community single-author PHP tool; author states it is "for education purposes only." Depends on third-party CLIs and SerpAPI.
missingPersonsRelevance: low
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: true
relatedTools:
- jsleak
- webosint
aliases:
- Alaa-abdulridha/SerpScan
tags:
- other-tools
- dorking
- recon
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# SerpScan

> A PHP CLI that automates search-engine dorking and attack-surface recon — subdomains, live hosts, JS files, endpoints, params — for a target domain.

## When to use
You have a `domain` (a subject's website or an organisation's) and want an automated sweep: dork it across Google/Bing/Yahoo/Yandex/Baidu via SerpAPI, enumerate subdomains, find live hosts, and crawl for JavaScript files, endpoints, parameters and directories. Infrastructure/attack-surface focused; useful for mapping a domain rather than finding a person directly.

## How to use it (`bestInteractionPattern`: cli)
1. Install PHP plus the external tools it orchestrates: subfinder, httpx, hakrawler. Get a SerpAPI key (free tier) — the human-in-the-loop gate.
2. Run against one domain: `php start.php -d target.com -t html` (or `-w domains.txt` for a batch; `-t json` for JSON).
3. Let it dork, enumerate subdomains, probe live hosts and crawl endpoints.
4. Read the HTML/JSON report: subdomains, active hosts, JS files, endpoints, params, directories.
5. Pivot: discovered JS files feed `[[jsleak]]`; subdomains/endpoints feed further mapping and manual review.

## Inputs → Outputs
- **In:** `domain` (single or a file of domains)
- **Out:** `domain` — subdomains, live hosts, JS files, endpoints, parameters, directories
- **Empty/negative result looks like:** few/no subdomains or endpoints (small footprint), or errors if SerpAPI quota is exhausted or the external CLIs aren't installed.

## Gotchas & OpSec
- Human-in-the-loop: SerpAPI key required (`api-key`); also depends on subfinder/httpx/hakrawler being present.
- OpSec: **active** — httpx/hakrawler touch the target's hosts; dorking itself is passive. Only run against authorised scope from a research egress.
- Author labels it education-only; as an unaudited orchestrator, verify findings before acting.

## Overlaps ("do both")
- Pairs with `[[jsleak]]` (mine the JS it discovers) and `[[webosint]]` (WHOIS/DNS context) — SerpScan finds the surface, those two go deeper into it.

## Trust & verifiability
`trust: unverified` — a small single-author tool that chains third-party services; corroborate discovered hosts/endpoints directly and respect scope/legality.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | serpscan |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (api-key) |
