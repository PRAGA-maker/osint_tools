---
id: myfitnesspal
name: MyFitnessPal
description: Use when you have a `username` and want to check whether it belongs to a MyFitnessPal member and read their public community-forum footprint — returns a `social-profile` and forum posts.
url: https://www.myfitnesspal.com
category: communities-forums
path:
- communities-forums
bestFor: Confirming a username exists on MyFitnessPal and mining its public community-forum posts for personal detail.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free account tier; the community forum is publicly readable without logging in. A Premium subscription only unlocks tracking features, not more profile visibility.
opsec: passive
opsecNote: Reading public forum threads and profile pages is passive and does not notify the member. Diaries and detailed profiles are private-by-default and usually require the member to have opted them public; do not create an account to "friend" the target — that is active and visible to them.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: MyFitnessPal is a legitimate mainstream fitness platform; content is user-generated and self-reported, so any personal detail in a forum post is unverified.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- whatsmyname
- sherlock
aliases:
- MFP
- myfitnesspal.com
tags:
- toddington
- curated-directory
- online-communities-blogs
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# MyFitnessPal

> A mainstream nutrition/fitness platform with a large public community forum — mainly useful as a username-existence check and for whatever a member has posted publicly.

## When to use
You are running a `username` across platforms and want to know whether it maps to a MyFitnessPal (MFP) account, and if so, whether that member has left a public trail in the MFP community forums. Fitness communities occasionally leak useful personal context — a location mentioned in a "local running group" thread, goals, injuries, a routine, or a linked handle — that corroborates identity or lifestyle. Treat this as a low-yield corroboration/pivot source, not a primary locator.

## How to use it (`bestInteractionPattern`: web-manual)
1. Check the public profile/community: search the MyFitnessPal community forum (community.myfitnesspal.com) for the `username`, and try the member profile path directly.
2. If the handle resolves to a member, read their public posts for self-disclosed detail (location hints, age/goals, other social handles).
3. Note that food diaries and detailed profile fields are private unless the member set them public — most are not visible without a friend connection.
4. Pivot: take any linked handle or location into other tools; run the same username through cross-platform checkers to see where else it appears.

## Inputs → Outputs
- **In:** `username`
- **Out:** `social-profile` (existence + public forum posts, any self-disclosed detail)
- **Empty/negative result looks like:** no member/forum hits for the handle — either the person isn't on MFP under that name, or their profile and diary are private (the common case). Absence here proves little.

## Gotchas & OpSec
- Human-in-the-loop: none for public reading.
- OpSec: **passive** while reading public forum content. Do **not** register and send a friend request to unlock a diary — that is active and alerts the target.
- Most of the app's data (diaries, weight, meals) is private by default; expect thin public results.
- Content is self-reported and casual; a location or age in a forum post is a lead, not a fact.

## Overlaps ("do both")
- Best run inside a username sweep with `[[whatsmyname]]` and `[[sherlock]]` — they flag the MFP account existence quickly across hundreds of sites, then you come here to read the public content.

## Trust & verifiability
`trust: community` — a legitimate platform, but everything visible is user-generated and unverified; corroborate any personal detail elsewhere.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | myfitnesspal |
| category | communities-forums |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
