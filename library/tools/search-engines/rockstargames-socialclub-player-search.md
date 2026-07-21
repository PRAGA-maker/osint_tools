---
id: rockstargames-socialclub-player-search
name: Rockstar Social Club Player/Crew Search
description: Use when you have a gaming `username`/handle and want a subject's Rockstar (GTA Online / Red Dead) profile and crews — returns a `social-profile` with activity and connections.
url: http://socialclub.rockstargames.com/crews/search/alltypes
category: search-engines
path:
- search-engines
bestFor: Finding a person's Rockstar Games Social Club profile and the crews they belong to, pivoting a gaming handle into a social graph.
selectorsIn:
- username
selectorsOut:
- social-profile
- associate
status: live
pricing: free
costNote: Free to use, but a (free) Rockstar Games / Social Club account and login are required to run searches and view most profile detail.
opsec: active
opsecNote: Searching requires logging into a Rockstar account, so activity is tied to that identity — use a dedicated sock-puppet account, never a personal one. Viewing a profile or crew, or interacting in-platform, can be visible to the subject; stay to passive viewing and do not friend/message the target.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Rockstar Games (first-party); profile/crew data is authoritative for the platform, though usernames and bios are player-chosen and not identity-verified.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools: []
aliases:
- Rockstar Games Social Club
- socialclub.rockstargames.com
tags:
- toddington
- curated-directory
- specialty-search
- gaming
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# Rockstar Social Club Player/Crew Search

> Rockstar Games' own player and crew directory — turn a GTA Online / Red Dead Online handle into a profile, the crews a person runs with, and their in-game social graph.

## When to use
You have a gaming `username`/handle (seen in a chat, a stream, a leak, or claimed by a subject) and want to check for a matching Rockstar Social Club profile. A hit gives you the player's crews (`associate` connections), activity, and a `social-profile` to correlate with the same handle elsewhere — valuable when a subject is more active in gaming than on mainstream social media.

## How to use it (`bestInteractionPattern`: web-manual)
1. Log into a sock-puppet Rockstar Games / Social Club account.
2. Open the Social Club crews/players search and enter the `username`/crew name.
3. Open a matching profile — note the crews they belong to, member lists (potential `associate`s), and any linked activity.
4. Keep to viewing only; do not send friend/crew requests or messages to the target.
5. Pivot: the same handle → cross-platform username search; crew co-members → their profiles; a linked stream/YouTube → more identity leads.

## Inputs → Outputs
- **In:** a gaming `username` / handle (or crew name)
- **Out:** a Rockstar `social-profile` plus crew membership and co-members (`associate` leads)
- **Empty/negative result looks like:** no matching player/crew — the handle isn't used on Rockstar, or the profile is private; a common handle may also return many unrelated players, so corroborate before assuming a match.

## Gotchas & OpSec
- **Human-in-the-loop: account-login.** Search needs a Rockstar account; isolate it.
- Handles are player-chosen and reused; a name match is a lead, not an identification.
- In-platform actions are visible — stay passive; friending/messaging alerts the subject.

## Overlaps ("do both")
- Pairs with cross-platform username-search tools — those tell you where else the handle appears; Social Club gives the Rockstar-specific profile and crew graph they don't cover.

## Trust & verifiability
`trust: trusted` — first-party Rockstar data, authoritative for the platform; identity behind a handle is still unverified, so confirm any real-world attribution with independent sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | rockstargames-socialclub-player-search |
| category | search-engines |
| selectorsIn → selectorsOut | username → social-profile, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
