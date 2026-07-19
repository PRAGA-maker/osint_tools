---
id: twitter-com
name: Twitter.com
description: Use when you have a `name`, keyword, or event and want eyewitness photos/media posted to X — returns `social-profile`s of posters and `image` content, filtered to the media view.
url: https://twitter.com/search?q=explosion&src=typd&mode=photos
category: image-video-face
path:
- image-video-face
bestFor: Pulling photo/video posts from X (Twitter) for a person, place, or event using the media-only search view.
selectorsIn:
- name
selectorsOut:
- social-profile
- image
status: degraded
pricing: free
costNote: Free, but since 2023 X requires a logged-in account to run and page through search results; logged-out search is largely blocked.
opsec: active
opsecNote: Searching now needs a login, so use a sock-puppet X account — never your real one. Viewing posts is passive to the poster, but liking/following/replying is visible; browse only.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party X search over public posts; the media itself is authoritative content, though X's ranking and login-gating limit what you can page through.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- X photo search
- Twitter media search
tags:
- reverse-image
- face
source: metaosint
lastVerified: '2026-07-15'
enrichment: full
relatedTools:
- global-terriorism-database
- murph-live
- parrot-security
- tormap
- twitter
- twitter-advanced-search
- twitter-analytics
- twitter-date-search
- twitter-image-search
- twitter-name-search-twitter-name-search
- twitter-x-location-search
---

# Twitter.com

> X (Twitter) search restricted to the **Photos/Media** view — a fast way to pull images and video posted about a person, place, or event, straight from the people who posted them.

## When to use
You want visual evidence from X: eyewitness photos of an incident, images tagged to a location or event, or media a subject posted. The `mode=photos` (media) filter strips out text-only chatter so you see pictures first — invaluable for missing-persons timelines (last-seen photos, event imagery) and for grabbing a subject's own uploaded images to run through face/reverse-image search.

## How to use it (`bestInteractionPattern`: web-manual)
1. Log into a **sock-puppet** X account (search now requires a login).
2. Build the query: replace `explosion` in the URL with your `name`, keyword, place, or event; keep `mode=photos` (or use the "Media" tab). Add X operators (`since:`/`until:`, `near:`, `filter:images`) to bound time and place.
3. Scroll the media results; open promising posts to read the poster's `social-profile`, caption, and timestamp/geolocation cues.
4. Pivot: download a subject's image for `[[digitaldigging-org-2]]`-style authenticity checks and reverse-image/face search; the poster account becomes a new lead.

## Inputs → Outputs
- **In:** `name`, keyword, place, or event (in the query)
- **Out:** `image`/video posts → poster `social-profile`s, captions, timestamps, location hints
- **Empty/negative result looks like:** few or no media hits — X ranking and login limits truncate results, so absence is weak; try alternate keywords, operators, and the "Latest" tab.

## Gotchas & OpSec
- Human-in-the-loop / **account-login**: search is login-gated post-2023 — use a burner account, as heavy querying can get accounts rate-limited or suspended.
- OpSec: **active** — you're logged in; browse only, never engage with the target's posts.
- Verify images before trusting them — X is awash with recycled/AI/mislabelled media; confirm provenance with reverse search.

## Overlaps ("do both")
- Pairs with `[[digitaldigging-org-2]]` (is this image real?) and reverse-image tools — X surfaces the media; those confirm it's genuine and trace where else it appears.

## Trust & verifiability
`trust: trusted` — it's X's own search over public posts, so the results are real content; the caveats are coverage (login-gating, ranking) and the authenticity of any individual image, not fabrication by an intermediary.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | twitter-com |
| category | image-video-face |
| selectorsIn → selectorsOut | name → social-profile, image |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
