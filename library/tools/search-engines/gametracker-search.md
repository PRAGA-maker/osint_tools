---
id: gametracker-search
name: Gametracker Search
description: Use when you have a gamer `username` and want their game-server activity profile — returns social-profile, reused username and last-seen server leads.
url: https://www.gametracker.com/profiles
category: search-engines
path:
- search-engines
bestFor: Finding a player's profile across tracked multiplayer game servers (CS, TF2, etc.) — aliases, servers frequented, and last-seen activity.
selectorsIn:
- username
selectorsOut:
- social-profile
- username
status: live
pricing: free
costNote: Free to search and view player/server profiles; no account required.
opsec: passive
opsecNote: You browse a public server-tracking site, not the player; the subject is not notified. Use a research browser.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Community server-tracking data scraped from game servers; profiles reflect only servers that run GameTracker, so coverage is partial and aliases are unverified.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- GameTracker
- gametracker.com
tags:
- toddington
- curated-directory
- gaming
- specialty-search
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# Gametracker Search

> A search over tracked multiplayer game servers — turn a gamer handle into a profile of aliases, servers frequented and last-seen activity.

## When to use
Your subject games online and you have a `username`/in-game handle. GameTracker indexes players on servers running its tracker (Counter-Strike, TF2, and other server-based titles), so you can find a player profile showing their aliases, the servers/clans they frequent, rough activity times, and when they were last seen. Useful for tying a handle to a community, spotting a routine, or finding a reused alias to pivot on.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.gametracker.com/profiles.
2. Search the `username`/handle (try variants — players cycle aliases).
3. Open a player profile: known aliases, servers/clans played, last-seen timestamps, and any linked clan pages.
4. Note reused aliases and the servers/clans as community pivots.
5. Pivot: a reused handle feeds username-enumeration tools; a clan/community site or Steam link feeds deeper gaming OSINT.

## Inputs → Outputs
- **In:** gamer `username`/handle
- **Out:** player `social-profile` (aliases, servers/clans, last-seen), reused `username` leads
- **Empty/negative result looks like:** no profile — the player only uses servers GameTracker doesn't track, plays non-server titles, or uses a different handle; absence isn't conclusive.

## Gotchas & OpSec
- Coverage is limited to **servers running GameTracker** — many players won't appear.
- Aliases and "last seen" are scraped and can be stale or spoofed; corroborate.
- A handle can be shared/recycled; same name ≠ same person.

## Overlaps ("do both")
- Pairs with Steam/username-enumeration tools — GameTracker gives the server-activity picture, Steam and enumeration connect the handle to a broader identity.

## Trust & verifiability
`trust: unverified` — community-scraped server data; treat profiles and aliases as leads to confirm on the linked community/Steam sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gametracker-search |
| category | search-engines |
| selectorsIn → selectorsOut | username → social-profile, username |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
