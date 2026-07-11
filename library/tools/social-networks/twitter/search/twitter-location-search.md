---
id: twitter-location-search
name: Twitter Location Search
description: Use when you have a `geolocation` (lat/long + radius) and want public X/Twitter posts sent from that area — returns `social-profile` posts geographically filtered.
url: https://twitter.com/search?q=geocode%3A36.1143855%2C-115.1727518%2C1km&src=typd
category: social-networks
path:
- social-networks
- twitter
- search
bestFor: Finding X/Twitter posts tied to specific coordinates and radius via the geocode: search operator.
selectorsIn:
- geolocation
selectorsOut:
- social-profile
- geolocation
status: degraded
pricing: free
costNote: Free search operator on X itself, but X now requires a logged-in account to run searches, and geolocated results are sparse (few users geotag posts).
opsec: active
opsecNote: Running the search now requires an X login — use a sock-puppet account, since the query and your viewing are tied to that account. You are querying X's own index; targets aren't directly contacted.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: This is X's native search operator, not a third party — results are authoritative for what X has indexed, though geotag coverage is thin.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: false
aliases:
- geocode search
- Twitter geo search
- X location search
tags:
- twitter
- x
- geolocation
- geocode
source: arf-seed
lastVerified: '2026-07-11'
enrichment: full
---

# Twitter Location Search

> X's built-in `geocode:` search operator, used to pull public posts from within a radius of a coordinate — a way to see who was tweeting near a place, subject to X's shrinking geotag coverage.

## When to use
You have a `geolocation` — a lat/long and radius, e.g. the scene of an event or a subject's last-known location — and want public X posts originating near it. Useful for event monitoring and placing accounts at a location/time. Temper expectations: very few users geotag posts now, and X requires login, so this is a supplementary geographic filter, not a comprehensive one.

## How to use it (`bestInteractionPattern`: web-manual)
1. Sign in to X with a sock-puppet account (search now requires login).
2. Build the query: `geocode:LAT,LONG,RADIUS` (e.g. `geocode:36.1143855,-115.1727518,1km`), optionally combined with keywords or a date range (`since:`/`until:`).
3. Run it via the search URL (e.g. `https://twitter.com/search?q=geocode%3A36.1143855%2C-115.1727518%2C1km`) or X's search bar.
4. Read results: posts whose geotag falls in the radius; expand accounts of interest.
5. Pivot: profile the accounts, combine with keyword/date filters to tighten, and reverse-image any posted media.

## Inputs → Outputs
- **In:** `geolocation` (lat, long, radius) + optional keywords/dates
- **Out:** `social-profile` posts geographically filtered, with any `geolocation` tags
- **Empty/negative result looks like:** few or no posts — most accounts don't geotag, so a blank result rarely means "no one was there"; widen the radius and add keywords.

## Gotchas & OpSec
- Geotag coverage has collapsed — treat hits as a bonus, not a census of who was present.
- X requires a logged-in account for search; use a puppet.
- The `geocode:` operator syntax and availability have shifted with X's changes — verify it still returns results before relying on it.

## Overlaps ("do both")
- Pairs with keyword/date advanced search and dedicated geo-social tools — combine the location filter with terms/times, and cross-check other platforms (Instagram/TikTok) that carry more geodata.

## Trust & verifiability
`trust: trusted` — it is X's native operator, so results are authoritative for X's index; the limitation is coverage (sparse geotags), not data quality. Marked `degraded` due to login-gating and thin geotag data.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | twitter-location-search |
| category | social-networks |
| selectorsIn → selectorsOut | geolocation → social-profile, geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
