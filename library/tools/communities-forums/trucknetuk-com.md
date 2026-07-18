---
id: trucknetuk-com
name: Trucknet UK
description: Use when you have a `username` linked to UK trucking/haulage and want their forum presence — returns their profile, posts and route/employer clues, exposing interests and `associate` links.
url: https://www.trucknetuk.com/
category: communities-forums
path:
- communities-forums
bestFor: Reading a UK professional-driver's posts and profile to surface employer, routes and interests under a handle.
selectorsIn:
- username
selectorsOut:
- social-profile
- username
- employer-org
status: live
pricing: free
costNote: Free to read public threads and profiles; an account is only needed to post.
opsec: passive
opsecNote: Reading public posts/profiles is passive and doesn't notify the user. Registration/posting is attributable — use a sock puppet if you must log in, and never message the target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Britain's largest professional-driver forum (80k+ members, millions of posts); content is user-generated and pseudonymous, so details are self-reported.
missingPersonsRelevance: medium
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- Trucknet UK
- trucknetuk.com
- TruckNet
tags:
- forums
- Forums
- uk
- haulage
- transport
source: uk-osint
lastVerified: '2026-07-18'
enrichment: full
---

# Trucknet UK

> Britain's biggest professional-driver forum; a haulage worker's profile and posts often reveal their employer, regular routes, vehicle type and community ties.

## When to use
You have a `username` you suspect belongs to a UK lorry driver, owner-operator or haulage worker, or you're profiling someone in that trade. Post histories here frequently expose the company they drive for (`employer-org`), regular routes and depots (location clues), the kind of work they do, and interactions with other members (`associate`) — a strong niche source when a subject's footprint points at professional driving.

## How to use it (`bestInteractionPattern`: web-manual)
1. Search the handle via a search engine — `site:trucknetuk.com "<username>"` — since it surfaces posts better than the on-site search. (The forum has migrated from `/phpBB/` to a modern Discourse-style site at trucknetuk.com; old phpBB links may redirect.)
2. Open the member's profile and post history: note stated employer, depots/routes mentioned, join date and recurring topics.
3. Follow threads they're active in for location detail (yards, delivery areas) and other handles they interact with (`associate`).
4. Pivot: a reused `username` feeds cross-platform enumeration; a named employer feeds company/registry research; route/depot mentions narrow `geolocation`.

## Inputs → Outputs
- **In:** `username` (or a topic/company to browse)
- **Out:** `social-profile` (forum profile + posts), confirmed `username`, `employer-org` clues, plus route/location and `associate` context
- **Empty/negative result looks like:** no member or only unrelated same-handle accounts — the person may not post here; absence isn't a finding.

## Gotchas & OpSec
- Human-in-the-loop: none to read; posting/messaging needs an account — avoid unless via a sock puppet.
- OpSec: passive; reading does not alert the user.
- Self-reported and pseudonymous: employer/route mentions are strong leads but unverified; corroborate before relying on them.

## Overlaps ("do both")
- Pairs with cross-platform username tools and company registries — the forum gives employer and route clues under a handle; a username checker finds the same handle elsewhere and a registry confirms the haulage company.

## Trust & verifiability
`trust: community` — a large, long-running UK forum, but its content is anonymous and user-generated; treat employer and location details as leads to corroborate.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | trucknetuk-com |
| category | communities-forums |
| selectorsIn → selectorsOut | username → social-profile, username, employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
