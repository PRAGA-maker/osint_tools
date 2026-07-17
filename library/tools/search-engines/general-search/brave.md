---
id: brave
name: Brave Search
description: Use when you have a `name`, `username` or `domain` and want an independent web index that returns different results than Google — returns `domain`, `social-profile` and page links.
url: https://search.brave.com/
category: search-engines
path:
- search-engines
- general-search
bestFor: A privacy-respecting general search with its own index and custom "Goggles" re-ranking, to catch pages Google/Bing miss.
selectorsIn:
- name
- username
- domain
selectorsOut:
- domain
- social-profile
status: live
pricing: free
costNote: Free to search in the browser with no account. An independent API exists with a free tier (limited monthly queries) and paid plans for volume.
opsec: passive
opsecNote: You query Brave, not the subject; the subject sees nothing. Brave markets no-profile/low-retention search, but the operator still sees your query and IP — use a clean browser/VPN for sensitive queries.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Brave Software on its own crawler/index (not a Google/Bing reseller), so it is an independent corroborating source.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- brave-browser
aliases:
- Brave
- search.brave.com
tags:
- general-search
source: arf-seed
lastVerified: '2026-07-17'
enrichment: full
---

# Brave Search

> A general web search engine with its own independent index and user-defined "Goggles" re-ranking — valuable in OSINT precisely because it surfaces a different result set than the Google/Bing duopoly.

## When to use
You have a `name`, `username`, `email` or `domain` and want a second, independent index over the same query. Because Brave crawls the web itself rather than reselling Google/Bing, it frequently ranks different pages first — a person's forum post, a small business page, a leaked profile — that the mainstream engines bury or omit. Reach for it whenever a Google/Bing search feels incomplete or you want to corroborate a finding against an independent crawler.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://search.brave.com/.
2. Enter the selector; use quotes for exact phrases and operators like `site:` and `intitle:` (supported).
3. Optionally apply a **Goggle** (a shareable re-ranking rule set) to bias results toward, say, personal blogs or forums and away from SEO farms.
4. Read results: look for `domain`s and `social-profile` links absent from your mainstream-engine run.
5. Pivot: open new pages and extract fresh `username`/`email`/`name` selectors for downstream lookups. For automation, use the Brave Search API's free tier.

## Inputs → Outputs
- **In:** `name`, `username`, `domain` (free-text query)
- **Out:** `domain`, `social-profile` and general page links
- **Empty/negative result looks like:** few or no results where a mainstream engine had many — Brave's index is smaller, so absence here is not absence on the web. Cross-check before concluding.

## Gotchas & OpSec
- OpSec: **passive** — nothing reaches the subject.
- Index is independent but smaller than Google's; use it *alongside* mainstream engines, not instead of them.
- Goggles change ranking, not the underlying index; a page not crawled by Brave cannot be surfaced by any Goggle.

## Overlaps ("do both")
- Pairs with mainstream general-search and with `[[million-short]]` — each independent index exposes pages the others rank away.

## Trust & verifiability
`trust: trusted` — a first-party independent engine from a known operator. Results point to primary pages; verify claims on the destination itself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | brave |
| category | search-engines |
| selectorsIn → selectorsOut | name, username, domain → domain, social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
