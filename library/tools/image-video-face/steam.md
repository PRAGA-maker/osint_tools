---
id: steam
name: Steam
description: Use when you have a `username`/handle and think the subject games on Steam — returns `social-profile`, `image` (avatar), `associate` (friends) and activity.
url: http://store.steampowered.com
category: image-video-face
path:
- image-video-face
bestFor: Finding a subject's Steam profile — avatar, games, friends list, activity and linked accounts.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- image
- associate
status: live
pricing: free
costNote: Free to view public profiles at steamcommunity.com; no account needed to read public profiles.
opsec: passive
opsecNote: Viewing a public profile is passive and doesn't notify the target. To see friends-only content you'd need to friend them (active) — use a sock-puppet and avoid that unless justified. Many profiles are set private.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Valve's first-party gaming platform; profile data is authoritative for the account, though handles/personas are self-chosen.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- Steam Community
- steampowered.com
tags:
- toddington
- curated-directory
- image-video-multimedia-search
- gaming
- steam
source: toddington-resources
lastVerified: '2026-07-11'
enrichment: full
---

# Steam

> Valve's gaming platform and its social layer (steamcommunity.com): a subject's Steam profile can expose an avatar, real-name field, friends list, activity times and linked handles — a rich, under-checked angle for gamers.

## When to use
You have a `username`/handle (or a name) and think the subject games, especially on PC. Steam Community profiles can reveal an avatar (`image` for reverse-search), a chosen persona and sometimes a real name, a friends list (`associate`), owned games and playtimes, comments, groups, and links to other platforms (Twitch/Discord/YouTube). Playtime patterns hint at timezone/routine.

## How to use it (`bestInteractionPattern`: web-manual)
1. Search the handle on Steam (steamcommunity.com) or via Google `site:steamcommunity.com "handle"`; profiles resolve at `/id/<vanity>` or `/profiles/<steamID>`.
2. Open the profile: avatar, persona/real-name, level, games, recent activity, comments, groups, and linked accounts.
3. If public, read the **friends list** for associates and the comments for interactions/aliases.
4. Note playtime/online patterns as a timezone/routine signal; capture the avatar for reverse-image.
5. Pivot: reverse-image the avatar, enumerate the handle across platforms, and follow linked Twitch/Discord/YouTube; use SteamID lookup sites for account history.

## Inputs → Outputs
- **In:** `username`/handle (or `name`)
- **Out:** `social-profile` (persona, games, groups, comments), `image` (avatar), `associate` (friends), activity/`metadata-exif` signals
- **Empty/negative result looks like:** no profile, or a private/limited profile showing only an avatar and level — many users lock profiles; absence doesn't mean they don't game.

## Gotchas & OpSec
- Profiles are frequently set **private/friends-only** — you'll often see just avatar + level.
- Personas and real-name fields are self-chosen; confirm identity via avatar/linked accounts, not the name field alone.
- Friending to see more is **active** and visible — avoid unless justified, and only via a sock-puppet.
- Steam has a Web API for programmatic profile/summary lookups (needs a key).

## Overlaps ("do both")
- Pairs with SteamID history sites (SteamDB/SteamID.uk), reverse-image search, and Twitch/Discord OSINT — those add account age/name history and the linked live-streaming/chat footprint.

## Trust & verifiability
`trust: trusted` — Valve's first-party platform, so account data is authoritative; identity attribution still needs corroboration since personas are self-selected.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | steam |
| category | image-video-face |
| selectorsIn → selectorsOut | username, name → social-profile, image, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
