---
id: kuaishou-com
name: Kuaishou (Kwai)
description: Use when you have a username or name and want to find a subject's short-video presence on China's Kuaishou/Kwai — returns profiles, videos, photos and location clues.
url: https://www.kuaishou.com/new-reco
category: social-networks
path:
- social-networks
bestFor: Finding and viewing a subject's short-form video content on China's second-largest short-video platform.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- name
- image
- geolocation
status: live
pricing: free
costNote: Free to browse public content; deeper interaction, following, and some profile/search features are gated behind a logged-in account, and registration typically needs a Chinese mobile number.
opsec: passive
opsecNote: Viewing public profiles/videos is passive, but Kuaishou heavily fingerprints and rate-limits anonymous web visitors and often forces a login wall. Use a sock-puppet account and clean browser; never follow, like or message from an attributable account. Video views can be counted.
humanInLoop: true
humanInLoopReason:
- account-login
- rate-limit
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Kuaishou Technology; this is the genuine first-party platform, though individual video content carries the usual social-media reliability caveats.
missingPersonsRelevance: high
coverage:
- global
- cn
auth: account
api: false
localInstall: false
registration: true
aliases:
- Kuaishou
- Kwai
- 快手
- kuaishou.com
tags:
- gsocialmedia
- General Social Media Sites
- china
- short-video
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# Kuaishou (Kwai)

> China's second-largest short-video network (Kwai internationally) — where a Chinese or diaspora subject's video footprint, faces and locations often live outside Western platforms.

## When to use
You have a `username` or `name` for a subject who is Chinese, China-based, or part of a Chinese-speaking community, and you want their short-video presence. Kuaishou (and its international twin Kwai) hosts everyday video that reveals faces, homes, workplaces, vehicles, routines and geotag-adjacent scenery — rich corroboration for identity, location and timeline that never appears on Instagram/TikTok-West.

## How to use it (`bestInteractionPattern`: web-manual)
1. Log into a sock-puppet Kuaishou account (web registration usually needs a Chinese mobile number; without login you'll hit a wall quickly).
2. Use the search function to look up a `name`/`username` — Chinese-character forms work far better than romanised spellings.
3. Open a matching profile: read the bio, video grid, and any location or hashtag tags. Note the stable user ID from the profile URL.
4. Watch videos for environmental detail — signage, landmarks, licence plates, interiors — that place the person.
5. Pivot: on-screen scenery feeds geolocation; the subject's face/thumbnail feeds reverse-image/face search; the same handle feeds cross-platform username enumeration (`[[sultan-username-search-tool-builder]]`).

## Inputs → Outputs
- **In:** `username` or `name` (prefer native Chinese characters)
- **Out:** `social-profile`, display `name`, `image` (face/thumbnails), and `geolocation` clues from video content/tags
- **Empty/negative result looks like:** no user match or a private/empty profile. Try the Chinese-character spelling and the international Kwai app search before concluding the subject isn't present.

## Gotchas & OpSec
- Human-in-the-loop: expect a login wall and rate-limiting; a Chinese phone number is often required for a usable account.
- Search native characters — a single romanised spelling misses most Chinese users.
- Content is subject to censorship/deletion and platform algorithms; a sparse profile may reflect removals, not inactivity.
- Never interact from the investigating account — likes/follows/views are surfaced.

## Overlaps ("do both")
- Pairs with `[[weibo-com]]` — the same subject often appears on both; cross-reference handles, faces and posted locations.
- Feeds reverse-image/face and geolocation tools — video stills are strong inputs for both.

## Trust & verifiability
`trust: trusted` — Kuaishou is the authentic first-party platform, so a confirmed account is a genuine presence; individual videos, however, can be staged, reposted or deleted, so corroborate location/identity claims across multiple clips or sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | kuaishou-com |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, name, image, geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login, rate-limit) |
