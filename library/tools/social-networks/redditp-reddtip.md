---
id: redditp-reddtip
name: redditp (reddtip)
description: Use when you have a Reddit `username` (or subreddit) and want to rapidly triage their image submissions in a slideshow — returns the subject's posted `image` set.
url: https://www.redditp.com
category: social-networks
path:
- social-networks
bestFor: Fast slideshow review of every image a Reddit user or subreddit has posted.
selectorsIn:
- username
selectorsOut:
- image
status: live
pricing: free
costNote: Free, open-source web viewer; no account needed to browse public content.
opsec: passive
opsecNote: Reads only public Reddit content and requires no login, so nothing links the viewing to you — but it renders full-resolution images from Reddit's CDN, so browse behind a VPN/sock-puppet if you are reviewing a live target's feed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Open-source community viewer (ubershmekel) sitting on top of Reddit's public JSON; it reformats content it does not host, so no independent data claims.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- reddtip
tags:
- reddit
- image-viewer
source: osintambition-social
lastVerified: '2026-07-29'
enrichment: full
---

# redditp (reddtip)

> Auto-advancing slideshow viewer for Reddit images — lets you triage a user's or subreddit's visual history far faster than scrolling the site.

## When to use
You have a Reddit `username` (or a subreddit) and want to review every image they have posted quickly — spotting faces, locations, or repeated imagery — without clicking through each thread on reddit.com.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.redditp.com in a sock-puppet browser.
2. Load a user feed via `https://www.redditp.com/u/USERNAME` (or a subreddit via `/r/SUBREDDIT`); the "user" option starts a user slideshow.
3. Use the playback controls (speed, NSFW toggle, fullscreen) to auto-advance through their images.
4. When an image is of interest, pause and open the original post on Reddit for context (title, comments, timestamp).
5. Pivot: pull interesting images into reverse-image search and EXIF checks; feed the source subreddit list into building the subject's interest/location profile.

## Inputs → Outputs
- **In:** `username` (Reddit user) or a subreddit
- **Out:** the subject's posted `image` stream
- **Empty/negative result looks like:** a text-only or deleted account shows an empty/looping slideshow — no images to review, not a tool error.

## Gotchas & OpSec
- It surfaces only image/link posts; text posts and comments are invisible here — use the main site or a Reddit search tool for those.
- Public content only; nothing private and no login.
- OpSec: **passive**; still browse behind a VPN so image-CDN requests are not tied to you.

## Overlaps ("do both")
- Pairs with a full Reddit user-history search tool (comments + text) for coverage this image-only viewer misses, and with reverse-image search on the frames it surfaces.

## Trust & verifiability
`trust: community` — an open-source reformatter of Reddit's public feed; every image traces back to a real Reddit post you can open and verify directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | redditp-reddtip |
| category | social-networks |
| selectorsIn → selectorsOut | username → image |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
