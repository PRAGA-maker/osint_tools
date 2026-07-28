---
id: duckduckgo-bangs
name: DuckDuckGo !bangs
description: Use when you want to jump a query straight into a specific site's search from one box — thousands of !shortcuts (e.g. !g, !w, !gh) that route to site-scoped searches.
url: https://duckduckgo.com/bang
category: search-engines
path:
- search-engines
bestFor: Routing a single query directly into a chosen site's search engine via a short !bang prefix.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free; core feature of DuckDuckGo search. No account. A browser extension can add bang buttons/menus, but bangs work natively in the DDG search box or address bar.
opsec: passive
opsecNote: A bang just rewrites your query into another site's search URL and redirects you there — that destination site then sees your request as normal. DuckDuckGo processes the query to route it. Passive; use a sock-puppet browser/VPN if the destination search is sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A first-party DuckDuckGo feature; the bang redirect list is maintained by DDG and widely used.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- DDG bangs
- '!bang'
tags:
- search
- shortcuts
- duckduckgo
source: cyb-detective
lastVerified: '2026-07-28'
enrichment: full
relatedTools:
- duckduckgo
- duckduckgo-ai-chat
- duckduckgo-com
---

# DuckDuckGo !bangs

> Thousands of `!shortcut` prefixes that fire your query straight into a specific site's own search — the fastest way to pivot one selector across many platforms from a single box.

## When to use
You have a `name`, `username`, `email` or keyword and want to run it through many sites' native search quickly, without visiting each one and finding its search box. Prefix the query with a bang (`!` + code) and DuckDuckGo redirects you to that site's search results. In OSINT this makes cross-platform pivoting fast: `!tw`, `!gh`, `!li`, `!yt`, `!archive`, `!whois`, and thousands more route the same selector into Twitter/X, GitHub, LinkedIn, YouTube, the Wayback Machine, WHOIS, etc.

## How to use it (`bestInteractionPattern`: web-manual)
1. In the DuckDuckGo search box (or your browser's address bar if DDG is default), type a bang + your query, e.g. `!gh someusername`.
2. DuckDuckGo redirects you to that site's search results for the query.
3. Browse the full list of bangs at https://duckduckgo.com/bang to find site-specific ones (registries, code hosts, social nets, archives).
4. Chain the same selector through several bangs to sweep platforms quickly.
5. Pivot: a hit (a matching `social-profile`, repo, or record) becomes the next lead; optionally add the bang-buttons browser extension for one-click routing.

## Inputs → Outputs
- **In:** any query — `name`, `username`, `email`, keyword — with a `!bang` prefix
- **Out:** the destination site's search results (e.g. a matching `social-profile`, repo, archived page)
- **Empty/negative result looks like:** the destination site returns no results, or an unknown bang falls back to a normal DDG search — check the bang code at the bang list.

## Gotchas & OpSec
- OpSec: the destination site sees your query normally once redirected — sock-puppet/VPN if that matters.
- A wrong/unknown bang silently degrades to a plain search; verify the code for niche sites.
- Bangs only reach a site's *public* search; login-gated results still need an account on that site.

## Overlaps ("do both")
- Complements dedicated username-enumeration tools — bangs are the fast manual sweep across specific sites; enumeration tools automate breadth. Do both: bangs for targeted platforms, an enumerator for the long tail.

## Trust & verifiability
`trust: trusted` — a first-party DuckDuckGo feature; it simply redirects to real site searches, so results are as trustworthy as the destination site.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | duckduckgo-bangs |
| category | search-engines |
| selectorsIn → selectorsOut | name, username → social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
