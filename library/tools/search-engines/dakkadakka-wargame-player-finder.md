---
id: dakkadakka-wargame-player-finder
name: DakkaDakka Wargame Player Finder
description: Use when your subject is a tabletop wargamer and you have a `username` or `geolocation` and want to find their DakkaDakka member profile/location — returns `social-profile`, `geolocation`.
url: http://www.dakkadakka.com/core/player_finder.jsp
category: search-engines
path:
- search-engines
bestFor: Locating members of the DakkaDakka wargaming community by area to tie a hobbyist alias to a rough location and forum profile.
selectorsIn:
- username
- geolocation
selectorsOut:
- social-profile
- geolocation
status: live
pricing: free
costNote: Free community feature; posting/messaging needs a free forum account, but the finder is browsable.
opsec: passive
opsecNote: Browsing the player finder is passive. To message a member you must register and log in — do that only from a sock-puppet account, never an attributable one.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A member-submitted directory on a large, long-running hobby forum — locations and details are self-reported and unverified.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- dakkadakka.com player finder
tags:
- toddington
- curated-directory
- specialty-search
- hobby-community
source: toddington-resources
lastVerified: '2026-07-22'
enrichment: full
---

# DakkaDakka Wargame Player Finder

> A member-locator on DakkaDakka, one of the largest Warhammer/tabletop-wargaming forums — niche but useful when your subject is a hobbyist who registered a rough location.

## When to use
Your subject is (or may be) a tabletop wargamer and you have a `username` to check, or a `geolocation` to enumerate. The player finder lets you find DakkaDakka members by area, tying a hobby alias to a self-reported location and a forum profile you can then read for further leaks (post history, gallery, linked socials).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.dakkadakka.com/core/player_finder.jsp.
2. Search by location/region (and cross-reference a known `username` against the returned members), or browse members near a target `geolocation`.
3. Open a matching member's profile: note their self-reported location, games played, join date, post/gallery activity, and any linked accounts or signatures.
4. Pivot: the forum `username` feeds username enumeration across other sites; a self-reported town narrows `geolocation`; post history often leaks names, events, and local store references.

## Inputs → Outputs
- **In:** `username` and/or `geolocation` (area to search)
- **Out:** `social-profile` (DakkaDakka member profile + any linked accounts), self-reported `geolocation`
- **Empty/negative result looks like:** no members in the area or no match for the handle — expected for anyone who is not an active registered DakkaDakka user; absence says nothing beyond "not on this forum."

## Gotchas & OpSec
- Coverage is limited to registered, opted-in members who set a location — a small slice of any population.
- Self-reported data is unverified and can be years stale; corroborate any location.
- Browsing is passive; only registration/messaging is attributable — use a sock puppet if you must contact someone.

## Overlaps ("do both")
- Pairs with general username-enumeration and social-profile tools — this narrows a hobbyist to a forum and rough location; those confirm identity across platforms.

## Trust & verifiability
`trust: community` — a self-reported member directory on a hobby forum; treat locations and profiles as leads to corroborate, not verified facts.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | dakkadakka-wargame-player-finder |
| category | search-engines |
| selectorsIn → selectorsOut | username, geolocation → social-profile, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
