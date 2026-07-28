---
id: duckduckgo-com
name: duckduckgo.com
description: Use when you have a `name`, `username` or any string and want unpersonalised search results and !bang shortcuts to pivot fast — returns `social-profile`, `name` and page leads.
url: https://duckduckgo.com/?t=hc
category: search-engines
path:
- search-engines
bestFor: Privacy-respecting, non-personalised web search with !bang operators for quick cross-site pivots.
selectorsIn:
- name
- username
selectorsOut:
- name
- social-profile
status: live
pricing: free
costNote: Free, no account, no ads-tracking profile; core search plus !bang redirects at no cost.
opsec: passive
opsecNote: DuckDuckGo does not build a personalised profile of you, so results aren't skewed by your history and your searches aren't tied to a persistent identity the way a logged-in Google session is — good hygiene for investigative queries. Searches still traverse your IP/network; use Tor or a VPN for sensitive subjects. Queries reach the target site only when you click a result.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A mainstream, reputable search engine; results come from its own crawl plus Bing, so coverage differs from Google — use it alongside, not instead of, other engines.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- DuckDuckGo
- DDG
tags:
- searchengines
- Search Engines
- privacy
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
relatedTools:
- duckduckgo
- duckduckgo-ai-chat
- duckduckgo-bangs
---

# duckduckgo.com

> A privacy-first search engine whose big OSINT advantages are unpersonalised results and !bang operators — clean, repeatable queries and one-keystroke pivots across sites.

## When to use
You have a `name`, `username`, phrase, or any lead and want to search the open web without your own history skewing the ranking, or you want to jump straight into another site's search via a !bang. Because results aren't personalised, two analysts get the same output — valuable for reproducible investigations. Also a useful second engine, since its index (own crawl + Bing) surfaces pages Google buries.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://duckduckgo.com/ and enter your query; use standard operators (`"exact phrase"`, `site:`, `-exclude`, `filetype:`).
2. Use **!bang** shortcuts to redirect the query into another site: `!tw <name>` (Twitter/X), `!li <name>` (LinkedIn), `!g <query>` (Google), `!wa` (Wayback), etc.
3. Read results for `social-profile` links, confirmed `name` spellings/variants, mentions, and documents.
4. For sensitive subjects, run it over Tor/VPN; DDG's no-personalisation helps but your network still sees traffic.
5. Pivot: profiles feed `[[sherlock]]`/`[[namechk]]`; documents feed metadata analysis; !bang straight into the platform where a hit lives.

## Inputs → Outputs
- **In:** `name`, `username`, phrase, or dork
- **Out:** ranked web results — `social-profile` URLs, `name` mentions, documents, cached pages
- **Empty/negative result looks like:** thin or no results — the subject isn't well-indexed here, or the query is too narrow. Absence in DDG is not absence on the web; re-run on Google/Bing/Yandex.

## Gotchas & OpSec
- Human-in-the-loop: none; occasional anti-bot friction on automated hammering.
- OpSec: **passive** and privacy-respecting (no personalised profile of you), but your IP/network still sees the traffic — add Tor/VPN for sensitive work.
- Coverage differs from Google; use it as one engine among several, never the only one.

## Overlaps ("do both")
- Pairs with `[[google-to-search-profiles-on-twitter]]` and other engines — DDG gives clean, unpersonalised results and fast !bang pivots; Google/Bing/Yandex cover pages DDG misses. Always cross-engine.

## Trust & verifiability
`trust: trusted` — a mainstream engine. It surfaces leads, not verified facts; confirm anything material on the primary source you click through to.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | duckduckgo-com |
| category | search-engines |
| selectorsIn → selectorsOut | name, username → name, social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
