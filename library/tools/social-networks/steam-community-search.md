---
id: steam-community-search
name: Steam Community User Search
description: Use when you have a `username`/persona or real `name` and want to find a matching Steam gaming profile — returns Steam `social-profile`s to pivot on friends, activity and linked accounts.
url: https://steamcommunity.com/search/users/
category: social-networks
path:
- social-networks
bestFor: Finding a person's Steam profile by persona name to pivot into their gaming footprint, friends and linked accounts.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- username
status: live
pricing: free
costNote: Free; searching the user directory requires being logged into a Steam account.
opsec: active
opsecNote: The user-search page requires a logged-in Steam session, so use a sock-puppet Steam account — never your real one. Viewing a public profile does not notify the owner, but befriending or messaging would; stop at passive profile viewing.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party Valve/Steam directory; the profiles returned are authoritative Steam accounts, though display-name matches need corroboration.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- Steam Community search
- Steam user search
tags:
- steam
- gaming
- social
- username
source: osintambition-social
lastVerified: '2026-07-23'
enrichment: full
---

# Steam Community User Search

> Steam's own user directory — search by persona/real name to locate a gaming profile and its friends, activity and linked accounts.

## When to use
You have a `username`/gamertag or real `name` and suspect the person games on Steam. A matching Steam `social-profile` is a rich pivot: public friends lists (`associate`s), owned games and playtime, comments, linked profiles, group memberships, and sometimes a real name or location the person volunteered. Gamers frequently reuse the same handle across platforms, so a Steam hit corroborates a username you found elsewhere.

## How to use it (`bestInteractionPattern`: web-manual)
1. Log into a **sock-puppet** Steam account and open https://steamcommunity.com/search/users/.
2. Search the persona name or real name.
3. Open candidate profiles; match on avatar, linked accounts, friends, and volunteered details.
4. If public: review friends (`associate`s), recent activity, game library, comments, and group memberships.
5. Pivot: the profile's custom URL/SteamID feeds SteamID lookup tools; a reused handle feeds cross-platform username search.

## Inputs → Outputs
- **In:** `username`/persona or real `name`
- **Out:** Steam `social-profile`(s), friends (`associate`s), activity, linked accounts, sometimes real name/location
- **Empty/negative result looks like:** no match, or a private profile with everything hidden — the person may use a different handle, not use Steam, or have locked their profile (privacy settings hide friends/games).

## Gotchas & OpSec
- **Login required** for the directory — always use a throwaway Steam account.
- Display names aren't unique and are user-changeable; confirm identity with corroborating signals, not the name alone.
- Privacy settings can hide friends/games/activity even on a real match.

## Overlaps ("do both")
- Pairs with SteamID lookup tools (SteamID.uk/SteamDB) and cross-platform username search — this finds the profile; those resolve SteamID history, past names, and the same handle on other sites.

## Trust & verifiability
`trust: trusted` — first-party Valve directory; the accounts are real Steam profiles, but a name match is a lead to corroborate, not an identification.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | steam-community-search |
