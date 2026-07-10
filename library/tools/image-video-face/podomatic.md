---
id: podomatic
name: Podomatic
description: Use when you have a `name`/`username` and want to find a subject's podcast presence — returns a social-profile with episodes, avatar and any voice/location clues.
url: https://www.podomatic.com
category: image-video-face
path:
- image-video-face
bestFor: Finding a person's podcasts/audio profile on Podomatic — episodes, profile bio and avatar that can leak voice, interests and location.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- image
status: live
pricing: free
costNote: Free to browse and listen; creators can pay for hosting tiers, but searching/listening is free and needs no account.
opsec: passive
opsecNote: Browsing and listening to public podcasts is passive toward the subject. Downloading audio for analysis is fine; just don't leave comments or follow from an attributable account.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Legitimate long-running podcast-hosting platform; profiles are self-created and unverified, so treat identity claims as self-asserted.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Podomatic
- podomatic.com
tags:
- toddington
- curated-directory
- image-video-multimedia-search
- podcast
- audio
source: toddington-resources
lastVerified: '2026-07-10'
enrichment: full
---

# Podomatic

> A podcast-hosting and social platform — a place to check for a subject's audio presence, where their own voice, interests and offhand location mentions may leak.

## When to use
You're enumerating a subject's media footprint and want to cover podcasts. If your subject hosts or appears in a podcast on Podomatic, the episodes are a rich, underused source: their actual voice, named guests (`associate`), interests, and casual disclosures of location, schedule or plans. Start from a `name` or a reused `username` and look for a matching creator `social-profile` with episodes and an avatar (`image`).

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to podomatic.com and search for the subject's `name`, podcast title, or reused `username`.
2. Open matching creator profiles; review the bio, avatar (`image`), links, and episode list.
3. Listen to episodes for self-disclosed details — location, routine, named people, events.
4. Note linked social accounts and any personal site in the profile/description.
5. Pivot: the avatar feeds reverse-image search; named guests feed associate research; a linked handle feeds cross-platform enumeration; voice can corroborate identity across other audio/video.

## Inputs → Outputs
- **In:** `name`, `username`, or podcast title
- **Out:** `social-profile` (podcast/creator profile + episodes), `image` (avatar/cover art)
- **Empty/negative result looks like:** no matching creator — meaning the subject isn't on Podomatic under that name/handle; podcasters spread across many hosts (Anchor/Spotify, Libsyn, etc.), so check others too.

## Gotchas & OpSec
- Podcasters use many platforms; Podomatic is one host — absence here doesn't rule out a podcast elsewhere.
- Profiles are self-asserted; confirm identity via voice, avatar and linked accounts.
- OpSec: passive; don't comment/follow from a real account.

## Overlaps ("do both")
- Pairs with podcast search engines (Listen Notes) and reverse-image search — search across hosts for the show, and run the avatar/cover through image tools to link identities.

## Trust & verifiability
`trust: unverified` — a legitimate host, but creator identities are self-created; corroborate any match with voice, imagery and cross-platform links.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | podomatic |
| category | image-video-face |
| selectorsIn → selectorsOut | name, username → social-profile, image |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
