---
id: spotify
name: Spotify
description: Use when you have a `username`/handle and want the person's public Spotify profile — returns social-profile, display name, avatar, and public playlists/followers.
url: https://play.spotify.com
category: image-video-face
path:
- image-video-face
bestFor: Confirming a reused handle maps to a Spotify account and reading its public display name, avatar, playlists, and follow graph.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- name
- image
- associate
status: live
pricing: freemium
costNote: Viewing public profiles and playlists is free; the paid Premium tier is for listening, not lookups.
opsec: passive
opsecNote: Opening open.spotify.com/user/<id> in a browser is an ordinary pageview; the target isn't notified. Avoid logging in with a personal account or following the target, which would surface you in their follower list.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: First-party Spotify pages; the account is real but display names/avatars are user-set and playlists reveal only what the user made public.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- open.spotify.com
- Spotify profile
tags:
- social-networks
- username-pivot
- music
source: toddington-resources
lastVerified: '2026-07-16'
enrichment: full
---

# Spotify

> A username pivot with low but occasionally useful yield: a public Spotify profile can confirm a handle, expose a display name and avatar, and reveal public playlists and a follow graph.

## When to use
You have a `username` and are enumerating where it exists, or you already know the subject's Spotify handle and want to squeeze it for leads. Spotify's OSINT value is modest — it's not a people database — but a public profile can confirm the handle is in use, hand you a display `name` and avatar (`image`) for reverse-image search, and expose public playlists and followed accounts (`associate`s) that hint at interests, language, and social ties. Note this URL (`play.spotify.com`) redirects to the modern `open.spotify.com`.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to `https://open.spotify.com/user/<username>` (or search a name in the web player).
2. If the profile loads, note the display name, avatar, and follower/following counts.
3. Open **Public Playlists** — titles, cover art, and collaborative playlists can name other people or reveal interests; check **Following** for linked artists/friends.
4. Save the avatar for reverse-image search; record followed/collaborating handles to enumerate elsewhere.
5. Pivot: avatar → face/image search; collaborator handles → cross-platform username enumeration.

## Inputs → Outputs
- **In:** `username` (or a `name` to search)
- **Out:** `social-profile` (the Spotify page), display `name`, avatar `image`, public-playlist collaborators / follows (`associate`)
- **Empty/negative result looks like:** "couldn't find that profile" (handle unused here), or a bare account with a default avatar and no public playlists — real but yielding nothing. Many users keep everything private, so a thin profile is common.

## Gotchas & OpSec
- Most personal data is optional and often absent; treat Spotify as a low-priority corroborator, not a primary source.
- A browser may occasionally prompt login to view some pages — use a sock-puppet account, never a personal one.
- OpSec: passive pageview; do not follow or add the target, which would expose your research account in their graph.

## Overlaps ("do both")
- Pairs with [[last-fm]] — both are music-handle pivots, but Last.fm profiles are usually richer (real name, country, friends), so run Last.fm when the handle appears on both.

## Trust & verifiability
`trust: community` — genuine first-party pages, but content is user-set and mostly optional, so anything found here is a lead to corroborate elsewhere.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | spotify |
| category | image-video-face |
| selectorsIn → selectorsOut | username, name → social-profile, name, image, associate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
