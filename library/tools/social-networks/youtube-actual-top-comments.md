---
id: youtube-actual-top-comments
name: YouTube Actual Top Comments
description: Use when you have a YouTube `social-profile`/video and want to surface a target's or subject's most-liked comments — returns `social-profile` and `associate` signals buried in a video's comment thread.
url: https://chromewebstore.google.com/detail/youtube-actual-top-commen/hbdmelobmfcompinikjdaiphhonbgfpn
category: social-networks
path:
- social-networks
bestFor: Sorting and searching a YouTube video's entire comment section by like-count instead of YouTube's opaque "Top comments" ranking.
selectorsIn:
- social-profile
selectorsOut:
- social-profile
- associate
status: live
pricing: free
costNote: Free Chrome extension; no account or in-app purchase.
opsec: passive
opsecNote: The extension re-renders comment data your browser already loads from YouTube; it does not post, like, or notify anyone. You are logged into Chrome, so browse from a sock-puppet Chrome profile if you don't want the viewing tied to your identity. It requests read access to youtube.com pages — vet permissions before install.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: unverified
trustNote: Third-party extension (~1,000 users, last updated 2022); functional but unaudited. Extensions with page-content access should be installed in an isolated browser profile.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- YouTube Actual Top Comments extension
tags:
- Social Media
- YouTube
source: cyb-detective
lastVerified: '2026-07-21'
enrichment: full
---

# YouTube Actual Top Comments

> A Chrome extension that re-sorts a YouTube video's comments strictly by like-count and makes the whole thread searchable — turning a noisy comment section into a scannable list.

## When to use
You are working a YouTube channel or video connected to a subject and need to mine the comments: to find the subject's own most-visible remarks, to see who the community engages with, or to search for a username, name, or phrase across an entire (often thousands-long) comment thread that YouTube only loads a few at a time. YouTube's default "Top comments" order is relevance-weighted and hides the raw popularity signal; this exposes it.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install from the Chrome Web Store (link above) into a dedicated sock-puppet Chrome profile.
2. Open the target YouTube video and scroll to comments; the extension lists them ordered by number of likes and adds a search box.
3. Use the search box to hunt for a username, handle, name, city, or keyword across all comments without waiting for infinite-scroll to load them.
4. Note the highest-liked comments (community sentiment / pinned voices) and any comment authored by the subject.
5. Pivot: a commenter's channel handle feeds `social-profile` and username tools; a name/phrase in a comment feeds people-search.

## Inputs → Outputs
- **In:** `social-profile` (a YouTube video or channel)
- **Out:** `social-profile` (commenter handles), `associate` (people the subject replies to / is mentioned by)
- **Empty/negative result looks like:** comments disabled on the video, or no match for your search term — the thread genuinely lacks it, or comments were removed/limited by the uploader.

## Gotchas & OpSec
- Chrome-only; it reads page content on youtube.com, so treat it like any content-access extension and isolate it in a throwaway profile.
- It only reorders comments your browser can already see — it does not recover deleted or hidden comments.
- Last updated 2022; if YouTube changes its comment DOM the extension may break — verify it is still sorting correctly on a known video.

## Overlaps ("do both")
- Pairs with a YouTube channel/username enumeration tool — that finds the account, this mines what the account and its audience actually said.

## Trust & verifiability
`trust: unverified` — a small third-party extension with no public audit; useful and low-risk in an isolated profile, but confirm any critical comment against the live YouTube thread (it can be edited or deleted).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | youtube-actual-top-comments |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile → social-profile, associate |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
