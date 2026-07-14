---
id: soundcloud
name: SoundCloud
description: Use when you have a `username` or `name` and want to find a subject's audio/podcast presence — returns a `social-profile` with avatar `image`, bio, location text, tracks, and follower links.
url: https://soundcloud.com
category: image-video-face
path:
- image-video-face
bestFor: Locating a subject's audio-social presence (music, DJ sets, podcasts) and pivoting from a reused handle to a profile with avatar, bio and location.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- image
- username
status: live
pricing: freemium
costNote: Browsing and searching public profiles/tracks is free without an account. A free login is needed to see followers/following lists and some engagement details.
opsec: passive
opsecNote: Public profile and track pages can be viewed without logging in — do that from a sock-puppet browser. Logging in to view followers ties the query to whatever account you use; use a research account, never a personal one.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: SoundCloud is a large, first-party audio-hosting platform; profile content is user-generated but the platform itself is authoritative for what a given handle has posted.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- soundcloud.com
tags:
- toddington
- curated-directory
- image-video-multimedia-search
- audio
- username
source: toddington-resources
lastVerified: '2026-07-13'
enrichment: full
---

# SoundCloud

> The largest open audio-social platform — a place a reused handle often resolves to a profile with an avatar, self-written bio and stated location.

## When to use
You have a `username` (or a `name`) and are enumerating a subject's social footprint. SoundCloud is worth checking whenever the person might make or share music, DJ sets, or podcasts — creators here frequently reuse the same handle as elsewhere, and profiles carry an avatar photo, a free-text bio, a location string, and links to other sites the person controls.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to `https://soundcloud.com/<username>` directly to test a known handle, or use the search box for a `name`.
2. On the search results, filter to People to isolate profiles from tracks.
3. Read the profile: avatar `image` (reverse-image it), bio text, location, external links, and uploaded/liked tracks — track titles and descriptions often reveal timeframes and places.
4. Log in with a research account only if you need the followers/following list to map associates.
5. Pivot: the avatar feeds reverse-image search; external links feed domain/username lookups; a confirmed handle feeds cross-platform username enumeration.

## Inputs → Outputs
- **In:** `username` or `name`
- **Out:** `social-profile`, avatar `image`, confirmed `username`, plus bio/location text and outbound links
- **Empty/negative result looks like:** the direct URL 404s and People search returns no matching photo/bio — the handle is unused here, which does not rule out the person having other accounts.

## Gotchas & OpSec
- Handles are not identity-verified; a matching name can be a fan account or impersonator — corroborate with the avatar and bio before treating it as the subject.
- OpSec: public pages need no login (stay passive). Only log in with a sock-puppet if you must see follower lists.

## Overlaps ("do both")
- Pairs with cross-platform username tools — SoundCloud confirms the audio-social branch that a broad handle sweep flags but does not render in detail.

## Trust & verifiability
`trust: trusted` — a major first-party platform; the platform reliably reflects what a handle posted, though the poster's identity claims are self-asserted.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | soundcloud |
