---
id: one-million-tweet-map
name: One Million Tweet Map
description: Use when you have a keyword/hashtag or `username` and want to see where recent geotagged tweets originate — returns geolocation of posts on a live world map.
url: https://onemilliontweetmap.com/
category: social-networks
path:
- social-networks
- twitter
- location-mapping
bestFor: Visualising the last ~24 hours of geotagged tweets for a keyword, hashtag or handle on an interactive world map.
selectorsIn:
- username
- name
selectorsOut:
- geolocation
- social-profile
status: degraded
pricing: free
costNote: Free to use in-browser; no account required. Value is now limited by how little geolocation Twitter/X exposes, not by a paywall.
opsec: passive
opsecNote: Read-only browsing of a third-party map; you never contact the target's account, so nothing is disclosed to them. Standard web-server logging by the map operator applies.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Independent visualiser (Maptimize) built on Twitter's public streaming data; not affiliated with Twitter/X, and its completeness depends entirely on the shrinking pool of geotagged, API-visible tweets.
missingPersonsRelevance: high
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
- OneMillionTweetMap
- onemilliontweetmap.com
tags:
- twitter
- geolocation
- location-mapping
source: arf-seed
lastVerified: '2026-07-10'
enrichment: full
---

# One Million Tweet Map

> A real-time world map of geotagged tweets — type a keyword or handle and see where matching posts are being sent from over roughly the last 24 hours.

## When to use
You want a geographic view of recent Twitter/X activity around a `username`, a hashtag, or a keyword — for example to see whether posts mentioning a person, place or event cluster in a particular city, or to catch a geotagged post that reveals a poster's location. It is a location/pattern tool, not a profile-lookup tool: the payoff is `geolocation` of posts, from which you may reach the posting `social-profile`.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://onemilliontweetmap.com/ — the map loads with the recent geotagged stream.
2. Use the search box to enter a keyword, `#hashtag`, or `@username`; the map re-filters to matching geotagged tweets.
3. Zoom/pan and use the time filter to focus on a region or window; click a marker to read the tweet and see the poster's handle.
4. Extract the marker's coordinates/city (`geolocation`) and the linked handle (`social-profile`).
5. Pivot: a handle feeds full Twitter/X profile OSINT; a location cluster feeds geolocation and local-source work.

## Inputs → Outputs
- **In:** keyword / `#hashtag` / `@username` (also plain `name` as a search term)
- **Out:** `geolocation` (mapped post origins), `social-profile` (posting handle)
- **Empty/negative result looks like:** an empty or near-empty map for your term — expected, because only a tiny fraction of tweets are geotagged and X's API restrictions have sharply cut what any external tool can see.

## Gotchas & OpSec
- **Degraded by design now:** since Twitter/X locked down its streaming/geolocation API, the volume of geotagged tweets reaching third parties is a fraction of what it once was. Treat a hit as a lucky bonus and absence as expected, not as evidence.
- Only shows tweets whose authors enabled precise geotagging — a small, self-selecting minority.
- OpSec: fully passive; you never touch the subject's account.

## Overlaps ("do both")
- Pairs with dedicated Twitter/X profile and advanced-search tools — this gives you *where* a post came from, while those give you the *who and what*; combine when a geotagged post surfaces a handle worth profiling.

## Trust & verifiability
`trust: community` — a well-known independent visualiser, but it can only reflect the limited geotagged data X still exposes; always confirm any location by opening the underlying tweet.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | one-million-tweet-map |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → geolocation, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
