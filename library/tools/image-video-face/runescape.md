---
id: runescape
name: RuneScape (Player Hiscores)
description: Use when you have a gamer `username` and want to confirm a RuneScape account and read its public hiscores/activity — returns a social-profile with skill stats.
url: https://secure.runescape.com/m=hiscore/compare
category: image-video-face
path:
- image-video-face
bestFor: Confirming a RuneScape display name exists and pulling its public skill/activity stats.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free public hiscores; no account or payment to look up a display name.
opsec: passive
opsecNote: Hiscore and profile lookups are read-only against Jagex's public pages and do not alert the player. Adding the player as a friend or messaging in-game is active — do not.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Jagex, the game's publisher; the hiscore stats are first-party and authoritative for that display name.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
aliases:
- RuneScape hiscores
- Old School RuneScape hiscores
tags:
- toddington
- curated-directory
- image-video-multimedia-search
- gaming
source: toddington-resources
lastVerified: '2026-07-16'
enrichment: full
---

# RuneScape (Player Hiscores)

> Jagex's public player hiscores: does this display name play RuneScape, and how active is the account — a niche username-presence and activity check.

## When to use
You are enumerating a `username`/gamertag across platforms and want to test whether it belongs to a RuneScape (or Old School RuneScape) player, and if so gauge how active/high-level the account is. Activity level can corroborate that a handle is genuinely used by your subject rather than a stale registration. Treat this as one node in a username sweep, not a standalone people-finder.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to the hiscores lookup: `https://secure.runescape.com/m=hiscore/compare` (RS3) or `https://secure.runescape.com/m=hiscore_oldschool/overall` (OSRS), and enter the display name.
2. If the name exists you get a stats table (total level, XP per skill, rank); "player not found / not ranked" means no such ranked account.
3. Read the stat spread — high recent-looking totals suggest an active player; note that display names are periodically recyclable.
4. Pivot: feed the same `username` into cross-platform enumerators and gaming forums (RuneScape's own community/Discords) where the player may reuse the handle.

## Inputs → Outputs
- **In:** `username` (RuneScape display name)
- **Out:** `social-profile` (confirmed account + public skill/activity stats)
- **Empty/negative result looks like:** "Player not found" or "not ranked" — either the name is unused or the account is below the ranking threshold; absence is weak evidence.

## Gotchas & OpSec
- Display names can be changed and old names recycled, so a match is to a *name*, not a guaranteed *person*; corroborate.
- Only ranked players appear; a real but low-level account may return "not ranked".
- OpSec: passive read-only lookup; never friend or DM the player from a real account.

## Overlaps ("do both")
- Pairs with `[[kongregate]]` and other gaming-community username checks — different player bases, so run the handle through several.

## Trust & verifiability
`trust: trusted` — the hiscores are Jagex's own first-party data for that display name; the identity-to-person link, however, is only as strong as the handle reuse behind it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | runescape |
| category | image-video-face |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
