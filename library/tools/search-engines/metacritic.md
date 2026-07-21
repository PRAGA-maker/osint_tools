---
id: metacritic
name: Metacritic
description: Use when you have a `username` and want to check for a matching reviewer profile revealing a person's ratings history and interests — returns `social-profile`.
url: https://www.metacritic.com
category: search-engines
path:
- search-engines
bestFor: Testing a reused handle against Metacritic's user reviewer profiles and reading a subject's public rating/review activity.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free to read profiles and reviews; an account is only needed to post your own reviews.
opsec: passive
opsecNote: Reading public reviewer profiles is passive and unlogged to the target. Only creating an account or posting would expose you. Browse from a sock-puppet session.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Established review aggregator (Fandom-owned); user profiles are pseudonymous and self-created, so a handle match is a lead, not identity proof.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- metacritic.com
tags:
- toddington
- curated-directory
- specialty-search
- reviews
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# Metacritic

> A movie/TV/game/music review aggregator whose OSINT value is its **user reviewer profiles** — another platform to test a handle against and to read a subject's ratings, timing, and interests.

## When to use
You're sweeping a `username` across platforms and want to see whether it's an active reviewer here. A Metacritic user profile exposes the person's review history (what they rated, when, and their written opinions), which corroborates interests, an activity timeline, and sometimes location or other-platform handles mentioned in reviews. Best used as one more node in a username-reuse map, not as a primary lookup.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open metacritic.com in a sock-puppet browser.
2. Try the direct profile path `metacritic.com/user/<username>` or search the handle to see if a reviewer account exists.
3. If found, read the review history: titles reviewed, dates, star ratings, and free-text opinions.
4. Note posting cadence and any personal details, links, or other handles the person drops in review text.
5. Pivot: feed the confirmed handle and any mentioned links back into a cross-platform username sweep; interests here can corroborate a profile built elsewhere.

## Inputs → Outputs
- **In:** `username`/handle
- **Out:** matching reviewer `social-profile` (rating/review history, join date, opinions)
- **Empty/negative result looks like:** a 404 user page or no search match — the handle isn't used here; weak negative evidence.

## Gotchas & OpSec
- Pseudonymous and self-created — a handle match confirms reuse, not real identity; corroborate before concluding.
- Niche signal: only useful if the subject reviews media, or as part of a broad handle sweep.
- OpSec: passive when reading; only account creation/posting is attributable.

## Overlaps ("do both")
- Pairs with cross-platform username finders and `[[rotten-tomatoes]]` — those flag where a handle might exist; here you read the actual review history.

## Trust & verifiability
`trust: unverified` — a legitimate mainstream site, but user profiles are self-reported and anonymous; treat a match as a lead to verify by content.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | metacritic |
| category | search-engines |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
