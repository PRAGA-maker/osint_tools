---
id: tokimeki-blue
name: tokimeki.blue
description: Use when you have a Bluesky `username` (handle) and want a TweetDeck-style, multi-column view of that account's posts, feeds and media to monitor it — returns social-profile activity and media.
url: https://tokimeki.blue/
category: social-networks
path:
- social-networks
bestFor: Monitoring a Bluesky target's timeline, feeds and media in customizable columns, like TweetDeck for Bluesky.
selectorsIn:
- username
selectorsOut:
- social-profile
- image
status: live
pricing: free
costNote: Free third-party Bluesky client (PWA). No payment; a Bluesky/AT Protocol account login is required to use it.
opsec: active
opsecNote: You must sign in with a Bluesky account, so use a dedicated sock-puppet account, never a personal one. Viewing does not notify the target, but following, liking, or reposting from your session is visible to them — stay read-only.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Independent client built on the public AT Protocol; it shows the same public posts the official app does, so data fidelity is high, but it is a third-party developer project, not Bluesky first-party.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- google-com-69
aliases:
- TOKIMEKI for Bluesky
- tokimeki bluesky client
tags:
- bluesky
- BlueSky / BSky Related Sites
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# tokimeki.blue

> A TweetDeck-style third-party Bluesky client that lets you watch a target's posts, feeds, and media across multiple columns and accounts at once.

## When to use
You have a subject's Bluesky handle (`username`, e.g. `alice.bsky.social`) and want to monitor their activity more efficiently than the default app allows — multiple columns (their posts, their likes, a search, a feed) side by side, media-only timelines, and keyword filters. Best when Bluesky is a confirmed channel for the subject and you need sustained observation rather than a one-off look.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://tokimeki.blue/ in a sock-puppet browser session and sign in with a **dedicated** Bluesky account (never your own).
2. Add a column and point it at the target `username` to pin their post timeline.
3. Add further columns: a media-only timeline (image evidence), their likes/reposts (interest and associate signals), and a keyword search across Bluesky.
4. Read the output: chronological posts, images, and interactions. An active account shows recent dated posts; note tagged locations, mentioned handles (`associate`), and posted media.
5. Pivot: handles the subject replies to feed further Bluesky/handle checks; a Google `site:bsky.app` dork (as in [[google-com-69]]) can surface the same handle elsewhere.

## Inputs → Outputs
- **In:** `username` (Bluesky handle)
- **Out:** `social-profile` (post history, follows, interactions), `image` (media timeline)
- **Empty/negative result looks like:** the handle resolves to an empty or suspended profile, or "account not found" — meaning the handle is wrong or the subject is not on Bluesky.

## Gotchas & OpSec
- Human-in-the-loop: account login is mandatory; the client cannot browse anonymously.
- OpSec: this is **active** because you are authenticated. Views are silent, but any like/follow/repost your session emits is attributable to your sock account. Keep the session read-only.
- It is a third-party client — treat availability as best-effort and cross-check anything critical against the official bsky.app profile.

## Overlaps ("do both")
- Pairs with a Google `site:` dork such as [[google-com-69]] (adapted to `site:bsky.app`) — the client gives you live column monitoring, the dork surfaces cached/older posts and the handle's appearance on other sites.

## Trust & verifiability
`trust: community` — an independent developer project on the public AT Protocol. It renders the same public data as the official client but is not maintained by Bluesky, so confirm high-stakes findings against bsky.app directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tokimeki-blue |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, image |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
