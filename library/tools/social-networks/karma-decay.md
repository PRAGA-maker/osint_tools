---
id: karma-decay
name: Karma Decay
description: Use when you have an `image` and want to find whether/where it was posted on Reddit — returns the Reddit submissions (subreddits, `username`s, dates) that used that image.
url: http://karmadecay.com/
category: social-networks
path:
- social-networks
bestFor: Reverse image search scoped to Reddit — tracing an image to the Reddit posts, subreddits, and accounts that shared it.
selectorsIn:
- image
selectorsOut:
- social-profile
- username
status: degraded
pricing: free
costNote: Free, no account. Long-running hobby project; availability can be intermittent (has returned 503s), and it covers image posts Reddit's index knows about.
opsec: passive
opsecNote: You submit an image URL or upload to Karma Decay; nothing is posted to Reddit or shown to any user. As with any upload, treat the image as disclosed to a third party — crop/strip sensitive detail if needed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A veteran community tool for Reddit reverse-image search; useful but its index is partial and uptime is not guaranteed.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- reverse-reddit-image-search
aliases:
- karmadecay.com
- KarmaDecay
tags:
- social-media
- reddit
- reverse-image-search
source: osint4all
lastVerified: '2026-07-17'
enrichment: full
---

# Karma Decay

> Reddit-scoped reverse image search — paste or upload an image and it finds the Reddit submissions that used it, with their subreddits, posters, and dates.

## When to use
You have an `image` (a profile picture, a photo from a post, a meme a subject reused) and want to know its Reddit history: where it was posted, by which accounts, and when. This links an image to `username`s and communities — useful for tying a photo to a Reddit identity, spotting reposts/impersonation, or discovering that a "personal" photo was lifted from elsewhere on Reddit. Directly relevant when a subject or a fake profile is Reddit-active.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://karmadecay.com/ (retry later if it returns a 503 — it can be intermittently down).
2. Paste the image URL, or upload the image file.
3. Review the matching Reddit submissions: subreddit, title, submitting `username`, score, and date.
4. Open promising submissions on Reddit to read context and the poster's history.
5. Pivot: a submitting `username` → their Reddit profile and post history → other handles/details; a subreddit → the community the subject frequents.

## Inputs → Outputs
- **In:** `image` (URL or upload)
- **Out:** Reddit submissions using the image — `social-profile`/`username` of posters, subreddits, dates
- **Empty/negative result looks like:** "no matches" — the image was never posted to Reddit, or isn't in Karma Decay's index (which is partial). A miss doesn't mean it's absent from Reddit; try a general reverse-image tool too.

## Gotchas & OpSec
- **Partial index + shaky uptime:** it doesn't cover all of Reddit and is periodically down. Treat a miss as inconclusive and retry/complement.
- Best on image *posts*; images only embedded in comments or off-site may not surface.
- Passive; nothing is disclosed to Reddit users.

## Overlaps ("do both")
- Pairs with a general reverse-image engine (Google Lens / Yandex) — those find the image across the whole web, while Karma Decay pinpoints the Reddit-specific history and accounts; run both.

## Trust & verifiability
`trust: community` — a long-standing but hobby-maintained tool with a partial index. Findings are real Reddit posts (verify on Reddit); absence is weak evidence given its coverage and downtime.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | karma-decay |
| category | social-networks |
| selectorsIn → selectorsOut | image → social-profile, username |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
