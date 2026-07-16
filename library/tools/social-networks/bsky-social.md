---
id: bsky-social
name: bsky.social (Bluesky)
url: https://bsky.social/about/blog/05-31-2024-search
category: social-networks
path:
- social-networks
description: Use when you have a `username` or `name` and want to find a Bluesky presence — returns a `social-profile` with posts, handle, bio and follow graph.
bestFor: Finding and reading a subject's Bluesky profile and posts, including full-text post search across the network.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- name
status: live
pricing: free
costNote: Free to use; public profiles and posts are readable without an account, though full search and interaction work best signed in (registration is free and open).
opsec: passive
opsecNote: Reading public profiles/posts (including via the AT Protocol's open data) is passive and doesn't notify the subject. Following/replying requires a login and is visible — keep to read-only, and note Bluesky's open protocol means posts are broadly accessible/archivable.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The official Bluesky network; the platform is authentic and its AT Protocol makes public data openly queryable, though individual accounts may be impersonators.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- Bluesky
- bsky.app
tags:
- bluesky
- BlueSky / BSky Related Sites
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
relatedTools:
- bsky-social-2
---

# bsky.social (Bluesky)

> Bluesky, the AT-Protocol social network — find a subject's handle and posts, with full-text post search and an open, queryable public data layer.

## When to use
You have a `username` or `name` and want to check for a Bluesky presence and read what the person posts. Bluesky has grown as a Twitter/X alternative, so it's a useful non-mainstream network to check; its full-text search (rolled out 2024) lets you find posts by keyword, and the open AT Protocol means public profiles/posts are broadly accessible and archivable.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open bsky.app (or try the handle directly at `bsky.app/profile/<handle>`).
2. Search the `name`/handle, or use post search to find keyword mentions across the network.
3. Read the profile: handle (often a custom domain), bio, posts, and follows/followers.
4. Note custom-domain handles — they often reveal a personal/employer website.
5. Pivot: a reused `username` feeds cross-platform enumeration; a custom-domain handle feeds `[[northdata-com]]`/WHOIS; posted media feeds reverse-image/geolocation.

## Inputs → Outputs
- **In:** `username` or `name`
- **Out:** `social-profile` (handle, bio, posts, follow graph), real `name`/domain where disclosed
- **Empty/negative result looks like:** no matching handle, or a lookalike — verify via custom domain, cross-links and posting style before attributing, since handles can be squatted or impersonated.

## Gotchas & OpSec
- Impersonation is possible; a custom-domain handle (verified) is stronger evidence of identity than a generic `.bsky.social` one.
- The open protocol means "deleted" posts may persist in third-party archives/relays.
- OpSec: reading is passive; logging in to follow/reply is active and visible to the subject.

## Overlaps ("do both")
- Pairs with `[[username-search-tool]]` (is the handle reused on X/Mastodon?) and Bluesky-specific viewers/graph tools for deeper follow-network analysis.

## Trust & verifiability
`trust: trusted` — the genuine Bluesky platform with an openly queryable public data layer; treat the *contents* of any single account as self-published and potentially impersonated until corroborated.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bsky-social |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
