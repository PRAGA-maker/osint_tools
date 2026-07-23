---
id: go-dork
name: go-dork
description: Use when you have a `domain` (or a dork query) and want to automate Google/Bing/etc. dorking from the CLI — returns matching URLs and `domain`s (exposed files, panels, indexed pages) fast.
url: https://github.com/dwisiswant0/go-dork
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Fast CLI automation of search-engine dorks across Google/Bing/DuckDuckGo/Yahoo/Shodan.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free and open source (Go); install via `go install`. No account, though heavy use benefits from proxies/API keys.
opsec: passive
opsecNote: Dorks query the search engines, not the target, so the target site sees nothing — but the search engines see your queries and will throw CAPTCHAs/blocks on volume. Route through proxies and pace requests.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Open-source tool from a well-known researcher (dwisiswant0); auditable Go source, widely used in recon workflows.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- apkleaks
aliases:
- dwisiswant0/go-dork
tags:
- Domain/IP/Links
- Dorks/Pentest/Vulnerabilities
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# go-dork

> A fast Go CLI for search-engine dorking: run advanced `site:`/`inurl:`/`filetype:` queries across Google, Bing, DuckDuckGo, Yahoo and Shodan and get the matching URLs back in bulk.

## When to use
You want to surface a `domain`'s exposed footprint through search operators — indexed config/backup files, login panels, directory listings, leaked documents, subdomains in the index — without hand-typing dorks into a browser. go-dork automates the queries and paginates results, making it the scripting layer for reconnaissance dorking against a target site or across the web.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `go install dw1.io/go-dork@latest` (per the repo).
2. Run a dork, e.g. `go-dork -q 'site:example.com ext:sql'` or `go-dork -q 'inurl:admin' -e google,bing -p 5`.
3. Choose the engine(s) with `-e`, pages with `-p`, and add a proxy with `-x` to avoid blocks.
4. Read the returned URLs/`domain`s.
5. Pivot: exposed files/endpoints feed manual review; discovered subdomains feed further web recon; leaked documents feed metadata analysis.

## Inputs → Outputs
- **In:** a dork query (often scoped to a `domain` with `site:`)
- **Out:** matching URLs / `domain`s from the chosen search engines
- **Empty/negative result looks like:** few/no results — commonly a rate-limit/CAPTCHA block rather than a truly empty index. Slow down, add proxies, or switch engines and retry.

## Gotchas & OpSec
- Search engines aggressively CAPTCHA/block automated dorking; without proxies and pacing you'll get throttled and see false "empty" results.
- Aggressive dorking of a specific target is a recon signal to the *search engine*, not the target site — but stay within legal/authorized bounds.
- OpSec: passive toward the target; use proxies to distribute queries and avoid your own IP being blocked.

## Overlaps ("do both")
- Pairs with `[[apkleaks]]` and manual Google dorking — go-dork automates broad discovery, then you drill into the exposed artifacts (APKs, files, panels) with specialized tools.

## Trust & verifiability
`trust: community` — open-source and from a reputable researcher; results come straight from the search engines, so they're verifiable by re-running the same dork manually.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | go-dork |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
