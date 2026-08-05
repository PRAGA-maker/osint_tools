---
id: rss-micro
name: RSS Micro
description: Use when you have a `name`, `domain`, or keyword and want to find and monitor RSS/Atom feeds mentioning it — returns matching feeds/posts pointing to `domain` and `social-profile`.
url: http://www.rssmicro.com/
category: archives-cache
path:
- archives-cache
bestFor: Keyword search across RSS/Atom feeds to discover blogs and news feeds mentioning a subject and to set up ongoing monitoring.
selectorsIn:
- name
- domain
selectorsOut:
- domain
- social-profile
status: degraded
pricing: free
costNote: Free keyword feed search; no account needed to run a query.
opsec: passive
opsecNote: Querying a feed search engine is passive — the subject isn't touched. Feeds you then subscribe to are pulled from their servers on your reader's schedule, not attributable to a manual visit.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running third-party RSS feed search engine (FeedRank); results depend on which feeds it has indexed and its index can be stale.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- feedly
- feedreader
- fetchrss
- rss-feed-reader
aliases:
- RSSMicro
- rssmicro.com
tags:
- web-monitoring
- rss
- feeds
source: awesome-osint
lastVerified: '2026-08-05'
enrichment: full
---

# RSS Micro

> A dedicated RSS/Atom feed search engine — surfaces the blogs and niche news feeds that mention a subject and won't necessarily rank in Google.

## When to use
You have a `name`, `domain`, brand, or keyword and want to (a) discover which blogs/feeds are talking about it and (b) stand up ongoing monitoring so new mentions come to you. Feed search reaches long-tail and niche sources — hobby blogs, small outlets, regional feeds — that a general web search buries, which is useful when building a picture of a low-profile subject's online footprint.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.rssmicro.com/ (the site sits behind a bot filter and may block automated fetches / be intermittently slow — use a real browser).
2. Enter your keyword/`name`/`domain` in the feed search box and run the query.
3. Review the returned feeds and recent posts; open the source sites to confirm relevance and capture the feed URL and `domain`.
4. Add promising feed URLs to your reader for continuous monitoring, and pivot the source `domain`/author into `social-profile` discovery.

## Inputs → Outputs
- **In:** `name` / `domain` / keyword
- **Out:** matching RSS/Atom feeds and posts → source `domain`, author `social-profile`
- **Empty/negative result looks like:** no feeds match, or results are stale/off-topic. The index is uneven and can lag; a blank result means the keyword isn't in its indexed feeds, not that no feed exists — retry the same keyword in another feed tool.

## Gotchas & OpSec
- Status is degraded: the front end is often behind an anti-bot wall and the index can be stale — treat it as one of several feed-search options, not authoritative.
- Feed search covers syndicated content only; sites without RSS won't appear.
- OpSec: passive; searching and subscribing reveal nothing to the subject.

## Overlaps ("do both")
- Discover feeds here, then manage and monitor them in `[[feedly]]` / `[[feedreader]]` / `[[rss-feed-reader]]`. Use `[[fetchrss]]` to generate a feed for a source that doesn't publish one, so it can be monitored too.

## Trust & verifiability
`trust: community` — an independent feed aggregator with an uneven, possibly dated index; use it to *find* sources, then verify each on the primary site before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | rss-micro |
| category | archives-cache |
| selectorsIn → selectorsOut | name, domain → domain, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
