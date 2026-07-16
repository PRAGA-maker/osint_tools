---
id: insta-timestamp-github-com
name: Insta Timestamp
description: Use when you have an Instagram post/reel/story open and want its exact upload date and time — a bookmarklet that returns the post's timestamp (metadata).
url: https://github.com/stegers/insta-timestamp
category: social-networks
path:
- social-networks
bestFor: Revealing the precise upload date/time of an Instagram post, reel or story from the desktop site via a browser bookmarklet.
selectorsIn:
- social-profile
selectorsOut:
- metadata-exif
status: live
pricing: free
costNote: Free open-source bookmarklet (JavaScript on GitHub); nothing to buy or install beyond saving a bookmark.
opsec: passive
opsecNote: The bookmarklet runs locally in your browser against the page you are already viewing — it sends nothing to a third party. You do, however, have to load the Instagram post yourself; if you view it while logged in, Instagram sees your account, so browse from a sock-puppet or logged-out session.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: Small open-source bookmarklet (stegers on GitHub); source is short and inspectable, but it depends on Instagram's page structure and can break when Instagram changes its DOM.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- insta-timestamp
- Instagram timestamp bookmarklet
tags:
- instagram
- Instagram Related Sites
- timestamp
- bookmarklet
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
relatedTools:
- stegers
---

# Insta Timestamp

> A one-click browser bookmarklet that reveals the exact upload date and time of the Instagram post, reel or story you're looking at — Instagram hides precise timestamps, and this surfaces them.

## When to use
You're viewing a specific Instagram post/reel/story and need its precise upload time to build a timeline — to establish when a subject was active, to sequence events, or to corroborate an alibi/sighting. Instagram only shows relative or coarse dates in the UI; this bookmarklet extracts the exact `metadata-exif`-style timestamp baked into the media ID and copies it (with the post URL) to your clipboard.

## How to use it (`bestInteractionPattern`: browser-extension)
1. From the GitHub repo, copy the bookmarklet JavaScript.
2. Create a new browser bookmark and paste the JavaScript as its URL; name it "Insta Timestamp".
3. On desktop instagram.com, open the target post, reel, or story.
4. Click the bookmark — the exact creation date/time (in your local timezone) appears and is copied to your clipboard along with the post URL.
5. Pivot: the timestamp anchors a timeline; combine with geotags/captions to place the subject at a time and place.

## Inputs → Outputs
- **In:** an open Instagram post/reel/story (a `social-profile`'s content)
- **Out:** `metadata-exif` (exact upload timestamp, converted to your timezone)
- **Empty/negative result looks like:** the bookmarklet returns nothing or errors — usually because Instagram changed its page structure, or you're not on a supported desktop post view; it doesn't mean the post has no timestamp.

## Gotchas & OpSec
- Desktop instagram.com only; won't work on the mobile app.
- **Fragile:** depends on Instagram's DOM/media-ID format — if IG changes it, update the bookmarklet or use an alternative shortcode-to-timestamp converter.
- You must load the post yourself; do it from a logged-out or puppet session to avoid exposing your identity to the account.

## Overlaps ("do both")
- Pairs with `[[instaloader-2]]` and Pictame — Instaloader's metadata also carries timestamps for bulk posts, while this is the fastest way to date a single post you're already viewing.

## Trust & verifiability
`trust: community` — a tiny inspectable open-source bookmarklet running client-side; the timestamp is derived from Instagram's own media ID, so it's reliable when the tool works, but verify against a second converter if a date is critical.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | insta-timestamp-github-com |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile → metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
