---
id: duckduckgo
name: DuckDuckGo
description: Use when you have a `name`, `username`, or `email` and want web results without a personalized filter bubble or search-history trail — returns ranked web pages and social/profile links.
url: https://duckduckgo.com/
category: search-engines
path:
- search-engines
- general-search
bestFor: Neutral, non-personalized general web search with clean operator support and a privacy-preserving anonymous page view.
selectorsIn:
- name
- username
- email
selectorsOut:
- social-profile
- domain
status: live
pricing: free
costNote: Free; no account required. No paid tier gating results.
opsec: passive
opsecNote: DuckDuckGo does not build a search profile of you and proxies image/result previews, so your queries aren't tied to a personal Google account. Results are still fetched by DDG's servers and your ISP/exit IP sees the connection — use a VPN/sock-puppet browser for a sensitive investigation.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by DuckDuckGo, an established privacy-focused search company; results are syndicated largely from Bing plus its own crawler.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- duckduckgo-ai-chat
- bing
- google
aliases:
- DDG
- duckduckgo.com
tags:
- search-engine
- privacy
source: arf-seed
lastVerified: '2026-07-17'
enrichment: full
---

# DuckDuckGo

> A privacy-preserving general search engine — useful in OSINT precisely because it doesn't personalize, so results aren't skewed by your own history and leave no account-linked trail.

## When to use
You want a clean, non-personalized web search over a `name`, `username`, `email`, or phrase, and you don't want the query tied to a logged-in Google/Bing profile or shaped by your prior searches. Good as a cross-check against Google (different index blend can surface pages Google buries) and for its `!bang` shortcuts that jump straight into other sites' searches.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://duckduckgo.com/ (ideally in a sock-puppet browser / over VPN for sensitive work).
2. Enter the selector. Operators supported: `site:`, `intitle:`, `filetype:`, quotes for exact phrase, `-term` to exclude.
3. Use `!bang` shortcuts to redirect the same query into another engine or site — e.g. `!g` (Google), `!li name` (LinkedIn), `!archive url`.
4. Read results; click the "Anonymous View" (proxy) option to open a page without the destination site seeing your IP.
5. Pivot: profile links → `[[bing]]` / `[[google]]` for corroboration; usernames → dedicated username-search tools.

## Inputs → Outputs
- **In:** `name`, `username`, `email`, or keyword string
- **Out:** ranked web pages, `social-profile` links, `domain` references
- **Empty/negative result looks like:** "No results found" or only generic/unrelated pages — the term is rare or the index doesn't cover it; retry on `[[google]]` or `[[bing]]`, whose indexes differ.

## Gotchas & OpSec
- Results are largely Bing-syndicated, so DDG can miss things Google indexes uniquely — never treat a null on DDG as absence; cross-run on other engines.
- No first-party advanced-search UI as deep as Google's; lean on operators and `!bang`s.
- Passive and privacy-preserving toward the *engine*, but your network path is still visible to your ISP — combine with a VPN for real anonymity.

## Overlaps ("do both")
- Pairs with `[[google]]` and `[[bing]]` — different indexes and ranking; run the same query across all three to maximize coverage.
- Pairs with `[[duckduckgo-ai-chat]]` for a conversational/summarized angle on the same query.

## Trust & verifiability
`trust: trusted` — a well-established privacy-first search company. Results are real search-index hits (mostly Bing-sourced), so verify individual pages as you would any search result, but the engine itself is reputable.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | duckduckgo |
| category | search-engines |
| selectorsIn → selectorsOut | name, username, email → social-profile, domain |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
