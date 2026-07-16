---
id: expand-all-facebook-comments-bookmarklet
name: Expand All Facebook Comments – Bookmarklet
description: Use when you have a Facebook post/`social-profile` thread and want to force every hidden comment and reply to load so you can read the full commenter list — returns associates, names and usernames.
url: http://com.hemiola.com/2015/08/29/expand-all
category: social-networks
path:
- social-networks
bestFor: Auto-clicking every "View more comments" / "View replies" fold on a Facebook post so the whole discussion is visible for reading or scraping.
selectorsIn:
- social-profile
selectorsOut:
- associate
- name
- username
status: degraded
pricing: free
costNote: Free snippet of JavaScript you save as a browser bookmark; nothing to buy or register.
opsec: active
opsecNote: You must be logged into Facebook to view the post, so the expansion runs from YOUR authenticated session — every comment you load is a request tied to your account. Use a sock-puppet Facebook profile, never the investigator's real account; loading a friends-only thread can leave a viewer trace.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: browser-extension
trust: community
trustNote: A hobbyist blog snippet (hemiola.com, 2015), not a maintained product; Facebook's DOM has been rewritten many times since, so the selectors it clicks may no longer match.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: false
aliases:
- Expand all Facebook comments
- Facebook comment expander bookmarklet
tags:
- facebook
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
relatedTools:
- com-hemiola-com
---

# Expand All Facebook Comments – Bookmarklet

> A one-click bookmarklet that repeatedly clicks Facebook's "View more comments" and "View replies" links so an entire comment thread loads at once.

## When to use
You are viewing a Facebook post (an event, a public page post, a missing-person appeal, a memorial) whose comment section is truncated behind "View more comments" and nested "View X replies" folds. You want the *complete* roster of people who commented — the associate cloud around the subject — without hand-clicking every fold. You have a `social-profile`/post URL and want the full commenter list (`associate`, `name`, `username`).

## How to use it (`bestInteractionPattern`: browser-extension)
1. Open the blog post at the URL and copy the bookmarklet's `javascript:` snippet; save it as a new bookmark inside a **sock-puppet** browser profile.
2. Log that sock-puppet account into Facebook and navigate to the target post so the comment area is on screen.
3. Click the saved bookmark. It loops through the visible "View more comments" / "View replies" controls and clicks them, pulling more of the thread into the page on each pass.
4. Let it run, scroll, and re-click until no new "view more" links appear — the full comment set is now loaded for reading or scraping.
5. Pivot: each commenter `name`/`username` becomes a fresh subject; the earliest/most-frequent commenters are candidate close `associate`s.

## Inputs → Outputs
- **In:** `social-profile` (a Facebook post/thread you can view)
- **Out:** `associate`, `name`, `username` (every account that commented or replied)
- **Empty/negative result looks like:** the bookmarklet fires but nothing new loads — either the thread was already fully expanded, the post is access-restricted, or (most likely on modern Facebook) the 2015-era selectors no longer match the current markup and it silently does nothing.

## Gotchas & OpSec
- Human-in-the-loop: requires being **logged into Facebook** — use a dedicated sock puppet, never a real investigator account.
- Age risk: written in 2015; Facebook's front-end has been rewritten repeatedly, so treat it as degraded and confirm it actually expands before relying on it.
- OpSec: **active** — loading each hidden comment is a request from your session; a private thread may register you as a viewer.

## Overlaps ("do both")
- Pairs with `[[maltego]]` — the bookmarklet surfaces the raw commenter list, Maltego maps the associate relationships between them.
- Pairs with an archiving tool when the live post is later deleted; expand-and-screenshot while it is still up.

## Trust & verifiability
`trust: community` — an unmaintained personal-blog snippet. It is transparent (you can read the JavaScript before running it) but there is no guarantee it still works against current Facebook, so verify behaviour each session.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | expand-all-facebook-comments-bookmarklet |
