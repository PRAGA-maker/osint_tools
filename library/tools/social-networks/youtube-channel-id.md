---
id: youtube-channel-id
name: YouTube Channel ID Finder
description: Use when you have a YouTube channel URL, handle, or username and want its canonical channel ID plus owner/profile details — returns social-profile, name.
url: https://commentpicker.com/youtube-channel-id.php
category: social-networks
path:
- social-networks
bestFor: Resolving a YouTube handle / custom URL to the stable channel ID and surfacing owner name, creation date, and stats.
selectorsIn:
- username
- social-profile
selectorsOut:
- social-profile
- name
status: live
pricing: freemium
costNote: Free for up to 2 lookups per day without login; a paid subscription removes the daily cap.
opsec: passive
opsecNote: The query goes to CommentPicker (which calls the YouTube Data API on its own key), not to the channel owner — the target is not notified. Nothing you submit beyond the public channel handle is required; use a neutral browser session.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Third-party utility (CommentPicker) wrapping YouTube's public Data API; the returned channel ID is authoritative because it comes straight from YouTube.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- YouTube channel ID lookup
tags:
- youtube
- channel-id
- social-media
source: osint4all
lastVerified: '2026-07-22'
enrichment: full
relatedTools:
- commentpicker-com
- commentpicker-com-2
- find-my-facebook-id-2
- instagram-user-id
---

# YouTube Channel ID Finder

> Resolve any YouTube channel URL, @handle, or username into its permanent `UC…` channel ID — the stable key you pivot on when handles and custom URLs change.

## When to use
You have a subject's YouTube presence as a `username`, @handle, custom URL, or a link to one of their videos, and you need the **canonical channel ID** — the immutable `UC…` identifier that survives handle/vanity-URL changes and lets you query the API, build archive URLs, or correlate across tools. It also returns owner-facing metadata (channel name, creation date, subscriber/video/view counts) useful for profiling and age-of-account checks.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://commentpicker.com/youtube-channel-id.php.
2. Paste the channel link, a video link, the @handle, or the username into the input.
3. Submit — it returns the `UC…` channel ID plus channel owner name, custom URL, creation date, and subscriber/video/view counts.
4. Copy the channel ID as your stable pivot key.
5. Pivot: feed the channel ID into the YouTube Data API, into `https://www.youtube.com/channel/<ID>` for archive/Wayback lookups, or correlate the creation date and stats against other social accounts.

## Inputs → Outputs
- **In:** `username` / `social-profile` (channel URL, @handle, video link, or username)
- **Out:** `social-profile` (channel ID + custom URL + stats), `name` (channel owner/display name)
- **Empty/negative result looks like:** an error or blank result when the handle doesn't resolve — the channel was renamed/deleted or the input was mistyped; try a video link from the channel instead.

## Gotchas & OpSec
- Free tier is capped at ~2 lookups/day without an account; for volume, batch your handles or use the YouTube Data API directly.
- The **channel display name is not the person's legal name** — treat it as a lead, not identity confirmation.
- OpSec: passive; the lookup hits CommentPicker/YouTube, never the channel owner.

## Overlaps ("do both")
- Pairs with `[[commentpicker-com]]` and `[[commentpicker-com-2]]` — same provider's ID finders for Instagram/TikTok; run the matching one per platform to resolve each handle to its stable ID.

## Trust & verifiability
`trust: community` — a third-party wrapper, but the channel ID it returns originates from YouTube's own Data API, so that core value is authoritative; the descriptive stats are as current as YouTube's public API.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | youtube-channel-id |
| category | social-networks |
| selectorsIn → selectorsOut | username, social-profile → social-profile, name |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
