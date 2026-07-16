---
id: reddit
name: Reddit
description: Use when you have a `username` and want a subject's full public post/comment history — returns a `social-profile` whose activity leaks `geolocation`, interests, routines and `associate` links.
url: https://www.reddit.com
category: social-networks
path:
- social-networks
bestFor: Mining a Reddit username's complete public comment/post history for self-disclosed location, employer, interests and timeline.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- geolocation
- associate
status: live
pricing: free
costNote: Free to browse public profiles and search; a free account raises rate limits and unlocks some search/sort options.
opsec: passive
opsecNote: Reading public profiles/subreddits is passive and unlogged to the subject. Do NOT comment, DM, or vote from an attributable account — interacting alerts the target. Use a sock-puppet account only if you need to reach gated content; never your own.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party major platform; the post history is authoritative for what the account said, though the account's real-world identity is self-asserted and pseudonymous by default.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- here
- r-opendirectories
- reddit-askmeanything
- reddit-com
- reddit-com-2
- reddit-darknet
- reddit-deep-web
- reddit-guide-to-opting-out-of-background-check-websites
- reddit-old-reddit-search
- reddit-onions
- reddit-r-translator
aliases:
- reddit.com
tags:
- major-social-networks
- reddit
- username
source: awesome-osint
lastVerified: '2026-07-13'
enrichment: full
---

# Reddit

> A pseudonymous forum whose users disclose an astonishing amount about themselves over time — a username's full public history is one of the richest single-selector OSINT sources.

## When to use
You have a Reddit `username` (or a `name`/handle you suspect maps to one) and want to build a profile of the person: where they live, work, what they own and do, their daily routine, and who they interact with. Redditors routinely reveal city, workplace, vehicle, relationships and schedule across years of comments — details that appear nowhere else — making the aggregate history far more valuable than any single post.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to `https://www.reddit.com/user/<username>` for the profile; use the Overview/Comments/Posts tabs.
2. Sort by New and Top, and page back through the full history — the oldest and most-upvoted comments often carry the most disclosure.
3. Note the subreddits they frequent (local city subs pin `geolocation`; hobby/work subs reveal interests and employer).
4. Use site search (`author:<username>` in queries, or a Google `site:reddit.com <username>` dork) to catch content the profile paginates away.
5. Pivot: named locations feed geolocation/people-search; recurring co-commenters feed `associate` mapping; a reused handle feeds cross-platform username enumeration.

## Inputs → Outputs
- **In:** `username` (or a candidate handle)
- **Out:** `social-profile`, self-disclosed `geolocation`, interests/employer, `associate` interactions, and a datable activity timeline
- **Empty/negative result looks like:** a suspended/deleted account ("this account has been deleted"), a profile with hidden/empty history, or no posts — try the Wayback Machine or pushshift-style archives for removed content.

## Gotchas & OpSec
- Pseudonymous: confirm the account maps to your subject via corroborating disclosures before attributing it.
- Deleted/removed comments may persist in third-party archives — check them for a fuller picture.
- OpSec: strictly passive while reading; any interaction (vote/comment/DM) is attributable and alerts the target — don't.

## Overlaps ("do both")
- Pairs with cross-platform username tools and Google `site:reddit.com` dorks — the dork surfaces indexed threads the on-site profile view drops, and username enumerators find the same handle elsewhere.

## Trust & verifiability
`trust: trusted` — the platform authoritatively reflects what the account posted; the leap from account to real identity rests on the disclosures you corroborate.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | reddit |
