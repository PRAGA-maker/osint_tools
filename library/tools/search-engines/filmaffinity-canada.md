---
id: filmaffinity-canada
name: FilmAffinity
description: Use when you have a `username` on the FilmAffinity movie community and want their profile — returns reviews, ratings history, and taste/activity signals.
url: http://www.filmaffinity.com
category: search-engines
path:
- search-engines
bestFor: Finding a subject's FilmAffinity user profile and mining their film reviews/ratings for a reused handle and personal-taste signals.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free film database and community; browsing needs no account, and public user profiles/reviews are viewable.
opsec: passive
opsecNote: Reading public profiles/reviews is passive; the user is not notified. Don't rate/comment or follow — that needs an account and is active. A scoped engine query suffices.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: An established film-rating community (Spanish origin, global user base); profiles are self-created and unverified, so identity claims are leads, while the ratings/review history is genuine activity.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- FilmAffinity
- filmaffinity.com
tags:
- movies
- community
- social-networking
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# FilmAffinity

> A film-rating community (part IMDb-style database, part social) — match a username to a member profile and read their reviews/ratings for a reused handle and taste/activity signals.

## When to use
You have a `username`/handle and want to check for a FilmAffinity profile. A member's public reviews, ratings history, and lists reveal a reused handle (feeds cross-platform enumeration), language/locale, activity timing, and personal taste — small corroborating signals that help confirm you have the same person across platforms.

## How to use it (`bestInteractionPattern`: web-manual)
1. Search the handle on https://www.filmaffinity.com, or scope an engine query: `site:filmaffinity.com "<username>"`.
2. Open the user profile: reviews, ratings, lists, join/activity dates, and any linked info.
3. Read reviews for language, locale hints, and writing style.
4. Pivot: the reused `username` feeds username enumeration; review language/timing narrows locale/timezone; taste overlap helps link accounts across sites.

## Inputs → Outputs
- **In:** `username`
- **Out:** `social-profile` (FilmAffinity member page, reviews, ratings)
- **Empty/negative result looks like:** no user matches, or a profile with no public activity — treat as "not active here," not proof of absence elsewhere.

## Gotchas & OpSec
- A niche corroboration source — useful for handle/taste matching, rarely decisive on its own.
- Profiles are self-reported; the activity history is the reliable part, identity claims are leads.
- OpSec: passive reading only.

## Overlaps ("do both")
- Complements username-enumeration and other review/community sites (Letterboxd, IMDb) — this adds one more platform to match a reused handle against.

## Trust & verifiability
`trust: community` — a genuine community with real activity histories; treat self-reported identity as a lead and the ratings/reviews as authentic behavior.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | filmaffinity-canada |
| category | search-engines |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
