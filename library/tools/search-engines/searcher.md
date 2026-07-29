---
id: searcher
name: Searcher
description: Use when you have a keyword/`name` and want results from many search engines at once — returns aggregated JSON links from Ask, Bing, Brave, DuckDuckGo, Yahoo, and Yandex.
url: https://github.com/davemolk/searcher
category: search-engines
path:
- search-engines
bestFor: Fast multi-engine search aggregation from the command line, scriptable over a list of queries.
selectorsIn:
- name
- username
selectorsOut:
- domain
- social-profile
status: live
pricing: free
costNote: Free, open-source Go tool; build/run locally, no account or API keys.
opsec: passive
opsecNote: Queries hit the search engines directly from your host, so your IP issues the searches — route through a VPN/proxy for attribution hygiene, and pace requests to avoid engine rate-limiting/CAPTCHAs. No target is contacted.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Open-source Go utility by davemolk; small project, code is readable and self-contained. Scrapes engine result pages, so it can break when an engine changes its HTML.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- searx
- one-liner-osint
aliases:
- davemolk/searcher
tags:
- meta-search
- cli
- scraper
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# Searcher

> A small, fast Go CLI that runs one base query (plus optional add-on terms) across six search engines and returns the merged results as JSON.

## When to use
You want to sweep a `name`, `username`, email, or phrase across multiple search engines quickly and get machine-readable output — for scripting, deduping, or feeding into other tooling. Handy when a single engine's results are thin or filtered, or when you want to batch many queries (a keyword list) at once during subject profiling.

## How to use it (`bestInteractionPattern`: cli)
1. Install Go, then `git clone https://github.com/davemolk/searcher` and build (`go build`), or `go install`.
2. Run with your base query and optional add-on terms; results come from Ask, Bing, Brave, DuckDuckGo, Yahoo, and Yandex.
3. Output is JSON to stdout (and can be saved to file) — pipe into `jq` to extract and dedupe URLs.
4. Read the merged links; cross-engine agreement raises confidence, unique hits from Yandex/Brave often surface what Google-centric searches miss.
5. Pivot: discovered `domain`s and `social-profile` URLs feed WHOIS/DNS and profile-enumeration tools.

## Inputs → Outputs
- **In:** `name` / `username` / keyword (base query + optional add-ons)
- **Out:** aggregated result links (JSON) → candidate `domain`s and `social-profile` URLs
- **Empty/negative result looks like:** empty JSON or errors for an engine — that engine changed its markup or rate-limited/CAPTCHA-blocked you; retry later, slow down, or rely on the engines that returned results.

## Gotchas & OpSec
- It scrapes HTML result pages, so engine layout changes or bot defenses (CAPTCHAs, rate limits) can silently drop an engine's results. Treat coverage as best-effort.
- Your IP runs the queries — use a VPN/proxy and reasonable pacing for OpSec and to avoid blocks.
- No relevance ranking beyond what each engine returns; dedupe and triage yourself.

## Overlaps ("do both")
- Pairs with a hosted metasearch like `[[searx]]` — SearX gives a privacy-respecting web UI across engines; Searcher gives scriptable JSON for batch/automation. Use SearX interactively, Searcher for pipelines.

## Trust & verifiability
`trust: community` — small open-source tool; source is inspectable and self-contained. Because it scrapes, verify important hits directly in the engine, and expect occasional breakage as engines change.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | searcher |
