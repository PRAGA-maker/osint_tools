---
id: ddgr
name: ddgr
description: Use when you want to script or automate DuckDuckGo searches from the terminal — returns search results as text or JSON, with bangs and region control.
url: https://github.com/jarun/ddgr
category: search-engines
path:
- search-engines
bestFor: Command-line DuckDuckGo search with JSON export, bang support, and Tor compatibility.
selectorsIn:
- name
- username
selectorsOut:
- domain
- social-profile
status: live
pricing: free
costNote: Free and open-source (GPL-3.0); `pip3 install ddgr` or via package managers. No account, no API key.
opsec: passive
opsecNote: Searches run from your machine to DuckDuckGo (which doesn't track/personalise like Google), and ddgr works over Tor for extra separation. Your queries still leave your host — use Tor/VPN for sensitive terms.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: trusted
trustNote: Well-known open-source utility by jarun (author of buku/googler); results mirror DuckDuckGo directly.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- DDGR
tags:
- search-engines
- duckduckgo
- cli
- automation
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
relatedTools:
- googler
---

# ddgr

> DuckDuckGo from the command line — script searches, pipe results to JSON, use bangs, and run over Tor, without a browser or API key.

## When to use
You want to automate or batch web searches over a subject's `name`/`username` without Google's tracking/personalisation and without an API key. ddgr returns DuckDuckGo results in the terminal (and JSON), so you can loop dork queries, feed results into scripts, and keep a low, privacy-respecting footprint — including over Tor.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip3 install ddgr` (or a package manager / from source).
2. Search: `ddgr "your query"`; add `--json` for machine-readable output, `-n 25` for more results, `--reg <region>` to set locale, and DuckDuckGo `!bangs` to target a site.
3. Read/parse the results (titles, URLs, snippets).
4. Pivot: result URLs surface `domain`s and `social-profile`s; script repeated queries (e.g. site-scoped dorks) to build a footprint. Route via Tor for sensitive work.

## Inputs → Outputs
- **In:** a search query built from `name`/`username` (+ region/bang options)
- **Out:** result links (`domain`, `social-profile`), snippets — as text or JSON
- **Empty/negative result looks like:** no results returned — the query genuinely matches nothing on DuckDuckGo, or you've been rate-limited (back off / route via Tor).

## Gotchas & OpSec
- DuckDuckGo's index differs from Google's — cross-check with a Google-backed tool (`[[serpapi]]`) for coverage.
- Heavy automated querying can get rate-limited; space requests.
- No API key needed, but it's scraping the HTML endpoint, so occasional breakage is possible.

## Overlaps ("do both")
- Complements `[[serpapi]]` (Google, structured, proxied) and manual dorking — use ddgr for free CLI DuckDuckGo runs; SerpApi when you need Google's index at scale.

## Trust & verifiability
`trust: trusted` — a mature, well-regarded open-source tool; it relays DuckDuckGo's own results, so verify individual hits against the live page when it matters.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ddgr |
| category | search-engines |
| selectorsIn → selectorsOut | name, username → domain, social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
