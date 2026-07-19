---
id: wikimedia-cloud-page-views
name: Wikipedia Pageviews Analysis
description: Use when you have a `name` or topic with a Wikipedia article and want its traffic over time — returns daily/monthly pageview counts you can compare across pages to gauge public attention and pin spikes to events.
url: https://pageviews.wmcloud.org/
category: social-networks
path:
- social-networks
bestFor: Charting and comparing Wikipedia article pageviews over time to measure and date public interest in a person or topic.
selectorsIn:
- name
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free tool on Wikimedia Cloud (built on the official Wikimedia pageviews API); no account required.
opsec: passive
opsecNote: You query aggregate Wikipedia traffic statistics, not any individual; nothing reaches the subject. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Community-built but based on the official Wikimedia pageviews API; the counts are Wikimedia's own aggregate statistics and are authoritative for article traffic (from mid-2015 onward).
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- Pageviews Analysis
- pageviews.wmcloud.org
tags:
- wikipedia
- analytics
- traffic
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# Wikipedia Pageviews Analysis

> The standard tool for charting how many times Wikipedia articles were viewed over time — enter a person's or topic's article and see traffic by day/month, or compare several articles to measure and date public attention.

## When to use
You have a `name` (or topic) with a Wikipedia article and want to gauge public interest over time: when attention spiked (often aligning with a news event, arrest, disappearance, or scandal), how sustained it was, or how two subjects compare in prominence. It's a context/timeline signal — good for pinning when a person became newsworthy — rather than a source of facts about the person; its direct locate-a-person value is low.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://pageviews.wmcloud.org/.
2. Enter the exact Wikipedia article title(s) for the `name`/topic (add more to overlay comparisons), choose the wiki/language and a date range.
3. Read the chart: spikes mark surges of attention; hover for daily counts. Data runs from mid-2015 (older ranges use the legacy stats.grok.se era, not covered).
4. Correlate spikes with a news timeline to date events, and use the "Topviews"/"Langviews" companion tools for related angles.
5. Pivot: a dated attention spike tells you when to search news archives and social platforms for the triggering event.

## Inputs → Outputs
- **In:** `name`/topic (as a Wikipedia article title)
- **Out:** `document-id`-style time-series of pageview counts (chartable, comparable, exportable)
- **Empty/negative result looks like:** no article/flat-zero — the subject may have no Wikipedia page (most people don't), or the title is misspelled; this tool only works for topics that have an article.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: fully **passive** — aggregate traffic stats, no individual exposure.
- Scope: requires a Wikipedia article to exist; measures *attention*, not truth. A spike shows interest, not what happened — always pair with a news/event source. Data begins ~July 2015.

## Overlaps ("do both")
- Pairs with Google Trends and news-archive search — pageviews date *encyclopedic* attention spikes, Google Trends dates *search* interest, and news archives supply the actual event behind a spike; together they build a why-and-when timeline.

## Trust & verifiability
`trust: trusted` — a community front-end over Wikimedia's official pageviews API; the numbers are Wikimedia's own aggregate statistics, reproducible via the API, so the data is authoritative for article traffic within its date coverage.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wikimedia-cloud-page-views |
| category | social-networks |
| selectorsIn → selectorsOut | name → document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
