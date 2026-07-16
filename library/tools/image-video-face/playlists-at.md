---
id: playlists-at
name: playlists.at
description: Use when you have a `name` or `username` and want to find a subject's YouTube uploads or appearances via advanced search operators — returns video hits and `social-profile` (channel) links.
url: https://playlists.at/youtube/search/
category: image-video-face
path:
- image-video-face
bestFor: Running advanced-operator YouTube searches to surface a person's videos, channel, and appearances that the native YouTube box buries.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free to use; no account required for search. Optional sign-in only for saving/creating playlists.
opsec: passive
opsecNote: You query playlists.at, which relays a search to YouTube — the target sees nothing. Standard web hygiene (sock-puppet browser/VPN) is enough; do not sign in with a real Google account.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Third-party front-end over YouTube's public search; results ultimately come from YouTube, so cross-check on youtube.com directly.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- playlists.at YouTube search
tags:
- youtube
- video-search
source: uk-osint
lastVerified: '2026-07-16'
enrichment: full
---

# playlists.at

> Advanced-search front-end for YouTube: apply search prefixes/filters the native box hides to pin down a person's videos, channel, and appearances.

## When to use
You have a `name`, `username`/handle, or a distinctive phrase tied to the subject and want their YouTube footprint — uploads, a channel, or third-party videos they appear in. The advanced operators help when the plain YouTube search is swamped by unrelated results.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://playlists.at/youtube/search/ in a sock-puppet browser (no Google login needed).
2. Enter the subject's `name`, handle, or an exact quoted phrase; apply the advanced search prefixes/filters offered (channel, date, exact match) to narrow.
3. Scan the video hits — click through to the owning channel to confirm it is the subject's `social-profile`.
4. Cross-check any promising channel directly on youtube.com (About tab, links, community posts) and pivot channel handle → username searches elsewhere.

## Inputs → Outputs
- **In:** `name`, `username`/handle, or an exact phrase
- **Out:** matching YouTube videos → owning channel `social-profile`(s)
- **Empty/negative result looks like:** zero or only generic/unrelated videos — the subject has no indexed YouTube presence under that term; try alias handles or the exact-phrase operator before concluding.

## Gotchas & OpSec
- It is a thin layer over YouTube's own index, so it inherits YouTube's coverage and freshness limits — a person with a channel but no public uploads may not surface.
- OpSec: passive; the target is not notified. Never search while signed into a real Google account, or watch history/recommendations leak your interest.
- Verify identity: a matching name is not a matching person — confirm via channel bio, linked socials, or corroborating faces before attributing.

## Overlaps ("do both")
- Pairs with a direct youtube.com channel review and username-pivot tools — playlists.at finds the videos, then handle/username lookups spread the same identity across other platforms.

## Trust & verifiability
`trust: unverified` — a third-party UI over YouTube search; the underlying data is YouTube's (authoritative for what YouTube indexes), but the front-end itself is not an official source, so confirm hits on youtube.com.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | playlists-at |
| category | image-video-face |
| selectorsIn → selectorsOut | name, username → social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
