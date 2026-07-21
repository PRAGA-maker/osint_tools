---
id: rotten-tomatoes
name: Rotten Tomatoes
description: Use when you have a `username` and want to check for a matching audience-reviewer profile revealing a person's ratings and interests — returns `social-profile`.
url: https://www.rottentomatoes.com
category: search-engines
path:
- search-engines
bestFor: Testing a reused handle against Rotten Tomatoes audience/user profiles and reading a subject's public ratings and reviews.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free to read profiles and reviews; an account (or Fandango-linked login) is only needed to post ratings.
opsec: passive
opsecNote: Reading public user profiles is passive and unlogged to the target. Only creating an account or rating would expose you. Browse from a sock-puppet session.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Major film/TV review site (Fandango-owned); audience profiles are pseudonymous and self-created, so a handle match is a lead, not identity proof.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- metacritic
aliases:
- rottentomatoes.com
tags:
- toddington
- curated-directory
- specialty-search
- reviews
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# Rotten Tomatoes

> A film/TV review site whose OSINT value is its **audience-user profiles** — one more platform to test a handle against and to read a subject's ratings, review text, and activity timing.

## When to use
You're mapping a `username` across platforms and want to see whether the same handle reviews films/TV here. A Rotten Tomatoes user profile can reveal rating history, written reviews (with incidental personal detail or other handles), and an activity timeline — corroborating interests and identity as part of a broader username-reuse map. Treat it as a supporting node, not a primary people-search.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open rottentomatoes.com in a sock-puppet browser.
2. Try the user-profile path `rottentomatoes.com/user/id/<id>` or search the handle to see whether an account exists.
3. If found, read the ratings/review history: titles, dates, scores, and any free-text reviews.
4. Note cadence and any personal details or links the person mentions.
5. Pivot: carry the confirmed handle and mentioned links into a cross-platform username sweep; interests here can back up a profile assembled elsewhere.

## Inputs → Outputs
- **In:** `username`/handle
- **Out:** matching audience `social-profile` (ratings, reviews, join date)
- **Empty/negative result looks like:** no matching user page — the handle isn't used here; weak negative evidence.

## Gotchas & OpSec
- Pseudonymous, self-created profiles — a handle match confirms reuse, not real identity.
- Accounts can be linked to Fandango; still, publicly you only see the review activity, not the underlying email.
- OpSec: passive when reading; only account creation/rating is attributable.

## Overlaps ("do both")
- Pairs with `[[metacritic]]` and cross-platform username finders — run the same handle across all of them, since a person who reviews on one film site often reviews on another.

## Trust & verifiability
`trust: unverified` — a legitimate mainstream site, but user profiles are self-reported and anonymous; treat a match as a lead to verify by content.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | rotten-tomatoes |
| category | search-engines |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
