---
id: sharkscope
name: SharkScope
description: Use when you have a poker `username` and want to confirm and profile the player behind it — returns tournament history, results and country, tying a handle to activity and rough `geolocation`.
url: http://www.sharkscope.com
category: search-engines
path:
- search-engines
bestFor: Resolving an online-poker screen name to a tracked player profile, activity timeline and country.
selectorsIn:
- username
selectorsOut:
- geolocation
- username
status: live
pricing: freemium
costNote: A free account gives a limited number of player searches per day; Gold subscription unlocks unlimited searches, full graphs and the desktop HUD.
opsec: passive
opsecNote: Searching a screen name does not notify the player. Registration is required and searches are rate-limited on the free tier, so use a sock-puppet account and pace queries.
humanInLoop: true
humanInLoopReason:
- account-login
- rate-limit
bestInteractionPattern: web-manual
trust: community
trustNote: Long-established poker-tracking service aggregating public tournament results from major sites; results data is broadly reliable but coverage is limited to tracked sites.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
aliases:
- Sharkscope
- sharkscope.com
tags:
- toddington
- curated-directory
- specialty-search
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# SharkScope

> The de-facto database of online-poker tournament results — feed it a screen name and it tells you whether that handle is a tracked player, and their history, stakes and country.

## When to use
Your subject uses (or is suspected to use) a particular online-poker screen name and you want to confirm the handle is real and active, when they played, at what stakes, and from which country. SharkScope tracks ~99.9% of online tournaments across major sites, so a hit ties a `username` to a concrete activity timeline and a declared/inferred country (`geolocation`) — a niche pivot, mainly useful when poker is already part of the subject's footprint.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://www.sharkscope.com and register a free account (searches require login).
2. Search the subject's `username`; if unsure of the site, use the multi-site/player search.
3. Read the profile: tournament history, ROI/profit, stakes played, active dates, and country/leaderboard categories.
4. Pivot: the activity timeline corroborates when/where the person was active; the country narrows `geolocation`; consistent stakes/schedule can link multiple handles believed to be the same person.

## Inputs → Outputs
- **In:** `username` (poker screen name)
- **Out:** `geolocation` (country), confirmed `username` activity, plus history/stakes/timeline context
- **Empty/negative result looks like:** "player not found" or no tracked results — the handle isn't a tracked tournament player (cash-game-only players and untracked sites won't appear); not proof the name is unused.

## Gotchas & OpSec
- Human-in-the-loop: free account required, and free-tier searches are capped per day (rate-limit) — pace queries or the limit blocks you.
- OpSec: passive; searching does not notify the player.
- Coverage is tournament results on tracked sites only; screen names are not identities — a handle links to a player profile, not to a real name, unless corroborated elsewhere.

## Overlaps ("do both")
- Pairs with multi-platform username-enumeration tools — SharkScope confirms poker activity and country for a handle, while a username checker tests whether the same screen name exists on non-poker platforms to broaden the footprint.

## Trust & verifiability
`trust: community` — SharkScope aggregates public tournament results and is well-regarded in the poker world, but it is a third-party tracker; treat the country and any name attribution as leads, not identity confirmation.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sharkscope |
| category | search-engines |
| selectorsIn → selectorsOut | username → geolocation, username |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login, rate-limit) |
