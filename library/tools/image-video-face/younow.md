---
id: younow
name: YouNow
description: Use when you have a `username` and want to check for a live-streaming profile with bio, photo, and broadcast history — returns a social-profile and image.
url: https://www.younow.com
category: image-video-face
path:
- image-video-face
bestFor: Checking whether a username maps to a public YouNow live-streamer profile.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- image
status: live
pricing: free
costNote: Free to browse public profiles; an account is only needed to broadcast or interact.
opsec: passive
opsecNote: Viewing a public profile at younow.com/<username> is passive and does not notify the user. Do not log in, follow, or enter a live broadcast chat with a real account, as that is visible to the broadcaster.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: YouNow is a real, established live-streaming platform; profile pages are first-party but user-supplied bios/photos are self-asserted and unverified.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- whatsmyname-web
- sherlock
aliases:
- younow.com
tags:
- livestreaming
- social-media
- username-check
source: toddington-resources
lastVerified: '2026-07-10'
enrichment: full
---

# YouNow

> A live-streaming social platform whose public profiles (younow.com/<username>) let you confirm a handle, grab a photo/bio, and see a person's broadcast presence.

## When to use
You have a `username` from another platform and want to check whether the same handle exists on YouNow and belongs to your subject. A profile gives you a photo, bio, follower relationships, and evidence of an active live-streaming presence — useful for confirming a handle, sourcing a current face image, or spotting a community the subject participates in.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go directly to `https://www.younow.com/<username>` to check a specific handle, or use the site's keyword search to discover broadcasters.
2. If the handle exists, read the profile: display name, bio, avatar/photo, follower counts, and whether they are live/recently broadcast.
3. Compare the photo and bio against your known subject to confirm it is the same person (usernames are not unique across platforms).
4. Pivot: a confirmed photo feeds face/reverse-image search; the same handle feeds cross-platform username enumeration.

## Inputs → Outputs
- **In:** `username` (or `name` via keyword search)
- **Out:** `social-profile` (bio, follower data, broadcast activity), `image` (avatar)
- **Empty/negative result looks like:** a "user not found" page or an unrelated broadcaster — a matching handle alone is not confirmation; verify the photo/bio.

## Gotchas & OpSec
- Human-in-the-loop: none for viewing public profiles.
- OpSec: **passive** while browsing anonymously. Do NOT log in and enter a live chat — your presence is shown to the broadcaster.
- Identity trap: handles are reused across the web; the same username on YouNow may be a different person.

## Overlaps ("do both")
- Pairs with `[[whatsmyname-web]]` — enumerate the handle across hundreds of sites at once rather than checking YouNow by hand.
- Pairs with `[[sherlock]]` — CLI username hunt to find every platform the handle appears on, including YouNow.

## Trust & verifiability
`trust: community` — first-party profile pages on a legitimate platform, but bios/photos are user-supplied and unverified; corroborate the identity before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | younow |
| category | image-video-face |
| selectorsIn → selectorsOut | username, name → social-profile, image |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
