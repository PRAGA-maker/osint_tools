---
id: mynetworktv-united-states
name: MyNetworkTV (United States)
description: Use when you have a US location and want the local broadcast station carrying MyNetworkTV — returns the affiliate station/market via its Locate A Station tool.
url: http://www.mynetworktv.com
category: communities-forums
path:
- communities-forums
bestFor: Finding which local US broadcast station and market carries MyNetworkTV programming for a given area.
selectorsIn:
- geolocation
selectorsOut:
- employer-org
status: live
pricing: free
costNote: Free network/programming site; over-the-air programming, no account needed to browse.
opsec: passive
opsecNote: Passive browsing of a public broadcast-network site; no subject interaction. Entering a ZIP/location in the station locator only queries the network's affiliate map, not anything about a person.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The official MyNetworkTV (Fox-owned programming service) site; authoritative for its own schedule and affiliate/station listings.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- MyNetworkTV
- mynetworktv.com
tags:
- toddington
- curated-directory
- broadcast
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# MyNetworkTV (United States)

> The official site of MyNetworkTV, a US broadcast programming service — mainly useful in OSINT for its "Locate A Station" affiliate-finder, mapping a location to the local station and market.

## When to use
This is a broadcast-network site, not a people database — its OSINT value is narrow. Reach for it when you need to tie a US `geolocation` to the local station/market carrying MyNetworkTV (e.g. corroborating a media-market reference, identifying the affiliate/`employer-org` in a market, or confirming programming that aired in an area on a given night).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.mynetworktv.com.
2. Use "Locate A Station" and enter the ZIP/area; read the local affiliate station and market.
3. Use the "On Tonight"/schedule section to confirm what programming aired and when.
4. Pivot: the affiliate/station name is an `employer-org` and market anchor; the schedule can corroborate a claimed viewing time/place.

## Inputs → Outputs
- **In:** `geolocation` (US ZIP/area)
- **Out:** local affiliate station / market (`employer-org`), program schedule
- **Empty/negative result looks like:** no affiliate for the area — MyNetworkTV isn't carried there; it won't return any person-level data (it never does).

## Gotchas & OpSec
- Not an investigative database — it yields broadcast/affiliate info only, never personal records.
- Schedules are current/forward-looking; historical airing confirmation may need a separate TV-listings archive.
- OpSec: passive; nothing about a subject is queried.

## Overlaps ("do both")
- Complements TV-listings and media-market reference tools when corroborating a broadcast-related detail; on its own it is a niche affiliate finder.

## Trust & verifiability
`trust: trusted` — first-party network site, authoritative for its own affiliates and schedule; simply low in person-level OSINT value.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mynetworktv-united-states |
| category | communities-forums |
| selectorsIn → selectorsOut | geolocation → employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
