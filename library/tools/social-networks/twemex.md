---
id: twemex
name: Twemex (Tweet Hunter X Sidebar)
description: Use when you're reading X/Twitter and want a research sidebar — returns quick access to a user's best tweets, quotes of a post, and your own search shortcuts.
url: https://chromewebstore.google.com/detail/twemex-sidebar-for-twitte/amoldiondpmjdnllknhklocndiibkcoe
category: social-networks
path:
- social-networks
bestFor: An in-page X sidebar that surfaces any user's top tweets, quote-tweets of a post, and faster search while browsing.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: freemium
costNote: Free core sidebar features; AI writing/inspiration features are reserved for paid Tweet Hunter subscribers. Now published as "Tweet Hunter X" (formerly Twemex).
opsec: active
opsecNote: The extension runs inside your logged-in X session and reads the pages you view, so it operates under whatever X account you use — use a sock-puppet browser profile and account, never your personal one.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: A third-party Chrome extension (by lempire/Tweet Hunter) with a clean store record; it enhances the X UI but reads your session, so vet permissions and isolate it.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- twitter-x-advanced-search
tags:
- Social Media
- Twitter
- browser-extension
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# Twemex (Tweet Hunter X Sidebar)

> A browser-extension sidebar for X that, as you view a profile or tweet, instantly surfaces that user's best posts, the quote-tweets of a post, and search shortcuts — speeding up manual X research.

## When to use
While manually reviewing a subject's X account, Twemex saves clicks: it shows a `username`'s highest-performing tweets (a fast way to find their most revealing/most-shared content), lists who quote-tweeted a given post (surfacing reactions and `associate`s), and adds search shortcuts. Best as a productivity layer on top of manual profile review.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install the extension (Tweet Hunter X / Twemex sidebar) from the Chrome Web Store into a dedicated sock-puppet browser profile.
2. Log into X with a sock-puppet account and open a target profile or tweet.
3. Use the sidebar to view the user's "Highlights"/best tweets for a quick read of their most notable content.
4. On a specific post, open the quotes view to see who commented via quote-tweet.
5. Use the search shortcuts to jump into filtered X searches faster.
6. Pivot: top tweets → content/leads worth archiving; quote-tweeters → `associate` mapping; then hand precise queries to `[[twitter-x-advanced-search]]`.

## Inputs → Outputs
- **In:** a `username`/profile or tweet you're viewing on X
- **Out:** that user's best tweets, quote-tweets of a post, and quicker search (`social-profile` context)
- **Empty/negative result looks like:** a sparse sidebar for low-activity or protected accounts — it can only reorganize what X shows your logged-in session, so it adds nothing X itself won't surface.

## Gotchas & OpSec
- It reads your live X session and the pages you view: treat it as having full access to that account/profile. Isolate it in a dedicated investigation browser and use a sock-puppet X account.
- It reorganizes X data rather than pulling hidden data — no magic access to deleted/protected posts.
- Premium AI features are paywalled and irrelevant to OSINT; the free sidebar is the useful part.
- OpSec: **active** — activity happens under your logged-in account.

## Overlaps ("do both")
- Pairs with `[[twitter-x-advanced-search]]` — Twemex speeds up ad-hoc browsing and surfaces top tweets/quotes, while Advanced Search runs the precise date/user/keyword queries.

## Trust & verifiability
`trust: community` — a reputable third-party extension, but it operates inside your X session; the tweets it surfaces are X's own data (authoritative), while the extension itself should be permission-vetted and isolated.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | twemex |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | browser-extension |
| opsec | active |
| human-in-loop | no |
