---
id: soundcloud-music-app-mobile-android
name: SoundCloud Music App (Mobile – Android)
description: Use when a subject may create or share audio and you have a `name`/`username` — SoundCloud profiles expose a `social-profile`, bio, links, and follower network.
url: https://play.google.com/store/apps/details?id=com.soundcloud.android
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Finding a subject's SoundCloud presence — profile, tracks, bio links, and social connections — from a reused username.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- associate
status: live
pricing: free
costNote: Free to browse profiles and stream on web/app; a subscription only removes ads and unlocks offline play. No account needed to view public profiles on the web.
opsec: passive
opsecNote: Viewing public SoundCloud profiles and tracks (via web or app) is passive and anonymous. Following, liking, or commenting requires login and is visible to the target — use a sock-puppet account if you interact, and prefer read-only observation.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: SoundCloud is a legitimate platform, but profiles are self-created and pseudonymous; identity links are inferential, not verified.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
aliases:
- SoundCloud
- SoundCloud Android app
tags:
- social-profile
- music
- add-ons-apps-extensions
source: toddington-resources
lastVerified: '2026-07-29'
enrichment: full
---

# SoundCloud Music App (Mobile – Android)

> An audio-sharing social network — investigatively useful when a subject makes or shares music/audio, exposing a profile, bio links, and a follower network from a reused handle.

## When to use
You have a `name` or `username` and suspect the subject uses SoundCloud (musicians, podcasters, producers, or anyone who reuses a handle across platforms). A profile yields a `social-profile`, a bio (often with links to other accounts/websites), uploaded tracks, and the follower/following network — a source of `associate` leads and cross-platform pivots. Note you don't need the app: public profiles are viewable on the web.

## How to use it (`bestInteractionPattern`: web-manual)
1. On soundcloud.com (or the app), search the subject's `username`/`name`, prioritising handles they reuse elsewhere.
2. Open a matching public profile; read the bio and any linked sites/socials.
3. Review uploads, likes, reposts, and the follow network for connections and interests.
4. Observe read-only; only log in (sock puppet) if you must access something gated.
5. Pivot: bio links and reused usernames feed cross-platform enumeration; followers/followings are `associate` leads; a linked website feeds domain OSINT.

## Inputs → Outputs
- **In:** `name` or `username`
- **Out:** `social-profile` (bio, links, tracks), `associate` links via followers/following
- **Empty/negative result looks like:** no profile or a near-empty one — the person may not use SoundCloud or uses a different handle; a common name yields lookalikes, so confirm via linked accounts.

## Gotchas & OpSec
- Pseudonymous: profiles are self-created; treat identity links as inferential until corroborated.
- Interacting (follow/like/comment) is visible — stay read-only or use a sock puppet.
- Handle collisions are common; verify via cross-linked accounts rather than name alone.

## Overlaps ("do both")
- Pair with cross-platform username-enumeration tools and reverse-image search on the avatar — SoundCloud gives one profile and its links; those confirm the same person across the rest of their footprint.

## Trust & verifiability
`trust: unverified` — the platform is legitimate, but any profile is self-authored and pseudonymous, so a SoundCloud match must be tied to the subject through corroborating links, not assumed.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | soundcloud-music-app-mobile-android |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | name, username → social-profile, associate |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
