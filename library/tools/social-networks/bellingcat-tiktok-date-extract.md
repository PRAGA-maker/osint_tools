---
id: bellingcat-tiktok-date-extract
name: Bellingcat TikTok Timestamp
description: Use when you have a TikTok video `social-profile` URL/ID and want its exact upload time — returns the precise `metadata-exif`-style creation timestamp.
url: https://bellingcat.github.io/tiktok-timestamp
category: social-networks
path:
- social-networks
bestFor: Decoding the exact upload date and time embedded in a TikTok video ID.
selectorsIn:
- social-profile
selectorsOut:
- metadata-exif
status: live
pricing: free
costNote: Free, open-source, no account; runs entirely in your browser.
opsec: passive
opsecNote: The timestamp is decoded locally from the numeric video ID — the tool does not query TikTok or notify anyone. You only need the ID/URL, which you likely already have.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Published by Bellingcat; the technique (unix time encoded in the ID's high bits) is deterministic and independently verifiable.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- bellingcat-name-variant-search
- telegram-group-joiner
aliases:
- TikTok timestamp
- tiktok-timestamp
tags:
- bellingcat-toolkit
- tiktok
- timestamp
source: bellingcat-toolkit
lastVerified: '2026-07-17'
enrichment: full
---

# Bellingcat TikTok Timestamp

> A one-field browser tool that decodes the exact upload date/time baked into a TikTok video's ID — TikTok only shows a coarse date, this gives you the second.

## When to use
You have a TikTok video (its URL or numeric ID) and need the precise upload timestamp — for building a timeline, verifying when footage of an event/person was posted, or debunking a "filmed live" claim. TikTok's UI shows only a rough date; the video ID itself encodes a Unix timestamp in its high bits, and this tool extracts it deterministically. Essential for chronolocation and establishing the earliest-known appearance of a clip.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://bellingcat.github.io/tiktok-timestamp in your browser.
2. Paste the full TikTok video URL (e.g. `.../video/7xxxxxxxxxxxxxxxxxx`) or just the numeric video ID.
3. Read the decoded upload date and time (down to the second, UTC).
4. Cross-check against the event you're timing — the upload time is a floor (the video existed by then), not the moment it was filmed.
5. Pivot: combine with reverse-image/geolocation on frames to fully chronolocate; compare against timestamps of the same clip on other platforms to find the original.

## Inputs → Outputs
- **In:** `social-profile` (a TikTok video URL or numeric ID)
- **Out:** exact upload `metadata-exif`-style timestamp (date + time to the second)
- **Empty/negative result looks like:** no/garbage output if you paste a profile URL, a non-video link, or a malformed ID — it needs a genuine *video* ID. It cannot tell you when the video was *filmed*, only *uploaded*.

## Gotchas & OpSec
- OpSec: **passive** — decoding is local; TikTok and the uploader are never contacted.
- The timestamp is upload time, not capture time; treat it as the latest-possible creation moment.
- Works on the video ID only — profile, sound, or hashtag URLs won't decode.

## Overlaps ("do both")
- Pairs with frame-level geolocation and reverse-image tools — this fixes the *when*, those fix the *where* and the *original source*.

## Trust & verifiability
`trust: trusted` — a Bellingcat tool implementing a deterministic, documented decoding of the ID; anyone can reproduce the same timestamp from the same ID.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bellingcat-tiktok-date-extract |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile → metadata-exif |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
