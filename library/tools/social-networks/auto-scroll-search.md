---
id: auto-scroll-search
name: Auto Scroll Search
description: Use when you need to find a `name`/`username`/keyword buried deep in an infinite-scroll feed (X, Facebook, Instagram, YouTube) — auto-scrolls and jumps to matches, surfacing the `social-profile`/post.
url: https://chrome.google.com/webstore/detail/auto-scroll-search/ieceeinfkigfaeoomfimmecebngempef/related
category: social-networks
path:
- social-networks
bestFor: In-page find (Ctrl-F) that keeps auto-loading an infinite feed until your term appears.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free Chrome extension (beta); no account or payment. Developer declares no data collection.
opsec: passive
opsecNote: Runs entirely client-side in your browser against whatever page you are already viewing — it sends nothing to the target. If you point it at a logged-in feed, you are acting as your own logged-in account, so use a sock-puppet account for any account-gated feed; the extension itself adds no extra exposure.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: Small independent extension (~10k users, 4.6★) by developer Glen Chiacchieri; declares no data collection, but it is unaudited third-party browser code — install in a research profile.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- Auto Scroll Search Chrome extension
tags:
- Social Media
- Universal
source: cyb-detective
lastVerified: '2026-07-22'
enrichment: full
---

# Auto Scroll Search

> A browser extension that turns Ctrl-F into an infinite-scroll-aware search — it keeps loading a feed and jumps to your keyword. Used in OSINT to dig a name or post out of a long social timeline.

## When to use
You are looking at an infinite-scroll page (an X/Twitter, Facebook, Instagram or YouTube feed, a long comment thread, a followers list) where the browser's native Ctrl-F only searches what's already loaded. You have a `name`, `username`, or keyword you expect to appear far down the feed and want the page to auto-scroll and load until it hits a match.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install "Auto Scroll Search" from the Chrome Web Store (chromewebstore.google.com) into a dedicated research browser profile.
2. Open the target feed in that profile (log into a sock-puppet account first if the feed is gated).
3. Click the extension and enter your search term (`name`/`username`/keyword); optionally enable auto-click of "load more" buttons.
4. Let it scroll — it pauses between scrolls and notifies via the tab title; use the first/prev/next/last controls to step through matches. The match location gives you the post/`social-profile` you wanted.

## Inputs → Outputs
- **In:** `name` / `username` / keyword, plus the feed you point it at
- **Out:** scrolled-to matches within the feed → the post or `social-profile` mentioning your term
- **Empty/negative result looks like:** it scrolls to the end without a hit — the term isn't present in the loaded feed (or the platform stopped serving more items); not proof it was never posted.

## Gotchas & OpSec
- It only searches what the site will actually load; platforms cap how far a feed paginates and may rate-limit aggressive scrolling — the extension pauses to avoid tripping this, but very long feeds can still stall.
- It operates on your live session: on a logged-in account your scrolling/viewing is normal account activity, so use a sock puppet, not a personal account, for sensitive targets.
- Third-party unaudited code — install in an isolated profile and review permissions.

## Overlaps ("do both")
- Pairs with platform-specific search operators and dedicated social-search tools: use those to query the platform's index first, and Auto Scroll Search to comb a specific feed the index doesn't expose.

## Trust & verifiability
`trust: community` — a small, well-reviewed indie extension with a no-data-collection declaration; treat the declaration as unverified and sandbox it in a research profile.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | auto-scroll-search |
| category | social-networks |
| selectorsIn → selectorsOut | name, username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
