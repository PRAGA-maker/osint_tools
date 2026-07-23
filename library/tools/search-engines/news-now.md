---
id: news-now
name: NewsNow
description: Use when you have a `name`, topic or `employer-org` and want a real-time, multi-source news feed about it — returns aggregated, timestamped article links to monitor coverage.
url: https://www.newsnow.co.uk
category: search-engines
path:
- search-engines
bestFor: Real-time aggregated news monitoring on a person, company or topic across many outlets.
selectorsIn:
- name
- employer-org
selectorsOut:
- name
- employer-org
status: live
pricing: free
costNote: Free to browse and search; optional free sign-in adds personalised "My Topics"/"My Feed". A paid B2B media-monitoring product (NewsNow Pro) exists but isn't needed for OSINT browsing.
opsec: passive
opsecNote: You read an aggregator's public feeds; nothing about the subject is sent to them. Sign-in personalisation ties saved topics to an account, so use a sock puppet if you save searches.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-established UK news aggregator that links out to original outlets; it curates/links rather than reports, so verify each story at its source.
missingPersonsRelevance: low
coverage:
- global
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- newsnow.co.uk
tags:
- news
- aggregator
- monitoring
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# NewsNow

> Independent real-time news aggregator: one continuously-updating stream pulling coverage of a person, company, or topic from thousands of outlets.

## When to use
You want to monitor what's being published about a subject right now and over time — a `name`, an `employer-org`, or a topic. NewsNow aggregates and timestamps headlines from thousands of sources into topic feeds, so you can watch breaking coverage, catch multiple outlets' angles on the same event, and set up a standing feed rather than repeatedly searching. Strong for UK/international press and dedicated topic pages.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.newsnow.co.uk and search the subject `name`/topic, or browse to a relevant topic page.
2. Read the reverse-chronological feed — each item shows the outlet and how long ago it was published.
3. Sort by latest to monitor breaking developments, or scan the range of sources for differing coverage.
4. Optionally sign in (sock-puppet account) to save the subject as a "My Topic" for an ongoing personalised feed.
5. Pivot: open each headline at its **original** outlet to verify; harvest named associates/places/dates from the articles.

## Inputs → Outputs
- **In:** a `name`, `employer-org`, or topic query
- **Out:** an aggregated, timestamped feed of article links (with corroborating `name`/`employer-org` mentions) across many outlets
- **Empty/negative result looks like:** a sparse or empty feed — little recent press coverage of the subject, or the query is too specific; broaden terms or check a dedicated topic page.

## Gotchas & OpSec
- It's an aggregator, not a publisher — always read and cite the original outlet, not the NewsNow link.
- Coverage skews to English-language/UK sources; combine with local-language news search for other regions.
- Feeds emphasise recency; for deep historical coverage use a dedicated newspaper archive instead.
- OpSec: passive; only saved-topic personalisation touches an account — use a sock puppet.

## Overlaps ("do both")
- Complements `[[newspapers-com]]` — NewsNow covers live, current reporting, while Newspapers.com holds the deep historical archive; together they span "now" and "then".

## Trust & verifiability
`trust: community` — a long-standing, reputable aggregator; it faithfully links to third-party outlets, so trust ultimately rests on each linked source, which you should open and verify.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | news-now |
| category | search-engines |
| selectorsIn → selectorsOut | name, employer-org → name, employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
