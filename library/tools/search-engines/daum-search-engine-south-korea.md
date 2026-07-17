---
id: daum-search-engine-south-korea
name: Daum Search Engine (South Korea)
description: Use when you have a `name`, `username` or Korean-language term and want South-Korean web/forum results Google misses — returns `domain`, `social-profile` and local pages.
url: http://www.daum.net
category: search-engines
path:
- search-engines
bestFor: Searching Korean-language web, news, blogs and cafés (forums) with a domestic index Google under-covers.
selectorsIn:
- name
- username
selectorsOut:
- domain
- social-profile
status: live
pricing: free
costNote: Free to search in the browser; no account needed for web search (a Kakao account is only needed for Daum Café/mail).
opsec: passive
opsecNote: You query a Korean portal, not the subject; nothing reaches them. The operator (Kakao) sees your query/IP — use a clean browser/VPN for sensitive terms, and a Korean IP can surface more localized results.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Major South-Korean portal operated by Kakao; a first-party domestic search index, not a scraper.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Daum
- daum.net
- Kakao Daum
tags:
- toddington
- curated-directory
- search-engines
- korea
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# Daum Search Engine (South Korea)

> One of South Korea's major portals (run by Kakao) with its own domestic index — the way to reach Korean-language blogs, news, and Daum Café forum posts that Google ranks poorly or never crawls.

## When to use
Your subject has a Korean footprint — a Korean `name` (Hangul), a handle used on Korean platforms, or a case that touches Korea — and Western engines return little. Daum indexes the Korean-language web, KakaoStory/blog content and its own Café (forum) communities, so it surfaces local pages, discussions and news that are effectively invisible on Google outside Korea. Use it as the Korean-market counterpart to a general web search.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://www.daum.net and use the search box (results also at search.daum.net).
2. Enter the term — ideally in Hangul; transliterate a romanized name into Korean for far better recall.
3. Work the vertical tabs: 웹(web), 뉴스(news), 블로그(blog), 카페(Café/forum), 이미지(images).
4. Read results for `domain`s and `social-profile`/Café links tied to the subject; a Kakao login is required only to read some Café posts.
5. Pivot: run the same query on Naver (the other big Korean engine) and feed found handles into cross-platform username search.

## Inputs → Outputs
- **In:** `name`, `username` or Korean-language term
- **Out:** `domain`, `social-profile` (blogs, Café posts), local news pages
- **Empty/negative result looks like:** thin results — often because the query was in English/romanized form; retry in Hangul before concluding the subject has no Korean presence.

## Gotchas & OpSec
- OpSec: **passive** — nothing reaches the subject.
- Korean-language queries hugely outperform romanized ones; this is the main failure mode.
- Some Café content is members-only and needs a Kakao account to view.

## Overlaps ("do both")
- Pairs with Naver and general engines — Daum and Naver each dominate different slices of the Korean web, so run both.

## Trust & verifiability
`trust: trusted` — a first-party major-portal index. Results are pointers; verify anything decisive on the destination Korean-language page.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | daum-search-engine-south-korea |
| category | search-engines |
| selectorsIn → selectorsOut | name, username → domain, social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
