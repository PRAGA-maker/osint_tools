---
id: crunchyroll
name: Crunchyroll
description: Use when you have a `username` and want to check for a matching anime-streaming profile — returns a `social-profile` (public display name, avatar, activity) if the handle is reused there.
url: https://www.crunchyroll.com
category: image-video-face
path:
- image-video-face
bestFor: Confirming a subject reuses a handle on Crunchyroll and pulling their public anime profile/avatar.
selectorsIn:
- username
selectorsOut:
- social-profile
- image
status: live
pricing: freemium
costNote: Viewing is free with ads or paid (Fan/Mega Fan tiers); creating an account to view another user's public profile is free.
opsec: passive
opsecNote: Browsing a public profile URL is passive, but Crunchyroll social features (following, commenting) are logged to your account. Use a sock-puppet account and never follow/interact with the target.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Sony/Crunchyroll LLC; first-party platform, but only a niche identity signal, not an investigative dataset.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- Crunchyroll anime
tags:
- toddington
- curated-directory
- image-video-multimedia-search
- username-pivot
source: toddington-resources
lastVerified: '2026-07-14'
enrichment: full
---

# Crunchyroll

> Anime/manga streaming platform whose only real OSINT value is as a username-reuse checkpoint: does the subject's handle exist here, and does the public profile add an avatar or display name?

## When to use
You are running a `username` across platforms and want to know whether the subject has (or reuses) a handle on Crunchyroll — a very large anime/streaming community. It is a weak, corroborating signal, useful mainly for younger subjects and anime fans, and best treated as one node in a broad username sweep rather than a primary source.

## How to use it (`bestInteractionPattern`: web-manual)
1. Sign in to a sock-puppet Crunchyroll account (free) at https://www.crunchyroll.com.
2. Try the profile URL pattern (e.g. via the social/community area) or search the community for the target `username`.
3. If a profile exists, read the public fields: display name, avatar (`image`), and any public lists/activity.
4. Do NOT follow, message, or comment — those actions notify the target.
5. Pivot: feed a confirmed handle/avatar into a cross-platform username tool like `[[whatsmyname]]` and reverse-image the avatar.

## Inputs → Outputs
- **In:** `username`
- **Out:** `social-profile` (public display name, avatar), `image` (avatar)
- **Empty/negative result looks like:** no profile for that handle, or a profile with default avatar and no public activity — treat as low/no signal, not proof of absence.

## Gotchas & OpSec
- Human-in-the-loop: account login required to browse community/profile features.
- Most profiles expose little beyond an avatar and username; do not over-weight a match.
- Common handles collide heavily — confirm with the avatar or a corroborating platform before attributing.

## Overlaps ("do both")
- Pairs with `[[whatsmyname]]` and other username checkers — they enumerate hundreds of sites at once, while this confirms and enriches the specific Crunchyroll node with an avatar/display name.

## Trust & verifiability
`trust: trusted` — first-party Sony/Crunchyroll platform, so any profile it shows is genuine; the caveat is investigative value (thin profiles), not data authenticity.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | crunchyroll |
| category | image-video-face |
| selectorsIn → selectorsOut | username → social-profile, image |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
