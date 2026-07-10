---
id: thread-reader
name: Thread Reader
description: Use when you have an X/Twitter thread `social-profile` URL and want it as one readable, preservable page — returns the full unrolled thread text and media in order.
url: https://threadreaderapp.com/
category: social-networks
path:
- social-networks
bestFor: Unrolling and preserving multi-tweet X/Twitter threads into a single readable page.
selectorsIn:
- social-profile
selectorsOut:
- social-profile
status: live
pricing: freemium
costNote: Free to unroll and read threads; a paid tier adds saving/search/export and removes limits.
opsec: passive
opsecNote: You submit a public tweet/thread URL; Thread Reader fetches and renders it. The author isn't notified by the unroll itself (though invoking the @threadreaderapp bot in a reply IS a public, visible action — prefer pasting the URL on the site). Use a sock-puppet browser and preserve a copy, since threads can be deleted.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running, widely used thread-unroll service; reliable for reading/preserving public X threads, but a third party dependent on X's API access.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Thread Reader App
- threadreaderapp.com
tags:
- twitter
- x
- thread-unroll
- preservation
source: osint4all
lastVerified: '2026-07-10'
enrichment: full
---

# Thread Reader

> Turn a scattered X/Twitter thread into one clean, scrollable page you can read and preserve — before the author edits or deletes it.

## When to use
You've found a multi-tweet X/Twitter thread relevant to a subject and want to read it end-to-end in order, or capture it before it disappears. Threads often contain the substance (a subject's account of events, a timeline, named people/places) that single tweets fragment; unrolling makes it analysable and preservable.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://threadreaderapp.com/ in a sock-puppet browser.
2. Paste the URL of any tweet in the thread (prefer this over @-mentioning the bot, which is publicly visible to the author).
3. Let it unroll — it assembles the whole thread into one page with text and media in sequence.
4. Read and **preserve**: save the page (and note the source URL + timestamp), since the original can be edited or deleted.
5. Pivot: named people feed the associate graph; images feed `[[reverse-image-search]]` (download originals via `[[cobalt-tools]]`); places feed geolocation; dates feed the timeline.

## Inputs → Outputs
- **In:** an X/Twitter thread/tweet `social-profile` URL
- **Out:** the full unrolled thread (`social-profile` content: text + media, in order) on one page
- **Empty/negative result looks like:** unroll fails or is partial — the thread is protected/deleted, the account is private, or X API limits blocked it. A failure is tool/visibility-side, not proof the thread never existed; try a direct (sock-puppet) view.

## Gotchas & OpSec
- **Public action risk:** replying with `@threadreaderapp unroll` is visible to the author and other users — paste the URL on the website instead to stay quiet.
- Depends on X API access, which has tightened; some threads won't unroll. Preserve what you get immediately.
- OpSec: **passive** when using the site directly; keep the session a sock puppet.

## Overlaps ("do both")
- Pairs with `[[cobalt-tools]]` (download the thread's media) and full-page capture/archiving tools — Thread Reader gives readable text; media downloaders and archives preserve the assets and provenance. Do both for a defensible record.

## Trust & verifiability
`trust: community` — a reputable, long-standing service; the unrolled content mirrors the live thread, so verify against the source (while it exists) and keep your own preserved copy.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | thread-reader |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile → social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
