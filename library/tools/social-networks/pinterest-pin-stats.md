---
id: pinterest-pin-stats
name: Pinterest Pin Stats (Chrome extension)
description: Use when you have a Pinterest `username`/board and want each pin's engagement and creation date to reconstruct activity timing — returns social-profile activity metadata.
url: https://chromewebstore.google.com/detail/pinterest-pin-stats-sort/mcmkeopcpbfgjlakblglpcccpodbjkel
category: social-networks
path:
- social-networks
bestFor: Overlaying saves/likes/comments and creation dates onto a Pinterest user's pins so you can sort them and read their activity timeline.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free Chrome extension (~10k users, 4.7★, updated 2026). Data is stored in your browser's local storage; the developer states no selling of data.
opsec: active
opsecNote: You must be browsing Pinterest while logged in, so the boards/pins you view are loaded under YOUR Pinterest session — use a sock-puppet Pinterest account. The extension reads the page you're on; it doesn't query Pinterest independently.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: browser-extension
trust: community
trustNote: An established, well-rated extension that surfaces Pinterest's own engagement/date fields on the page. It reflects what Pinterest exposes, so the metrics are as accurate as Pinterest's data.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: true
registration: false
invitationOnly: false
relatedTools:
- pinterest
aliases:
- Pinterest Pin Stats - Sort Pins
tags:
- pinterest
source: awesome-osint
lastVerified: '2026-07-15'
enrichment: full
---

# Pinterest Pin Stats (Chrome extension)

> Turns a Pinterest profile into a sortable dataset — saves, likes, comments and, crucially, pin creation dates — so you can read *when* and *how actively* a subject used Pinterest.

## When to use
You're examining a subject's Pinterest and want more than a visual board — you want the metadata: which pins are most engaged, and especially **creation dates**, which reveal activity windows, time-of-day patterns (a timezone tell), and periods of life the boards document. Useful for lifestyle/interest profiling and timeline reconstruction in a person investigation.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install "Pinterest Pin Stats - Sort Pins" from the Chrome Web Store.
2. Log into Pinterest with a **sock-puppet** account.
3. Open the target's profile/board and browse normally — the extension overlays saves/likes/comments and creation dates on each pin.
4. Open the Pin Stats Table to sort by likes, comments, or date across the collection.
5. Pivot: creation-date clusters feed a `timeline`/timezone hypothesis; heavily-saved pins reveal interests and possible locations/associates.

## Inputs → Outputs
- **In:** `username` (a Pinterest profile/board you can browse)
- **Out:** `social-profile` activity metadata — per-pin saves/likes/comments and creation dates
- **Empty/negative result looks like:** no stats overlay — the profile/board is private or empty, or Pinterest didn't expose the fields; you can only see what your logged-in account can load.

## Gotchas & OpSec
- Human-in-the-loop: requires a logged-in Pinterest session — use a throwaway account, never your own.
- It only annotates pages you actually open; it doesn't crawl the whole account by itself.
- OpSec: active — boards load under your Pinterest identity; sock-puppet it.

## Overlaps ("do both")
- Pairs with plain Pinterest profile review — this adds the quantitative/timing layer the UI hides.
- Combine with reverse-image search on pinned photos to link interests/locations to other platforms.

## Trust & verifiability
`trust: community` — a well-rated extension surfacing Pinterest's own metrics; the numbers are Pinterest's, so they're reliable, but interpret creation dates as activity signals, not hard biography.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pinterest-pin-stats |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | browser-extension |
| opsec | active |
| human-in-loop | yes (account-login) |
