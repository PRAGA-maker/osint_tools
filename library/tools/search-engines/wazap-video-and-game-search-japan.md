---
id: wazap-video-and-game-search-japan
name: Wazap (Japan game community)
description: Use when you have a Japanese-gaming `username` or game title and want to search a large Japanese game database/community for profiles, reviews and handles — returns community posts and account leads.
url: https://wazap.com/
category: search-engines
path:
- search-engines
bestFor: Searching a Japanese video-game database and user community for a gamer handle, review, or game-linked profile.
selectorsIn:
- username
selectorsOut:
- username
- social-profile
status: live
pricing: free
costNote: Free to browse and search; a free account is only needed to post, not to read.
opsec: passive
opsecNote: Browsing/searching public game pages and profiles is passive and invisible to the target. Create a sock-puppet account only if you need to view members-restricted content.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A long-running Japanese gaming community/database; user-generated content, so profiles and posts are unvetted.
missingPersonsRelevance: low
coverage:
- jp
auth: none
api: false
localInstall: false
registration: false
aliases:
- wazap.com
- jp.wazap.com
tags:
- toddington
- curated-directory
- specialty-search
- gaming
- japan
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# Wazap (Japan game community)

> A large Japanese video-game database and user community — a niche source for tying a gamer handle to reviews, posts, and a game-linked profile in the Japanese scene.

## When to use
Your subject has a Japanese-gaming footprint and you have a `username` or a game they engage with. Gaming communities are where people reuse handles and reveal interests, timezone, and social ties, and Japanese-scene activity is poorly indexed by Western tools. Wazap lets you search its game database and user community to find a matching profile or posts. This is a specialty, low-frequency source — reach for it when the lead is Japanese gaming.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://wazap.com/ (jp.wazap.com redirects here).
2. Search the site for the `username` or the game title of interest (interface is Japanese — use a translator).
3. Inspect matching user profiles, reviews, and posts for the handle, activity, and stated interests.
4. Note reused handles and any linked accounts.
5. Pivot: a confirmed handle feeds cross-platform username-search; game/community context corroborates interests and possible timezone.

## Inputs → Outputs
- **In:** a gaming `username` or game title
- **Out:** community profiles/posts → matching `username`, linked `social-profile`, interest signals
- **Empty/negative result looks like:** no matching profile/posts — expected unless the subject is active on this specific community; absence is not evidence of no gaming presence elsewhere.

## Gotchas & OpSec
- Japanese-language and Japan-scoped: use a translator; low relevance for non-Japanese subjects.
- User-generated: handles and claims are unverified — corroborate before relying.
- Niche/low-yield: treat as a supplementary source, not a primary one.
- OpSec: passive for reading.

## Overlaps ("do both")
- Pairs with general username-search and other gaming-profile tools — this one covers the Japanese community that broad tools miss, so run both when the lead is a handle.

## Trust & verifiability
`trust: unverified` — an established but community-driven Japanese gaming site; content is user-submitted, so treat any find as a lead to confirm on another platform.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wazap-video-and-game-search-japan |
| category | search-engines |
| selectorsIn → selectorsOut | username → username, social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
