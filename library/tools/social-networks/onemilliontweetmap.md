---
id: onemilliontweetmap
name: OneMillionTweetMap
description: Use when you have a place and want geotagged tweets there — plots recent X/Twitter posts on a live world map, returning location-bearing `social-profile`s and `geolocation` context.
url: http://onemilliontweetmap.com
category: social-networks
path:
- social-networks
bestFor: Visualising recent geotagged tweets on a map to find posts/accounts near a location or event.
selectorsIn:
- geolocation
selectorsOut:
- social-profile
- geolocation
status: degraded
pricing: free
costNote: Free, no account. Its yield depends on X/Twitter data access and the shrinking share of users who geotag posts, so coverage is thin and can break with X API changes.
opsec: passive
opsecNote: Viewing a map of public tweets is passive and does not notify anyone. Opening an account/tweet from the map is a normal public view; do it from a sock-puppet context and avoid interacting.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party geotagged-tweet mapper; accurate for tweets that carry precise geotags, but only a small fraction of tweets are geotagged and access depends on X's API.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- one-million-tweet-map
- twitter-image-search
- trends24
aliases:
- One Million Tweet Map
- onemilliontweetmap.com
tags:
- twitter
- geolocation
- map
source: awesome-osint
lastVerified: '2026-07-10'
enrichment: full
---

# OneMillionTweetMap

> A live world map of geotagged tweets — zoom to a place to see recent public X/Twitter posts pinned there, and the accounts behind them.

## When to use
You have a `geolocation` (a city, neighbourhood, venue, or event area) and want to find public tweets — and posters — physically tagged there. Geotagged posts can place a subject or witnesses at a location and time, surface event imagery, and reveal accounts active in an area. It's a geo-discovery lens, strongest around events; note that only a small minority of tweets carry precise geotags.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://onemilliontweetmap.com and navigate/zoom to the target `geolocation`.
2. Filter by keyword/hashtag and time window if the interface allows, to focus on an event.
3. Click clustered pins to read the tweets and open the posting accounts.
4. Note timestamps and any imagery for corroboration.
5. Pivot: accounts feed X profile/bio search; keywords feed `[[twitter-image-search]]`; local trend context comes from `[[trends24]]`.

## Inputs → Outputs
- **In:** a `geolocation` (map area), optionally keyword/time filters
- **Out:** geotagged tweets, posting `social-profile`s, and `geolocation` context
- **Empty/negative result looks like:** few/no pins in an area — expected, since geotagging is rare and X's data access is limited; absence is weak evidence, not proof nobody tweeted there.

## Gotchas & OpSec
- Status **degraded**: only a small fraction of tweets are geotagged, and X's API restrictions can thin or break the feed — treat coverage as partial.
- Geotags can be set to a general place (not exact) or spoofed — corroborate before trusting a location.
- OpSec: passive; a public-tweet map with no notification. Sock puppet for opening accounts.

## Overlaps ("do both")
- Overlaps with `[[one-million-tweet-map]]` (same concept) and complements `[[twitter-image-search]]` and `[[trends24]]` — combine geo, keyword, and trend views for event coverage.

## Trust & verifiability
`trust: community` — accurate for genuinely geotagged tweets, but limited by low geotag rates and X API access. Verify any placement against the tweet content and a second signal.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | onemilliontweetmap |
| category | social-networks |
| selectorsIn → selectorsOut | geolocation → social-profile, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
