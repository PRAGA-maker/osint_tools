---
id: feed-filter-maker
name: Feed Filter Maker
description: Use when you have a `name`/`username` to monitor and want alerts only on relevant items — returns a filtered RSS/Atom feed URL matching your keywords.
url: http://feed.janicek.co
category: archives-cache
path:
- archives-cache
bestFor: Building a keyword-filtered RSS feed to monitor a subject or topic without the noise.
selectorsIn:
- name
- username
selectorsOut: []
status: live
pricing: free
costNote: Free web tool (and Chrome app); no account.
opsec: passive
opsecNote: Passive monitoring — the tool fetches and filters public feeds; the subject is not contacted. Your keyword filters are processed by the third-party service, so keep them non-sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A small independent utility that transforms public RSS/Atom feeds; it adds no data, only filters existing feeds.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- feed.janicek.co
tags:
- web-monitoring
- rss
source: awesome-osint
lastVerified: '2026-08-04'
enrichment: full
---

# Feed Filter Maker

> Wraps any RSS/Atom feed with include/exclude keyword (or regex) filters and hands back a new feed URL — turning a noisy source into a targeted monitor.

## When to use
You have a source that publishes an RSS/Atom feed (a news site, a blog, a forum, a court/records feed) and want to be alerted only when it mentions your subject — a `name`, `username`, company, or place. Feed Filter Maker builds a filtered feed you subscribe to in any reader for ongoing, hands-off monitoring. It is a standing-watch tool, not a one-off search.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://feed.janicek.co.
2. Paste the source feed URL.
3. Add **inclusion** filters (keep items matching your subject's name/handle/keywords) and/or **exclusion** filters (drop noise), with optional regex and case-insensitivity.
4. Generate the filtered feed URL and subscribe to it in your RSS reader.
5. Pivot: matching items become leads — follow each to its source and enrich named people/entities with targeted tools.

## Inputs → Outputs
- **In:** `name`, `username` (as filter keywords) + a source feed URL
- **Out:** none as a selector — a filtered feed URL delivering only matching items
- **Empty/negative result looks like:** the filtered feed stays empty — meaning nothing in the source has matched yet (broaden keywords or confirm the source actually covers your subject).

## Gotchas & OpSec
- Only works on sources that expose an RSS/Atom feed; no feed, nothing to filter.
- Over-narrow filters silently miss items; test with broad terms first, then tighten.
- Passive and safe, but your filter keywords pass through a third-party service — keep them generic.

## Overlaps ("do both")
- Complements a news-search/aggregator tool — use search for the initial sweep, then a filtered feed here to catch *future* mentions automatically.

## Trust & verifiability
`trust: community` — an independent utility that only reshapes existing public feeds; verify every surfaced item against its original source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | feed-filter-maker |
| category | archives-cache |
| selectorsIn → selectorsOut | name, username →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
