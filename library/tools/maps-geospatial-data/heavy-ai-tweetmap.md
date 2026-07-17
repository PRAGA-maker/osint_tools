---
id: heavy-ai-tweetmap
name: Heavy.ai Tweetmap
description: Use when you have a keyword or `geolocation` and want to see the geographic distribution of geotagged tweets — returns location patterns from a large tweet archive.
url: https://www.heavy.ai/demos/tweetmap
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Visualizing hundreds of millions of geotagged tweets on a zoomable map, filtered by keyword/hashtag, to see where a term was tweeted.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: degraded
pricing: free
costNote: Free public demo of HEAVY.AI's GPU database; no account required.
opsec: passive
opsecNote: You browse an aggregate tweet visualization, not the subject; nothing is disclosed to any target. Safe from any browser.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A vendor demo, not a maintained OSINT dataset. Twitter/X closed its free API in July 2023, so the feed is effectively a frozen historical archive, not live real-time data.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- HEAVY.AI Tweetmap
- MapD Tweetmap
tags:
- toddington
- curated-directory
- geospatial
- twitter
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# Heavy.ai Tweetmap

> A GPU-powered demo that plots a huge archive of geotagged tweets on a map — see, by keyword, where something was tweeted from.

## When to use
You want the geographic pattern of geotagged tweets for a keyword/hashtag — where a term clustered, from global down to neighborhood scale. Useful for understanding the spatial footprint of an event or topic. Because it's a vendor demo built before the 2023 Twitter API shutdown, treat it as a **historical** archive of geotagged tweets, not a current feed.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.heavy.ai/demos/tweetmap.
2. Enter a keyword/hashtag filter and pan/zoom the map to your area of interest (`geolocation`).
3. Read the density/heat of geotagged tweets — where the term was tweeted, and relative volume by area.
4. Drill down to neighborhood scale to see local concentration.
5. Pivot: a location cluster narrows a search area; note that only the small fraction of geotagged tweets appear, so use it as a lead, not a census.

## Inputs → Outputs
- **In:** keyword/hashtag + a map `geolocation` extent
- **Out:** geographic distribution/density of matching geotagged tweets (`geolocation` patterns)
- **Empty/negative result looks like:** no points for a term/area — expected, since only geotagged tweets (a minority) are indexed and the archive is frozen; absence is not evidence.

## Gotchas & OpSec
- **Frozen data** (`status: degraded`): the Twitter API closed in 2023, so this no longer reflects current activity.
- Only geotagged tweets are shown — a tiny, non-representative slice of all tweets.
- It's aggregate visualization, not per-user search; you won't pull an individual's tweets here.

## Overlaps ("do both")
- Pairs with live X/Twitter search and other tweet-mapping tools — Tweetmap shows the historical geospatial aggregate; live search covers the present and specific accounts.

## Trust & verifiability
`trust: unverified` — a vendor demo, not a curated OSINT source; the geographic picture is historical and partial, so corroborate any lead against primary tweet data.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | heavy-ai-tweetmap |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
