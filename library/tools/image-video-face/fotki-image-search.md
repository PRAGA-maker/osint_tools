---
id: fotki-image-search
name: Fotki Image Search
description: Use when you have a `username`, `name` or keyword and want to find public photo galleries hosted on Fotki — returns image, social-profile.
url: http://search.fotki.com
category: image-video-face
path:
- image-video-face
bestFor: Surfacing a subject's public photo albums on the Fotki photo-sharing community by keyword or username.
selectorsIn:
- username
- name
selectorsOut:
- image
- social-profile
status: degraded
pricing: free
costNote: Free to browse and search public galleries; Fotki accounts have paid premium tiers but searching and viewing public content is free.
opsec: passive
opsecNote: Searching and viewing public albums does not notify the gallery owner. Do not create an account or leave comments from an attributable identity; browse logged-out through a sock-puppet session.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Fotki is a long-running third-party photo-sharing community; content is user-uploaded, so treat any identity inference as a lead, not proof.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- search.fotki.com
- Fotki
tags:
- toddington
- curated-directory
- image-video-multimedia-search
source: toddington-resources
lastVerified: '2026-07-16'
enrichment: full
relatedTools:
- fotki
- search-fotki-com
---

# Fotki Image Search

> Keyword/username search across the Fotki photo-sharing community — a place personal albums live that Google often misses.

## When to use
You have a `username` (people frequently reuse handles across photo sites) or a `name`/keyword and want to check whether the subject keeps public photo albums on Fotki. Useful for pulling candidate `image`/`face` material and a linked gallery `social-profile` you can then feed to reverse-image or face-search tools.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open `search.fotki.com` in a logged-out sock-puppet browser session.
2. Enter the target `username` or a `name`/keyword and search.
3. Read the results:
   - Hits are galleries/albums with thumbnails — open a gallery to confirm it belongs to your subject (bio, location, cross-linked handles) and to harvest full-resolution `image`s.
   - The gallery URL/handle is a `social-profile` pivot.
4. Pivot: download a clear face crop and run it through reverse-image / face-search tools; check the same username on other photo and social platforms.

## Inputs → Outputs
- **In:** `username` or `name`/keyword
- **Out:** `image` (gallery photos), `social-profile` (the Fotki gallery/handle)
- **Empty/negative result looks like:** no galleries returned, or only unrelated stock/hobby albums — meaning the handle isn't on Fotki, not that the person has no photos online.

## Gotchas & OpSec
- **Degraded:** the site currently sits behind bot-protection (Anubis challenge) that can block automated fetches — expect to solve a browser challenge and drive it manually.
- Fotki content skews to older accounts; absence is weak evidence.
- OpSec: passive; viewing public galleries is not visible to the owner. Never comment or follow from an attributable account.

## Overlaps ("do both")
- Pairs with `[[fotki]]` / `[[search-fotki-com]]` (same provider, different entry points) and with any reverse-image engine — Fotki finds the album, the reverse-image tool tells you where else that face appears.

## Trust & verifiability
`trust: community` — a genuine, long-lived photo community, but all content is user-supplied; corroborate any identity match before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | fotki-image-search |
| category | image-video-face |
| selectorsIn → selectorsOut | username, name → image, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
