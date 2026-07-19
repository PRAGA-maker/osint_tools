---
id: twitter-x-location-search
name: Twitter/X Location Search
description: Use when you have a `geolocation` and want posts sent from near it — returns geotagged X/Twitter posts and the `social-profile`s behind them via the geocode search operator.
url: https://twitter.com/explore
category: social-networks
path:
- social-networks
bestFor: Finding X/Twitter posts near given coordinates using the geocode search operator.
selectorsIn:
- geolocation
selectorsOut:
- social-profile
status: degraded
pricing: free
costNote: Free via X's own search; a logged-in X account is generally required to see results.
opsec: passive
opsecNote: You query X's search index, not any user — no one is notified you searched near a location. You'll likely need to be logged in; use a sock-puppet X account, since searching ties activity to whatever account you use.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Uses X's native search; results are genuine posts, but X's geo-search has been unreliable/degraded since the API and platform changes, so coverage is partial and inconsistent.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- Twitter geocode search
- X near location search
tags:
- twitter
- x
- geolocation
- bellingcat
source: bellingcat-toolkit
lastVerified: '2026-07-18'
enrichment: full
relatedTools:
- global-terriorism-database
- murph-live
- parrot-security
- tormap
- twitter
- twitter-advanced-search
- twitter-analytics
- twitter-com
- twitter-date-search
- twitter-image-search
- twitter-name-search-twitter-name-search
---

# Twitter/X Location Search

> Using X/Twitter's `geocode:` search operator to surface posts sent from near a set of coordinates — a way to find who was tweeting at a place and time.

## When to use
You have a `geolocation` (an incident site, a last-known location, a venue) and want to find X posts made near it — to identify witnesses, spot on-the-ground media, or place an account at a location during an event. Classic Bellingcat technique. Manage expectations: X's geo-search has degraded badly since 2023 (most posts aren't geotagged and the operator is patchy), so treat hits as a bonus, not a reliable census.

## How to use it (`bestInteractionPattern`: web-manual)
1. Log into a sock-puppet X account and open search.
2. Query with the geocode operator: `geocode:LAT,LONG,RADIUS` (e.g. `geocode:51.5074,-0.1278,1km`), optionally add keywords and a date filter (`since:`/`until:`).
3. Switch between "Latest" and "Top" tabs; sort/skim results for posts genuinely from the area.
4. Read the output: posts near the coordinates and the accounts (`social-profile`) that made them.
5. Pivot: an account posting from the location feeds profile-analysis and cross-platform tools; embedded media feeds reverse-image/geolocation.

## Inputs → Outputs
- **In:** `geolocation` (lat, long + radius), optional keywords/dates
- **Out:** geotagged/near-location X posts and the posting `social-profile`s
- **Empty/negative result looks like:** few or no results — expected, because geotagging is now rare on X and the operator is unreliable; absence is NOT evidence no one posted from there.

## Gotchas & OpSec
- **Heavily degraded:** post-API-lockdown, geo-search returns a small, inconsistent slice; don't treat gaps as ground truth, and re-run/vary the radius.
- Requires being logged in; use a sock puppet, never a real account.
- Coordinates + radius syntax is finicky — verify the operator is actually filtering, not being ignored.
- OpSec: passive to targets; tied to whatever account you search from.

## Overlaps ("do both")
- Pairs with location-based tools on other platforms ([[sn-radar-vk-photo-search]] for VK, Snapchat/Instagram location features) — since X geo-coverage is thin, triangulate across platforms rather than relying on X alone.

## Trust & verifiability
`trust: community` — results are authentic X posts, but the geo-search mechanism is unreliable and partial, so use it as one lead source among several and verify each account's location independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | twitter-x-location-search |
