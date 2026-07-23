---
id: steam-id-finder
name: Steam ID Finder
description: Use when you have a Steam vanity name or profile URL (`username` / `social-profile`) and want every SteamID format plus the public profile — returns `social-profile` and account identifiers.
url: https://steamidfinder.com/lookup/
category: social-networks
path:
- social-networks
bestFor: Converting a Steam vanity URL/username into SteamID64/SteamID3/SteamID and pulling the public profile snapshot.
selectorsIn:
- username
- social-profile
selectorsOut:
- social-profile
- device-id
status: live
pricing: freemium
costNote: Free web lookups; no account needed for the basic converter.
opsec: passive
opsecNote: The tool queries Steam's public profile data on your behalf; the target is not notified. Viewing a profile directly while logged into your own Steam account can appear in "recent visitors" on some setups — use the finder, not your logged-in client, for a quiet look.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Third-party utility over Steam's public API/community pages; the ID math is deterministic and reliable, profile fields are only as current as Steam's public data.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- steamidfinder.com
- SteamID lookup
tags:
- steam
- gaming
- id-converter
source: osint4all
lastVerified: '2026-07-23'
---

# Steam ID Finder

> A one-box converter and profile viewer: paste a Steam vanity URL or username and get every SteamID format plus the account's public profile.

## When to use
You have a Steam `username`/vanity name or a profile URL (`social-profile`) for a subject and need the canonical, immutable **SteamID64** (and SteamID3/SteamID) so you can pivot to other Steam-aware tools, or you just want a quick look at the public profile — avatar, real-name field, group memberships, and account creation date — without opening it in your logged-in client.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://steamidfinder.com/lookup/.
2. Enter the vanity name (e.g. `gaben`) or paste the full profile URL.
3. Read the result: SteamID64/SteamID3/SteamID, plus the public profile card (avatar, display name, real-name if set, account age, ban status where shown).
4. Pivot: the SteamID64 is the stable key for gamer-tag search engines, friend-network mappers, and cross-game username lookups; the avatar feeds reverse-image search; a real-name field feeds people search.

## Inputs → Outputs
- **In:** `username` (vanity) or `social-profile` (Steam profile URL)
- **Out:** `social-profile` (public profile snapshot) and account identifiers (`device-id`: SteamID64/SteamID3/SteamID)
- **Empty/negative result looks like:** "user not found" (vanity never claimed/changed) or a private profile that resolves an ID but shows no detail — the ID is still valid and pivotable even when the profile is private.

## Gotchas & OpSec
- Vanity URLs are user-changeable; the SteamID64 is not — always record the numeric ID, not just the vanity name.
- A private profile still yields a valid SteamID64, which other tools can use even when this page shows little.
- OpSec: **passive** — the lookup shields you from appearing as a profile visitor; don't browse the target from your own logged-in Steam client.

## Overlaps ("do both")
- Pairs with gamer-username search engines and Steam friend/network mappers — this resolves and displays the ID; those expand it into aliases, friends, and cross-platform accounts.

## Trust & verifiability
`trust: community` — the ID conversion is deterministic and trustworthy; treat profile fields (especially the free-text real-name) as claims to corroborate, not confirmed identity.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | steam-id-finder |
| category | social-networks |
| selectorsIn → selectorsOut | username, social-profile → social-profile, device-id |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
