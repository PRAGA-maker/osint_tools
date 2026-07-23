---
id: shared-count
name: SharedCount
description: Use when you have a URL/`domain` and want its social engagement counts (Facebook shares/reactions/comments, Pinterest pins) — returns per-URL social-metric numbers to gauge reach.
url: https://www.sharedcount.com/
category: documents-metadata
path:
- documents-metadata
bestFor: Measuring how widely a specific URL was shared/engaged with on Facebook and Pinterest.
selectorsIn:
- domain
selectorsOut: []
status: live
pricing: freemium
costNote: Free tier ~500 API requests/day after registering for a free API key; paid plans for higher volume. Founded 2010, still operating.
opsec: passive
opsecNote: You submit target URLs to SharedCount, which queries the social platforms' public count endpoints — you're not touching the target's account. Queries are tied to your API key/account, so use a sock-puppet registration.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: web-manual
trust: unverified
trustNote: Established commercial analytics service; the counts come from platform APIs, whose coverage has shrunk over the years (esp. as Facebook restricted share data), so treat numbers as approximate.
missingPersonsRelevance: low
coverage:
- global
auth: api-key
api: true
localInstall: false
registration: true
aliases:
- sharedcount.com
tags:
- toddington
- curated-directory
- useful-websites-tools-documents
- social-metrics
source: toddington-resources
lastVerified: '2026-07-23'
enrichment: full
---

# SharedCount

> Social-engagement meter for URLs: how many times was this exact link shared, reacted to, or pinned?

## When to use
You have a specific URL (an article, a post, a page on a `domain`) and want to know how much traction it got on social platforms — Facebook shares/reactions/comments and Pinterest pins. Useful for gauging the reach and virality of a piece of content in an investigation: which of a subject's posts spread, whether a rumour actually propagated, or how influential a page was.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register at https://www.sharedcount.com for a free API key (free tier ~500 requests/day).
2. Query a single URL in the dashboard, or call the API with your key: `GET api.sharedcount.com/v1.1/?url=<URL>&apikey=<KEY>`.
3. Read the returned counts: Facebook engagement (shares/reactions/comments), Pinterest pins, total.
4. For many URLs, batch through the API within your daily quota.
5. Pivot: high-engagement URLs mark content worth reading in full and identify where a subject's message actually spread.

## Inputs → Outputs
- **In:** a URL / page on a `domain`
- **Out:** social engagement counts (Facebook shares/reactions/comments, Pinterest pins, totals)
- **Empty/negative result looks like:** all-zero counts — the URL genuinely had little social traction, OR the platform no longer exposes that count via API (Facebook has restricted share data); zero is not always "unpopular".

## Gotchas & OpSec
- Human-in-the-loop: you must register for a free API key first.
- Platform coverage has eroded — Facebook in particular limits share counts, so numbers under-report and shouldn't be treated as exact.
- Counts are per-exact-URL; tracking params or http/https/www variants split the totals — normalise the URL.
- OpSec: passive; queries tie to your API key, so register with a sock puppet.

## Overlaps ("do both")
- Complements archive/monitoring tools — SharedCount quantifies a URL's reach, while an archiver preserves the content that reach pointed at.

## Trust & verifiability
`trust: unverified` — a long-running commercial service returning platform-sourced counts; reliability is bounded by how much share data the social platforms still expose, which has declined, so treat figures as approximate.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | shared-count |
| category | documents-metadata |
| selectorsIn → selectorsOut | domain →  |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (api-key) |
