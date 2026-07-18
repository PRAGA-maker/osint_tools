---
id: yougotthenews
name: YouGotTheNews
description: Use when you have a `name` or `employer-org` and want news/media mentions of them — returns articles that can reveal associates, roles and events.
url: https://yougotthenews.com/
category: search-engines
path:
- search-engines
- news-search
bestFor: Running a focused news/media search on a person or organisation to surface coverage a general web search buries.
input: ''
output: ''
selectorsIn:
- name
- employer-org
selectorsOut:
- associate
- employer-org
status: live
pricing: free
costNote: Free tool within the YouGotIntel "Free" suite (by business-intelligence author Sam Richter); premium engines are separate and paid, but the news search itself is free with no login.
opsec: passive
opsecNote: A meta news-search front-end; you query news indexes, not the target, so it is passive and leaves no trace for the subject. A clean browser session is plenty.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Curated search front-end from a known business-intelligence practitioner (Sam Richter / YouGotIntel); it queries third-party news sources, so result quality depends on those underlying indexes.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- YouGotIntel News
tags:
- news-search
- media
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# YouGotTheNews

> A free news-search front-end (part of the YouGotIntel suite) that focuses queries on news and media coverage of a person or organisation.

## When to use
You have a `name` or `employer-org` and want to find news and media mentions — obituaries, local reporting, business coverage, court/incident stories — that a general web search drowns out. In a locate/missing-persons context, news coverage can pin down a last-known event, an employer, named associates or relatives, or confirm a death; it is a corroboration and lead-generation layer rather than a direct locator.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://yougotthenews.com/ (it forwards into the YouGotIntel free tools; use the "YouGotTheNews" news search).
2. Enter the subject's `name` (in quotes for exactness) or `employer-org`, adding a town or middle name to cut noise.
3. Scan the returned articles for dates, locations, named relatives/associates, and roles.
4. Pivot: an associate or employer named in an article feeds people-search and social-profile tools; a place/date feeds public-records and local-news follow-up.

## Inputs → Outputs
- **In:** `name` and/or `employer-org` (+ location qualifier)
- **Out:** news articles yielding `associate`, `employer-org`, events, dates
- **Empty/negative result looks like:** no articles returned — the subject may have no news footprint, or the underlying indexes lack coverage; try a plain search engine and local outlets before concluding there is nothing.

## Gotchas & OpSec
- It is a front-end over third-party news indexes; coverage and freshness depend on those sources, and common names produce noisy results — always disambiguate.
- The original domain redirects into the broader YouGotIntel platform, which also markets paid "Premium" engines; stay in the free news tool.
- OpSec: passive; you query news, never the target.

## Overlaps ("do both")
- Complements general search engines and dedicated news archives — YouGotTheNews focuses the query on media, while a broad web search catches non-news mentions the news filter misses.

## Trust & verifiability
`trust: community` — a curated search front-end from a reputable BI practitioner, but results are only as good as the third-party news indexes it queries; verify facts against the original outlet.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | yougotthenews |
| category | search-engines |
| selectorsIn → selectorsOut | name, employer-org → associate, employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
