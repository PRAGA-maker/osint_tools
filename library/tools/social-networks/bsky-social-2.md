---
id: bsky-social-2
name: bsky.social
description: Use when you have a `username`/`name` and want their Bluesky presence — returns the profile, posts, and follow graph (`social-profile`) on an unusually open, API-friendly network.
url: https://bsky.social/about/support
category: social-networks
path:
- social-networks
bestFor: Finding and reading a subject's Bluesky (AT Protocol) profile, posts, and connections.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- name
status: live
pricing: free
costNote: Free to browse public profiles and posts; much of the network is viewable without an account via the app or bsky.app. A (free) account enables in-app search and following.
opsec: passive
opsecNote: Reading public posts/profiles is passive and doesn't notify the target. Bluesky's AT Protocol is extremely open — public posts are broadcast on a firehose and widely mirrored — which is great for collection but also means your own account's activity is equally public. Follow/like from a sock puppet only.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: bsky.social is the flagship, first-party Bluesky service. Genuine platform data, and unusually verifiable because the underlying records are openly published on the AT Protocol.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- clearsky-app
- twitter-x
aliases:
- Bluesky
- bsky.app
tags:
- bluesky
- BlueSky / BSky Related Sites
- at-protocol
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# bsky.social

> Bluesky — a Twitter-style network built on the open AT Protocol, where a subject's profile, posts, and social graph are unusually easy to collect and cross-verify.

## When to use
Your subject may be on Bluesky (a common landing spot for people who left Twitter/X), and you have a `username` (handle, e.g. `alice.bsky.social` or a custom domain) or a `name` to look for. Bluesky often reuses handles from other platforms, public posts reveal interests/locations/connections, and — because it's built on an open protocol — the data is exceptionally amenable to structured collection and provenance checks.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the app at bsky.app (or go directly to `https://bsky.app/profile/<handle>`); use search for the `username`/`name` or keywords.
2. Read the profile: handle (note custom-domain handles double as a website/identity signal), bio, posts, followers/following, and pinned content.
3. For deeper enumeration, use the open AT Protocol / third-party tools that index the public firehose (follows, blocks, post history).
4. Note the account's DID and creation data — the protocol exposes verifiable account provenance.
5. Pivot: reused handles and custom-domain handles feed username/domain work; the follow graph feeds `associate` mapping; corroborate cross-platform with `[[twitter-x]]`.

## Inputs → Outputs
- **In:** `username`/handle or `name`
- **Out:** `social-profile` — bio, posts, follower/following graph, DID/handle provenance, `name`
- **Empty/negative result looks like:** no matching handle/profile — the person may not be on Bluesky, uses a different handle, or a custom-domain handle you haven't guessed. Try handle variants and other platforms.

## Gotchas & OpSec
- Human-in-the-loop: none for public reading; only in-app search/following needs a login.
- OpSec: **passive** while reading; **active** if you follow/like/reply (public). Use a sock puppet. Remember the firehose makes *everything* public, including your own account's actions.
- Custom-domain handles are a strong identity link (the person controls that domain) — verify and exploit them.

## Overlaps ("do both")
- Pairs with AT-Protocol utilities like `[[clearsky-app]]` (block lists, follower analysis) and cross-platform checks against `[[twitter-x]]` — the open protocol means third-party tools can surface follows/blocks/history the app UI hides. Combine app browsing with protocol-level tools.

## Trust & verifiability
`trust: trusted` — first-party platform data, and more verifiable than most social networks because account records and posts are openly published on the AT Protocol. Still confirm identity via bio links, custom domains, and cross-platform corroboration before drawing conclusions.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bsky-social-2 |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
