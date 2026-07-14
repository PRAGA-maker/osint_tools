---
id: trevorfox-com
name: Reddit Post Date Finder (trevorfox.com)
description: Use when you have a Reddit post/comment `social-profile` URL and want its exact creation timestamp — returns precise UTC/local date-time metadata for timeline analysis.
url: https://trevorfox.com/reddit-post-date-finder/
category: social-networks
path:
- social-networks
bestFor: Recovering the exact UTC and local timestamp of a Reddit post/comment from its shareable URL.
selectorsIn:
- social-profile
selectorsOut: []
status: live
pricing: free
costNote: Free single-purpose web utility; no account or payment.
opsec: passive
opsecNote: The tool reads publicly available data embedded in Reddit's pages; it does not post, vote, or notify anyone. Running it is passive. It does not require a Reddit login.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A personal-site utility by Trevor Fox; it derives timestamps from Reddit's own public data, so the value it returns is verifiable against Reddit directly.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Reddit post date finder
- reddit timestamp finder
tags:
- reddit
- gsocialmedia
- General Social Media Sites
- timestamp
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# Reddit Post Date Finder (trevorfox.com)

> A one-trick utility that turns a Reddit post/comment URL into an exact timestamp — replacing Reddit's vague "3 months ago" with a precise UTC and local date-time.

## When to use
You're reconstructing a subject's activity timeline on Reddit and need the *exact* time a post or comment was made — Reddit's UI often shows only relative times, and precise timestamps matter for establishing presence, sequencing events, or correlating with other evidence (a subject was online at time X, or posted just before/after an incident). Paste the item's URL and get the exact moment.

## How to use it (`bestInteractionPattern`: web-manual)
1. On Reddit, copy the post's or comment's **shareable URL** (it contains the base-36 ID the tool decodes).
2. Open https://trevorfox.com/reddit-post-date-finder/ and paste the URL into the box.
3. Read the output: exact **UTC** date-time and your **local** date-time.
4. Repeat across a subject's posts to build a precise activity timeline.
5. Pivot: timestamps feed timezone inference (posting patterns → likely local time / region), correlation with other platforms, and pattern-of-life analysis.

## Inputs → Outputs
- **In:** a Reddit post/comment `social-profile` URL
- **Out:** exact creation timestamp (UTC + local); no personal identifiers
- **Empty/negative result looks like:** an error or blank output — usually a malformed/non-Reddit URL, or a deleted item whose ID no longer resolves. It returns time only, never identity.

## Gotchas & OpSec
- This returns a **timestamp only** — not a name, location, or profile. It's an enrichment step, not an identification tool.
- Needs the item's URL (with its ID); it won't work from a screenshot or a username alone.
- Reddit shows post times in your local zone in the UI; use the tool's UTC value as the canonical reference when comparing across sources.
- OpSec: fully passive; no Reddit login, no interaction with the target.

## Overlaps ("do both")
- Pairs with Reddit user-history tools and archive viewers — those enumerate what a user posted; this pins exactly *when*. Combine posting timestamps to infer timezone/pattern-of-life, then corroborate with activity on other platforms.

## Trust & verifiability
`trust: community` — a personal-site utility, but the timestamp is derived from Reddit's own public post ID, so you can verify it directly against Reddit. Low risk of fabricated data.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | trevorfox-com |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile →  |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
