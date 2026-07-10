---
id: trends24
name: Trends24
description: Use when you have a place and time and want to know what was trending on X/Twitter there — returns ranked trending topics by country/city with an historical archive for context.
url: http://trends24.in
category: social-networks
path:
- social-networks
bestFor: Live and historical X/Twitter trending-topic tracking by country and city, useful for event/context analysis.
selectorsIn:
- geolocation
selectorsOut:
- metadata-exif
status: live
pricing: free
costNote: Free, ad-supported; no account needed to view current or archived trends.
opsec: passive
opsecNote: Reading aggregated trend data is passive and touches no individual or account. Standard sock-puppet browsing is more than sufficient.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running third-party tracker of X/Twitter trends; data mirrors Twitter's trend lists (subject to Twitter's own manipulation/algorithm quirks), archived by location.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- getdaytrends
- one-million-tweet-map
aliases:
- Trends24
- trends24.in
tags:
- twitter
- trends
source: awesome-osint
lastVerified: '2026-07-10'
enrichment: full
---

# Trends24

> A live and historical tracker of X/Twitter trending topics broken down by country and city — context intelligence, not a people-finder.

## When to use
You want to understand the social-media conversation around a place and time: what was trending on X/Twitter in a specific country/city, right now or at some past hour. This is context/situational-awareness tooling — useful for corroborating when/where an event drew attention, spotting local hashtags to search, or grounding a timeline — rather than for locating an individual (hence low direct MP relevance).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://trends24.in and pick a country/city from the location list.
2. Read the current top trends (ranked), and scroll the timeline/archive to see what trended earlier in the day.
3. Note local hashtags/terms to pivot into X search around your subject or event.
4. Pivot: promising hashtags feed X keyword/image search; geographic trend spikes can be mapped alongside `[[one-million-tweet-map]]`.

## Inputs → Outputs
- **In:** a `geolocation` (country/city selection) and a time
- **Out:** ranked trending topics/hashtags (`metadata-exif`-style contextual metadata) with an historical archive
- **Empty/negative result looks like:** a smaller locale may show only global/national trends with little local specificity — not all cities are covered granularly.

## Gotchas & OpSec
- Reflects Twitter's own trend lists, which can be gamed or algorithmically skewed — treat trends as signals, not ground truth.
- Not a person-search tool; its MP value is contextual (timelines, local hashtags), not identifying.
- OpSec: fully passive; no contact with any account.

## Overlaps ("do both")
- Pairs with `[[getdaytrends]]` (another trend archive — cross-check coverage) and `[[one-million-tweet-map]]` for the geographic tweet view.

## Trust & verifiability
`trust: community` — a reliable long-running mirror of Twitter's trend data, but only as trustworthy as Twitter's trends themselves. Use for context; verify any specific claim against the underlying tweets.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | trends24 |
| category | social-networks |
| selectorsIn → selectorsOut | geolocation → metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
