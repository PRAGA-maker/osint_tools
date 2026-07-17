---
id: google-news-search
name: Google News Search
description: Use when you have a `name`, `employer-org`, or event and want news coverage across outlets and time — returns articles, dates, and named associates/locations from reporting.
url: https://news.google.com/
category: search-engines
path:
- search-engines
- news-search
bestFor: Aggregated news search across thousands of outlets, with date filtering to build a timeline.
selectorsIn:
- name
- employer-org
selectorsOut:
- associate
- geolocation
- name
status: live
pricing: free
costNote: Free to search and read the aggregator; individual linked outlets may have their own paywalls.
opsec: passive
opsecNote: News searching is read-only and never contacts the subject. Google logs your queries/IP; use a clean/private session and a puppet Google account if you want the searches off your main profile.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Google News is a first-party aggregator indexing established outlets; reliability depends on the underlying publication, not the aggregator.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- google-advanced-search
- google-alerts
- bing-news
aliases:
- news.google.com
- Google News advanced search
tags:
- news
- media
- search
source: awesome-osint
lastVerified: '2026-07-17'
enrichment: full
---

# Google News Search

> Google's news aggregator indexed across thousands of outlets, with operators and date filters that turn a name or organization into a chronological trail of press coverage.

## When to use
You have a `name`, an `employer-org`, or an event/incident and want to know what has been reported — an arrest, a court case, an accident, a business filing, an obituary, a local-news mention. News often carries identifying detail (age, city, employer, relatives, the exact date and place of an event) that general web search buries, and date filtering lets you build a timeline or pin down when something happened.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://news.google.com/ and search the `name`/`employer-org` in quotes for exact matches.
2. Refine with operators and the tools: quote phrases, add a city or `intitle:`, and use the date/time-range filter to bound the search or build a timeline.
3. Read across multiple outlets — corroborate a claim before trusting a single report; note the article date and dateline (`geolocation`).
4. Extract named associates, locations, ages, and roles from the reporting.
5. Pivot: set a `[[google-alerts]]` on the same query for future coverage; feed named people/places into people-search and mapping tools.

## Inputs → Outputs
- **In:** `name`, `employer-org`, event/keyword
- **Out:** articles with dates, `associate` (people named in reporting), `geolocation` (datelines/locations), `name` corroboration
- **Empty/negative result looks like:** no articles — the subject/event never made indexed news, or coverage is only in outlets Google doesn't index (very local papers, non-English press). Try the outlet's own site and non-English terms before concluding there's no coverage.

## Gotchas & OpSec
- The aggregator only indexes what its partner outlets publish; small-town and paywalled reporting may be missing — search the local paper directly too.
- News can be wrong or later corrected; corroborate across outlets and prefer primary sources for critical facts.
- OpSec: **passive** — reading news never touches the subject.

## Overlaps ("do both")
- Pairs with `[[google-advanced-search]]` (broader web, catches non-news mentions) and `[[google-alerts]]` (ongoing monitoring of the same query) — run the web search for depth and set an alert so new coverage finds you.

## Trust & verifiability
`trust: trusted` — the aggregator faithfully indexes established outlets, but the accuracy of any story rests with the publishing outlet, so verify important claims against the primary report.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-news-search |
| category | search-engines |
| selectorsIn → selectorsOut | name, employer-org → associate, geolocation, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
