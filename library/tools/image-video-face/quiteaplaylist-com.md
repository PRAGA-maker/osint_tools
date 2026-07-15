---
id: quiteaplaylist-com
name: quiteaplaylist.com
description: Use when you have a YouTube playlist (a subject's `social-profile`) and want to recover videos that were deleted or made private — returns the IDs/titles of the removed videos so you can hunt archived copies.
url: https://quiteaplaylist.com/
category: image-video-face
path:
- image-video-face
bestFor: Recovering the identities of deleted or private YouTube videos that once appeared in a playlist.
selectorsIn:
- social-profile
selectorsOut:
- social-profile
- metadata-exif
status: live
pricing: free
costNote: Free web tool; no account required.
opsec: passive
opsecNote: You submit a public playlist URL to a third-party site; it queries YouTube data, not the uploader, and does not notify anyone. Your query is visible to the tool operator — use a clean session.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Independent single-purpose utility; it exposes real YouTube video IDs that a playlist still references but that are no longer publicly viewable — accurate for what it does, but a small third-party tool with no guarantees.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- quite a playlist
- quiteaplaylist
tags:
- youtube
- YouTube Related Sites
- deleted-video-recovery
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# quiteaplaylist.com

> A single-purpose YouTube utility: paste a playlist and it names the videos that have since been deleted or made private, so you can go find archived copies.

## When to use
You have a YouTube playlist tied to your subject (their own playlist, or one that included their uploads — treat the playlist/channel as a `social-profile`) and you notice videos are missing. This tool recovers the IDs/titles of the removed entries. That matters when a subject has scrubbed content: knowing the exact video ID lets you search the Wayback Machine, Google cache, or re-upload mirrors for what they deleted.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://quiteaplaylist.com/.
2. Paste the YouTube playlist URL (or ID) into the tool.
3. It lists the playlist's entries and flags those now "[Deleted video]" or "[Private video]", recovering the underlying video ID and, where available, the original title.
4. Take each recovered video ID and search archives: `web.archive.org` for `youtube.com/watch?v=<id>`, Google/Bing cache, and re-upload sites.
5. Pivot: a recovered title/ID feeds archive searches and reverse-video lookups; the uploader (if resolvable) feeds channel/username investigation.

## Inputs → Outputs
- **In:** `social-profile` = YouTube playlist URL/ID
- **Out:** removed video IDs + original titles (`metadata-exif`-style metadata), links to the deleted/private entries
- **Empty/negative result looks like:** every entry still resolves as public — meaning nothing in that playlist was deleted/privatised, so there's nothing to recover here.

## Gotchas & OpSec
- Scope: it recovers *identifiers*, not the video content — you still need an archive to view a deleted video, and many deleted videos were never archived.
- Depends on the playlist still referencing the removed videos; a fully deleted/private playlist yields nothing.
- OpSec: passive; you touch the tool and YouTube, never the uploader.

## Overlaps ("do both")
- Pairs with the Wayback Machine and reverse-video-search tools — this names what was deleted, and those are where you try to recover or match the actual footage.

## Trust & verifiability
`trust: unverified` — a small independent utility, but its output (a video ID a playlist still points to) is directly checkable against YouTube, so results are easy to confirm.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | quiteaplaylist-com |
| category | image-video-face |
| selectorsIn → selectorsOut | social-profile → social-profile, metadata-exif |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
