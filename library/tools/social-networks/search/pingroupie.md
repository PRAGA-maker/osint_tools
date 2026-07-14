---
id: pingroupie
name: PinGroupie
description: Use when you have a Pinterest `username` or board and want to analyse their boards, pins, and interests — returns `social-profile` data (boards, pin themes, followers) that reveals a subject's interests and locations.
url: https://pingroupie.com/
category: social-networks
path:
- social-networks
- search
bestFor: Profiling a Pinterest account's boards and pins to infer interests, plans, and location clues.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: freemium
costNote: Free to search and browse the board/category directory; heavier analytics/filtering may prompt an account.
opsec: passive
opsecNote: Works against Pinterest's public data; no login needed and the target is not notified. Fully passive so long as you don't log into Pinterest and follow/interact.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-standing third-party Pinterest analytics/board-discovery site; reliable for public board data, but a scraper-style tool subject to Pinterest changes.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Pin Groupie
- pingroupie.com
tags:
- pinterest
- board-analysis
- social-media
source: arf-seed
lastVerified: '2026-07-14'
enrichment: full
---

# PinGroupie

> A Pinterest board-and-analytics explorer — surface a subject's boards and pins to read their interests, aspirations, and sometimes their location or plans.

## When to use
You have a Pinterest `username` (or want to find boards around a theme tied to a subject) and need to mine what they save. Pinterest is quietly revealing: boards on "our wedding," "new house in [place]," "[hobby]," or specific products can expose plans, location, tastes, and lifestyle — useful context in a missing-person or identity investigation. PinGroupie helps analyse boards and discover related ones beyond Pinterest's own limited search.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://pingroupie.com/.
2. Search by keyword/category to find boards, or look up boards/pins associated with the target `username`.
3. Read the board list, pin themes, follower/engagement stats, and descriptions.
4. Note location hints, named events, and product/brand affinities.
5. Pivot: the Pinterest profile → cross-platform username checks; pinned images → reverse-image; location/plan clues → geolocation and timeline work.

## Inputs → Outputs
- **In:** `username` (or theme keyword)
- **Out:** `social-profile` context — boards, pin themes, followers, descriptions, interest/location clues
- **Empty/negative result looks like:** no boards for the handle or a private account — Pinterest activity is often sparse/private; a miss isn't conclusive.

## Gotchas & OpSec
- Third-party scraper: coverage and freshness depend on Pinterest's current structure; may lag or break.
- Board themes are suggestive, not definitive — a "house in X" board is a lead, not proof of residence.
- Confirm the account is your subject (handle collisions) before drawing conclusions.

## Overlaps ("do both")
- Pairs with direct Pinterest profile review and `[[whatsmyname]]` username enumeration — this adds board discovery/analytics the native UI hides.

## Trust & verifiability
`trust: community` — a third-party analytics layer over public Pinterest data; the data is genuine but scraper-dependent, so verify key findings on Pinterest itself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pingroupie |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
