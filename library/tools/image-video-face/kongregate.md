---
id: kongregate
name: Kongregate
description: Use when you have a gamer `username` and want to check for a matching public profile on the Kongregate browser-games community — returns a social-profile with activity and avatar.
url: https://www.kongregate.com
category: image-video-face
path:
- image-video-face
bestFor: Confirming whether a username is a real Kongregate account and reading its public profile/avatar.
selectorsIn:
- username
selectorsOut:
- social-profile
- image
status: live
pricing: free
costNote: Free to browse public profiles; no account needed to view them.
opsec: passive
opsecNote: Viewing a public Kongregate profile is passive and does not notify the account holder. Logging in to view would tie the lookup to your account, so browse logged-out; commenting or friending is active and leaks you.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Kongregate is a real, long-running games platform (owned by MTG/Kongregate); profile data is user-supplied, so treat display names and bios as self-asserted.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
aliases: []
tags:
- toddington
- curated-directory
- image-video-multimedia-search
- gaming
source: toddington-resources
lastVerified: '2026-07-16'
enrichment: full
---

# Kongregate

> A large browser-games community where a reused gamertag may resolve to a public profile — a niche username-presence check.

## When to use
You are running a `username` across platforms (Sherlock-style) and want to know whether the handle also exists on Kongregate, an established Flash/HTML5 games portal with a social layer (profiles, avatars, badges, forum posts). Best treated as one more node in a username-enumeration sweep for a subject who games, not as a primary people-finder.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to `https://www.kongregate.com/accounts/<username>` (substitute the handle) in a logged-out browser.
2. If the account exists you get a public profile: avatar, level/badges, games played, and forum/comment history; a 404 means the handle is not taken there.
3. Read the avatar (`image`) and any linked info; scan forum posts for other handles or personal detail the subject volunteered.
4. Pivot: reuse a confirmed avatar in reverse-image search; feed the same `username` into cross-platform enumerators for other hits.

## Inputs → Outputs
- **In:** `username`
- **Out:** `social-profile` (Kongregate account, activity, forum posts), `image` (avatar)
- **Empty/negative result looks like:** a 404 / "user not found" page — the handle is simply unregistered here; it is weak evidence, since gamers pick handles freely and many accounts are dormant.

## Gotchas & OpSec
- Profile fields are self-asserted; a matching handle does not prove it is the same person as on another site.
- The platform has wound down much of its Flash catalogue, so many old profiles are inactive — presence, not recency, is the signal.
- OpSec: passive when logged out; do not comment or friend from a real account.

## Overlaps ("do both")
- Pairs with `[[runescape]]` and other gaming-community username checks — each covers a different player base, so a handle absent on one may surface on another.

## Trust & verifiability
`trust: community` — Kongregate itself is a legitimate, established platform, but profile content is user-supplied and should be corroborated before you treat it as identity evidence.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | kongregate |
| category | image-video-face |
| selectorsIn → selectorsOut | username → social-profile, image |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
