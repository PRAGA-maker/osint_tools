---
id: tagged-com
name: Tagged
description: Use when you have a `username` or `name` and think the subject uses the Tagged social/dating network — returns `social-profile`, `name`, photos (login required).
url: https://www.tagged.com/
category: social-networks
path:
- social-networks
bestFor: Finding a subject's profile on Tagged, a social-discovery/dating platform (The Meet Group).
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- name
- image
status: live
pricing: free
costNote: Free to join and use; browsing/searching members requires a registered account.
opsec: active
opsecNote: Viewing profiles requires logging in, so you must use a sock-puppet account; on a social/dating platform, viewing or messaging can be visible to the target (profile views, "met/skip"). Keep interaction minimal and never use a real account.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A real, operating social/dating network (The Meet Group); profile content is user-supplied and self-selected, so identity claims need corroboration.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- Tagged.com
tags:
- gsocialmedia
- General Social Media Sites
- dating
- social-discovery
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# Tagged

> A long-running social-discovery/dating network (owned by The Meet Group): a place a subject may have a profile with photos, location and interests — behind a login wall.

## When to use
You have a `username` or `name` and reason to think the subject uses Tagged (a dating/meet-people platform active since 2004). Profiles can yield photos (for reverse-image), a stated location/age, interests and a self-written bio — useful for identity, appearance and pattern-of-life, especially for subjects active on dating/social-discovery apps rather than mainstream socials.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register a **sock-puppet** account at https://www.tagged.com/ (browsing requires login).
2. Use member search/browse to look for the `username`/`name`, filtering by location/age if known.
3. Open a candidate profile: photos, stated location/age, interests, bio.
4. Capture photos for reverse-image search; note location/interest claims.
5. Pivot: reverse-image the profile photos, match the handle across platforms, and corroborate the stated location.

## Inputs → Outputs
- **In:** `username` or `name`
- **Out:** `social-profile` (bio, interests), `name`, `image` (profile photos)
- **Empty/negative result looks like:** no matching member — the subject isn't on Tagged or uses a different handle/name; profile visibility settings may also hide them from search.

## Gotchas & OpSec
- **Login required** — only ever use a sock-puppet; a real account exposes you.
- Dating-platform mechanics can surface your interest to the target (profile views, likes) — browse carefully, don't interact.
- Profiles are self-supplied and often embellished — treat age/location/photos as claims to verify.

## Overlaps ("do both")
- Pairs with reverse-image search and other dating/social platforms — the photo is the strongest cross-link, and subjects often reuse it across apps.

## Trust & verifiability
`trust: community` — a genuine operating platform; profile data is authoritative only for the account itself, so corroborate identity via the photo/handle across sources before asserting it's your subject.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tagged-com |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, name, image |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
