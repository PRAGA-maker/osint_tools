---
id: repostsleuth
name: Repost Sleuth
description: Use when you have an image and want to find where it was posted on Reddit before — returns the matching Reddit posts (social-profile, username, geolocation context) via reverse-image matching.
url: https://repostsleuth.com/
category: social-networks
path:
- social-networks
bestFor: Reverse-image searching Reddit to find every earlier post of an image and the accounts/subreddits that shared it.
selectorsIn:
- image
selectorsOut:
- social-profile
- username
status: live
pricing: freemium
costNote: Free to search by image or Reddit URL; a Patreon supports the project but the public search is free.
opsec: passive
opsecNote: You upload an image or paste a Reddit URL to a third-party service; it queries Reddit's public index, not the target. Don't upload sensitive/private imagery to an external site. No Reddit user is notified of your search.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Well-known, heavily-used Reddit repost-detection bot/site (open-source, ~1M searches/day); matching is reliable but limited to Reddit-indexed content.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- RepostSleuth
- Reddit Repost Sleuth
- repostsleuth.com
tags:
- social-networks
- reddit
- reverse-image
source: cyb-detective
lastVerified: '2026-07-18'
enrichment: full
---

# Repost Sleuth

> A Reddit-specific reverse-image engine: give it an image (or a Reddit link) and it finds every earlier Reddit post of that picture and the accounts that shared it.

## When to use
You have an `image` — a profile photo, a "for sale" pic, a meme, a supposedly original snapshot — and want to know if and where it appeared on Reddit first. Repost Sleuth surfaces the earliest matching Reddit posts, exposing the `username`s and subreddits (`social-profile`) that shared it. That reveals whether a photo is stolen/recycled (catfish and scam detection) and gives you Reddit accounts to pivot on for context, timing, and location clues.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://repostsleuth.com/search.
2. Either paste a Reddit post URL, or upload/link an image to search by picture.
3. Read the matches: each hit shows the subreddit, the posting account, the date, and a visual-similarity score — sort by oldest to find the likely original.
4. Pivot: the earliest poster and subreddit are leads — profile the Reddit `username` (post history, other images, stated location) and reverse-image the same picture on Google Lens/Yandex for coverage beyond Reddit.

## Inputs → Outputs
- **In:** `image` (upload/link) or a Reddit post URL
- **Out:** `social-profile` (subreddit + post), `username` (Reddit account that posted it), with dates and similarity scores
- **Empty/negative result looks like:** no matches — the image was never posted to Reddit (or not indexed); this says nothing about the image appearing elsewhere on the web, so also run a general reverse-image search.

## Gotchas & OpSec
- Human-in-the-loop: none, though heavy use may be rate-limited.
- OpSec: passive toward the target, but you upload to a third party — don't submit sensitive/private images. No Reddit user is alerted.
- Scope: Reddit only. A repost hit shows sharing, not authorship; the "earliest" Reddit post isn't necessarily the true origin — corroborate with a web-wide reverse-image search.

## Overlaps ("do both")
- Pairs with general reverse-image tools (Google Lens, Yandex, `[[depositphotos-reverse-image-search]]`) — Repost Sleuth owns Reddit coverage, the others catch the same image across the wider web and stock libraries.

## Trust & verifiability
`trust: community` — it is a mature, widely-relied-upon open-source Reddit tool; matches are verifiable by opening the linked Reddit posts directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | repostsleuth |
| category | social-networks |
| selectorsIn → selectorsOut | image → social-profile, username |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
