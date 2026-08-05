---
id: finddit-viralharia
name: Finddit (viralharia)
description: Use when you have a `username` or a keyword and want to search Reddit posts/comments — returns matching Reddit `social-profile` activity.
url: https://viralharia.github.io/finddit
category: social-networks
path:
- social-networks
bestFor: Keyword/username search across Reddit posts and comments from a lightweight web front-end.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free single-page web app; no account or key needed. Runs against Reddit's public search endpoints.
opsec: passive
opsecNote: Queries hit Reddit's public search, not the target's account, so the subject is not notified. The request originates from your browser/IP — use a sock-puppet session if you are searching a sensitive handle. No login means no footprint on your own Reddit identity.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Community-built GitHub Pages front-end by a single developer (viralharia); it is a thin wrapper over Reddit's own search, so result accuracy tracks Reddit, but availability depends on one unaffiliated maintainer.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Reddit Search (viralharia)
tags:
- reddit
- search
source: osintambition-social
lastVerified: '2026-08-05'
enrichment: full
---

# Finddit (viralharia)

> A lightweight web front-end that runs keyword and username searches over Reddit's public search API — a faster way to sweep Reddit than the native UI.

## When to use
You have a `username` you suspect is active on Reddit, or a distinctive keyword/phrase (a handle, a real name, a place, a piece of jargon a subject uses), and you want to surface their posts and comments quickly. A hit gives you a Reddit `social-profile` and the surrounding thread context to pivot from.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://viralharia.github.io/finddit in a clean/sock-puppet browser session.
2. Type the search term — a username (search their exact handle) or a keyword/name.
3. Set **Sort By** (Relevance or Latest) and the result count (5–100), then submit.
4. Read the results: each is a Reddit post/comment. Click through to the thread to confirm authorship and read surrounding context.
5. Pivot: a confirmed handle feeds cross-platform username tools; recurring subreddits reveal interests/location; comment history is a timeline of activity.

## Inputs → Outputs
- **In:** `username` or `name`/keyword
- **Out:** matching Reddit posts/comments → the author's `social-profile` and thread links
- **Empty/negative result looks like:** no results returned, or only unrelated keyword hits — treat as "not found via this query," not proof the handle is unused (try the native Reddit search and Latest sort before concluding).

## Gotchas & OpSec
- Human-in-the-loop: none — it is a plain search box, no CAPTCHA or login.
- OpSec: passive; queries go to Reddit, not to the subject, so no notification is generated. Requests still carry your IP.
- Reliability: it depends on Reddit's search endpoint and on one unaffiliated maintainer; if it returns nothing, cross-check with Reddit's own search before trusting the negative.

## Overlaps ("do both")
- Pairs with any broad Reddit search or username-enumeration tool: this narrows to Reddit content, while cross-platform username checkers tell you where else the same handle appears.

## Trust & verifiability
`trust: unverified` — a community GitHub Pages wrapper over Reddit's public search; the underlying data is Reddit's (reliable), but the tool itself is maintained by one unaffiliated developer and could go offline without notice.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | finddit-viralharia |
