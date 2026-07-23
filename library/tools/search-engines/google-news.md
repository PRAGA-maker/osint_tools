---
id: google-news
name: Google News
description: Use when you have a `name`, `employer-org`, or event and want news coverage across thousands of outlets — returns aggregated articles, dates and sources.
url: https://news.google.com
category: search-engines
path:
- search-engines
bestFor: Aggregated news search across global outlets by keyword, entity, or date.
selectorsIn:
- name
- employer-org
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free; no account (personalisation/alerts need a Google login). Supports keyword search and topic feeds.
opsec: passive
opsecNote: Standard search over public news; passive. Logged into Google it personalises and logs your searches — use a sock-puppet/logged-out session for sensitive queries.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Google's news aggregator — reliable as an index of published coverage; the trustworthiness of any individual article is the outlet's, not Google's.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- news.google.com
tags:
- search-engines
- news
- media
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# Google News

> Aggregated news search across thousands of outlets — the fast way to find press coverage of a person, company, or event.

## When to use
You have a `name`, `employer-org`, place, or event and want to know what has been reported: news articles, dates, and which outlets covered it. Useful for building a timeline, finding named associates and quotes, locating a subject in the news, and surfacing local reporting (obituaries, court coverage, missing-person appeals) that people-search tools miss.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://news.google.com and search the `name`/`employer-org`/event; use quotes and operators to tighten.
2. Sort/filter by relevance or recency; open the "Full Coverage" view to see multiple outlets on one story.
3. Read across sources to corroborate and to find named people, dates, and locations.
4. Pivot: article bylines and named people become new `name`s to research; a quoted `social-profile` or outlet link feeds further OSINT; set a Google Alert (login) to monitor.

## Inputs → Outputs
- **In:** `name`, `employer-org`, or event keywords
- **Out:** aggregated articles with dates, outlets, and (via coverage) linked people/`social-profile`s
- **Empty/negative result looks like:** few/no articles — the subject isn't in indexed news (common for private individuals); try local outlets directly or a general web search.

## Gotchas & OpSec
- Coverage skews to indexed, often English-language and recent sources; older/local/paywalled reporting can be missed.
- Logged-in results are personalised — use a clean session for neutral results.
- It indexes coverage; verify facts against the primary outlet and multiple sources.

## Overlaps ("do both")
- Pairs with general web search/`[[serpapi]]` and archive tools — Google News finds the coverage; archives preserve it and web search catches non-news mentions.

## Trust & verifiability
`trust: trusted` — a reliable aggregator/index of published news; judge each article by its outlet, and corroborate claims across independent sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-news |
| category | search-engines |
| selectorsIn → selectorsOut | name, employer-org → social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
