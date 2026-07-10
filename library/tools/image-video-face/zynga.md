---
id: zynga
name: Zynga
description: Use when you have a gaming `username` and suspect the subject plays a Zynga social game — returns whether that handle maps to an in-game `social-profile` and avatar `image`.
url: https://www.zynga.com
category: image-video-face
path:
- image-video-face
bestFor: Context on a subject who plays Zynga social games (Words With Friends, Zynga Poker, FarmVille) — a weak username/profile pivot, not a people-search engine.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- image
status: live
pricing: free
costNote: Playing Zynga games is free (freemium in-game purchases); there is no public people-search — any lookup happens inside a game client.
opsec: active
opsecNote: Zynga offers no passive public search; to check a handle you must be inside a game (Words With Friends lets you search players by username), which is ACTIVE — searching for or adding a player can notify them. Use a sock-puppet game account, never your own.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: Zynga is a legitimate social-gaming company, but as an OSINT resource it has no public search interface; utility is marginal and indirect (in-game handle matching only).
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- y8
- namechk-2
aliases:
- Zynga games
- Words With Friends
tags:
- toddington
- curated-directory
- gaming
source: toddington-resources
lastVerified: '2026-07-10'
enrichment: full
---

# Zynga

> A social-gaming company (Words With Friends, Zynga Poker, FarmVille) — of marginal, indirect OSINT value: at best you can match a known gaming handle to an in-game profile, not run any public people-search.

## When to use
Reach for this only when other evidence already suggests the subject plays a Zynga title and you have a candidate gaming `username`. Words With Friends in particular lets you search for players by username, so a matching handle plus avatar can weakly corroborate identity or activity. This is a low-yield pivot — treat it as a nice-to-have, not a primary lookup.

## How to use it (`bestInteractionPattern`: web-manual)
1. There is no useful search on zynga.com's marketing site — the lookup lives inside a game. Install/open a Zynga game (e.g. Words With Friends) on a **sock-puppet** account.
2. Use the in-game "add/search player" feature to search the candidate `username`.
3. If a player matches, note the display `name` and avatar `image`; many Zynga accounts also link to Facebook, which can be a further pivot.
4. Do NOT send a game invite or message — stop at the match.
5. Pivot: an avatar image feeds reverse-image search; a Facebook link (where exposed) feeds Facebook OSINT; the confirmed handle feeds `[[namechk-2]]` cross-platform username checks.

## Inputs → Outputs
- **In:** a gaming `username` (and a guess at which Zynga title)
- **Out:** in-game `social-profile` match and avatar `image` (indirectly)
- **Empty/negative result looks like:** no player matches the handle — extremely common, and not evidence of anything given how many people don't play these games.

## Gotchas & OpSec
- Human-in-the-loop: requires an **account login** in a specific game; there is no web search.
- OpSec: **active** — in-game player search/add can notify the target and surface you in suggestions. Sock-puppet only.
- Very low signal: this should be near the bottom of a workflow, used only when a Zynga link is already suspected.

## Overlaps ("do both")
- Pairs with `[[y8]]` as another gaming-platform handle check, and with `[[namechk-2]]` to test the same username across many mainstream platforms at once (usually far more productive).

## Trust & verifiability
`trust: unverified` — Zynga is a real company but exposes no public search, so any "result" is an in-game match you obtain manually. Utility is marginal; do not over-weight a handle collision.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | zynga |
| category | image-video-face |
| selectorsIn → selectorsOut | username, name → social-profile, image |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
